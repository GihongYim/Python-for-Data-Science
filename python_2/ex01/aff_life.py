from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")

    country_data = data.loc['South Korea']
    print(country_data)
    sns.lineplot(data=country_data)
    plt.title('South Korea expectancy Projections')

    plt.show()

if __name__ == "__main__":
    main()