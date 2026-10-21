"""
Sales Data Analytics with Python & Power BI
--------------------------------------------
Step 1: Load the raw sales data.
Step 2: Clean it (handle missing values and duplicates).
Step 3: Generate summary statistics (by region, by product, monthly trend).
Step 4: Export clean, Power-BI-ready CSV files.
Step 5: (Optional) Plot a quick chart in Python to sanity-check the numbers.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------- Step 1: Load the data ----------
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
print(f"Loaded {len(df)} rows.")

# ---------- Step 2: Clean the data ----------
# Drop exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df)} duplicate row(s).")

# Fill missing Quantity with the column median, missing Revenue by recomputing it
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

unit_price = (df["Revenue"] / df["Quantity"]).median()
df["Revenue"] = df["Revenue"].fillna(df["Quantity"] * unit_price)

df["Quantity"] = df["Quantity"].astype(int)
df["Revenue"] = df["Revenue"].astype(float).round(2)

# Save the cleaned dataset — this is the file you import into Power BI
df.to_csv("cleaned_sales_data.csv", index=False)
print("Saved cleaned_sales_data.csv")

# ---------- Step 3: Summary statistics ----------
by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly_trend = df.groupby("Month")["Revenue"].sum()

print("\nRevenue by Region:\n", by_region)
print("\nRevenue by Product:\n", by_product)
print("\nMonthly Revenue Trend:\n", monthly_trend)

# Export summary tables — these also plug straight into Power BI visuals
by_region.to_csv("summary_by_region.csv")
by_product.to_csv("summary_by_product.csv")
monthly_trend.to_csv("summary_monthly_trend.csv")

# ---------- Step 4: Quick chart (optional sanity check) ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
by_region.plot(kind="bar", ax=axes[0], title="Revenue by Region", color="#1a3fb0")
monthly_trend.plot(kind="line", marker="o", ax=axes[1], title="Monthly Revenue Trend", color="#1a3fb0")
plt.tight_layout()
plt.savefig("revenue_overview.png", dpi=150)
print("\nSaved chart to revenue_overview.png")
