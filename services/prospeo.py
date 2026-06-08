import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

if not API_KEY:
    raise ValueError("PROSPEO_API_KEY not found in .env file")

HEADERS = {
    "X-KEY": API_KEY,
    "Content-Type": "application/json"
}

# =========================
# STEP 1: SEARCH PERSON
# =========================

search_url = "https://api.prospeo.io/search-person"

search_payload = {
    "page": 1,
    "filters": {
        "company": {
            "names": {
                "include": ["Microsoft"]
            }
        }
    }
}

search_response = requests.post(
    search_url,
    json=search_payload,
    headers=HEADERS
)

search_data = search_response.json()

print("\n===== SEARCH RESPONSE =====")
print("Status:", search_response.status_code)
print("Error:", search_data.get("error"))

if search_data.get("error"):
    print(search_data)
    exit()

results = search_data.get("results", [])

if not results:
    print("No people found.")
    exit()

first_person = results[0]

print("\n===== FIRST PERSON =====")
print("Name:", first_person["person"]["full_name"])
print("Title:", first_person["person"]["current_job_title"])

person_id = first_person["person"]["person_id"]

print("Person ID:", person_id)

# =========================
# STEP 2: ENRICH PERSON
# =========================

enrich_url = "https://api.prospeo.io/enrich-person"

enrich_payload = {
    "only_verified_email": True,
    "data": {
        "person_id": person_id
    }
}

enrich_response = requests.post(
    enrich_url,
    json=enrich_payload,
    headers=HEADERS
)

enrich_data = enrich_response.json()

print("\n===== ENRICH RESPONSE =====")
print("Status:", enrich_response.status_code)

if enrich_data.get("error"):
    print("Enrichment failed:")
    print(enrich_data)
    exit()

person = enrich_data.get("person", {})
email_data = person.get("email", {})

print("\n===== EMAIL DETAILS =====")
print("Status:", email_data.get("status"))
print("Revealed:", email_data.get("revealed"))
print("Email:", email_data.get("email"))

print("\n===== SUCCESS =====")
print("Lead Name:", person.get("full_name"))
print("Lead Email:", email_data.get("email"))