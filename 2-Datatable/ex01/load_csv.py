import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load dataset from path 
        prints the dimensions of the dataset
        return as pandas dataframe
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def main():
    df = load("life_expectancy_years.csv")
    print(df)


if __name__ == "__main__":
    main()
