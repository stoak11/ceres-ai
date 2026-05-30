# Monday kickoff — Ceres AI (14 days)

**Team:** 4 · **Repo:** this repository only (team-owned)  
**Reference (conception / ETL lab):** `ml-farm-recolt-forecast` on Stan's machine — not the source of truth for commits.

---

## North star (one sentence)

**One national model, one temporal eval story, one demo with a France map — everything else is a GitHub issue after Demo Day.**

---

## MVP done = 

- [ ] Everyone runs `python scripts/check_setup.py`
- [ ] Everyone runs `python scripts/baseline_lag1.py` and gets ~same MAE
- [ ] Eval protocol agreed (`config/eval.yaml`)
- [ ] One tabular model (HistGB or Ridge) + feature ablation
- [ ] Short eval note (what beats lag-1, what doesn't)
- [ ] Demo: dept + year → prediction + drivers + map (Week 2)

**Out of scope:** 95 dept models, full S2 CNN, production API, metric bragging without forward check.

---

## Monday agenda (90 min)

| When | What |
|------|------|
| 0:00 | Problem, MVP, non-goals |
| 0:15 | Clone repo, `pip install -r requirements.txt`, `check_setup.py` |
| 0:30 | Walk through `data/mart/DATA_CARD.md` + `docs/DATA_SCALE.md` |
| 0:45 | Sign off `config/eval.yaml` |
| 1:00 | GitHub: 5 issues, branch rules |
| 1:15 | First PR: reproduce lag-1 baseline |

---

## GitHub hygiene

- `main` protected · PRs from `feat/*`
- One line per experiment in `docs/EXPERIMENT_LOG.md`
- No secrets in repo

---

## Stretch (only if core is green)

- NUTS2-level ensemble (not 95 dept models)
- Pull daily weather from legacy into `data/optional/weather_daily/` (gitignored)
- Gradio demo in `apps/` (Week 2)

---

## CEO (Stan)

- Integration + eval discipline + demo polish  
- Legacy repo for heavy ETL only — export fresh `modeling_mart.csv` when data changes
