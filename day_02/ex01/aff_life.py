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
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return

    aff_life(dataset)


if __name__ == "__main__":
    main()
