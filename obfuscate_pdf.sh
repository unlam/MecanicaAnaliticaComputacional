#!/usr/bin/env bash

set -euo pipefail

usage() {
  echo "Usage: $0 <pdf_path> [dpi]"
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

INPUT="$1"
DPI="${2:-130}"

if [[ ! -f "$INPUT" ]]; then
  echo "[ERROR] File not found: $INPUT" >&2
  exit 1
fi

case "${INPUT,,}" in
  *.pdf) ;;
  *)
    echo "[ERROR] Not a PDF file: $INPUT" >&2
    exit 1
    ;;
esac

if ! command -v pdftoppm >/dev/null 2>&1; then
  echo "[ERROR] Missing dependency: pdftoppm" >&2
  exit 1
fi

if ! command -v img2pdf >/dev/null 2>&1; then
  echo "[ERROR] Missing dependency: img2pdf" >&2
  exit 1
fi

INPUT_DIR="$(dirname "$INPUT")"
BASENAME="$(basename "$INPUT")"
OUTPUT_TMP="$(mktemp --tmpdir="$INPUT_DIR" ".${BASENAME}.obfuscated.XXXXXX.pdf")"
TEMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TEMP_DIR"
  if [[ -f "$OUTPUT_TMP" ]]; then
    rm -f "$OUTPUT_TMP"
  fi
}
trap cleanup EXIT

pdftoppm -r "$DPI" "$INPUT" "$TEMP_DIR/page"

mapfile -d '' PAGE_IMAGES < <(
  find "$TEMP_DIR" -maxdepth 1 -type f -name 'page-*.ppm' -print0 | sort -zV
)

if [[ ${#PAGE_IMAGES[@]} -eq 0 ]]; then
  echo "[ERROR] No page images were generated for: $INPUT" >&2
  exit 1
fi

img2pdf "${PAGE_IMAGES[@]}" -o "$OUTPUT_TMP"

mv -f "$OUTPUT_TMP" "$INPUT"

echo "[OK] Obfuscated: $INPUT"
