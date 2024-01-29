import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load


def change_suffix(x):
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
    except Exception:
        return
    income_data = income_data.set_index('country')
    print(income_data['1900'])
    year_income_data = income_data['1900']
    try:
        pop_data = load("life_expectancy_years.csv")
    except Exception:
        return
    pop_data = pop_data.set_index('country')
    print(pop_data['1900'])
    year_pop_data = pop_data['1900']
    sns.scatterplot(x=year_income_data, y=year_pop_data)
    plt.xscale('log')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name___}: {e}")
