import pandas as pd
import sqlite3

data = pd.read_csv("final_data.csv")

conn = sqlite3.connect("database.db")

data.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data Loaded Successfully")