#!/usr/bin/env bash
#
# update-vmarc.sh
#
# Keeps execs/zvmtools.vmarc in sync with execs/*.exec.
#
# VMARC (and the "vma" CLI that manages it) has no exposed "delete member"
# option -- vma only supports "-a" (add/replace) and "-x" (extract). So
# rather than trying to patch the existing archive in place (which would
# require tracking adds/deletes/renames separately), this script always
# rebuilds zvmtools.vmarc FROM SCRATCH from whatever *.exec files currently
# exist in execs/. That one operation correctly handles all three cases
# the task asked for:
#
#   - exec ADDED    -> picked up because it matches execs/*.exec
#   - exec DELETED  -> no longer picked up, so it's absent from the rebuild
#   - exec MODIFIED -> re-added with its new content, replacing the old copy
#
# Rebuilding is deterministic: subfile timestamps in the archive come from
# each source file's own mtime, so re-running this with no underlying
# changes produces a byte-identical archive (no noisy diffs/commits).
#
# Usage:
#   ./update-vmarc.sh [execs_dir] [vma_binary]
#
# Defaults:
#   execs_dir  = <repo_root>/execs
#   vma_binary = <repo_root>/bin/vma   (built by build-vma.sh if missing)
#
# Exit codes:
#   0 = ran successfully (archive may or may not have changed)
#   1 = error (missing execs dir, no .exec files, vma failure, etc.)
#
# On success, prints "CHANGED" or "UNCHANGED" to stdout on the last line
# so callers (e.g. a CI workflow) can decide whether to commit.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
VMA="$REPO_ROOT/bin/vma"

EXECS_DIR="${1:-${REPO_ROOT}/execs}"
# VMA_BIN="${2:-${REPO_ROOT}/bin/vma}"
ARCHIVE_NAME="zvmtools.vmarc"
ARCHIVE_PATH="${EXECS_DIR}/${ARCHIVE_NAME}"

if [[ ! -d "${EXECS_DIR}" ]]; then
    echo "error: execs directory not found: ${EXECS_DIR}" >&2
    exit 1
fi

# Build vma on demand if it isn't already available.
if [[ ! -x "${VMA}" ]]; then
    echo "vma binary not found at ${VMA}; building it..."
    "${SCRIPT_DIR}/build-vma.sh" "${VMA}"
fi

shopt -s nullglob
execs=("${EXECS_DIR}"/*.exec)
shopt -u nullglob

if [[ ${#execs[@]} -eq 0 ]]; then
    echo "error: no .exec files found in ${EXECS_DIR}" >&2
    exit 1
fi

echo "Found ${#execs[@]} exec(s) in ${EXECS_DIR}."

# Snapshot the old archive (if any) so we can tell the caller whether
# anything actually changed.
OLD_HASH=""
if [[ -f "${ARCHIVE_PATH}" ]]; then
    OLD_HASH="$(sha256sum "${ARCHIVE_PATH}" | awk '{print $1}')"
fi

WORK_ARCHIVE="$(mktemp -u "${EXECS_DIR}/.zvmtools.XXXXXX.vmarc")"

# Build the new archive from scratch in a temp file:
#   -a  add files
#   -t  translate text to EBCDIC on add (these are REXX source execs)
# vma derives the stored CMS filename/filetype from each disk filename's
# own "name.ext" (e.g. calc.exec -> CALC EXEC), uppercasing automatically.
pushd "${EXECS_DIR}" >/dev/null
"${VMA}" -a -t "${WORK_ARCHIVE}" *.exec
popd >/dev/null

NEW_HASH="$(sha256sum "${WORK_ARCHIVE}" | awk '{print $1}')"

mv -f "${WORK_ARCHIVE}" "${ARCHIVE_PATH}"

if [[ "${OLD_HASH}" == "${NEW_HASH}" ]]; then
    echo "Archive unchanged: ${ARCHIVE_PATH}"
    echo "UNCHANGED"
else
    echo "Archive rebuilt: ${ARCHIVE_PATH}"
    "${VMA}" "${ARCHIVE_PATH}"
    echo "CHANGED"
fi
