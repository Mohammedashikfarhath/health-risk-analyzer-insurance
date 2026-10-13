"""Data cleaning utilities for Health Risk Analyzer Insurance project."""
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Deduplicate, standardize strings, add engineered risk features."""
    df = df.copy()
    df = df.drop_duplicates()

    # Standardize categoricals
    for col in ["sex", "smoker", "region"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()

    # Engineered features
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 35, 50, 100],
        labels=["18-25", "26-35", "36-50", "51+"],
    )

    def bmi_cat(b):
        if b < 18.5:
            return "Underweight"
        if b < 25:
            return "Normal"
        if b < 30:
            return "Overweight"
        return "Obese"

    df["bmi_category"] = df["bmi"].apply(bmi_cat)
    df["is_smoker"] = (df["smoker"] == "yes").astype(int)
    df["is_obese"] = (df["bmi"] >= 30).astype(int)
    df["is_senior"] = (df["age"] >= 50).astype(int)
    # Simple risk score 0-3
    df["risk_score"] = df["is_smoker"] + df["is_obese"] + df["is_senior"]
    df["high_cost_flag"] = (df["charges"] > 20000).astype(int)

    return df


def summary_tables(df: pd.DataFrame) -> dict:
    """Return key aggregation tables."""
    tables = {}
    tables["by_smoker"] = df.groupby("smoker")["charges"].agg(
        ["count", "mean", "median", "std"]
    )
    tables["by_bmi_category"] = df.groupby("bmi_category")["charges"].agg(
        ["count", "mean", "median"]
    )
    tables["by_age_group"] = df.groupby("age_group", observed=True)["charges"].agg(
        ["count", "mean", "median"]
    )
    tables["by_region"] = df.groupby("region")["charges"].agg(
        ["count", "mean", "median"]
    )
    tables["by_risk_score"] = df.groupby("risk_score")["charges"].agg(
        ["count", "mean", "median"]
    )
    return tables
