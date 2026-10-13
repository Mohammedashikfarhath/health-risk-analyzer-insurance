# Health Risk Analyzer — Insights Summary

Dataset: `data/insurance.csv` → `data/insurance_clean.csv` (1337 rows after 1 duplicate removed, 0 missing values).

## Key Findings (verified by `src/run_eda.py`)

1. **Smoking is the dominant driver (corr 0.79)**
   - Smokers: n=274, mean $32,050, median $34,456
   - Non-smokers: n=1063, mean $8,440, median $7,345
   - ~3.8x mean difference.

2. **Combined risk compounds**
   - Risk score = smoker + obese + senior(50+)
   - 0: $6,252 | 1: $10,166 | 2: $22,918 | 3: $46,973 (n=41)
   - High-cost cases almost always have 2+ risk factors.

3. **Age matters (corr 0.30)**
   - 18-25: $9,111 | 26-35: $10,495 | 36-50: $14,029 | 51+: $18,084

4. **BMI matters (corr 0.20)**
   - Obese (n=706): $15,572 | Overweight: $10,987 | Normal: $10,409 | Underweight: $8,852
   - BMI + smoking interaction clearly visible in scatter.

5. **Region / children / sex are weak**
   - Southeast $14,735 highest, Southwest $12,346 lowest — small vs smoking gap.
   - Children corr 0.067 — negligible.

## Business Recommendations
- Price smoking risk explicitly; fund cessation programs.
- Bundle age+BMI+smoking into tiered risk score for underwriting.
- Target 51+ obese smokers for preventive care — highest expected charges.
- Don't over-weight region in pricing; focus on lifestyle factors.

## Reproduce
```
pip install -r requirements.txt
python src/run_eda.py
jupyter notebook notebooks/01_eda_health_insurance.ipynb
```
Charts: `outputs/charts/`, Tables: `outputs/tables/`
