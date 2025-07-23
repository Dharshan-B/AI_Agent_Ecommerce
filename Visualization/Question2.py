import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_total_sales = pd.read_csv('data/Product-Level-Total-Sales-and-Metrics.csv')

df_ad_sales = pd.read_csv('data/Product-Level-Ad-Sales-and-Metrics.csv')

df_total_sales['date'] = pd.to_datetime(df_total_sales['date'])
df_ad_sales['date'] = pd.to_datetime(df_ad_sales['date'])


daily_total_sales = df_total_sales.groupby('date')['total_sales'].sum().reset_index()
daily_ad_sales = df_ad_sales.groupby('date')['ad_sales'].sum().reset_index()

df_merged_sales = pd.merge(daily_total_sales, daily_ad_sales, on='date', how='inner')

plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='total_sales', data=df_merged_sales, label='Total Sales')
sns.lineplot(x='date', y='ad_sales', data=df_merged_sales, label='Ad Sales')
plt.title('Comparison of Total Sales and Ad Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.savefig('Visualization/Screenshots/image1.jpg')
plt.show() 