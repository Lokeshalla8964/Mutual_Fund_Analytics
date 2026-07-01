import pandas as pd

scheme_performance = pd.read_csv("data/raw/07_scheme_performance.csv")

risk_choice = "Moderate"   # Change to Low, Moderate, or High

recommendation = (
    scheme_performance[
        scheme_performance["risk_grade"] == risk_choice
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

print(recommendation)