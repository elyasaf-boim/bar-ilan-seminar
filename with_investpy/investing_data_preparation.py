import datetime
from math import ceil

import investpy
import pandas as pd
import numpy as np
from const import bad_stocks, RISK_FREE

FROM_DATE = "01/03/2002"
TO_DATE = "01/01/2020"


def get_data_from_investing_dot_com():
    stocks = investpy.get_stocks_list(country="israel")
    stocks = list(set(stocks) - set(bad_stocks))
    all_stocks_data = []
    for stock in stocks:
        data = investpy.get_stock_historical_data(stock=stock, country='israel', from_date=FROM_DATE,
                                                  to_date=TO_DATE, interval='weekly')
        data = data.drop(columns="Open High Low Volume Currency".split())
        data.columns = [stock]
        all_stocks_data.append(data)
    d = all_stocks_data[0].reset_index()
    for d2 in all_stocks_data[1:]:
        d = d.merge(d2.reset_index(), how='outer', on='Date')
    d.set_index('Date')
    d.to_csv("..\\Data\\investing_raw_data.csv")


def compute_df(years=1):
    df = pd.read_csv("..\\Data\\investing_raw_data.csv", index_col=0, header=0)
    good_stocks = pd.read_csv('../Data/good_stocks.csv')
    good_stocks.columns = ['stocks', 'cnt']
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df[good_stocks['stocks']]
    df = df.sort_index()
    df = df.apply(pd.to_numeric)
    df = np.log(df.resample('W').ffill().pct_change() + 1)
    df.to_csv('../Data/investing_raw_weekly_return.csv')
    df = df.rolling(52 * years).std()
    df = df.groupby([df.index.year, df.index.month]).last().T
    df = _sort_by_volatility(df)
    df.to_csv("..\\Data\\investing_deciles.csv")


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


def calc_monthly_return_of_deciles():
    raw_data = pd.read_csv("../Data/investing_raw_data.csv", index_col=1, header=0)
    raw_data.index = pd.to_datetime(raw_data.index, format='%d-%m-%y')
    deciles = pd.read_csv("../Data/investing_deciles.csv").rename(
        columns={'Unnamed: 0': 'year', 'Unnamed: 1': 'month'})
    cols = raw_data.columns
    cols = [c.split()[0] for c in cols]
    raw_data.columns = cols
    d_df = deciles[["year", "month", "D0"]]
    idx = []
    for index, row in d_df.iterrows():
        idx.append(f"{row['year']}_{row['month']}")
    cols = [f"D{i}" for i in range(10)]
    res_df = pd.DataFrame(columns=cols, index=idx)
    for i in range(10):
        d_df = deciles[["year", "month", f"D{i}"]]
        for index, row in d_df.iterrows():
            year = row["year"]
            month = row["month"]
            d_stocks = list(filter(lambda x: str(x).upper() == x, row[f"D{i}"].split()))
            d_stocks = [symbol.translate({ord(i): None for i in "'[]"}) for symbol in d_stocks]
            if d_stocks != ['']:
                d_raw_data = raw_data[d_stocks].ffill()
                d_raw_data.index = pd.to_datetime(d_raw_data.index)
                d_raw_data = np.log(d_raw_data.resample("M").ffill().pct_change() + 1)
                if int(month) == 12:
                    month = 1
                    year = int(year) + 1
                else:
                    year = int(year)
                    month = int(month) + 1

                res_df[f"D{i}"][f"{row['year']}_{row['month']}"] = d_raw_data.iloc[
                                                                       d_raw_data.index.get_loc(
                                                                           datetime.datetime(year, month, 1),
                                                                           method='nearest')].sum() / len(d_stocks)
    res_df.to_csv("..\\Data\\investing_deciles_monthly_return_new.csv")


def compute_deciles_excess_return():
    rr_return = RISK_FREE
    deciles_return = pd.read_csv('..\\Data\\investing_deciles_monthly_return_new.csv')
    deciles_return = deciles_return.rename(columns={'Unnamed: 0': 'Date'})
    deciles_return.Date = pd.to_datetime(deciles_return.Date.str.split('_').str.join('/') + "/01", format='%Y/%m/%d')
    deciles_return = deciles_return.set_index('Date')
    deciles_excess_return = rr_return.join(deciles_return, how='outer')
    deciles_excess_return['return'] = deciles_excess_return['return'].ffill()
    deciles_excess_return = deciles_excess_return[~(deciles_excess_return.D0.isnull())]
    deciles_excess_return = deciles_excess_return.sub(deciles_excess_return['return'], axis=0)
    deciles_excess_return.to_csv('..\\Data\\investing_deciles_monthly_excess_return.csv')


def compute_ta125_excess_return():
    rr_return = RISK_FREE
    ta125_return = pd.read_csv('../Data/maya_ta125_monthly_return.csv')
    ta125_return.Date = pd.to_datetime(ta125_return.Date)
    ta125_return = ta125_return.reset_index()
    ta125_return = ta125_return.set_index('Date').drop('index', axis=1)
    ta125_return_excess_return = rr_return.join(ta125_return, how='outer')
    ta125_return_excess_return['return'] = ta125_return_excess_return['return'].ffill()

    ta125_return_excess_return = ta125_return_excess_return[~(ta125_return_excess_return.TA125.isnull())]
    ta125_return_excess_return = ta125_return_excess_return.sub(ta125_return_excess_return['return'], axis=0)
    ta125_return_excess_return = np.log(ta125_return_excess_return + 1)
    ta125_return_excess_return.to_csv('..\\Data\\ta125_monthly_excess_return.csv')


def merge_ta125_and_deciles():
    rr_return = RISK_FREE
    ta125 = pd.read_csv('..\\Data\\ta125_monthly_excess_return.csv')
    ta125.Date = pd.to_datetime(ta125.Date)
    ta125 = ta125.set_index('Date').drop('return', axis=1)
    deciles = pd.read_csv('..\\Data\\investing_deciles_monthly_excess_return.csv')
    deciles.Date = pd.to_datetime(deciles.Date)
    deciles = deciles.set_index('Date').drop('return', axis=1)

    merged_df = deciles.join(ta125, how='outer')
    merged_df.TA125 = merged_df.TA125.ffill()
    merged_df = merged_df[~(merged_df.D0.isnull())]

    merged_df = merged_df.join(rr_return, how='outer')
    merged_df['return'] = merged_df['return'].ffill()
    merged_df = merged_df[~(merged_df.D0.isnull())]

    merged_df.to_csv('..\\Data\\final_merged_df.csv')


if __name__ == '__main__':
    merge_ta125_and_deciles()
