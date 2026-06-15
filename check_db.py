import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")

data = pd.read_sql(
    "SELECT * FROM customers",
    conn
)

print(data)

conn.close()