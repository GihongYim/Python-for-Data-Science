from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = load("life_expectancy_years.csv")
    print(data)
    data = data.set_index('country')
    country_data = data.loc['South Korea']
    country_data.index = country_data.index.astype(np.int64)
    print(type(country_data))
    sns.lineplot(data=country_data)
    plt.title('South Korea expectancy Projections')

    plt.show()


if __name__ == "__main__":
    main()
