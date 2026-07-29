import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Style
sns.set_theme(style="whitegrid")

# Load dataset
df = pd.read_csv("42_Cases_under_crime_against_women.csv", sep="\t")

# Clean columns
df.columns = df.columns.str.strip()

# Convert numeric
df["Cases_Reported"] = pd.to_numeric(df["Cases_Reported"], errors="coerce")

# Remove nulls
df = df.dropna(subset=["Cases_Reported"])

# Group
state_data = df.groupby("Area_Name", as_index=False)["Cases_Reported"].sum()

# Sort + Top 10
state_data = state_data.sort_values("Cases_Reported", ascending=False).head(10)

# 🎨 COLOR FIX (IMPORTANT LINE)
plt.figure(figsize=(12,6))

sns.barplot(
    data=state_data,
    x="Area_Name",
    y="Cases_Reported",
    palette="viridis"   # 🔥 THIS adds multiple colors
)

plt.title("Top 10 Crime Areas in India")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()