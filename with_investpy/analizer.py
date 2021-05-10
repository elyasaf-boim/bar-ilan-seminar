import datetime
import itertools
import math
from math import ceil

import pandas as pd
import numpy as np
from const import bad_stocks, RISK_FREE


def compute_deciles_std():
    df = pd.read_csv("..\\Data\\investing_raw_data.csv", index_col=0, header=0)
    good_stocks = pd.read_csv('../Data/good_stocks.csv')
    good_stocks.columns = ['stocks', 'cnt']
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df[good_stocks['stocks']]
    df = df.sort_index()
    df = df.apply(pd.to_numeric)
    df_before_std = df.copy()
    df = np.log(df.resample('W').ffill().pct_change() + 1)
    df = df.rolling(52 * 1).std()
    deciles = pd.read_csv("../Data/investing_deciles.csv").rename(
        columns={'Unnamed: 0': 'year', 'Unnamed: 1': 'month'})
    deciles['Date'] = pd.to_datetime(deciles['year'].map(str) + '/' + deciles['month'].map(str) + '/01')
    deciles = deciles[deciles.columns[2:]]
    deciles = deciles.set_index('Date')
    deciles_lst = [f'D{i}' for i in range(10)]
    for col in deciles_lst:
        print(col)
        d = deciles[col]
        for dt, stocks in d.items():
            stocks = list(filter(lambda x: len(x) > 10, stocks.split("'")))
            if stocks:

                decile_std_by_dt = df[stocks].iloc[df.index.get_loc(dt, method='nearest')]
                if decile_std_by_dt.count() > 0:
                    pairs_set = set()
                    for i, j in itertools.product(stocks, stocks):
                        if i != j:
                            if i > j:
                                pairs_set.add((i, j))
                            else:
                                pairs_set.add((j, i))
                    weith = 1 / decile_std_by_dt.count()

                    res = 0
                    for i, j in pairs_set:
                        tmp = df_before_std[[i, j]]
                        tmp = tmp[
                            (df_before_std.index < dt) & (df_before_std.index > dt - datetime.timedelta(weeks=52))]
                        corr = 0 if pd.isna(tmp[i].ffill().bfill().corr(
                            tmp[j].ffill().bfill())) else tmp[i].ffill().bfill().corr(
                            tmp[j].ffill().bfill())
                        res += 2 * weith ** 2 * decile_std_by_dt[i] * decile_std_by_dt[j] * corr

                    for i in stocks:
                        res += weith ** 2 * decile_std_by_dt[i] ** 2
                    deciles.at[dt, f'{col}_std'] = math.sqrt(res)
    deciles.to_csv('../Data/declies_with_std.csv')


if __name__ == '__main__':
    compute_deciles_std()
