from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")

    print(data)
    # sns.lineplot(x=data.columns, y=data.loc['South Korea'], data=data)
    # plt.title('South Korea expectancy Projections')

    # plt.show()

if __name__ == "__main__":
    main()