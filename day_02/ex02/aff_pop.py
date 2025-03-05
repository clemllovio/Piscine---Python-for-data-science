from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def convert_population_data(population_data):
    """
    Convert the population data to a list of floats
    """
    value_list = []
    for value in population_data:
        if value[-1] in 'MBk':
            numeric_part = value[:-1]
            if value[-1] == 'M':
                value_list.append(float(numeric_part) * 1000000)
            elif value[-1] == 'k':
                value_list.append(float(numeric_part) * 1000)
            elif value[-1] == 'B':
                value_list.append(float(numeric_part) * 1000000000)
        else:
            value_list.append(float(value))

    return value_list


def change_format(value, _):
    """
    Change the format of the y-axis
    """
    if value < 1000:
        return f"{value}"
    elif value < 1000000:
        return f"{value / 1000:.0f}k"
    elif value < 1000000000:
        return f"{value / 1000000:.0f}M"
    else:
        return f"{value / 1000000000:.0f}B"


def aff_pop(dataset: pd.DataFrame):
    """
    Plots the population projections for France and Belgium over time
    based on the provided dataset.
    """
    france_dataset = dataset.loc["France"]
    belgium_dataset = dataset.loc["Belgium"]

    france_years = list(france_dataset.index)
    france_values = convert_population_data(france_dataset.values)
    plt.plot(np.asarray(france_years, float), np.asarray(france_values, float))

    belgium_years = list(belgium_dataset.index)
    belgium_values = convert_population_data(belgium_dataset.values)
    plt.plot(np.asarray(belgium_years, float),
             np.asarray(belgium_values, float))

    plt.xlim(1800, 2050)
    plt.locator_params(axis='y', nbins=4)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(change_format))

    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.title("Population Projections")

    plt.legend(["France", "Belgium"])
    plt.show()


def main():
    """
        Loads a dataset containing life expectancy data and processes it.
    """
    dataset = load("population_total.csv")
    if dataset is None:
        return 1

    aff_pop(dataset)
    return 0


if __name__ == "__main__":
    main()
