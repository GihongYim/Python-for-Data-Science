# This code uses data provided by Gapminder.org.
# The data is available under the CC-BY license.

import pandas as pd

def load(filename):
    '''open csv dataset'''
    try:
        data = pd.read_csv(filename, index_col=True)
    except FileNotFoundError:
        print("FileNotFoundError:  No such file or directory: {filename}")
        data = ""
    return data


# Data attribution
# Source: Gapminder.org (https://www.gapminder.org/)
# License: CC-BY