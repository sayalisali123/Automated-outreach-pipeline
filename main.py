import csv

from services.ai_writer import generate_email
from services.logger import log_email
from services.brevo_mailer import send_email

# ==========================
# CONFIG
# ==========================

CSV_FILE = "data/leads.csv"

TEST_EMAIL = "work.sayali1908@gmail.com"

MAX_LEADS = 1

# ==========================
# LOAD LEADS
# ==========================

def load_leads():

    leads = []

    with open(
        CSV_FILE,
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            leads.append(row)

    return leads


# ==========================
# PIPELINE
# ==========================

def run_pipeline():

    print("\n🚀 Automated Outreach Pipeline\n")

    leads = load_leads()

    print(f"Loaded {len(leads)} leads from CSV")

    selected_leads = leads[:MAX_LEADS]

    print(f"Processing first {len(selected_leads)} leads\n")

    generated_emails = []

    for lead in selected_leads:

        name = lead["name"]
        title = lead["title"]
        company = lead["company"]

        email_body = generate_email(
            name,
            title,
            company
        )

        generated_emails.append({
            "name": name,
            "email": lead["email"],
            "company": company,
            "body": email_body
        })

        print(f"✅ Generated email for {name}")

    print("\n==============================")
    print("SAFETY CHECK")
    print("==============================")

    print(
        f"\nReady to send "
        f"{len(generated_emails)} email(s)"
        f"\nDestination: {TEST_EMAIL}"
    )

    confirmation = input(
        "\nContinue? (y/n): "
    ).strip().lower()

    if confirmation != "y":

        print("\n❌ Operation cancelled")
        return

    print("\nSending...\n")

    for email_data in generated_emails:

        success = send_email(
            TEST_EMAIL,
            f"Outreach for {email_data['name']}",
            email_data["body"]
        )

        if success:

            print(
                f"✅ Email sent for "
                f"{email_data['name']}"
            )

            log_email(
                email_data["name"],
                TEST_EMAIL,
                email_data["company"],
                "SENT"
            )

        else:

            print(
                f"❌ Email failed for "
                f"{email_data['name']}"
            )

            log_email(
                email_data["name"],
                TEST_EMAIL,
                email_data["company"],
                "FAILED"
            )

    print("\n✅ Pipeline Completed Successfully\n")


if __name__ == "__main__":
    run_pipeline()