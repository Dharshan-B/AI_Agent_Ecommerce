import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_eligibility = pd.read_csv('data/Product-Level-Eligibility-Table.csv')


df_eligibility['eligibility_date'] = pd.to_datetime(df_eligibility['eligibility_datetime_utc']).dt.date
df_eligibility['eligibility_date'] = pd.to_datetime(df_eligibility['eligibility_date']) # Convert back to datetime for plotting


eligible_products = df_eligibility[df_eligibility['eligibility'] == True]


eligible_products_count = eligible_products.groupby('eligibility_date').size().reset_index(name='num_eligible_products')

plt.figure(figsize=(12, 6))
sns.lineplot(x='eligibility_date', y='num_eligible_products', data=eligible_products_count)
plt.title('Number of Eligible Products Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Eligible Products')
plt.grid(True)
plt.tight_layout()
#plt.savefig('Visualization/Screenshots/image3.jpg')
plt.show() 