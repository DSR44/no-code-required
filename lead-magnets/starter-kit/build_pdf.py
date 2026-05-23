#!/usr/bin/env python3
"""Build The $0 AI Starter Kit PDF from HTML (Playwright, same as Sparklebox)."""

import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
MJS = os.path.join(BASE, "build_pdf.mjs")
PDF = os.path.join(BASE, "the-0-dollar-ai-starter-kit.pdf")


def main():
    print("Building The $0 AI Starter Kit PDF...")
    result = subprocess.run(["node", MJS], cwd=BASE, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        sys.exit(1)
    print(result.stdout.strip())
    if os.path.exists(PDF):
        print(f"Done: {PDF} ({os.path.getsize(PDF) // 1024} KB)")


if __name__ == "__main__":
    main()
