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
import common  # noqa: E402


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
    assert len(tab) == 4                      # synthetic series starts in 2011, before the first halving
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


def test_yahoo_symbol_mapping():
    assert fd.yahoo_symbol("BRK.B") == "BRK-B"
    assert fd.yahoo_symbol("9880.HK") == "9880.HK"
    assert fd.yahoo_symbol("BTC-USD") == "BTC-USD"
    assert fd.yahoo_symbol("NVDA") == "NVDA"


def test_parquet_round_trip(tmp_path):
    prices = _synthetic_prices()
    pq = common.write_prices(prices, tmp_path / "p.parquet")
    back = common.load_prices(pq)
    assert list(back.columns) == ["date", "symbol", "close"]
    assert back["date"].iloc[0] == prices["date"].iloc[0] and str(back["symbol"].dtype) != "category"
    assert np.allclose(back["close"].to_numpy(), prices["close"].to_numpy(), rtol=1e-6)
    gz = common.write_prices(prices, tmp_path / "p.csv.gz")
    assert len(common.load_prices(gz)) == len(prices)
    # screener accepts parquet input
    ev = ts.find_events(common.load_prices(pq), 730, 10)
    assert set(ev["symbol"]) == {"AAA"}


def test_parse_screener_rows():
    rows = [{"symbol": "NVDA", "name": "NVIDIA", "lastsale": "$223.03", "marketCap": "5,420,000,000,000",
             "sector": "Technology", "industry": "Semiconductors", "ipoyear": "1999"},
            {"symbol": "BRK/B", "name": "Berkshire", "lastsale": "$500.00", "marketCap": "", "sector": ""},
            {"symbol": "XYZ", "name": "x", "lastsale": "NA", "marketCap": "NA"}]
    m = fd.parse_screener_rows(rows, asof="2026-09-24")
    assert m.loc[0, "market_cap"] == 5.42e12 and abs(m.loc[0, "shares"] - 5.42e12 / 223.03) < 1
    assert m.loc[1, "symbol"] == "BRK.B" and m.loc[1, "shares"] is None or np.isnan(m.loc[1, "shares"])
    assert np.isnan(m.loc[2, "last_price"])


def _stooq_zip(tmp_path):
    import zipfile
    hdr = "<TICKER>,<PER>,<DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n"
    def rows(sym, closes, start="20240603"):
        d = pd.bdate_range(start, periods=len(closes))
        return hdr + "".join(f"{sym}.US,D,{x.strftime('%Y%m%d')},000000,1,1,1,{c},100,0\n" for x, c in zip(d, closes))
    zp = tmp_path / "d_us_txt.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("data/daily/us/nasdaq stocks/1/nvda.us.txt", rows("NVDA", [1200, 1210, 1220, 1230, 1240, 124, 125, 126]))
        z.writestr("data/daily/us/nyse stocks/1/brk-b.us.txt", rows("BRK-B", [400, 401, 402, 403, 404, 405, 406, 407]))
        z.writestr("data/daily/us/nasdaq etfs/1/xbi.us.txt", rows("XBI", [90, 91, 92, 93, 94, 95, 96, 97]))
        z.writestr("data/daily/pl/wse stocks/pko.txt", "ignored")
    return zp


def _stooq_uk_hourly_zip(tmp_path):
    import zipfile
    hdr = "<TICKER>,<PER>,<DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n"
    body = hdr + "".join(f"BP.UK,60,20240603,{t},1,1,1,{c},10,0\n" for t, c in
                         [("090000", 500), ("100000", 505), ("160000", 510)])
    body += "BP.UK,60,20240604,090000,1,1,1,520,10,0\n"
    zp = tmp_path / "h_uk_txt.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("data/hourly/uk/lse stocks/1/bp.uk.txt", body)
    return zp


def test_uk_hourly_collapses_to_daily(tmp_path):
    zp = _stooq_uk_hourly_zip(tmp_path)
    assert fd.stooq_to_symbol("data/hourly/uk/lse stocks/1/bp.uk.txt") == "BP.L"
    d = fd.stooq_prices(zp, {"BP.L"}, start="2020-01-01")
    assert list(d["date"]) == ["2024-06-03", "2024-06-04"] and list(d["close"]) == [510.0, 520.0]
    assert fd.stooq_prices(zp, {"NVDA"}, start="2020-01-01").empty


def test_stooq_extract_and_symbols(tmp_path):
    zp = _stooq_zip(tmp_path)
    assert fd.stooq_to_symbol("data/daily/us/nyse stocks/1/brk-b.us.txt") == "BRK.B"
    assert fd.stooq_to_symbol("data/daily/pl/wse stocks/pko.txt") is None
    d = fd.stooq_prices(zp, {"NVDA", "BRK.B", "XBI"}, start="2020-01-01")
    assert set(d["symbol"]) == {"NVDA", "BRK.B", "XBI"} and len(d) == 24
    assert d[d["symbol"] == "NVDA"]["date"].iloc[0] == "2024-06-03"
    stocks = fd.stooq_prices(zp, None, start="2020-01-01", stocks_only=True)
    assert set(stocks["symbol"]) == {"NVDA", "BRK.B"}
    # unadjusted 10:1 split on 2024-06-10 must be flagged
    warns = fd.check_split_adjustment(d)
    assert warns and warns[0].startswith("NVDA")
    # adjusted data are not flagged
    adj = d.copy(); adj.loc[(adj["symbol"] == "NVDA") & (adj["date"] < "2024-06-10"), "close"] /= 10
    assert fd.check_split_adjustment(adj) == []


def test_to_weekly():
    dates = pd.bdate_range("2024-06-03", periods=10)  # two full weeks
    daily = pd.DataFrame({"date": dates.strftime("%Y-%m-%d"), "symbol": "AAA", "close": range(1, 11), "volume": 1.0})
    w = fd.to_weekly(daily)
    assert list(w.columns) == ["date", "symbol", "close"]
    assert list(w["close"]) == [5, 10] and list(w["date"]) == ["2024-06-07", "2024-06-14"]


def test_parse_coingecko_rows():
    rows = [{"id": "bitcoin", "name": "Bitcoin", "current_price": 85686.0, "market_cap": 1.69e12,
             "circulating_supply": 19.9e6, "fully_diluted_valuation": 1.8e12},
            {"id": "unknowncoin", "name": "x", "current_price": 1, "market_cap": 1}]
    m = fd.parse_coingecko_rows(rows, asof="2026-09-24")
    assert len(m) == 1 and m.loc[0, "symbol"] == "BTC-USD" and m.loc[0, "market_cap"] == 1.69e12


def test_rate_limit_detector():
    assert fd._is_rate_limit(Exception("Too Many Requests. Rate limited. Try after a while."))
    assert not fd._is_rate_limit(Exception("connection reset"))


def test_find_stooq_zip_copies_into_cache(tmp_path, monkeypatch):
    src = _stooq_zip(tmp_path)
    # pad to pass the size sanity check
    with open(src, "ab") as f:
        f.write(b"\0" * 11_000_000)
    monkeypatch.setattr(fd, "CACHE", tmp_path / "cache")
    monkeypatch.setattr(fd, "ROOT", tmp_path / "nowhere")
    monkeypatch.setattr(Path, "home", staticmethod(lambda: tmp_path / "nohome"))
    found = fd.find_stooq_zip(src)
    assert found == tmp_path / "cache" / "d_us_txt.zip" and found.exists()
    assert fd.find_stooq_zip(None) == found          # second call uses the cache
    monkeypatch.setattr(fd, "CACHE", tmp_path / "empty")
    assert fd.find_stooq_zip(None) is None


def test_fixed_start_rates_synthetic():
    prices = _synthetic_prices()
    fx = ts.fixed_start_rates(prices, 730, multiples=(3, 10))
    allrows = fx[fx["bucket"] == "ALL"]
    assert {"start", "alive", "n_10x", "rate_10x", "censored"} <= set(allrows.columns)
    # AAA is flat at 1.0 until row ~1000 (Nov 2018) then runs to 12 by row 1300 (Jan 2020):
    # from 2018-01-01 the 730-day forward max is 12x; from 2019-01-01 the entry is already ~2.6 so <10x
    r2018 = allrows[allrows["start"].str.startswith("2018")].iloc[0]
    assert r2018["n_10x"] == 1 and r2018["alive"] == 3
    r2019 = allrows[allrows["start"].str.startswith("2019")].iloc[0]
    assert r2019["n_10x"] == 0 and r2019["n_3x"] == 2      # AAA (~4.6x) and CCC (~3.2x)
    # from 2016-01-01: nobody 10x's; CCC (10x over 4 years) makes 3.16x, so n_3x == 1
    r2016 = allrows[allrows["start"].str.startswith("2016")].iloc[0]
    assert r2016["n_10x"] == 0 and r2016["n_3x"] == 1
    assert allrows["censored"].iloc[-1]


def test_btc_cycle_peak_window():
    idx = pd.date_range("2016-01-01", "2026-09-24")
    s = pd.Series(10.0, index=idx)
    s[pd.Timestamp("2017-12-16")] = 100.0     # 2016-cycle peak, day 525
    s[pd.Timestamp("2018-12-15")] = 5.0       # low  (min after peak)
    s[pd.Timestamp("2024-03-13")] = 500.0     # pre-2024-halving run-up: must NOT be the 2020 cycle peak
    s[pd.Timestamp("2021-11-10")] = 300.0     # true 2020-cycle peak
    tab = bc.cycle_table(s)
    r2016 = tab[tab["halving"] == "2016-07-09"].iloc[0]
    assert r2016["peak_date"] == "2017-12-16" and r2016["post_low_date"] == "2018-12-15"
    r2020 = tab[tab["halving"] == "2020-05-11"].iloc[0]
    assert r2020["peak_date"] == "2021-11-10" and r2020["peak"] == 300.0
    assert "2012-11-28" not in set(tab["halving"])          # data start after that halving: row skipped


def test_conditional_rates_synthetic():
    import conditional_rates as cr
    prices = _synthetic_prices()
    d = cr.per_symbol_table(prices, meta=None, window_days=730)
    assert {"symbol", "year", "prior_ret", "dd3y", "fwd_max", "end_ratio", "dd_bucket", "prior_bucket"} <= set(d.columns)
    assert d["year"].min() >= 2016 and d["year"].max() <= 2024      # needs a year before and two after
    t = cr.summarise(d, "dd_bucket")
    assert (t["p_max_10x"] <= 1).all() and (t["n"].sum() == len(d))
    # AAA after its crash (row 1300 onwards: 12 -> 3) sits ~75% below its 3-year high in 2021-2022 starts
    aaa = d[(d["symbol"] == "AAA") & (d["year"].isin([2021, 2022]))]
    assert (aaa["dd3y"] < -0.6).all()
