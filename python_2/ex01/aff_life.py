from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
        1) life_expectancy_years.csv file to pd.DataFrame
        2) display following graph
            x axis : year [1800, 2080]
            y axis : life expectancy
    """
    try:
        data = load("life_expectancy_years.csv")
        # country = 'South Korea'
        country = 'France'
        print(data)
        data = data.set_index('country')
        country_data = data.loc[country]
        country_data.index = country_data.index.astype(np.int64)
        print(type(country_data))
        sns.lineplot(data=country_data)
        plt.title(f'{country} expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        return None


if __name__ == "__main__":
    """main function for aff_list.py
    """
    main()
