# Reference repository (not team remote)

**Path (local):** `C:\Users\stani\Documents\ml-farm-recolt-forecast`

Use it as a **lab / conception dividend** — ETL, satellite download, Gradio explorer, QA agent, HF Space experiments.

**Team works in:** `ceres-ai` (this repo).

## When to touch legacy

| Need | Legacy command / path |
|------|-------------------------|
| Refresh Agreste labels | `py scripts/ingest_agreste_saa.py` |
| Rebuild mart + DB | `py scripts/export_modeling_dataframe.py --rebuild-db` |
| Copy mart here | `data/processed/modeling_mart.csv` → `ceres-ai/data/mart/` |
| Daily weather | `data/raw/weather/meteostat_daily_by_department.parquet` |
| Satellite ingest | `scripts/run_satellite_backfill.py` |
| Full architecture docs | `docs/PROJECT_DOCUMENTATION.md` |
| Imaging roadmap | `docs/SATELLITE_IMAGING_ROADMAP.md` |

Do **not** ask the team to clone legacy on day 1 unless they own a specific pull task.
