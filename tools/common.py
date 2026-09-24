"""Shared I/O helpers: long-format price tables as gzip CSV or Parquet."""
from __future__ import annotations

import gzip
from pathlib import Path

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype


def load_prices(path: str | Path) -> pd.DataFrame:
    """Read a long-format price table (date, symbol, close[, volume]) from .parquet, .csv or .csv.gz.
    Dates come back as ISO strings; symbols as plain str."""
    path = Path(path)
    df = pd.read_parquet(path) if path.suffix == ".parquet" else pd.read_csv(path)
    if is_datetime64_any_dtype(df["date"]):
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    else:
        df["date"] = df["date"].astype(str)
    df["symbol"] = df["symbol"].astype(str)
    return df


def write_prices(df: pd.DataFrame, path: str | Path) -> Path:
    """Write a long-format price table. Parquet (zstd, categorical symbol, float32 close) is ~5x
    smaller than gzip CSV and is what the universe tier uses so it fits in git."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".parquet":
        out = df.copy()
        out["date"] = pd.to_datetime(out["date"])
        out["symbol"] = out["symbol"].astype("category")
        out["close"] = out["close"].astype("float32")
        if "volume" in out.columns:
            out["volume"] = out["volume"].astype("float32")
        out.to_parquet(path, engine="pyarrow", compression="zstd", index=False)
    elif path.suffixes[-2:] == [".csv", ".gz"]:
        with gzip.open(path, "wt", newline="") as f:
            df.to_csv(f, index=False)
    else:
        df.to_csv(path, index=False)
    return path
