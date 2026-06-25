import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned CSV files
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Save tables into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database created successfully!")
print("Tables created:")
print("1. fact_nav")
print("2. fact_transactions")
print("3. fact_performance")