#!/usr/bin/env python3
"""
options_10x.py -- how big an underlying move is needed to turn a leveraged
instrument into a 10x, and how likely that is under a lognormal model.

Sections
  1. LEAPS (long-dated OTM calls): Black-Scholes, strike solved from target
     delta; required underlying return for 10x AT EXPIRY; probability under a
     lognormal with a stated real-world drift; P(expire worthless); expected
     multiple; Monte-Carlo probability of the option's mark-to-market value
     TOUCHING 10x at any point before expiry.
  2. Daily-rebalanced leveraged ETFs: continuous-time approximation
        ln(L_T/L_0) ~= L*ln(S_T/S_0) - (L^2-L)/2 * sigma^2 * T - costs*T
     giving the variance-drag table and worked scenarios.
  3. Perpetual futures / margin: liquidation thresholds, funding drag, and the
     reflection-principle probability that a driftless lognormal path touches
     the liquidation barrier before horizon T.

Everything here is model output, not data. No market prices are used.
Run:  python3 tools/options_10x.py            (prints markdown tables)
Deps: numpy, scipy
"""
from __future__ import annotations

import math
import sys

import numpy as np
from scipy.stats import norm

R_RISKFREE = 0.04  # continuously compounded risk-free rate assumption (stated, not fetched)


# ----------------------------------------------------------------------------
# 1. Black-Scholes helpers
# ----------------------------------------------------------------------------
def bs_call(S, K, T, r, sigma):
    if T <= 0:
        return max(S - K, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)


def bs_call_vec(S, K, T, r, sigma):
    """Vectorised over S and T (numpy arrays), scalar K/r/sigma."""
    S = np.asarray(S, dtype=float)
    T = np.asarray(T, dtype=float)
    out = np.maximum(S - K, 0.0)
    live = T > 1e-12
    if np.any(live):
        Tl = T[live] if T.shape == S.shape else T
        Sl = S[live]
        d1 = (np.log(Sl / K) + (r + 0.5 * sigma**2) * Tl) / (sigma * np.sqrt(Tl))
        d2 = d1 - sigma * np.sqrt(Tl)
        out[live] = Sl * norm.cdf(d1) - K * np.exp(-r * Tl) * norm.cdf(d2)
    return out


def strike_for_delta(S, T, r, sigma, delta):
    """Closed form: delta = N(d1)  =>  K = S*exp((r + sigma^2/2)T - N^-1(delta)*sigma*sqrt(T))."""
    d1 = norm.ppf(delta)
    return S * math.exp((r + 0.5 * sigma**2) * T - d1 * sigma * math.sqrt(T))


def prob_above(S0, level, T, sigma, mu_total):
    """P(S_T >= level) when E[S_T] = S0*exp(mu_total*T), lognormal with vol sigma."""
    z = (math.log(S0 / level) + (mu_total - 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    return norm.cdf(z)


def expected_call_payoff(S0, K, T, sigma, mu_total):
    """E[max(S_T-K,0)] under lognormal with E[S_T]=S0*e^{mu T}."""
    F = S0 * math.exp(mu_total * T)
    d1 = (math.log(F / K) + 0.5 * sigma**2 * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return F * norm.cdf(d1) - K * norm.cdf(d2)


def mc_touch_10x(S0, K, T, r, sigma, mu_total, c0, target=10.0, n_paths=20000, steps_per_year=252, seed=1):
    """Probability that the BS mark-to-market of the call reaches target*c0 at
    any daily close before expiry (path-dependent 'take profit' probability),
    plus probability that the option is >= target*c0 at expiry only."""
    rng = np.random.default_rng(seed)
    n_steps = int(round(T * steps_per_year))
    dt = T / n_steps
    drift = (mu_total - 0.5 * sigma**2) * dt
    vol = sigma * math.sqrt(dt)
    logS = np.full(n_paths, math.log(S0))
    touched = np.zeros(n_paths, dtype=bool)
    for i in range(1, n_steps + 1):
        logS += drift + vol * rng.standard_normal(n_paths)
        tau = T - i * dt
        val = bs_call_vec(np.exp(logS), K, np.full(n_paths, max(tau, 0.0)), r, sigma)
        touched |= val >= target * c0
    S_T = np.exp(logS)
    at_expiry = np.maximum(S_T - K, 0.0) >= target * c0
    return touched.mean(), at_expiry.mean()


def leaps_table(S0=100.0, deltas=(0.10, 0.20, 0.30), ivs=(0.40, 0.60, 0.80, 1.00),
                tenors=(1.0, 2.0), r=R_RISKFREE, drifts=(0.0, 0.10), mc=True):
    rows = []
    print("### LEAPS: underlying return needed for 10x at expiry, and its probability\n")
    print("Assumptions: Black-Scholes, r = %.0f%% (continuous), no dividends, no bid/ask, "
          "European exercise at expiry. Strike solved from target delta. "
          "Drift columns: real-world expected annual return of the underlying "
          "(0%% = no edge; +10%% = generous equity premium). Lognormal with the same "
          "sigma as the IV, i.e. the market's vol is assumed correct (no vol premium)."
          % (r * 100))
    print()
    hdr = ("| T (yr) | IV | delta | K/S0 | premium (% of S0) | breakeven ret. | "
           "**ret. for 10x** | sigma-units of ret. | P(10x at expiry) drift 0% | "
           "P(10x at expiry) drift +10% | P(touch 10x MTM, drift +10%) | P(expire worthless, drift +10%) | "
           "E[multiple] drift +10% |")
    print(hdr)
    print("|" + "---|" * 13)
    for T in tenors:
        for iv in ivs:
            for d in deltas:
                K = strike_for_delta(S0, T, r, iv, d)
                c0 = bs_call(S0, K, T, r, iv)
                s_star = K + 10.0 * c0
                ret10 = s_star / S0 - 1.0
                breakeven = (K + c0) / S0 - 1.0
                sig_units = math.log(s_star / S0) / (iv * math.sqrt(T))
                p0 = prob_above(S0, s_star, T, iv, drifts[0])
                p1 = prob_above(S0, s_star, T, iv, drifts[1])
                p_worthless = 1.0 - prob_above(S0, K, T, iv, drifts[1])
                e_mult = expected_call_payoff(S0, K, T, iv, drifts[1]) / c0
                if mc:
                    p_touch, _ = mc_touch_10x(S0, K, T, r, iv, drifts[1], c0)
                else:
                    p_touch = float("nan")
                rows.append(dict(T=T, iv=iv, delta=d, K=K, c0=c0, ret10=ret10, p0=p0, p1=p1,
                                 p_touch=p_touch, p_worthless=p_worthless, e_mult=e_mult))
                print("| %.0f | %.0f%% | %.2f | %.2f | %.1f%% | %+.0f%% | **%+.0f%%** | %.2f | %.1f%% | %.1f%% | %.1f%% | %.0f%% | %.2fx |"
                      % (T, iv * 100, d, K / S0, c0 / S0 * 100, breakeven * 100, ret10 * 100,
                         sig_units, p0 * 100, p1 * 100, p_touch * 100, p_worthless * 100, e_mult))
    print()
    return rows


def leaps_given_move(S0=100.0, moves=(1.0, 2.0, 3.0), ivs=(0.40, 0.60, 0.80, 1.00),
                     deltas=(0.10, 0.20, 0.30), T=1.0, r=R_RISKFREE):
    print("### LEAPS: multiple delivered AT EXPIRY if the underlying rises +100%%, +200%%, +300%% (T = %.0f yr)\n" % T)
    print("| IV | delta | K/S0 | premium (% of S0) | " + " | ".join("x on +%.0f%%" % (m * 100) for m in moves) + " |")
    print("|" + "---|" * (4 + len(moves)))
    for iv in ivs:
        for d in deltas:
            K = strike_for_delta(S0, T, r, iv, d)
            c0 = bs_call(S0, K, T, r, iv)
            mults = [max(S0 * (1 + m) - K, 0.0) / c0 for m in moves]
            print("| %.0f%% | %.2f | %.2f | %.1f%% | " % (iv * 100, d, K / S0, c0 / S0 * 100)
                  + " | ".join("%.1fx" % x for x in mults) + " |")
    print()


# ----------------------------------------------------------------------------
# 2. Leveraged ETFs
# ----------------------------------------------------------------------------
def letf_factor(L, gross_ret, sigma, T, funding=0.045, fee=0.01):
    """Median-path multiple of a daily-rebalanced L-x ETF given the underlying's
    total gross return (S_T/S_0), realised vol sigma, horizon T, borrowing rate
    on the (L-1) notional, and expense ratio."""
    drag = 0.5 * (L**2 - L) * sigma**2 * T
    cost = ((L - 1) * funding + fee) * T
    return gross_ret**L * math.exp(-drag - cost)


def letf_tables():
    print("### Leveraged ETF variance drag: exp(-(L^2-L)/2 * sigma^2 * T)  (underlying flat, before fees/financing)\n")
    print("| realised vol | 2x, 1 yr | 2x, 2 yr | 3x, 1 yr | 3x, 2 yr |")
    print("|---|---|---|---|---|")
    for s in (0.30, 0.40, 0.60, 0.80, 1.00):
        vals = [math.exp(-0.5 * (L**2 - L) * s**2 * T) for L in (2, 3) for T in (1, 2)]
        print("| %.0f%% | %s |" % (s * 100, " | ".join("%.2fx (%+.0f%%)" % (v, (v - 1) * 100) for v in vals)))
    print()
    print("### Leveraged ETF median outcome vs underlying move (T = 1 yr; financing 4.5% on borrowed notional, fee 1%/yr)\n")
    print("| underlying | realised vol | 2x ETF | 3x ETF | naive L*return |")
    print("|---|---|---|---|---|")
    for g in (0.5, 1.0, 2.0, 3.0, 4.0):
        for s in (0.40, 0.60, 0.80):
            f2 = letf_factor(2, g, s, 1.0)
            f3 = letf_factor(3, g, s, 1.0)
            print("| %+.0f%% (%.1fx) | %.0f%% | %.2fx | %.2fx | 2x: %.1fx, 3x: %.1fx |"
                  % ((g - 1) * 100, g, s * 100, f2, f3, 1 + 2 * (g - 1), 1 + 3 * (g - 1)))
    print()
    print("### Underlying gross multiple a 2x / 3x ETF needs for a 10x (T = 1 and 2 yr)\n")
    print("| realised vol | 2x, 1 yr | 2x, 2 yr | 3x, 1 yr | 3x, 2 yr |")
    print("|---|---|---|---|---|")
    for s in (0.40, 0.60, 0.80, 1.00):
        cells = []
        for L in (2, 3):
            for T in (1, 2):
                drag = 0.5 * (L**2 - L) * s**2 * T + ((L - 1) * 0.045 + 0.01) * T
                g = (10.0 * math.exp(drag)) ** (1.0 / L)
                cells.append("%.2fx" % g)
        print("| %.0f%% | %s |" % (s * 100, " | ".join(cells)))
    print()


# ----------------------------------------------------------------------------
# 3. Perps / margin
# ----------------------------------------------------------------------------
def perp_tables():
    print("### Perpetuals: liquidation distance and probability of being liquidated within T (driftless lognormal, reflection principle)\n")
    print("Liquidation when equity falls to maintenance margin m (0.5% here): price drop = (1/L)*(1 - m*L) approx 1/L - m.\n")
    print("P(min_{t<=T} S_t <= b*S_0) = 2*N( ln(b) / (sigma*sqrt(T)) ) for zero drift.\n")
    print("| leverage | liq. drop | vol 40%, 3m | vol 40%, 12m | vol 60%, 3m | vol 60%, 12m | vol 80%, 12m |")
    print("|---|---|---|---|---|---|---|")
    m = 0.005
    for L in (2, 3, 5, 10, 20):
        drop = 1.0 / L - m
        b = 1.0 - drop
        cells = []
        for s, T in ((0.40, 0.25), (0.40, 1.0), (0.60, 0.25), (0.60, 1.0), (0.80, 1.0)):
            p = 2 * norm.cdf(math.log(b) / (s * math.sqrt(T)))
            cells.append("%.0f%%" % (min(p, 1.0) * 100))
        print("| %dx | -%.1f%% | %s |" % (L, drop * 100, " | ".join(cells)))
    print()
    print("Same, with a bullish drift of +50%/yr expected return (the case where you are RIGHT on direction):\n")
    print("| leverage | liq. drop | vol 60%, 12m | vol 80%, 12m | vol 100%, 12m |")
    print("|---|---|---|---|---|")
    for L in (2, 3, 5, 10):
        drop = 1.0 / L - m
        b = 1.0 - drop
        cells = []
        for s in (0.60, 0.80, 1.00):
            T = 1.0
            mu = math.log(1.5) - 0.5 * s**2  # log-drift for E[S_T]=1.5*S0
            # P(min <= b) with drift: standard hitting-probability formula
            lb = math.log(b)
            p = norm.cdf((lb - mu * T) / (s * math.sqrt(T))) + math.exp(2 * mu * lb / s**2) * norm.cdf((lb + mu * T) / (s * math.sqrt(T)))
            cells.append("%.0f%%" % (min(p, 1.0) * 100))
        print("| %dx | -%.1f%% | %s |" % (L, drop * 100, " | ".join(cells)))
    print()
    print("### Funding drag on a long perp (paid every 8h; annualised = rate*3*365)\n")
    print("| funding / 8h | annualised | cost on 3x notional per yr (% of equity) | cost on 5x |")
    print("|---|---|---|---|")
    for f in (0.0001, 0.0003, 0.0005, 0.0010):
        ann = f * 3 * 365
        print("| %.2f%% | %.0f%% | %.0f%% | %.0f%% |" % (f * 100, ann * 100, ann * 3 * 100, ann * 5 * 100))
    print()


if __name__ == "__main__":
    mc = "--no-mc" not in sys.argv
    print("# options_10x.py output\n")
    leaps_table(mc=mc)
    leaps_given_move(T=1.0)
    leaps_given_move(T=2.0)
    letf_tables()
    perp_tables()
