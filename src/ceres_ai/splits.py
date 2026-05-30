"""Temporal train/test splits (no random shuffle)."""
from __future__ import annotations

import pandas as pd


def temporal_holdout(
    df: pd.DataFrame,
    *,
    train_years_max: int = 2019,
    test_years_min: int = 2020,
    require_yield: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    out = df.copy()
    if require_yield and "yield_t_ha" in out.columns:
        out = out[out["yield_t_ha"].notna()]
    train = out[out["year"] <= train_years_max]
    test = out[out["year"] >= test_years_min]
    return train, test


def lag1_predictions(df: pd.DataFrame) -> pd.Series:
    """Persistence: previous year's yield per department."""
    d = df.sort_values(["department_code", "year"])
    return d.groupby("department_code")["yield_t_ha"].shift(1)
