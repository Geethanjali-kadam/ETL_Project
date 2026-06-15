import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")

old_data = pd.read_sql(
    "SELECT * FROM customers",
    engine
)

new_data = pd.read_csv(
    "new_data.csv"
)

final_data = pd.concat(
    [old_data, new_data]
)

final_data = final_data.drop_duplicates(
    subset="customer_id",
    keep="last"
)

print(final_data)

final_data.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("Upsert Completed Successfully")