import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df.index, df["value"], color="red")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    return fig


def draw_bar_plot():
    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_group = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_group.plot(kind="bar", figsize=(12, 6)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        title="Months",
        labels=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    )

    return fig


def draw_box_plot():
    df_box = df.copy()

    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime("%b")

    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    df_box["month"] = pd.Categorical(df_box["month"], categories=month_order, ordered=True)

    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    return fig
