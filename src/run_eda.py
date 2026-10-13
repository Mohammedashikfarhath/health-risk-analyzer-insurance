"""Run full EDA and export cleaned data, charts and summary tables."""
import os
import pandas as pd
from data_cleaning import load_data, clean_data, summary_tables
from visualizations import (
    save_charges_distribution, save_age_vs_charges, save_bmi_vs_charges,
    save_smoker_boxplot, save_avg_charges_by_category, save_region_charges,
    save_correlation_heatmap, save_risk_score_chart,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(BASE, "data", "insurance.csv")
DATA_CLEAN = os.path.join(BASE, "data", "insurance_clean.csv")
CHART_DIR = os.path.join(BASE, "outputs", "charts")
TABLE_DIR = os.path.join(BASE, "outputs", "tables")

os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(TABLE_DIR, exist_ok=True)

df = load_data(DATA_RAW)
print(f"Raw shape: {df.shape}")
print(df.head().to_string())
print(df.describe().to_string())
print("Missing:\n", df.isnull().sum().to_string())

cdf = clean_data(df)
cdf.to_csv(DATA_CLEAN, index=False)
print(f"Cleaned shape: {cdf.shape} -> {DATA_CLEAN}")

tables = summary_tables(cdf)
for name, t in tables.items():
    out = os.path.join(TABLE_DIR, f"{name}.csv")
    t.to_csv(out)
    print(f"\n== {name} ==\n{t.to_string()} -> {out}")

save_charges_distribution(cdf, os.path.join(CHART_DIR, "01_charges_distribution.png"))
save_age_vs_charges(cdf, os.path.join(CHART_DIR, "02_age_vs_charges.png"))
save_bmi_vs_charges(cdf, os.path.join(CHART_DIR, "03_bmi_vs_charges.png"))
save_smoker_boxplot(cdf, os.path.join(CHART_DIR, "04_smoker_boxplot.png"))
save_avg_charges_by_category(cdf, os.path.join(CHART_DIR, "05_avg_by_bmi_category.png"))
save_region_charges(cdf, os.path.join(CHART_DIR, "06_avg_by_region.png"))
save_correlation_heatmap(cdf, os.path.join(CHART_DIR, "07_correlation_heatmap.png"))
save_risk_score_chart(cdf, os.path.join(CHART_DIR, "08_risk_score.png"))

# Console insights
print("\n--- KEY INSIGHTS ---")
print("Smoker mean vs non-smoker mean:")
print(tables["by_smoker"].to_string())
print("\nRisk score means:")
print(tables["by_risk_score"].to_string())
print("\nCorr age/bmi/smoker with charges:")
print(cdf[["age","bmi","children","charges","is_smoker","risk_score"]].corr(numeric_only=True)["charges"].to_string())
print("\nDone. Charts in outputs/charts, tables in outputs/tables")
