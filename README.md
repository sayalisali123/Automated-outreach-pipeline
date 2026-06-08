# Automated Outreach Pipeline

An end-to-end outreach automation system built using Python and Brevo.

The pipeline accepts a company domain as input, discovers matching leads, generates personalized outreach emails, provides a safety approval step, delivers emails through Brevo, and logs all outreach activity automatically.

---

## Features

### Company Domain Input

* User enters a target company domain
* Domain is mapped to matching company leads
* Supports organization-specific outreach workflows

### Lead Discovery

* Retrieves leads from a structured lead dataset
* Company-based filtering
* CSV-powered lead management

### AI Email Generation

* Generates personalized outreach emails
* Uses lead information such as name, title, and company
* Produces HTML-ready email content

### Safety Approval Workflow

* Human confirmation required before sending
* Prevents accidental outreach
* Allows review of generated campaigns

### Email Delivery

* Integration with Brevo Email API
* Automated email dispatch
* Delivery status monitoring

### Activity Logging

* Timestamped outreach records
* Success and failure tracking
* CSV-based audit trail

---

## Tech Stack

* Python
* Requests
* Python Dotenv
* Brevo API
* CSV Processing

---

## Project Structure

```text
automated-outreach-pipeline/

├── data/
│   └── leads.csv

├── services/
│   ├── ai_writer.py
│   ├── brevo.py
│   ├── brevo_mailer.py
│   ├── logger.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   └── ocean.py

├── .env
├── .gitignore
├── email_log.csv
├── main.py
├── requirements.txt
└── README.md
```

---

## Pipeline Flow

```text
User Input (Company Domain)
            ↓
Lead Discovery
            ↓
AI Email Generation
            ↓
Safety Approval
            ↓
Email Delivery (Brevo)
            ↓
Activity Logging
```

---

## Example Workflow

```text
Enter company domain:
microsoft.com

🔍 Lead Discovery Complete: 25 leads found

Processing first 3 leads

✅ Generated email for Maya Subhadra
✅ Generated email for Tyler Groth
✅ Generated email for Ari Hevosmaa

==============================
SAFETY CHECK
==============================

Ready to send 3 email(s)

Destination: work.sayali1908@gmail.com

Continue? (y/n): y

Sending...

Brevo Status: 201
✅ Email sent for Maya Subhadra
✅ Email sent for Tyler Groth
✅ Email sent for Ari Hevosmaa

✅ Pipeline Completed Successfully
```

---

## Safety Features

Before any email is delivered:

* Manual user confirmation required
* Controlled lead processing limit
* Delivery status verification
* Automated activity logging

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sayalisali123/Automated-outreach-pipeline.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BREVO_API_KEY=your_key
PROSPEO_API_KEY=your_key
EAZYREACH_CLIENT_ID=your_id
EAZYREACH_CLIENT_SECRET=your_secret
```

Run the application:

```bash
python main.py
```

---

## Current Prototype Scope

The current implementation demonstrates:

* Company-domain-based workflow initiation
* Lead discovery from a curated dataset
* AI-powered personalized outreach generation
* Approval-based email delivery
* Brevo integration
* Automated logging and tracking

For demonstration purposes, the included dataset contains Microsoft leads.

---

## Future Enhancements

* Real-time lead discovery using Prospeo
* Ocean.io company intelligence integration
* EazyReach enrichment workflows
* Campaign analytics dashboard
* Email open and click tracking
* Retry and recovery mechanisms
* Domain-authenticated sender infrastructure

---

## Author

Sayali Sali

Built as part of a Software Engineering Outreach Automation Assignment.
