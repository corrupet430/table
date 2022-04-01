import pandas as pd
from pandas import DataFrame

def print_result(df: DataFrame, profit_home_open):
    sum_df = df[profit_home_open].sum()
    count = df.shape[0]

    bets_df = df[profit_home_open].cumsum()

    print('Count:', count)
    print(bets_df.plot())

def print_profit_home_result(df: DataFrame):
    print_result(df, 'profit_home_open')