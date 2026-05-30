# Data card — `modeling_mart.csv`

**Grain:** one row = **one French department × one harvest year**  
**Primary target:** `yield_t_ha` (soft wheat, t/ha)  
**Rows:** 1,425 (95 depts × 15 years, 2010–2024)  
**Rows with yield:** 1,419  

## Label provenance (in this file)

| `yield_source` | Rows | Notes |
|----------------|------|--------|
| `agreste_saa` | 1,380 | Official dept-native (primary) |
| `eurostat_apro_cpshr_subnational` | 30 | Gap-fill only |
| `pik_france_county_1900_2018` | 10 | Overlap / legacy bridge |
| missing | 5 | No label |

## Feature columns (planting-season + static)

| Column | Description |
|--------|-------------|
| `ps_tavg_c`, `ps_tmin_c`, `ps_tmax_c`, `ps_prcp_mm`, `ps_et0_mm` | Weather aggregates (planting months Sep–Dec) |
| `clay_g_kg`, `sand_g_kg`, `silt_g_kg`, `phh2o`, `soc_dg_kg` | SoilGrids @ dept centroid |
| `ps_ndvi_fused`, `ndvi_source` | Fused NDVI (S2 > MODIS > Copernicus proxy) |
| `spring_*`, `summer_*`, `gdd_*`, `drought_spring_flag` | Extended seasonal features |

## What this file is **not**

- Not daily weather (see `docs/DATA_SCALE.md`)
- Not satellite imagery (only scalar NDVI per year)
- Not commune-level

## Refresh from legacy repo

If labels or features need updating, re-export from the reference repo:

```powershell
# In ml-farm-recolt-forecast (reference only)
py scripts/ingest_agreste_saa.py
py scripts/export_modeling_dataframe.py --rebuild-db
# Copy data/processed/modeling_mart.csv → this repo data/mart/
```
