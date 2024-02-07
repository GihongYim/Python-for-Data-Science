import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load


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


def x_formatter(x, pos):
    return str(int(round(x / 1e3, 0))) + "k"


def main():
    """
    display dotplot
    x axis -> income
    y axis -> life expectancy

    """
    try:
        income_data = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        income_data = income_data.set_index('country')
        year = '1900'
        print(income_data[year])
        year_income_data = income_data[year]
        pop_data = load("life_expectancy_years.csv")
        pop_data = pop_data.set_index('country')
        print(pop_data[year])
        year_pop_data = pop_data[year]
        ax = sns.scatterplot(x=year_income_data,
                             y=year_pop_data,
                             label="country")
        plt.title(year)
        plt.legend(loc='upper left')
        plt.xscale('log')
        ax.xaxis.set_major_formatter(x_formatter)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        return None


if __name__ == "__main__":
    """main function for proejction_life.py
    """
    main()
