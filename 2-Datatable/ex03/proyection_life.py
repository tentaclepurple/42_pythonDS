from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def scatter_income_life(gdp: pd.DataFrame, life: pd.DataFrame,\
        save_path: str):
    """
    Scatter plot of income vs life expectancy
    """
    if gdp is not None and life is not None:
        income_data = gdp["1900"]
        life_data = life["1900"]

        plt.figure(figsize=(8, 6))
        plt.scatter(income_data, life_data, alpha=0.5)

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()

        plt.savefig(save_path, bbox_inches='tight')
        plt.close() 
        print(f"Plot saved as {save_path}")

    else:
        raise AssertionError("Error loading dataset")

def main():
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life = load("life_expectancy_years.csv")
        scatter_income_life(gdp, life, "income_vs_life.png")


    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
