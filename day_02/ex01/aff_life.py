from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def aff_life(dataset: pd.DataFrame):
    """
    Plots the life expectancy in France over the years.
    """
    country_dataset = dataset.loc["France"]
    years = list(country_dataset.index)
    values = list(country_dataset.values)

    plt.plot(np.asarray(years, float), values)
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.title("France life expectancy")
    plt.show()


def main():
    """
    Loads a dataset containing life expectancy data and processes it.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return 1

    aff_life(dataset)
    return 0


if __name__ == "__main__":
    main()
