import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
ad_sales_df = pd.read_csv("Product-Level-Ad-Sales-and-Metrics.csv")
total_sales_df = pd.read_csv("Product-Level-Total-Sales-and-Metrics.csv")

sns.set(style="whitegrid")


total_ad_sales = ad_sales_df["Ad Sales"].sum()
total_ad_spend = ad_sales_df["Ad Spend"].sum()
plt.figure(figsize=(6, 6))
plt.pie([total_ad_sales, total_ad_spend], labels=["Ad Sales", "Ad Spend"], autopct='%1.1f%%', startangle=140)
plt.title("RoAS: Ad Sales vs Ad Spend")
plt.show()
