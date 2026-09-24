"""Synthetic-data tests for the analysis tooling. Run: python -m pytest tools/tests -q"""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import tenx_math as tm  # noqa: E402
import tenx_screener as ts  # noqa: E402
import btc_cycle as bc  # noqa: E402
import fetch_data as fd  # noqa: E402
import watchlist as wl  # noqa: E402


def test_required_cagr():
    assert math.isclose(tm.required_cagr(10, 2), math.sqrt(10) - 1)
    assert math.isclose(tm.required_cagr(10, 1), 9.0)


def test_expected_value_and_breakeven():
    # 10% chance of 10x, 60% chance of losing 80%, 30% flat
    ev = tm.expected_value(0.10, 0.60, loss=0.8)
    assert math.isclose(ev, 0.10 * 9 - 0.60 * 0.8)
    be = tm.breakeven_p10(0.60, loss=0.8)
    assert math.isclose(tm.expected_value(be, 0.60, loss=0.8), 0.0, abs_tol=1e-12)


def test_kelly_zero_when_negative_ev():
    assert tm.kelly_fraction(0.02, 0.80, loss=0.9) == 0.0
    k = tm.kelly_fraction(0.15, 0.50, loss=0.8)
    assert 0.0 < k < 0.5


def test_p_at_least_one():
    assert math.isclose(tm.p_at_least_one(10, 0.1), 1 - 0.9 ** 10)


def _synthetic_prices():
    dates = pd.bdate_range("2015-01-01", "2025-12-31")
    n = len(dates)
    rows = []
    # A: flat then 12x over 300 trading days, then crash
    a = np.ones(n)
    a[1000:1300] = np.linspace(1, 12, 300)
    a[1300:] = 3
    # B: steady 20%/yr, never 10x within 2y
    b = 1.2 ** (np.arange(n) / 252)
    # C: 10x but over 4 years (should NOT count in a 730-day window)
    c = 10 ** (np.arange(n) / (252 * 4))
    for sym, arr in (("AAA", a), ("BBB", b), ("CCC", c)):
        rows.append(pd.DataFrame({"date": dates.strftime("%Y-%m-%d"), "symbol": sym, "close": arr}))
    return pd.concat(rows, ignore_index=True)


def test_screener_finds_only_true_10x():
    prices = _synthetic_prices()
    ev = ts.find_events(prices, window_days=730, multiple=10)
    assert set(ev["symbol"]) == {"AAA"}
    assert (ev["multiple"] >= 10).all()
    # window that is long enough for CCC's 4-year 10x
    ev4 = ts.find_events(prices, window_days=365 * 4 + 30, multiple=10)
    assert {"AAA", "CCC"} <= set(ev4["symbol"])


def test_screener_base_rates_shape():
    prices = _synthetic_prices()
    ev = ts.find_events(prices, 730, 10)
    rates = ts.base_rates(prices, ev, 730)
    assert {"year", "symbols_alive", "symbols_with_event", "rate", "censored"} <= set(rates.columns)
    assert rates["symbols_alive"].max() == 3
    assert rates["censored"].iloc[-1]  # last year cannot have a full forward window


def test_forward_max_ratio_simple():
    close = np.array([1.0, 2.0, 0.5, 5.0])
    dates = np.array(["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04"], dtype="datetime64[D]")
    r = ts.forward_max_ratio(close, dates, window_days=2)
    assert math.isclose(r[0], 2.0)   # window (t, t+2d] -> days 2,3 -> max 2.0
    assert math.isclose(r[1], 2.5)   # days 3,4 -> 5/2
    assert math.isclose(r[2], 10.0)  # day 4 -> 5/0.5
    assert np.isnan(r[3])


def test_btc_cycle_table_on_synthetic():
    idx = pd.date_range("2011-01-01", "2026-09-24")
    t = np.arange(len(idx))
    # crude: exponential trend with a 4-year sine so peaks/troughs exist
    price = 10 * np.exp(t / 900) * (1 + 0.8 * np.sin(2 * np.pi * (t - 500) / 1461))
    s = pd.Series(price, index=idx)
    tab = bc.cycle_table(s)
    assert len(tab) == 4
    assert tab["complete"].iloc[:3].all() and not tab["complete"].iloc[3]
    now = bc.where_now(s)
    assert now["days_since_halving"] == (pd.Timestamp("2026-09-24") - pd.Timestamp("2024-04-20")).days
    assert now["drawdown_from_cycle_peak_%"] <= 0


def test_tidy_multiindex():
    dates = pd.date_range("2024-01-01", periods=3)
    cols = pd.MultiIndex.from_product([["Close", "Volume"], ["AAA", "BRK-B"]])
    raw = pd.DataFrame(np.arange(12, dtype=float).reshape(3, 4), index=dates, columns=cols)
    long = fd.tidy(raw, ["AAA", "BRK-B"])
    assert set(long.columns) == {"date", "symbol", "close", "volume"}
    assert set(long["symbol"]) == {"AAA", "BRK.B"}
    assert len(long) == 6


def test_is_common_filter():
    assert fd.is_common("NVDA", "NVIDIA Corporation - Common Stock")
    assert not fd.is_common("ABCDW", "ABCD Corp - Warrant")
    assert not fd.is_common("XYZ", "XYZ Fund Preferred Shares")
    assert not fd.is_common("BRK$A", "Berkshire")


def test_watchlist_math(tmp_path):
    p = tmp_path / "w.csv"
    p.write_text("symbol,name,theme,entry_date,entry_price,entry_mcap,target_multiple,thesis,catalysts,"
                 "kill_criteria,status,note_file\nAAA,A,ai,2026-09-24,10,1e9,,t,c,k,open,\n")
    df = wl.load_watchlist(p)
    assert df["implied_mcap"].iloc[0] == 1e10 and df["target_price"].iloc[0] == 100
    prices = tmp_path / "p.csv"
    prices.write_text("date,symbol,close\n2026-09-24,AAA,10\n2026-10-01,AAA,25\n")
    df2 = wl.attach_prices(df, prices)
    assert df2["multiple_so_far"].iloc[0] == 2.5 and df2["remaining_x"].iloc[0] == 4.0
