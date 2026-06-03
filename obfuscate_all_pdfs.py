#!/usr/bin/env python3
"""Obfuscate every PDF in a repository by rasterizing and rebuilding it."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find all PDFs in a repo and obfuscate each one in place."
    )
    parser.add_argument(
        "repo_root",
        nargs="?",
        default=".",
        help="Repository root to scan (default: current directory).",
    )
    parser.add_argument(
        "--script",
        default="obfuscate_pdf.sh",
        help="Path to the per-file obfuscation bash script.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=130,
        help="Rasterization DPI passed to the bash script (default: 130).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print matching PDFs without modifying them.",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Keep processing remaining PDFs after an error.",
    )
    return parser.parse_args()


def find_pdfs(repo_root: Path) -> list[Path]:
    return sorted(path for path in repo_root.rglob("*.pdf") if path.is_file())


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    script_path = Path(args.script)
    if not script_path.is_absolute():
        script_path = (repo_root / script_path).resolve()

    if not script_path.is_file():
        print(f"[ERROR] Script not found: {script_path}")
        return 1

    pdfs = find_pdfs(repo_root)
    if not pdfs:
        print(f"No PDF files found under {repo_root}")
        return 0

    print(f"Found {len(pdfs)} PDF files under {repo_root}")
    failed = 0

    for pdf_path in pdfs:
        if args.dry_run:
            print(f"[DRY-RUN] Would obfuscate: {pdf_path}")
            continue

        print(f"[RUN] {pdf_path}")
        result = subprocess.run(
            [str(script_path), str(pdf_path), str(args.dpi)],
            text=True,
            capture_output=True,
            check=False,
        )

        if result.returncode != 0:
            failed += 1
            if result.stdout.strip():
                print(result.stdout.strip())
            if result.stderr.strip():
                print(result.stderr.strip())
            print(f"[FAILED] {pdf_path}")
            if not args.continue_on_error:
                print("Stopping on first error. Use --continue-on-error to keep going.")
                return 1
            continue

        if result.stdout.strip():
            print(result.stdout.strip())

    if failed:
        print(f"Completed with failures: {failed} of {len(pdfs)} PDFs failed.")
        return 1

    print(f"Done. Successfully processed {len(pdfs)} PDFs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
