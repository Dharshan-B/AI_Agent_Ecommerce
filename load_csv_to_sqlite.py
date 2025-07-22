import pandas as pd
import sqlite3
import os

#db existing
os.makedirs("db", exist_ok=True)

# Connecting to SQLite 
conn = sqlite3.connect("db/ecommerce.db")

# Mapping of table names
files = {
    "TotalSalesMetrics": "data/Product-Level-Total-Sales-and-Metrics.csv",
    "AdSalesMetrics": "data/Product-Level-Ad-Sales-and-Metrics.csv",
    "Eligibility": "data/Product-Level-Eligibility-Table.csv"
}

#Loading the Each CSV files 
for table_name, filename in files.items():
    try:
        df = pd.read_csv(filename)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f" Loaded {filename} into table '{table_name}'")
    except Exception as e:
        print(f"Failed to load {filename}: {e}")

conn.close()
print(" All data loaded into ecommerce.db!")
