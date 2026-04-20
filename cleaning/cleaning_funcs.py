import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_percent_missing(df):
    for column in df:

        # Select column contents by column
        # name using [] operator
        missing = df[column].isnull().sum() / len(df)
        missing = missing * 100
        print(f"{column}: {round(missing, 2)}%")

def check_for_NR(df):
    for column in df:

        # Select column contents by column
        # name using [] operator
        S = df[column].isin(['N.R.']).any()
        print(f"{column}: {S}")

def check_for_S(df):
    for column in df:

        # Select column contents by column
        # name using [] operator
        S = df[column].isin(['S']).any()
        print(f"{column}: {S}")

def impute(og, new):
    for column in og:
        if og[column].dtype == 'float64':
            median = og[column].median()
            new[column] = new[column].fillna(median)
    return new

def comp_dist(og, new, column):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # original variable distribution
    og[column].plot(kind='kde', ax=ax)

    # variable imputed with the median
    new[column].plot(kind='kde', ax=ax, color='red')

    lines, labels = ax.get_legend_handles_labels()
    ax.legend(lines, labels, loc='best')

    plt.show()

def make_plots(og, new):
    for column in og:
        if og[column].dtype == 'float64':
            comp_dist(og, new, column)

def plot_one(df, column):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    df[column].plot(kind='kde', ax=ax)

    ax.set_xlim(-5000, 5000)

    lines, labels = ax.get_legend_handles_labels()
    ax.legend(lines, labels, loc='best')

    plt.show()