#!/usr/bin/env python3
"""Quick validation for admet_xgb API (single + batch)."""

from __future__ import annotations

import time

from admet_xgb import (
    score_ames,
    score_bbb,
    score_cyp2c9_inhib,
    score_cyp2d6_inhib,
    score_cyp3a4_inhib,
    score_dili,
    score_herg_inhib,
    score_pgp_inhib,
    is_ames,
    is_bbb,
    is_cyp2c9_inhib,
    is_cyp2d6_inhib,
    is_cyp3a4_inhib,
    is_dili,
    is_herg_inhib,
    is_pgp_inhib,
    score_ames_batch,
    score_bbb_batch,
    score_cyp2c9_inhib_batch,
    score_cyp2d6_inhib_batch,
    score_cyp3a4_inhib_batch,
    score_dili_batch,
    score_herg_inhib_batch,
    score_pgp_inhib_batch,
    is_ames_batch,
    is_bbb_batch,
    is_cyp2c9_inhib_batch,
    is_cyp2d6_inhib_batch,
    is_cyp3a4_inhib_batch,
    is_dili_batch,
    is_herg_inhib_batch,
    is_pgp_inhib_batch,
)

SINGLE = "O=C1CN=C(c2ccccc2Cl)c2cc([N+](=O)[O-])ccc2N1"
BATCH = [
    "O=C1Nc2ccc(Cl)cc2C(c2ccccc2Cl)=NC1O",
    "c1ccccc1N2N(C)C(C)=C(C2=O)N(C)CS(=O)(=O)O",
    "COC(=O)Nc3nc2ccc(C(=O)c1ccccc1)cc2[nH]3",
    "O=C(CC)N(C1CCN(CC1)CCc2ccccc2)c3ccccc3",
    "ClC1=CC=C([C@H]2C3=C([C@H](CC2)NC)C=CC=C3)C=C1Cl",
]


def print_single() -> None:
    print("Single SMILES:", SINGLE)
    print("bbb:", score_bbb(SINGLE), is_bbb(SINGLE))
    print("cyp2c9_inhib:", score_cyp2c9_inhib(SINGLE), is_cyp2c9_inhib(SINGLE))
    print("cyp2d6_inhib:", score_cyp2d6_inhib(SINGLE), is_cyp2d6_inhib(SINGLE))
    print("cyp3a4_inhib:", score_cyp3a4_inhib(SINGLE), is_cyp3a4_inhib(SINGLE))
    print("pgp_inhib:", score_pgp_inhib(SINGLE), is_pgp_inhib(SINGLE))
    print("herg_inhib:", score_herg_inhib(SINGLE), is_herg_inhib(SINGLE))
    print("ames:", score_ames(SINGLE), is_ames(SINGLE))
    print("dili:", score_dili(SINGLE), is_dili(SINGLE))


def print_batch() -> None:
    print("Batch SMILES:", BATCH)
    print("bbb:", score_bbb_batch(BATCH), is_bbb_batch(BATCH))
    print(
        "cyp2c9_inhib:", score_cyp2c9_inhib_batch(BATCH), is_cyp2c9_inhib_batch(BATCH)
    )
    print(
        "cyp2d6_inhib:", score_cyp2d6_inhib_batch(BATCH), is_cyp2d6_inhib_batch(BATCH)
    )
    print(
        "cyp3a4_inhib:", score_cyp3a4_inhib_batch(BATCH), is_cyp3a4_inhib_batch(BATCH)
    )
    print("pgp_inhib:", score_pgp_inhib_batch(BATCH), is_pgp_inhib_batch(BATCH))
    print("herg_inhib:", score_herg_inhib_batch(BATCH), is_herg_inhib_batch(BATCH))
    print("ames:", score_ames_batch(BATCH), is_ames_batch(BATCH))
    print("dili:", score_dili_batch(BATCH), is_dili_batch(BATCH))


if __name__ == "__main__":
    print_single()
    t0 = time.perf_counter()
    print_batch()
    elapsed = time.perf_counter() - t0
    per_chem = elapsed / max(1, len(BATCH))
    print(f"Batch runtime: {elapsed:.4f}s total, {per_chem:.4f}s per chemical")
