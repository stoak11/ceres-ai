# Data scale — what you have vs how to go wider

**MVP prediction unit:** department × year (~**1,400** labeled points).  
That is the **hard ceiling** for independent yield labels in France at this grain.

You already have **much more material** at other resolutions — use them for **features** and **research**, not fake extra labels.

---

## Tier 0 — Shipped in this repo (start Monday)

| Asset | Rows | Path |
|-------|------|------|
| Modeling mart | 1,425 | `data/mart/modeling_mart.csv` |
| Dept centroids | 95 | `config/departments_france.csv` |
| Agreste labels (optional) | 1,380 | `data/optional/yield_agreste_saa.parquet` |
| PIK labels (optional) | 11,537 | `data/optional/yield_pik_1900_2018.parquet` |

```python
from ceres_ai.data import load_mart, load_optional_pik
```

---

## Tier 1 — Wider **time** (same dept grain)

| Source | Rows | Years | Use |
|--------|------|-------|-----|
| Agreste (mart) | ~1,380 | 2010–2024 | **MVP labels** |
| PIK / GFZ | **~11,500** | **1900–2018** | Long-history baselines, pretrain, robustness tests |

**Caution:** PIK ≠ Agreste definition. Do not merge blindly for 2019+ claims.

**How to get:** already in `data/optional/`. Refresh from legacy: `wheat_yield_department.parquet`.

---

## Tier 2 — Richer **inputs** (same 1,400 labels)

Pull from **legacy repo** (`ml-farm-recolt-forecast`) — **do not commit multi-GB files here** without Git LFS.

| Layer | ~Rows | Use |
|-------|-------|-----|
| Weather **daily** | **~2.3M** | LSTM / TFT; sequence → one yield |
| Weather monthly | 17,100 | Custom seasonal windows |
| MODIS 16-day NDVI | 11,400 | Phenology curves |
| S2 NDVI monthly | 3,800 | Finer vegetation |
| S2 scene catalog | 24,642 | Compositing metadata |

**Legacy paths:**

- `data/raw/weather/meteostat_daily_by_department.parquet`
- `data/raw/satellite/modis/modis_ndvi_16day_by_department.parquet`

**Pattern:** 1,400 **targets**, millions of **timesteps** — valid if eval uses group splits by dept/year.

---

## Tier 3 — Spatial / vision (post-MVP)

| Approach | Volume | Doc |
|----------|--------|-----|
| Zonal NDVI over dept polygon | same n, better signal | legacy `SATELLITE_IMAGING_ROADMAP.md` |
| S2 chips + CNN | 10⁴+ patches | same |

---

## Tier 4 — Geography / crops (scope change)

- EU / MARS regions — transfer learning  
- Other Agreste crops — multi-task (~1,380 × crops)

---

## Decision tree

```
Need more rows for ML?
├─ Same dept×year labels? → You can't (max ~1,425 France wheat)
├─ Richer features?       → Tier 2 (daily weather, NDVI series)
├─ Longer history?        → Tier 1 (PIK 1900–2018)
├─ Images?                → Tier 3 (chips — not MVP)
└─ More countries/crops?    → Tier 4 (new project phase)
```

---

## What **not** to do

- Treat 12 monthly weather rows as 12× more yield samples (leakage)  
- 95 separate dept models on ~15 points each (overfit)  
- Report holdout MAE without lag-1 baseline  

See `config/eval.yaml` for the team contract.
