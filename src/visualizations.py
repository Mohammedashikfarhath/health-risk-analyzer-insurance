"""Reusable matplotlib/seaborn charts for the insurance EDA."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


def save_charges_distribution(df, path):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["charges"], kde=True, bins=30, ax=ax)
    ax.set_title("Distribution of Insurance Charges")
    ax.set_xlabel("Charges (USD)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_age_vs_charges(df, path):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="age", y="charges", hue="smoker", alpha=0.7, ax=ax)
    ax.set_title("Age vs Charges (by Smoking Status)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_bmi_vs_charges(df, path):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="bmi", y="charges", hue="smoker", alpha=0.7, ax=ax)
    ax.set_title("BMI vs Charges (by Smoking Status)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_smoker_boxplot(df, path):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x="smoker", y="charges", ax=ax)
    ax.set_title("Charges: Smokers vs Non-Smokers")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_avg_charges_by_category(df, path):
    order = ["Underweight", "Normal", "Overweight", "Obese"]
    grp = df.groupby("bmi_category")["charges"].mean().reindex(order)
    fig, ax = plt.subplots(figsize=(8, 5))
    grp.plot(kind="bar", ax=ax, color="#1C355D")
    ax.set_title("Average Charges by BMI Category")
    ax.set_ylabel("Avg Charges")
    plt.xticks(rotation=15)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_region_charges(df, path):
    grp = df.groupby("region")["charges"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    grp.plot(kind="barh", ax=ax, color="#294F42")
    ax.set_title("Average Charges by Region")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_correlation_heatmap(df, path):
    num = df[["age", "bmi", "children", "charges", "is_smoker", "risk_score"]].corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(num, annot=True, fmt=".2f", cmap="Blues", ax=ax)
    ax.set_title("Correlation Heatmap")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_risk_score_chart(df, path):
    grp = df.groupby("risk_score")["charges"].mean()
    fig, ax = plt.subplots(figsize=(7, 5))
    grp.plot(kind="bar", ax=ax, color="#B3502E")
    ax.set_title("Average Charges by Risk Score (smoker+obese+senior)")
    ax.set_xlabel("Risk Score (0-3)")
    ax.set_ylabel("Avg Charges")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
