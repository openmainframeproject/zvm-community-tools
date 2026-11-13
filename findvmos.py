#!/usr/bin/env python3
"""findvmos.py - search the z/VM Community Tools "complete table" and fetch one match.

Usage:
    findvmos.py TERM [TERM ...]          search; if exactly one match, download it
    findvmos.py --refresh spoolkit       re-download the cached README first
    findvmos.py --readme README.md dir   use a local copy of the README
    findvmos.py --dest /tmp/sw --type zip filelist

All TERMs must appear (case-insensitive) in the package name or description.
If several packages match, they are listed and nothing is downloaded -- unless
exactly one of them has a name equal to the term (so "CC" finds CC, not CCC).

Exit codes: 
  0 ok, 
  1 no match, 
  2 several matches, 
  3 download/resolve problem.
"""
import argparse
import os
import re
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

README_URL = ("https://raw.githubusercontent.com/openmainframeproject/zvm-community-tools/main/README.md")
# Static (non-JavaScript) listing of the IBM z/VM Download Library.  The
# "z/VM Downloads" links in the README point at a JavaScript search page
# (#search=NAME) that carries no file URLs, so the real links are scraped here.
IBM_LISTING_URL = "https://www.vm.ibm.com/download/packages/"
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "zvmsw")
CACHE_MAX_AGE = 24 * 3600
UA = {"User-Agent": "zvmsw/1.0 (z/VM community tools catalog helper)"}

ROW = re.compile(r'^\|\s*\*\*(?P<name>.+?)\*\*\s*\|\s*(?P<desc>.*?)\s*\|\s*'
                 r'\[(?P<src>[^\]]+)\]\((?P<url>[^)\s]+)\)\s*\|?\s*$')


# ----------------------------------------------------------------- catalog --
def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def load_readme(path, refresh):
    if path:
        with open(path, encoding="utf-8") as f:
            return f.read()
    cache = os.path.join(CACHE_DIR, "README.md")
    fresh = (os.path.exists(cache)
             and time.time() - os.path.getmtime(cache) < CACHE_MAX_AGE)
    if refresh or not fresh:
        try:
            data = http_get(README_URL)
            os.makedirs(CACHE_DIR, exist_ok=True)
            with open(cache, "wb") as f:
                f.write(data)
        except (urllib.error.URLError, OSError) as exc:
            if not os.path.exists(cache):
                sys.exit("cannot fetch README and no cached copy: %s" % exc)
            print("warning: using stale cache (%s)" % exc, file=sys.stderr)
    with open(cache, encoding="utf-8") as f:
        return f.read()


def parse_catalog(text):
    """Return the rows of the table in the 'complete-table-section' section."""
    entries, inside, seen = [], False, set()
    for line in text.splitlines():
        if 'id="complete-table-section"' in line:
            inside = True
            continue
        if not inside:
            continue
        if line.startswith("## Source Notes"):
            break
        m = ROW.match(line)
        if not m:
            continue
        e = m.groupdict()
        key = (e["name"].lower(), e["url"].lower())
        if key in seen:                      # README lists a few rows twice
            continue
        seen.add(key)
        entries.append(e)
    return entries


def search(entries, terms, name_only=False):
    terms = [t.lower() for t in terms]
    hits = []
    for e in entries:
        hay = e["name"].lower() if name_only else \
            (e["name"] + " " + e["desc"]).lower()
        if all(t in hay for t in terms):
            hits.append(e)
    return hits


def pick_single(hits, terms):
    if len(hits) == 1:
        return hits[0]
    exact = [e for e in hits if e["name"].lower() == " ".join(terms).lower()]
    return exact[0] if len(exact) == 1 else None


# ------------------------------------------------------- source resolution --
class ListingParser(HTMLParser):
    """Collect table rows: cell texts and links (tolerates unclosed tags)."""

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.rows = base, []
        self._row = self._cell = self._a = None

    def _close_cell(self):
        if self._cell is not None and self._row is not None:
            self._row["cells"].append("".join(self._cell).strip())
        self._cell = None

    def _close_row(self):
        self._close_cell()
        if self._row is not None:
            self.rows.append(self._row)
        self._row = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self._close_row()
            self._row = {"cells": [], "links": []}
        elif tag in ("td", "th") and self._row is not None:
            self._close_cell()
            self._cell = []
        elif tag == "a" and self._row is not None:
            href = dict(attrs).get("href")
            if href:
                self._a = {"href": urllib.parse.urljoin(self.base, href),
                           "text": []}

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)
        if self._a is not None:
            self._a["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._a is not None and self._row is not None:
            self._a["text"] = "".join(self._a["text"]).strip()
            self._row["links"].append(self._a)
            self._a = None
        elif tag in ("td", "th"):
            self._close_cell()
        elif tag == "tr":
            self._close_row()

    def close(self):
        super().close()
        self._close_row()


def ibm_files(name, html):
    """Return {'vmarc': url, 'zip': url, 'tar': url} for package NAME."""
    p = ListingParser(IBM_LISTING_URL)
    p.feed(html)
    p.close()
    for row in p.rows:
        if row["cells"] and row["cells"][0].strip().lower() == name.lower():
            files = {}
            for a in row["links"]:
                m = re.match(r"(VMARC|ZIP|TAR)\b", a["text"], re.I)
                if m:
                    files[m.group(1).lower()] = a["href"]
            return files
    return {}


def classify(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    if host.endswith("ibm.com") and "#search=" in url:
        return "ibm"
    if host == "github.com":
        return "github"
    if re.search(r"\.(vmarc|zip|tar|tgz|tar\.gz)$", url, re.I):
        return "direct"
    return "page"


def parse_github(url):
    """github.com/o/r[/tree/BRANCH/sub/dir] -> (owner, repo, ref, subdir)."""
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    owner, repo = parts[0], re.sub(r"\.git$", "", parts[1])
    ref, sub = "HEAD", ""
    if len(parts) >= 4 and parts[2] in ("tree", "blob"):
        ref, sub = parts[3], "/".join(parts[4:])
    return owner, repo, ref, sub


# --------------------------------------------------------------- downloads --
def save(url, dest, fallback_name):
    name = os.path.basename(urllib.parse.urlparse(url).path) or fallback_name
    path = os.path.join(dest, name)
    print("  downloading %s" % url)
    with open(path, "wb") as f:
        f.write(http_get(url, timeout=300))
    print("  saved %s (%d bytes)" % (path, os.path.getsize(path)))
    return path


def extract_tar(path, dest, subdir=""):
    """Unpack a GitHub tarball; keep only SUBDIR if given. Returns the root."""
    with tarfile.open(path) as tar:
        members = tar.getmembers()
        top = members[0].name.split("/")[0]
        prefix = top + ("/" + subdir.strip("/") if subdir else "")
        wanted = [m for m in members
                  if m.name == prefix or m.name.startswith(prefix + "/")]
        if not wanted:
            raise RuntimeError("path %r not found in archive" % subdir)
        root = os.path.realpath(dest)
        for m in wanted:                      # refuse path traversal
            tgt = os.path.realpath(os.path.join(root, m.name))
            if not (tgt == root or tgt.startswith(root + os.sep)):
                raise RuntimeError("unsafe path in archive: %s" % m.name)
        try:
            tar.extractall(dest, members=wanted, filter="data")
        except TypeError:                     # Python < 3.12
            tar.extractall(dest, members=wanted)
    return os.path.join(dest, prefix)


# ----------------------------------------------------- install description --
VMARC_HOWTO = """\
Installing a VMARC package on z/VM (steps from IBM's download page):
  1. Upload the .vmarc file to CMS in BINARY (e.g. FTP binary mode),
     naming it  fn VMARC A  (fn = package name).
  2. Reblock it to fixed 80-byte records:
         PIPE < fn VMARC A | fblock 80 00 | > fn VMARC A F 80
  3. Unpack it with VMARC (get VMARC MODULE from IBM's download page if
     you do not have it):
         VMARC UNPK fn VMARC A
  4. Read the unpacked README / DOC / INSTALL files; many packages only
     need their EXECs on an accessed disk or in a shared segment.
  ZIP archives hold PC content and TAR archives hold UNIX content: unpack
  those on Linux (unzip / tar xf) and follow the files they contain."""

KNOWN = {
    ("zvm-community-tools", "execs"):
        "Upload execs/zvmtools.vmarc to z/VM in BINARY and unpack it with\n"
        "  VMARC UNPK (see steps above). REXX EXECs need no build step.",
    ("zvm-community-tools", "dmscmd"):
        "Follow 'Building DMSCMD' in dmscmd/README.md in the repository.",
    ("zvm-community-tools", "zlma"):
        "Run the install script 'instzlma' from a Linux system; its header\n"
        "  comments describe the steps.",
    ("s390-tools", ""):
        "Usually already part of your s390x Linux distribution; try the\n"
        "  package manager (e.g. apt install s390-tools) before building.",
}


def linux_hints(root):
    """Guess build/install steps from what is in the unpacked tree."""
    if not os.path.isdir(root):
        return []
    names = set(os.listdir(root))
    out = []
    if "configure" in names:
        out.append("./configure && make && sudo make install")
    elif "CMakeLists.txt" in names:
        out.append("cmake -S . -B build && cmake --build build "
                   "&& sudo cmake --install build")
    elif "Makefile" in names or "makefile" in names:
        out.append("make && sudo make install   (check 'make help' first)")
    if "setup.py" in names or "pyproject.toml" in names:
        out.append("python3 -m pip install .   (preferably in a venv)")
    elif "requirements.txt" in names:
        out.append("python3 -m pip install -r requirements.txt")
    if "go.mod" in names:
        out.append("go build ./...")
    if "Cargo.toml" in names:
        out.append("cargo build --release")
    if "package.json" in names:
        out.append("npm install")
    for n in sorted(names):
        if re.match(r"(inst|install)", n, re.I) and \
                os.path.isfile(os.path.join(root, n)):
            out.append("Read and run ./%s (install script)" % n)
    docs = [n for n in sorted(names)
            if re.match(r"(readme|install|doc)", n, re.I)]
    if docs:
        out.append("Read: " + ", ".join(docs))
    return out


def has_cms_content(root):
    for base, _dirs, files in os.walk(root):
        for f in files:
            if re.search(r"\.(vmarc|exec|rexx|xedit)$", f, re.I):
                return True
    return False


def describe(entry, kind, files, root, owner_repo_sub):
    lines = ["", "=" * 70,
             "%s - %s" % (entry["name"], entry["desc"]),
             "Source: %s (%s)" % (entry["src"], entry["url"]), "=" * 70]
    if kind == "ibm":
        lines.append(VMARC_HOWTO if "vmarc" in files else
                     "No VMARC file: unpack the ZIP/TAR on Linux and follow "
                     "the files it contains.")
        lines.append("\nIBM's license agreement for the download library "
                     "applies; listing there is not a\nguarantee that the "
                     "package is open source - check the license inside.")
    elif kind == "github":
        owner, repo, sub = owner_repo_sub
        lines.append("Code unpacked in: %s" % root)
        note = KNOWN.get((repo, sub.split("/")[0] if sub else ""))
        if note:
            lines.append("Project-specific note:\n  " + note)
        hints = linux_hints(root)
        if hints:
            lines.append("On Linux, based on the files found:")
            lines += ["  - " + h for h in hints]
        if has_cms_content(root) or repo in ("zvm-community-tools",):
            lines.append("")
            lines.append("The tree contains CMS content (EXEC/REXX/XEDIT/"
                         "VMARC).")
            lines.append(VMARC_HOWTO)
        if not hints and not note:
            lines.append("No build files recognised; read the README in "
                         "the unpacked directory.")
    elif kind == "direct":
        lines.append(VMARC_HOWTO)
    else:
        lines.append("This entry points at a web page or directory, not a "
                     "single file:\n  %s\nOpen it and pick the file you "
                     "need." % entry["url"])
    return "\n".join(lines)


# -------------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("terms", nargs="+", help="search term(s)")
    ap.add_argument("--readme", help="use this local README.md")
    ap.add_argument("--refresh", action="store_true",
                    help="re-fetch the README instead of using the cache")
    ap.add_argument("--dest", default="zvmsw-downloads",
                    help="download directory (default: %(default)s)")
    ap.add_argument("--type", choices=["vmarc", "zip", "tar"],
                    help="for IBM packages: only this archive type")
    ap.add_argument("--name-only", action="store_true",
                    help="match package names only, not descriptions")
    args = ap.parse_args()

    entries = parse_catalog(load_readme(args.readme, args.refresh))
    if not entries:
        sys.exit("no table rows found - has the README layout changed?")
    hits = search(entries, args.terms, args.name_only)
    if not hits:
        print("No match for: %s" % " ".join(args.terms))
        return 1
    entry = pick_single(hits, args.terms)
    if entry is None:
        print("%d matches - refine the search term:" % len(hits))
        for e in hits:
            print("  %-20s %-22s %s" % (e["name"], e["src"], e["desc"][:70]))
        return 2

    kind = classify(entry["url"])
    dest = os.path.join(args.dest, re.sub(r"[^\w.$-]", "_", entry["name"]))
    os.makedirs(dest, exist_ok=True)
    print("Match: %s  [%s]" % (entry["name"], entry["src"]))
    files, root, ogs = {}, dest, None
    try:
        if kind == "ibm":
            html = http_get(IBM_LISTING_URL).decode("utf-8", "replace")
            files = ibm_files(entry["name"], html)
            if args.type:
                files = {k: v for k, v in files.items() if k == args.type}
            if not files:
                print("Could not find download links for %s on %s.\nOpen %s "
                      "in a browser." % (entry["name"], IBM_LISTING_URL,
                                         entry["url"]))
                print(describe(entry, kind, files, root, None))
                return 3
            for typ, url in files.items():
                save(url, dest, "%s.%s" % (entry["name"], typ))
        elif kind == "github":
            owner, repo, ref, sub = parse_github(entry["url"])
            ogs = (owner, repo, sub)
            url = "https://github.com/%s/%s/archive/%s.tar.gz" % (
                owner, repo, urllib.parse.quote(ref, safe=""))
            tarball = save(url, dest, "%s.tar.gz" % repo)
            root = extract_tar(tarball, dest, sub)
            print("  unpacked to %s" % root)
        elif kind == "direct":
            files = {"vmarc": entry["url"]}
            save(entry["url"], dest, entry["name"])
    except (urllib.error.URLError, OSError, RuntimeError,
            tarfile.TarError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 3

    text = describe(entry, kind, files, root, ogs)
    print(text)
    with open(os.path.join(dest, "HOWTO-INSTALL.txt"), "w") as f:
        f.write(text + "\n")
    return 0 if kind != "page" else 3


if __name__ == "__main__":
    sys.exit(main())

