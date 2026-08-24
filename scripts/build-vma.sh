#!/usr/bin/env bash
#
# build-vma.sh
#
# Fetches and builds the "vma" command-line utility (list/extract/create
# VMARC archives), used by update-vmarc.sh to maintain execs/zvmtools.vmarc.
#
# vma's homepage (https://www.homerow.net/zvm/vma/) only ships source
# tarballs/binaries for interactive download, so for CI/automation we build
# the CLI tool directly from Leland Lucius's public-domain source, mirrored
# on GitHub. Only vma.c/vmalib.c (the CLI) are compiled -- the wxWidgets GUI
# (vmagui) is not needed and is skipped.
#
# Usage:
#   ./build-vma.sh [output_path]
#
# Default output_path is ./bin/vma relative to the repo root this script
# lives in (i.e. <repo>/bin/vma).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OUT_BIN="${1:-${REPO_ROOT}/bin/vma}"

VMA_SRC_REPO="https://github.com/moshix/vmarcUNIX.git"

if [[ -x "${OUT_BIN}" ]]; then
    echo "vma already built at ${OUT_BIN}, skipping build."
    exit 0
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "${WORKDIR}"' EXIT

echo "Fetching vma source from ${VMA_SRC_REPO} ..."
git clone --depth 1 "${VMA_SRC_REPO}" "${WORKDIR}/vmarcUNIX" >/dev/null 2>&1

echo "Compiling vma CLI ..."
mkdir -p "$(dirname "${OUT_BIN}")"
cc -O2 -D_ALL_SOURCE \
    -o "${OUT_BIN}" \
    "${WORKDIR}/vmarcUNIX/src/vma.c" \
    "${WORKDIR}/vmarcUNIX/src/vmalib.c"

chmod +x "${OUT_BIN}"
echo "Built ${OUT_BIN}:"
"${OUT_BIN}" -V
