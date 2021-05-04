from math import ceil

import investpy
import pandas as pd

from data import another_bad_stocks, bad_stocks

FROM_DATE = "01/03/2002"
TO_DATE = "01/01/2020"


def get_data_from_investing_dot_com():
    stocks = investpy.get_stocks_list(country="israel")
    stocks = list(set(stocks) - set(bad_stocks) - set(another_bad_stocks))
    all_stocks_data = []
    for stock in stocks:
        data = investpy.get_stock_historical_data(stock=stock, country='israel', from_date=FROM_DATE,
                                                  to_date=TO_DATE, interval='weekly')
        data = data.drop(columns="Open   High    Low   Volume Currency".split())
        data.columns = [f'{stock} close price']
        all_stocks_data.append(data)
    d = all_stocks_data[0].reset_index()
    for d2 in all_stocks_data[1:]:
        d = d.merge(d2.reset_index(), how='outer', on='Date')
    d.set_index('Date')
    d.to_csv("..\\Data\\investing_raw_data.csv")
    return d


def compute_df(years=1):
    df = pd.read_csv("..\\Data\\investing_raw_data.csv", index_col=0, header=0)
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df.resample('W').ffill().pct_change()
    df = df.rolling(52 * years).std()
    df = df.groupby([df.index.year, df.index.month]).last().T


def _sort_by_volatility(df):
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


if __name__ == '__main__':
    get_data_from_investing_dot_com()
