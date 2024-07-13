from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def convert_population_to_float(pop):
    """
    Convert population values from strings to floats.
    E.g., '1.5M' to 1.5e6, '1k' to 1e3
    """
    if 'M' in pop:
        return float(pop.replace('M', '')) * 1e6
    elif 'k' in pop:
        return float(pop.replace('k', '')) * 1e3
    else:
        return float(pop)


def plot_country_life_expectancy(country_1: str, country_2: str,\
        df: pd.DataFrame, save_path: str):
    """
    Plot pop comparison of two countries
    """
    if df is not None:

        plt.figure(figsize=(8, 6))
        data_1 = df[df['country'] == country_1].iloc[:, 1:]
        data_2 = df[df['country'] == country_2].iloc[:, 1:]

        pop_1 = data_1.values.flatten()

        pop_2 = data_2.values.flatten()
        years = data_1.columns.astype(int)

        pop_1 = [convert_population_to_float(pop) for pop in pop_1]
        pop_2 = [convert_population_to_float(pop) for pop in pop_2]

        plt.plot(years, pop_1, label=country_1)
        plt.plot(years, pop_2, label=country_2)

        plt.title("Population Proyections")
        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40))
        plt.xlim(1800, 2040)
        plt.ylabel("Population")
        plt.legend()
        plt.tight_layout()
        max_pop = max(max(pop_1), max(pop_2))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

        plt.savefig(save_path, bbox_inches='tight')
        plt.close() 
        print(f"Plot saved as {save_path}")
    else:
        raise AssertionError("Error loading dataset")

def main():
    try:
        df = load("population_total.csv")
        print(df)
        plot_country_life_expectancy("Spain", "France", df, "output.png")
    
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
