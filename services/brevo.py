import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

url = "https://api.brevo.com/v3/smtp/email"

headers = {
    "accept": "application/json",
    "api-key": BREVO_API_KEY,
    "content-type": "application/json"
}

payload = {
    "sender": {
        "name": "Sayali",
        "email": "sayalisali192004@gmail.com"
    },
    "to": [
        {
            "email": "work.sayali1908@gmail.com"
        }
    ],
    "subject": "Brevo Test Email",
    "htmlContent": """
    <html>
      <body>
        <h2>Hello!</h2>
        <p>This email was sent using Brevo API.</p>
      </body>
    </html>
    """
}

response = requests.post(
    url,
    json=payload,
    headers=headers
)

print(response.status_code)
print(response.text)