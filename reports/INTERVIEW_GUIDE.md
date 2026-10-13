# Interview Guide — Health Risk Analyzer Insurance

## 1. Project Explanation (what to say)

**One-line:**
Analyzed 1,338 insurance records to find what drives charges — smoking, age, BMI — using Python EDA + Power BI.

**Repo:** https://github.com/Mohammedashikfarhath/health-risk-analyzer-insurance

**Stack:** Python (pandas, matplotlib, seaborn), Jupyter, Power BI, GitHub
**Data:** `age, sex, bmi, children, smoker, region, charges` → cleaned + engineered `age_group, bmi_category, risk_score (smoker+obese+senior), high_cost_flag`

**Key results (use these numbers):**
- Smokers: $32,050 mean vs non-smokers $8,440 — **3.8x gap, corr 0.79**, strongest driver
- Risk score: 0:$6.2k → 1:$10.1k → 2:$22.9k → 3:$47k — risk compounds
- Age corr 0.30 (18-25 $9.1k → 51+ $18k), BMI corr 0.20 (Obese $15.5k vs Normal $10.4k)
- Region/children weak (SE $14.7k vs SW $12.3k, children corr 0.07)

## 2. How to Tell the Interviewer

**30-sec pitch:**
> "I built a Health Risk Analyzer on 1,300+ insurance records. Using Python EDA I found smoking is the top cost driver at 3.8x higher charges, and combined risk — smoker + obese + senior — pushes average charges from $6k to $47k. I visualized this in Python and documented a 3-page Power BI dashboard spec with KPIs and DAX."

**2-min STAR version:**
- **S:** Insurers overprice/underprice because they don't quantify lifestyle risk.
- **T:** Quantify impact of age, BMI, smoking, region on charges.
- **A:** Cleaned data (1 duplicate removed, 0 nulls), engineered risk_score, did univariate/bivariate/correlation, exported 8 charts + 5 tables, wrote Power BI guide with slicers, Key Influencers, DAX.
- **R:** Proved smoking dominates, region doesn't — recommendation: tier pricing by risk_score + fund cessation/preventive care for 51+ obese smokers.

**Closing line:**
> "I can walk you through the notebook, the 8 charts, or the Power BI DAX — which do you want to see?"

## 3. Likely Interview Questions + Short Answers

**Project / Business:**
1. Why this project? → Show underwriting use-case: fair pricing + targeted wellness.
2. Business impact? → Tiered pricing, cessation programs, prioritize high-risk cohort (41 cases score=3, ~$47k avg).
3. What with more data? → Add claim history, income, pre-existing conditions; build regression to predict charges (RMSE/MAE).

**Python / EDA:**
4. How handle missing/duplicates/outliers? → `drop_duplicates()` (1338→1337), `isnull().sum()` = 0, IQR + boxplots, right-skew charges noted, median vs mean.
5. Why engineered risk_score? → Captures interaction; single features miss compounding. Proved by monotonic $6k→$47k gradient.
6. Correlation vs causation? → 0.79 smoking correlation is strong but not proof; confounders exist — hence grouped + risk_score analysis.

**Visualization / Power BI:**
7. Why those charts? → Histogram (skew), boxplot (smoker gap), scatter hue=smoker (interaction), bar (BMI/region), heatmap (correlations).
8. Design Power BI dashboard? → P1 Overview (cards + slicers), P2 Drivers (scatter + bars), P3 Segments (Key Influencers + high-cost drill-through). DAX: Avg Charges, Median Charges, % Smokers, High Risk Count.
9. Power BI vs Python? → Python for deep EDA/reproducibility, Power BI for slicers + business users.

**Statistics / Follow-ups:**
10. Age vs BMI — which matters more? → Age (0.30 > 0.20), but smoking dwarfs both.
11. Region significant? → No — small $2k spread vs $23k smoker gap; SE highest but driven by lifestyle mix.
12. How validate? → Group means + medians (outlier-robust), correlation matrix, high-cost drill-down.

**Tough ones:**
- SQL: `SELECT smoker, region, AVG(charges) FROM insurance GROUP BY 1,2;`
- Predict charges? → Linear Regression baseline, then Random Forest/XGBoost, RMSE/MAE, log-transform skewed charges.
- Ethics → Don't use sex/region to discriminate; focus on modifiable risks.
