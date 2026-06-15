import pandas as pd

data = pd.read_csv("final_data.csv")

missing_values = data.isnull().sum()

print(missing_values)

if missing_values.sum() == 0:
    print("Data Validation Passed")
else:
    print("Data Validation Failed")