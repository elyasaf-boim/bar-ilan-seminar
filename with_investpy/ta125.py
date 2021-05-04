import datetime
from math import ceil

import investpy
import pandas as pd


investpy.get_index_historical_data(index='TA 125', country='israel', from_date='01/01/2018', to_date='01/01/2019')


def fun():
    df = pd.read_csv("C:\\Users\\Ofra\\PycharmProjects\\bar-ilan-seminar\\Data\\maya_ta_125.csv").set_index('Date')
    df.index = pd.to_datetime(df.index)
