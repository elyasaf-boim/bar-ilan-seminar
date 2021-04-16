from utils import get_raw_data, calc_weekly_return,calc_annum_std, sort_by_volatility

if __name__ == '__main__':
    df = get_raw_data()
    df = calc_weekly_return(df)
    df = calc_annum_std(df)
    df = sort_by_volatility(df)
    df.to_csv("C:\\Users\\RIVIK\\PycharmProjects\\bar-ilan-seminar\\out.csv")
