from utils import get_raw_data, calc_weekly_return, calc_annum_std, sort_by_volatility

if __name__ == '__main__':
    years = 1
    df = get_raw_data(how_many_stocks=None)
    df = calc_weekly_return(df)
    df = calc_annum_std(df, years=years)
    df = sort_by_volatility(df)
    df.to_csv(f".\\out-{years}.csv")
