"""Load the modeling mart and optional label extensions."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
MART_CSV = ROOT / "data" / "mart" / "modeling_mart.csv"
OPTIONAL = ROOT / "data" / "optional"


def mart_path() -> Path:
    return MART_CSV


def load_mart() -> pd.DataFrame:
    """Dept × year table (primary modeling grain)."""
    df = pd.read_csv(MART_CSV)
    if "department_code" in df.columns:
        df["department_code"] = df["department_code"].astype(str).str.zfill(2)
    return df


@lru_cache(maxsize=1)
def load_optional_pik() -> pd.DataFrame:
    """PIK county-level yields 1900–2018 (~11.5k rows). See docs/DATA_SCALE.md."""
    p = OPTIONAL / "yield_pik_1900_2018.parquet"
    if not p.exists():
        raise FileNotFoundError(f"Missing {p}")
    df = pd.read_parquet(p)
    if "department_code" in df.columns:
        df["department_code"] = df["department_code"].astype(str).str.zfill(2)
    return df


@lru_cache(maxsize=1)
def load_optional_agreste_labels() -> pd.DataFrame:
    """Agreste SAA labels only (~1.38k rows). Subset of mart provenance."""
    p = OPTIONAL / "yield_agreste_saa.parquet"
    if not p.exists():
        raise FileNotFoundError(f"Missing {p}")
    return pd.read_parquet(p)


def summarize(df: pd.DataFrame | None = None) -> str:
    df = df if df is not None else load_mart()
    lines = [
        f"shape: {df.shape[0]} rows × {df.shape[1]} cols",
        f"years: {df['year'].min()}–{df['year'].max()}",
        f"departments: {df['department_code'].nunique()}",
    ]
    if "yield_t_ha" in df.columns:
        n = int(df["yield_t_ha"].notna().sum())
        lines.append(f"rows with yield: {n}")
    if "yield_source" in df.columns:
        lines.append("yield_source:\n" + df["yield_source"].value_counts().to_string())
    return "\n".join(lines)
