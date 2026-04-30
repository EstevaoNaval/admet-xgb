"""Predictor classes for ADMET properties."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

import numpy as np

from .core import predict_scores


@dataclass(frozen=True)
class PropertyPredictor:
    """Base predictor for a single ADMET property."""

    task: str

    def score(self, smiles: str) -> float:
        scores, valid = predict_scores([smiles], self.task)
        if not valid:
            return float("nan")
        return float(scores[0])

    def score_batch(self, smiles_list: Iterable[str]) -> List[float]:
        smiles = list(smiles_list)
        scores, valid = predict_scores(smiles, self.task)
        out = [float("nan")] * len(smiles)
        for pos, score in zip(valid, scores):
            out[pos] = float(score)
        return out

    def is_positive(self, smiles: str, threshold: float = 0.5) -> bool:
        score = self.score(smiles)
        return bool(score >= threshold)

    def is_positive_batch(
        self, smiles_list: Iterable[str], threshold: float = 0.5
    ) -> List[bool | None]:
        smiles = list(smiles_list)
        scores, valid = predict_scores(smiles, self.task)
        out: List[bool | None] = [None] * len(smiles)
        for pos, score in zip(valid, scores):
            out[pos] = bool(score >= threshold)
        return out


class BBPPredictor(PropertyPredictor):
    pass


class CYP2C9InhibPredictor(PropertyPredictor):
    pass


class CYP2D6InhibPredictor(PropertyPredictor):
    pass


class CYP3A4InhibPredictor(PropertyPredictor):
    pass


class PgpInhibPredictor(PropertyPredictor):
    pass


class HergInhibPredictor(PropertyPredictor):
    pass


class AmesPredictor(PropertyPredictor):
    pass


class DiliPredictor(PropertyPredictor):
    pass


BBB = BBPPredictor(task="bbb_martins")
CYP2C9 = CYP2C9InhibPredictor(task="cyp2c9_veith")
CYP2D6 = CYP2D6InhibPredictor(task="cyp2d6_veith")
CYP3A4 = CYP3A4InhibPredictor(task="cyp3a4_veith")
PGP = PgpInhibPredictor(task="pgp_broccatelli")
HERG = HergInhibPredictor(task="herg")
AMES = AmesPredictor(task="ames")
DILI = DiliPredictor(task="dili")
