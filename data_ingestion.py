import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        print("=" * 50)
        print("File:", file)

        df = pd.read_csv(os.path.join(folder, file))

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
