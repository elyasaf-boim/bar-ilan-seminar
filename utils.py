from math import ceil
import pandas as pd
import investpy
import pandas_datareader as web
from data import bad_stocks, another_bad_stocks


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_raw_data(from_date="1990-01-01", to_date="2020-01-01", how_many_stocks=None):
    stocks = investpy.get_stocks_list(country="israel")
    stocks = set(stocks) - set(bad_stocks) - set(another_bad_stocks)
    stocks = [f"{stock}.TA" for stock in stocks][:how_many_stocks]
    df = None
    count = 1
    for i in list(chunks(stocks, 20)):
        print(f"round number: {count}")
        count = count + 1
        if df is None:
            df = web.get_data_yahoo(i, start=from_date, end=to_date, interval='w', chunksize=len(i))
        else:
            df_2 = web.get_data_yahoo(i, start=from_date, end=to_date, interval='w', chunksize=len(i))
            df = pd.concat([df, df_2], axis=1, join="inner")
    return df


def calc_weekly_return(df):
    return df['Adj Close'].resample('W').ffill().pct_change()


def calc_annum_std(df, years=1):
    df = df.rolling(52 * years).std()
    return df.groupby([df.index.year, df.index.month]).last().T


def sort_by_volatility(df):
    deciles = {}
    all_month = df.columns
    for i in range(10):
        deciles[f"D{i}"] = {}
        for m in all_month:
            deciles[f"D{i}"][m] = []
    for month in all_month:
        t_df = df[month].copy()
        t_df = t_df.sort_values().dropna()
        df_len = t_df.shape[0]
        step = ceil(df_len / 10)
        start = 0
        if step != 0:
            for i in range(10):
                end = (i + 1) * step if i != 9 else None
                if start is None or start >= df_len:
                    break
                if end is None or end >= df_len:
                    end = None
                deciles[f"D{i}"][month] = str(t_df[start:end].index.values.copy())
                start = end
    return pd.DataFrame(deciles)
