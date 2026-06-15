from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///database.db")

query = "SELECT * FROM customers"

data = pd.read_sql(query, engine)

print(data)