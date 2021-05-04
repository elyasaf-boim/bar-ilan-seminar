import matplotlib.pyplot as plt
import pandas as pd


def plot_market_port_monthly_return():
    df = pd.read_csv("./Data/market_portfolio_monthly_return.csv")
    plt.plot("Date", "Adj Close", data=df)
    plt.xlabel('Date')
    plt.ylabel('Monthly Return')
    plt.show()


if __name__ == '__main__':
    plot_market_port_monthly_return()
