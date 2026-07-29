# ===============================
# CrimeVisionAI - Day 1 EDA
# ===============================

import pandas as pd

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv(
    "42_Cases_under_crime_against_women.csv",
    sep="\t"
)

# -------------------------------
# 2. Basic Info
# -------------------------------
print("Rows:", len(df))
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------
# 3. Clean Column Names
# -------------------------------
df.columns = df.columns.str.strip()

print("\nCleaned Columns:")
print(df.columns)

# -------------------------------
# 4. Dataset Info
# -------------------------------
print("\nDataset Info:")
print(df.info())

# -------------------------------
# 5. Missing Values Check
# -------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# 6. Statistical Summary
# -------------------------------
print("\nStatistical Summary:")
print(df.describe(include='all'))

# -------------------------------
# 7. Shape of Dataset
# -------------------------------
print("\nDataset Shape (Rows, Columns):")
print(df.shape)