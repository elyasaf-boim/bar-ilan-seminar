import datetime
from math import ceil

import investpy
import pandas as pd
import numpy as np

from const import bad_stocks

FROM_DATE = "01/03/2002"
TO_DATE = "01/01/2020"


def calc_log_monthly_return_of_deciles():
    raw_data = pd.read_csv("../Data/investing_raw_data.csv", index_col=1, header=0)
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
                d_raw_data = d_raw_data.resample("M").ffill().pct_change()
                if int(month) == 12:
                    month = 1
                    year = int(year) + 1
                else:
                    year = int(year)
                    month = int(month) + 1

                res_df[f"D{i}"][f"{row['year']}_{row['month']}"] = d_raw_data.iloc[
                    d_raw_data.index.get_loc(datetime.datetime(year, month, 1), method='nearest')].mean()
    res_df.to_csv("..\\Data\\investing_deciles_monthly_return.csv")


def compute_df_log(years=1):
    df = pd.read_csv("..\\Data\\investing_raw_data.csv", index_col=0, header=0)
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df.resample('W').ffill()
    for col in df.columns:
        df[f'log return {col}'] = np.log(df[col]) - np.log(df[col].shift(1))
    df = df.rolling(52 * years).std()
    df = df.groupby([df.index.year, df.index.month]).last().T
    df = _sort_by_volatility(df)
    df.to_csv("..\\Data\\investing_deciles.csv")


if __name__ == '__main__':
    compute_df_log()
