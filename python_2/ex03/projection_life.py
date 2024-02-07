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
        print(income_data['1900'])
        year_income_data = income_data['1900']
        pop_data = load("life_expectancy_years.csv")
        pop_data = pop_data.set_index('country')
        print(pop_data['1900'])
        year_pop_data = pop_data['1900']
        sns.scatterplot(x=year_income_data, y=year_pop_data, label="person")
        plt.legend(loc='upper left')
        plt.xscale('log')
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
