from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_country_life_expectancy(country: str,\
        df: pd.DataFrame, save_path: str):
    """
        Plot life expectancy of a country
    """
    if df is not None:
        if country in df['country'].values:
            country_data = df[df['country'] == country].T
            country_data.columns = country_data.iloc[0]

            country_data = country_data.drop(country_data.index[0])
            country_data.index = country_data.index.astype(int)
            country_data = country_data.astype(float)
            
            plt.figure(figsize=(8, 6))
            sns.lineplot(data=country_data, legend=False)
            plt.title(f'{country} Life expectancy proyections')
            plt.xlabel('Year')
            plt.ylabel('Life Expectancy')
            plt.legend(labels=[country])
            
            x_ticks = range(int(country_data.index.min()),\
                int(country_data.index.max()) + 1, 40)
            plt.xticks(ticks=x_ticks)

            plt.gca().get_legend().remove()
            
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            print(f"Plot saved as {save_path}")
        else:
            raise AssertionError("Country not found in dataset")
    else:
        raise AssertionError("Error loading dataset")

def main():
    try:
        df = load("life_expectancy_years.csv")
        print(df)
        plot_country_life_expectancy("Spain", df, "output.png")
    
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()