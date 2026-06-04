# ==========================================
# CUSTOMER SHOPPING TRENDS ANALYSIS PROJECT
# ==========================================

# STEP 1: Import Required Libraries

import pandas as pd
import matplotlib.pyplot as plt

# STEP 2: Load Dataset

df = pd.read_csv("shopping_trends.csv")

# STEP 3: Display Basic Information

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Records:")
print(df.head())

# STEP 4: Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# STEP 5: Check Duplicate Records

print("\nDuplicate Records:")
print(df.duplicated().sum())

# STEP 6: Basic Statistics

print("\nStatistical Summary:")
print(df.describe())

# STEP 7: Total Revenue

total_revenue = df["Purchase Amount (USD)"].sum()

print("\nTotal Revenue:")
print(total_revenue)

# STEP 8: Average Purchase Amount

average_purchase = df["Purchase Amount (USD)"].mean()

print("\nAverage Purchase Amount:")
print(round(average_purchase,2))

# STEP 9: Gender Wise Revenue

gender_revenue = df.groupby("Gender")["Purchase Amount (USD)"].sum()

print("\nGender Wise Revenue:")
print(gender_revenue)

# STEP 10: Category Wise Revenue

category_revenue = df.groupby("Category")["Purchase Amount (USD)"].sum()

print("\nCategory Revenue:")
print(category_revenue)

# STEP 11: Top Selling Products

top_products = df.groupby("Item Purchased")["Purchase Amount (USD)"].sum()

top_products = top_products.sort_values(ascending=False)

print("\nTop Products:")
print(top_products.head(10))

# STEP 12: Location Wise Revenue

location_revenue = df.groupby("Location")["Purchase Amount (USD)"].sum()

location_revenue = location_revenue.sort_values(ascending=False)

print("\nTop Locations:")
print(location_revenue.head())

# STEP 13: Payment Method Analysis

payment_analysis = df["Payment Method"].value_counts()

print("\nPayment Methods:")
print(payment_analysis)

# STEP 14: Seasonal Sales Analysis

season_sales = df.groupby("Season")["Purchase Amount (USD)"].sum()

print("\nSeason Wise Revenue:")
print(season_sales)

# STEP 15: Subscription Analysis

subscription_sales = df.groupby("Subscription Status")["Purchase Amount (USD)"].sum()

print("\nSubscription Revenue:")
print(subscription_sales)

# STEP 16: Review Rating Analysis

avg_rating = df["Review Rating"].mean()

print("\nAverage Rating:")
print(round(avg_rating,2))

# ==========================================
# VISUALIZATION SECTION
# ==========================================

# Chart 1 : Category Revenue

category_revenue.plot(kind="bar",figsize=(8,5))

plt.title("Category Wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# Chart 2 : Season Revenue

season_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)

plt.title("Season Wise Sales")
plt.ylabel("")
plt.show()

# Chart 3 : Payment Methods

payment_analysis.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

# Chart 4 : Top 10 Products

top_products.head(10).plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Top 10 Products")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.show()

print("\nProject Analysis Completed Successfully.")