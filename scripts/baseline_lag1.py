#!/usr/bin/env python3
"""Minimal baseline: lag-1 persistence on temporal holdout (test years >= 2020)."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ceres_ai.data import load_mart
from ceres_ai.splits import lag1_predictions


def mae(y_true, y_pred) -> float:
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    if mask.sum() == 0:
        return float("nan")
    return float(np.abs(y_true[mask] - y_pred[mask]).mean())


def main() -> None:
    df = load_mart()
    df = df[df["yield_t_ha"].notna()].copy()
    df["pred_lag1"] = lag1_predictions(df)
    test = df[df["year"] >= 2020]
    score = mae(test["yield_t_ha"].values, test["pred_lag1"].values)
    print(f"Lag-1 MAE (test years >= 2020): {score:.3f} t/ha")
    print(f"Test rows: {len(test)}")


if __name__ == "__main__":
    main()
