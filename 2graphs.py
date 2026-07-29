import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("20_Victims_of_rape.csv", sep="\t")

# Clean column names
df.columns = df.columns.str.strip()

# Convert numeric column
df["Rape_Cases_Reported"] = pd.to_numeric(
    df["Rape_Cases_Reported"],
    errors="coerce"
)

# Group by state
state_data = (
    df.groupby("Area_Name")["Rape_Cases_Reported"]
      .sum()
      .sort_values(ascending=False)
)

# Plot
plt.figure(figsize=(12,6))
state_data.plot(kind="bar")

plt.title("State-wise Rape Cases in India")
plt.xlabel("State")
plt.ylabel("Rape Cases Reported")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()