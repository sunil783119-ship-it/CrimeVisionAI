import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("42_Cases_under_crime_against_women.csv", sep="\t")

# Clean column names
df.columns = df.columns.str.strip()

# Convert numeric column (important)
df["Cases_Reported"] = pd.to_numeric(df["Cases_Reported"], errors="coerce")

# Group by Area (State equivalent)
state_data = df.groupby("Area_Name")["Cases_Reported"].sum().sort_values(ascending=False)

# Plot
plt.figure(figsize=(12,6))
state_data.plot(kind="bar")

plt.title("State-wise Crime Cases in India")
plt.xlabel("State (Area_Name)")
plt.ylabel("Cases Reported")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()