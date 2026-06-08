import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("EAZYREACH_CLIENT_ID")
client_secret = os.getenv("EAZYREACH_CLIENT_SECRET")

# Step 1: Get Auth Token
auth_url = "https://api.superflow.run/b2b/createAuthToken/"

auth_payload = {
    "clientId": client_id,
    "clientSecret": client_secret
}

auth_response = requests.post(auth_url, json=auth_payload)

token_data = auth_response.json()

auth_token = token_data.get("auth_token")

print("Auth Success:", auth_response.status_code == 200)

# Step 2: Get Wallet Balance
balance_url = "https://api.superflow.run/b2b/getGreenBalance"

headers = {
    "Authorization": f"Bearer {auth_token}"
}

balance_response = requests.get(balance_url, headers=headers)

print("\nWallet Balance Response:")
print(balance_response.status_code)
print(balance_response.text)