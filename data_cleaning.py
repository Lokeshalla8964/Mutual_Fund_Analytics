import pandas as pd

# Load CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Missing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only expense ratio between 0.1 and 2.5
df = df[(df["expense_ratio_pct"] >= 0.1) & (df["expense_ratio_pct"] <= 2.5)]

# Save cleaned file
df.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("Cleaning Completed Successfully!")
print("Final Shape:", df.shape)
print(df.head())