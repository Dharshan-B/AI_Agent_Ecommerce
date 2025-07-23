import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_total_sales = pd.read_csv('data/Product-Level-Total-Sales-and-Metrics.csv')

df_total_sales['date'] = pd.to_datetime(df_total_sales['date'])

daily_total_sales = df_total_sales.groupby('date')['total_sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='total_sales', data=daily_total_sales)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('total_sales_over_time.png')
plt.show() 