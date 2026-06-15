import pandas as pd

customers = pd.read_csv("data/customers.csv")
payments = pd.read_csv("data/payments.csv")

merged_data = pd.merge(
    customers,
    payments,
    on="customer_id"
)

print("Merged Data")
print(merged_data)

merged_data.to_csv(
    "final_data.csv",
    index=False
)