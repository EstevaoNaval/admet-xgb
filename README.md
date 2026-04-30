# admet-xgb

Modern ADMET predictors (XGBoost + RDKit fingerprints) for:

- BBB (blood-brain barrier)
- CYP2C9, CYP2D6, CYP3A4 inhibition
- P-gp inhibition
- hERG inhibition
- Ames
- DILI

The models are packaged in [src/admet_xgb/models](src/admet_xgb/models) and loaded on demand.

## Installation

Requires Python 3.11+ and RDKit.

From source:

```bash
pip install -e .
```

Or build/install a wheel:

```bash
pip install git+https://github.com/EstevaoNaval/admet-xgb
```

## Quick use

Single SMILES:

```python
from admet_xgb import score_bbb, is_bbb

score = score_bbb("CCO")
flag = is_bbb("CCO", threshold=0.5)
```

Batch SMILES:

```python
from admet_xgb import score_bbb_batch, is_bbb_batch

scores = score_bbb_batch(["CCO", "CCN"])
flags = is_bbb_batch(["CCO", "CCN"], threshold=0.5)
```

Other properties follow the same pattern:

- `score_cyp2c9_inhib`, `is_cyp2c9_inhib`
- `score_cyp2d6_inhib`, `is_cyp2d6_inhib`
- `score_cyp3a4_inhib`, `is_cyp3a4_inhib`
- `score_pgp_inhib`, `is_pgp_inhib`
- `score_herg_inhib`, `is_herg_inhib`
- `score_ames`, `is_ames`
- `score_dili`, `is_dili`

Batch variants are available for each property with `_batch` suffix.

## Notes

- Invalid SMILES return `nan` for scores and `None` for boolean batch flags.
- Features are MACCS (167 bits) plus Morgan (radius 2, 2048 bits).

## License

This project is licensed under the GNU Lesser General Public License - see the [LICENSE](LICENSE) file for details.

## References

Tian, H., Ketkar, R. & Tao, P. ADMETboost: a web server for accurate ADMET prediction. J Mol Model 28, 408 (2022). https://doi.org/10.1007/s00894-022-05373-8

## Sanity check

```bash
python scripts/test_admet_xgb.py
```
