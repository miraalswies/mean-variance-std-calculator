import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue")

    # First line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    years_extended = pd.Series(range(df["Year"].min(), 2051))
    ax.plot(
        years_extended,
        slope * years_extended + intercept,
        "r",
        label="Best Fit (All Data)"
    )

    # Second line of best fit (from year 2000)
    df_2000 = df[df["Year"] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )

    years_extended_2 = pd.Series(range(2000, 2051))
    ax.plot(
        years_extended_2,
        slope2 * years_extended_2 + intercept2,
        "green",
        label="Best Fit (2000+)"
    )

    # Labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    return fig
