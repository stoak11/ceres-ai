# Ceres AI

Indicative **soft-wheat yield** (t/ha) for France at **department × harvest year** scale.  
Le Wagon MVP — team-owned repo (14 days).

**Labels:** Agreste SAA (primary) · **Features:** weather, soil, fused NDVI (planting season)  
**Grain:** 95 departments · 2010–2024 · **~1,419** labeled rows

---

## Quick start (Monday)

```powershell
git clone https://github.com/stoak11/ceres-ai.git
cd ceres-ai
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python scripts/check_setup.py
python scripts/baseline_lag1.py
```

```python
# Notebook / REPL
import sys; sys.path.insert(0, "src")
from ceres_ai.data import load_mart, summarize
print(summarize())
df = load_mart()
```

---

## Repo layout

```
ceres-ai/
├── data/mart/modeling_mart.csv    # ← start here (DATA_CARD.md)
├── data/optional/                 # PIK 1900–2018, Agreste labels
├── config/departments_france.csv
├── config/eval.yaml                 # eval contract
├── src/ceres_ai/                    # load_mart, splits
├── scripts/                         # check_setup, baseline_lag1
├── notebooks/01_mart_overview.ipynb
└── docs/KICKOFF.md                  # Monday agenda
```

---

## MVP checklist

See `docs/KICKOFF.md`.

---

## License

MIT