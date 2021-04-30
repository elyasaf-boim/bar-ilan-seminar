import datetime

import pandas as pd


def calc_monthly_return_of_deciles():
    raw_data = pd.read_csv("./Data/raw_data.csv", index_col=[0], header=[0, 1])
    deciles = pd.read_csv("./Data/deciles_by_volatility_3_years_back.csv").rename(
        columns={'Unnamed: 0': 'year', 'Unnamed: 1': 'month'})
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
            d_stocks = row[f"D{i}"].split()
            d_stocks = [symbol.translate({ord(i): None for i in "'[]"}) for symbol in d_stocks]
            if d_stocks != ['']:
                d_raw_data = raw_data["Adj Close"][d_stocks].ffill()
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
    return res_df


if __name__ == '__main__':
    calc_monthly_return_of_deciles()
