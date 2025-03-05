from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def projection_life(income_dataset: pd.DataFrame,
                    life_expectancy_dataset: pd.DataFrame):
    """
    Visualizes the relationship between income and life expectancy
    for the year 1900 by plotting a scatter plot
    """
    income_1900 = income_dataset.loc[:, '1900'].tolist()
    life_expectancy_1900 = life_expectancy_dataset.loc[:, '1900'].tolist()

    print(income_1900)
    plt.scatter(income_1900, life_expectancy_1900)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.title('1900')
    plt.xscale('log')
    plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter())
    plt.show()

    print(life_expectancy_1900)


def main():
    """
    Loads a dataset containing life expectancy data and processes it.
    """
    life_expectancy_dataset = load("life_expectancy_years.csv")
    if life_expectancy_dataset is None:
        return 1

    income_dataset = (
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
    if income_dataset is None:
        return 1

    projection_life(income_dataset, life_expectancy_dataset)
    return 0


if __name__ == "__main__":
    main()
