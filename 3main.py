import pandas as pd
df = pd.read_csv(
    "42_Cases_under_crime_against_women.csv",
     sep="\t"
)

print(df.columns)