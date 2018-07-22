"""Use alpha vantage API to get stock data."""

from alpha_vantage.timeseries import TimeSeries

ALPHAVANTAGE_API_KEY = input("Enter you key")

ts = TimeSeries(key=ALPHAVANTAGE_API_KEY)
data, metadata = ts.get_intraday('GOOGL')