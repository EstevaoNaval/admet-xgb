"""Public API functions for ADMET predictions."""

from __future__ import annotations

from typing import Iterable, List

from .predictors import AMES, BBB, CYP2C9, CYP2D6, CYP3A4, DILI, HERG, PGP


def score_bbb(smiles: str) -> float:
    return BBB.score(smiles)


def score_cyp2c9_inhib(smiles: str) -> float:
    return CYP2C9.score(smiles)


def score_cyp2d6_inhib(smiles: str) -> float:
    return CYP2D6.score(smiles)


def score_cyp3a4_inhib(smiles: str) -> float:
    return CYP3A4.score(smiles)


def score_pgp_inhib(smiles: str) -> float:
    return PGP.score(smiles)


def score_herg_inhib(smiles: str) -> float:
    return HERG.score(smiles)


def score_ames(smiles: str) -> float:
    return AMES.score(smiles)


def score_dili(smiles: str) -> float:
    return DILI.score(smiles)


def is_bbb(smiles: str, threshold: float = 0.5) -> bool:
    return BBB.is_positive(smiles, threshold=threshold)


def is_cyp2c9_inhib(smiles: str, threshold: float = 0.5) -> bool:
    return CYP2C9.is_positive(smiles, threshold=threshold)


def is_cyp2d6_inhib(smiles: str, threshold: float = 0.5) -> bool:
    return CYP2D6.is_positive(smiles, threshold=threshold)


def is_cyp3a4_inhib(smiles: str, threshold: float = 0.5) -> bool:
    return CYP3A4.is_positive(smiles, threshold=threshold)


def is_pgp_inhib(smiles: str, threshold: float = 0.5) -> bool:
    return PGP.is_positive(smiles, threshold=threshold)


def is_herg_inhib(smiles: str, threshold: float = 0.5) -> bool:
    return HERG.is_positive(smiles, threshold=threshold)


def is_ames(smiles: str, threshold: float = 0.5) -> bool:
    return AMES.is_positive(smiles, threshold=threshold)


def is_dili(smiles: str, threshold: float = 0.5) -> bool:
    return DILI.is_positive(smiles, threshold=threshold)


def score_bbb_batch(smiles_list: Iterable[str]) -> List[float]:
    return BBB.score_batch(smiles_list)


def score_cyp2c9_inhib_batch(smiles_list: Iterable[str]) -> List[float]:
    return CYP2C9.score_batch(smiles_list)


def score_cyp2d6_inhib_batch(smiles_list: Iterable[str]) -> List[float]:
    return CYP2D6.score_batch(smiles_list)


def score_cyp3a4_inhib_batch(smiles_list: Iterable[str]) -> List[float]:
    return CYP3A4.score_batch(smiles_list)


def score_pgp_inhib_batch(smiles_list: Iterable[str]) -> List[float]:
    return PGP.score_batch(smiles_list)


def score_herg_inhib_batch(smiles_list: Iterable[str]) -> List[float]:
    return HERG.score_batch(smiles_list)


def score_ames_batch(smiles_list: Iterable[str]) -> List[float]:
    return AMES.score_batch(smiles_list)


def score_dili_batch(smiles_list: Iterable[str]) -> List[float]:
    return DILI.score_batch(smiles_list)


def is_bbb_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return BBB.is_positive_batch(smiles_list, threshold=threshold)


def is_cyp2c9_inhib_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return CYP2C9.is_positive_batch(smiles_list, threshold=threshold)


def is_cyp2d6_inhib_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return CYP2D6.is_positive_batch(smiles_list, threshold=threshold)


def is_cyp3a4_inhib_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return CYP3A4.is_positive_batch(smiles_list, threshold=threshold)


def is_pgp_inhib_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return PGP.is_positive_batch(smiles_list, threshold=threshold)


def is_herg_inhib_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return HERG.is_positive_batch(smiles_list, threshold=threshold)


def is_ames_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return AMES.is_positive_batch(smiles_list, threshold=threshold)


def is_dili_batch(
    smiles_list: Iterable[str], threshold: float = 0.5
) -> List[bool | None]:
    return DILI.is_positive_batch(smiles_list, threshold=threshold)
