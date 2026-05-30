# Optional datasets (not required for Week 1)

| File | Rows | Purpose |
|------|------|---------|
| `yield_agreste_saa.parquet` | 1,380 | Labels only — same as most of mart |
| `yield_pik_1900_2018.parquet` | 11,537 | Long history 1900–2018 — robustness / pretrain |

```python
from ceres_ai.data import load_optional_pik
```

## Larger pulls (gitignored — add locally)

Create folders and copy from legacy repo:

- `weather_daily/` ← `meteostat_daily_by_department.parquet` (~2.3M rows, **~large**)
- `satellite/` ← MODIS / S2 parquets

See `docs/DATA_SCALE.md`.
