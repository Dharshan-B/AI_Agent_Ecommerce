import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ad_sales_df = pd.read_csv("Product-Level-Ad-Sales-and-Metrics.csv")
total_sales_df = pd.read_csv("Product-Level-Total-Sales-and-Metrics.csv")

sns.set(style="whitegrid")


plt.figure(figsize=(12, 6))
top_cpc_df = ad_sales_df.sort_values(by="CPC", ascending=False).head(10)
sns.barplot(x="Product Name", y="CPC", data=top_cpc_df)
plt.title("Top 10 Products by CPC")
plt.xlabel("Product")
plt.ylabel("Cost Per Click (CPC)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
