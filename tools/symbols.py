"""Symbol lists for fetch_data.py. Edit freely; keep the core list small.

Crypto uses Yahoo's 'XXX-USD' convention. Equities use exchange tickers ('.' for share classes).
"""

# Benchmarks and the assets that anchor the research (daily, 12 years).
CORE_SYMBOLS = [
    "SPY", "QQQ", "IWM", "GLD", "SLV", "TLT", "UUP",
    "NVDA", "TSLA", "MSTR", "COIN", "PLTR", "SMCI", "CVNA", "APP", "RKLB",
    "BTC-USD", "ETH-USD", "SOL-USD",
]

# Candidates from the theme screens (daily, 12 years). Appended to as the screens produce names.
# Keep this in sync with data/watchlist.csv.
WATCH_SYMBOLS = [
    # crypto proxies / miners
    "MSTR", "COIN", "HOOD", "CRCL", "GLXY", "IREN", "CORZ", "CIFR", "WULF", "HUT", "MARA", "RIOT",
    # AI / semis second order
    "CRDO", "LITE", "COHR", "AAOI", "POET", "ALAB", "MRVL", "RMBS", "CAMT", "ONTO", "FORM", "ACMR",
    "BE", "VRT", "CRWV", "NBIS", "APLD", "MU", "SNDK", "AXTI", "NVTS", "NSCL",
    # nuclear / energy / uranium
    "OKLO", "SMR", "NNE", "LEU", "UEC", "UUUU", "DNN", "NXE", "EU", "URG", "CCJ", "SRUUF",
    "EOSE", "FLNC", "GEV", "ORA", "GFUZ",
    # quantum / robotics / space / defence
    "IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "QNT", "INFQ", "HQ", "SERV", "RR", "SYM", "OUST", "HSAI", "9880.HK",
    "RKLB", "ASTS", "PL", "BKSY", "RDW", "LUNR", "FLY", "KRMN", "AVAV", "RCAT", "ONDS", "KTOS", "UMAC",
    # biotech (from notes/themes/biotech.md; all pending verification)
    "XBI", "NTLA", "BEAM", "CRSP", "RXRX", "SDGR", "CMPS", "MNMD", "ABOS", "RNAC", "KYTX", "LRMR",
    # commodities equities
    "MP", "USAR", "AG", "HL", "CDE", "EXK", "SILV", "VZLA", "ALB", "SBSW", "IMPUY",
    # crypto
    "BTC-USD", "ETH-USD", "SOL-USD", "HYPE-USD", "LINK-USD", "AAVE-USD", "SUI-USD", "APT-USD",
    "ENA-USD", "PENDLE-USD", "DOGE-USD", "XRP-USD", "BNB-USD",
]
