import sqlite3

conn = sqlite3.connect("db/ecommerce.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(Eligibility);")
columns = cursor.fetchall()

print("Columns in Eligibility:")
for col in columns:
    print(col)

conn.close()
