"""Use alpha vantage API to get stock data (TimeSeries only)."""

from alpha_vantage.timeseries import TimeSeries

def get_intraday_data(API_KEY, ticker, interval):
    """get dataframe of the given stocks."""
    ts = TimeSeries(API_KEY, output_format='pandas')
    data, metadata = ts.get_intraday(symbol=ticker, 
                                    interval=interval, outputsize='full')
    return data

def get_daily(API_KEY, ticker):
    """get dataframe of bbands for the given stocks."""
    ts = TimeSeries(API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='compact')
    return data