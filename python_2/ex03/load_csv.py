# This code uses data provided by Gapminder.org.
# The data is available under the CC-BY license.

import pandas as pd


def load(filename):
    """_summary_
        load csv file and make pandas DataFrame

    Args:
        filename (str): .csv file

    Returns:
        pd.DataFrame: filename.csv ->
    """
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"FileNotFoundError:  No such file or directory: {filename}")
        data = ""
        raise FileNotFoundError
    return data


def main():
    pass


if __name__ == "__main__":
    main()


# Data attribution
# Source: Gapminder.org (https://www.gapminder.org/)
# License: CC-BY
