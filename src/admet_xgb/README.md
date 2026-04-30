# admet-xgb

Modern ADMET predictors (XGBoost + RDKit) for:

- BBB
- CYP2C9, CYP2D6, CYP3A4 inhibition
- Pgp inhibition
- hERG inhibition
- Ames
- DILI

## Quick use

```python
from admet_xgb import score_bbb, is_bbb

score = score_bbb("CCO")
flag = is_bbb("CCO", threshold=0.5)
```

Batch:

```python
from admet_xgb import score_bbb_batch, is_bbb_batch

scores = score_bbb_batch(["CCO", "CCN"])
flags = is_bbb_batch(["CCO", "CCN"], threshold=0.5)
```
