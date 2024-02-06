from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def change_suffix(x):
    """_summary_
        change M, k,... etc to scientific notation e+06, e+03.... etc....
    Args:
        x (string): ex) 10M, 100k ....

    Returns:
        np.int64: 10e+06 ... 100e+03......
    """
    x = x.replace('M', 'e+06')
    x = x.replace('k', 'e+03')
    return x


def main():
    """_summary_
        display two country life expectance over the year[1800, 2080]
    """
    try:
        data = load("population_total.csv")
        data = data.set_index('country')
        country_data = data.loc[['South Korea', 'France']]
        country_data = \
            country_data.map(change_suffix).astype('float64').transpose()
        print(country_data)
        country_data.index = country_data.index.astype(np.int64)
        sns.lineplot(data=country_data)
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        return None


if __name__ == "__main__":
    main()
