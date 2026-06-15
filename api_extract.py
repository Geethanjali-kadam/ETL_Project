import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "api_data.csv",
    index=False
)

print("API Data Saved Successfully")