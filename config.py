from dotenv import load_dotenv
import os

load_dotenv()

stripe_key = os.getenv("STRIPE_API_KEY")
salesforce_key = os.getenv("SALESFORCE_API_KEY")

print("Stripe Key:", stripe_key)
print("Salesforce Key:", salesforce_key)
