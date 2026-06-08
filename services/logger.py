import csv
import os
from datetime import datetime

LOG_FILE = "email_log.csv"


def log_email(name, email, company, status):

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "name",
                "email",
                "company",
                "status"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name,
            email,
            company,
            status
        ])