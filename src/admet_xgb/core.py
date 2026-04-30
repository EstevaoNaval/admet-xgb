"""Core utilities for ADMET XGBoost predictors."""

from __future__ import annotations

import json
from functools import lru_cache
from importlib.resources import files
from pathlib import Path
from typing import Iterable, List, Tuple

import numpy as np
import xgboost as xgb
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem, MACCSkeys

RDLogger.DisableLog("rdApp.*")

MODELS_DIR = files("admet_xgb").joinpath("models")


def smiles_to_features(smiles_list: Iterable[str]) -> Tuple[np.ndarray, List[int]]:
    """Convert SMILES list to fixed-size feature vectors.

    Features:
    - MACCS (167 bits)
    - Morgan radius=2, nBits=2048
    Final size: 2215
    """
    feats: List[np.ndarray] = []
    valid_idx: List[int] = []

    for idx, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(str(smi))
        if mol is None:
            continue

        maccs = np.array(list(MACCSkeys.GenMACCSKeys(mol)), dtype=np.float32)
        morgan = np.array(
            list(AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)),
            dtype=np.float32,
        )
        feats.append(np.concatenate([maccs, morgan], axis=0))
        valid_idx.append(idx)

    if not feats:
        raise ValueError("No valid SMILES were parsed. Check your input.")

    return np.vstack(feats), valid_idx


def _model_path(task: str) -> Path:
    return Path(MODELS_DIR / f"{task}_modern_xgb.json")


def _meta_path(task: str) -> Path:
    return Path(MODELS_DIR / f"{task}_modern_xgb.meta.json")


def _load_metadata(task: str) -> dict:
    meta_path = _meta_path(task)
    return json.loads(meta_path.read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def load_task_model(task: str) -> tuple[object, dict]:
    """Load a task model + metadata with caching."""
    meta = _load_metadata(task)
    task_type = meta["task_type"]
    model_path = _model_path(task)

    if task_type == "binary":
        model: object = xgb.XGBClassifier()
    else:
        model = xgb.XGBRegressor()

    model.load_model(str(model_path))
    return model, meta


def predict_scores(
    smiles_list: Iterable[str], task: str
) -> Tuple[np.ndarray, List[int]]:
    """Return scores for a list of SMILES and the valid indices."""
    X, valid_idx = smiles_to_features(smiles_list)
    model, meta = load_task_model(task)
    expected = int(meta["n_features"])

    if X.shape[1] != expected:
        raise ValueError(
            f"Feature mismatch: model expects {expected}, got {X.shape[1]}"
        )

    if meta["task_type"] == "binary":
        score = model.predict_proba(X)[:, 1]
    else:
        score = model.predict(X)

    return np.asarray(score, dtype=np.float64), valid_idx
