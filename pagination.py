import requests
import pandas as pd

all_data = []

for page in range(1, 4):

    url = f"https://jsonplaceholder.typicode.com/posts?_page={page}&_limit=10"

    response = requests.get(url)

    data = response.json()

    all_data.extend(data)

    print(f"Page {page} Downloaded")

df = pd.DataFrame(all_data)

print(df)

df.to_csv(
    "pagination_data.csv",
    index=False
)

print("Pagination Data Saved Successfully")