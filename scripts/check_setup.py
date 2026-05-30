#!/usr/bin/env python3
"""Verify clone + data + imports. Run: python scripts/check_setup.py"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ceres_ai.data import load_mart, summarize  # noqa: E402


def main() -> int:
    print("Ceres AI setup check\n")
    mart = ROOT / "data" / "mart" / "modeling_mart.csv"
    if not mart.exists():
        print(f"FAIL: missing {mart}")
        return 1
    df = load_mart()
    print(summarize(df))
    print("\nOK — ready for Monday.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
