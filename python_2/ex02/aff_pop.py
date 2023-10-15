from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def change_suffix(x):
    x = x.replace('M', 'e+06')
    x = x.replace('k', 'e+03')
    return x


def main():
    data = load("population_total.csv")
    data = data.set_index('country')
    country_data = data.loc[['South Korea', 'France']]
    country_data = country_data.map(change_suffix).astype('float64').transpose()
    print(country_data)
    country_data.index = country_data.index.astype(np.int64)
    sns.lineplot(data=country_data)
    plt.show()

if __name__ == "__main__":
    main()