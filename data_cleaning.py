import pandas as pd

data = pd.read_csv("final_data.csv")

print("Before Cleaning")
print(data)

data["name"] = data["name"].fillna("Unknown")

print("\nAfter Cleaning")
print(data)

data.to_csv(
    "cleaned_data.csv",
    index=False
)

print("\nCleaned data saved successfully")