#File to collect yfinance data

import yfinance as yf
from datetime import datetime
import pandas as pd
import numpy as np

Date_5=f"2017{str(datetime.now().date())[-6:]}"

stocks = pd.read_csv("./src/data/CAC40_tickers.csv", on_bad_lines="skip", delimiter=";")


y_tickers = yf.Tickers(list(stocks["Symbol"].values))
stocks_data = y_tickers.history(start=Date_5)