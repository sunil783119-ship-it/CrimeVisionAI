import pandas as pd
df = pd.read_csv(
    "20_Victims_of_rape.csv",
     sep="\t"
)
print("Rows:", len(df))
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())
df.columns = df.columns.str.strip()

print("\nCleaned Columns:")
print(df.columns)
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDataset Shape (Rows, Columns):")
print(df.shape)
