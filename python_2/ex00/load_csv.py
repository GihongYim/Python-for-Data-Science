import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load csv file

    Args:
        path (str): csv filepath

    Returns:
        pd.DataFrame:  csv-> pd.DataFrame
    """

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main():
    pass


if __name__ == "__main__":
    main()
