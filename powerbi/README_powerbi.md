# Power BI Dashboard Guide

Use `data/insurance_clean.csv` as source (already cleaned + has `age_group, bmi_category, risk_score, high_cost_flag`).

## Pages to Build

**Page 1 — Overview**
- Cards: Avg Charges, Median Charges, % Smokers, Avg BMI, High-risk count (risk_score>=2)
- Slicers: smoker, region, bmi_category, age_group
- Clustered column: Avg Charges by smoker
- Histogram: Charges distribution

**Page 2 — Risk Drivers**
- Scatter: BMI (x) vs Charges (y), legend smoker
- Scatter: Age vs Charges, legend smoker
- Bar: Avg Charges by BMI Category (Under/Normal/Over/Obese)
- Bar: Avg Charges by Age Group
- Matrix: Region x Smoker → Avg Charges

**Page 3 — Segments**
- Key Influencers visual: Analyze `high_cost_flag` or `charges` by age, bmi, smoker, bmi_category
- Table with conditional formatting: region, avg charges, smoker %, avg BMI
- Filter high-cost (>20000) drill-through

## Suggested DAX
```
Avg Charges = AVERAGE(insurance_clean[charges])
Median Charges = MEDIAN(insurance_clean[charges])
% Smokers = DIVIDE(CALCULATE(COUNTROWS(insurance_clean), insurance_clean[smoker]="yes"), COUNTROWS(insurance_clean))
High Risk Count = CALCULATE(COUNTROWS(insurance_clean), insurance_clean[risk_score]>=2)
Smoker Premium = [Avg Charges Smokers] - [Avg Charges NonSmokers]
```

## Export
Save as `powerbi/health_risk_dashboard.pbix`, then export 2-3 PNGs + PDF and link them in main README.
Python charts in `outputs/charts/` can be used as reference layout.
