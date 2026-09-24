#!/usr/bin/env python3
"""
Arithmetic that every 10x candidate has to survive. Standard library only.

    uv run python tools/tenx_math.py implied --mcap 2.5e9            # what 10x means in market cap
    uv run python tools/tenx_math.py cagr --multiple 10 --years 2     # required annualised return
    uv run python tools/tenx_math.py ev --p10x 0.08 --ploss 0.6 --loss 0.8   # expected value + Kelly
    uv run python tools/tenx_math.py portfolio --n 10 --p 0.08        # P(at least one 10x in n bets)

Definitions
-----------
* implied market cap: current market cap x 10. Compare with the largest companies in the same
  industry; if nobody in the industry has ever been worth that, the narrative needs to explain
  why this one will be.
* required CAGR for 10x in T years: 10**(1/T) - 1  (2 y: 216 %/y; 1 y: 900 %/y).
* three-outcome bet: with probability p10 you get +900 % (10x), with probability ploss you lose
  `loss` (e.g. 80 %), otherwise you get `mid` (default 0 %). EV per unit staked and the Kelly
  fraction (numerical maximisation of expected log wealth) tell you whether the bet is worth
  making and how big it can be. Kelly is an upper bound; half-Kelly or less is normal.
* portfolio: if you make n independent bets each with probability p of a 10x, the chance that
  at least one pays is 1 - (1-p)**n. The chance that the whole sleeve is still profitable
  depends on the loss distribution; use `ev`.
"""
from __future__ import annotations

import argparse
import math


def implied_market_cap(mcap: float, multiple: float = 10.0) -> float:
    return mcap * multiple


def required_cagr(multiple: float, years: float) -> float:
    return multiple ** (1.0 / years) - 1.0


def expected_value(p10: float, ploss: float, loss: float = 0.8, mid: float = 0.0,
                   multiple: float = 10.0) -> float:
    """Expected return per unit staked for a three-outcome bet."""
    pmid = 1.0 - p10 - ploss
    if pmid < -1e-12:
        raise ValueError("p10 + ploss must be <= 1")
    return p10 * (multiple - 1.0) + ploss * (-loss) + pmid * mid


def kelly_fraction(p10: float, ploss: float, loss: float = 0.8, mid: float = 0.0,
                   multiple: float = 10.0, grid: int = 2000) -> float:
    """Kelly fraction for the three-outcome bet by maximising E[log(1 + f*R)] on a grid."""
    pmid = 1.0 - p10 - ploss
    outcomes = [(p10, multiple - 1.0), (ploss, -loss), (pmid, mid)]
    best_f, best_g = 0.0, -math.inf
    for i in range(grid + 1):
        f = i / grid
        if f * loss >= 1.0:
            break
        g = sum(p * math.log(1.0 + f * r) for p, r in outcomes if p > 0)
        if g > best_g:
            best_f, best_g = f, g
    return best_f


def p_at_least_one(n: int, p: float) -> float:
    return 1.0 - (1.0 - p) ** n


def breakeven_p10(ploss: float, loss: float = 0.8, mid: float = 0.0, multiple: float = 10.0) -> float:
    """Probability of 10x needed for EV = 0, holding ploss fixed."""
    # p10*(m-1) - ploss*loss + (1-p10-ploss)*mid = 0
    num = ploss * loss - (1.0 - ploss) * mid
    den = (multiple - 1.0) - mid
    return num / den


def fmt_money(x: float) -> str:
    for unit, div in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if abs(x) >= div:
            return f"${x / div:,.2f}{unit}"
    return f"${x:,.0f}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("implied"); s.add_argument("--mcap", type=float, required=True)
    s.add_argument("--multiple", type=float, default=10.0)

    s = sub.add_parser("cagr"); s.add_argument("--multiple", type=float, default=10.0)
    s.add_argument("--years", type=float, default=2.0)

    s = sub.add_parser("ev"); s.add_argument("--p10x", type=float, required=True)
    s.add_argument("--ploss", type=float, required=True); s.add_argument("--loss", type=float, default=0.8)
    s.add_argument("--mid", type=float, default=0.0); s.add_argument("--multiple", type=float, default=10.0)

    s = sub.add_parser("portfolio"); s.add_argument("--n", type=int, required=True)
    s.add_argument("--p", type=float, required=True)

    a = ap.parse_args()
    if a.cmd == "implied":
        print(f"{fmt_money(a.mcap)} -> {fmt_money(implied_market_cap(a.mcap, a.multiple))} at {a.multiple:g}x")
    elif a.cmd == "cagr":
        print(f"{a.multiple:g}x in {a.years:g} y requires {required_cagr(a.multiple, a.years) * 100:.0f} %/y")
    elif a.cmd == "ev":
        ev = expected_value(a.p10x, a.ploss, a.loss, a.mid, a.multiple)
        k = kelly_fraction(a.p10x, a.ploss, a.loss, a.mid, a.multiple)
        be = breakeven_p10(a.ploss, a.loss, a.mid, a.multiple)
        print(f"EV per unit staked: {ev:+.2f}  (break-even P(10x) = {be:.3f} at P(loss)={a.ploss})")
        print(f"Kelly fraction: {k:.3f} of sleeve (half-Kelly {k / 2:.3f})")
    elif a.cmd == "portfolio":
        print(f"P(at least one 10x in {a.n} bets at p={a.p}): {p_at_least_one(a.n, a.p):.3f}")


if __name__ == "__main__":
    main()
