import pandas as pd

try:
    data = pd.read_csv("final_data.csv")
    print(data)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)