from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = load("life_expectancy_years.csv")
    print(data)
    data = data.set_index('country')
    country_data = data.loc['South Korea']
    print(country_data)
    sns.lineplot(data=country_data)
    plt.title('South Korea expectancy Projections')
    plt.xticks(np.arange(100, 200 ,1))

    plt.show()

if __name__ == "__main__":
    main()