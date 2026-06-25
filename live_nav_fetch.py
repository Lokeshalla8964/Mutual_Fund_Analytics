import requests
import pandas as pd

# AMFI Code for HDFC Top 100 Direct
amfi_code = "125497"

# API URL
url = f"https://api.mfapi.in/mf/{amfi_code}"

# Get data from API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print Scheme Name
print("Scheme Name:", data["meta"]["scheme_name"])

# Convert NAV history to DataFrame
df = pd.DataFrame(data["data"])

# Save as CSV
df.to_csv("data/raw/live_nav.csv", index=False)

print("Live NAV data saved successfully!")
print(df.head())