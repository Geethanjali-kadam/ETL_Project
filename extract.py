import pandas as pd

customers = pd.read_csv("data/customers.csv")
payments = pd.read_csv("data/payments.csv")

print("Customers Data")
print(customers)

print("\nPayments Data")
print(payments)