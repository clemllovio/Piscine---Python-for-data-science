from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def convert_population_data(population_data):
    return [float(str(val).replace("M", "")) for val in population_data]

def aff_pop(dataset: pd.DataFrame):
    france_dataset = dataset.loc["France"]
    belgium_dataset = dataset.loc["Belgium"]

    france_years = list(france_dataset.index)
    france_values = convert_population_data(france_dataset.values)
    plt.plot(np.asarray(france_years, float), np.asarray(france_values, float))

    belgium_years = list(belgium_dataset.index)
    belgium_values = convert_population_data(belgium_dataset.values)
    plt.plot(np.asarray(belgium_years, float), np.asarray(belgium_values, float))

    plt.xlim(1800, 2050)
    plt.locator_params(axis='y', nbins=4)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x}M'))

    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.title("Population Projections")

    plt.legend(["France", "Belgium"])
    plt.show()

def main():
    dataset = load("population_total.csv")
    if dataset is None:
        return

    aff_pop(dataset)


if __name__ == "__main__":
    main()
