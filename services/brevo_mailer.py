import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def send_email(to_email, subject, html_content):

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
                "email": to_email
            }
        ],
        "subject": subject,
        "htmlContent": html_content
    }

    try:

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        print("Brevo Status:", response.status_code)

        if response.status_code == 201:
            return True

        print(response.text)
        return False

    except Exception as e:
        print("Brevo Error:", e)
        return False