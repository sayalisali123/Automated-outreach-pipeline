# Automated Outreach Pipeline

An end-to-end cold outreach automation system built using Python, Prospeo, and Brevo.

The pipeline automates lead discovery, enrichment, personalized email generation, delivery, and activity logging with minimal human intervention.

---

## Features

### Lead Discovery
- Search and retrieve professional contacts
- Company-based lead sourcing
- CSV lead storage

### Contact Enrichment
- Retrieve verified work emails
- Capture job titles and company information
- Store LinkedIn profile references

### Personalized Outreach
- Generate personalized outreach emails
- Dynamic content based on lead information
- HTML email support

### Email Delivery
- Integration with Brevo Email API
- Real email delivery support
- Safety confirmation before sending

### Logging
- Email activity logging
- Timestamped records
- CSV export

---

## Tech Stack

- Python
- Requests
- Python Dotenv
- Prospeo API
- Brevo API
- CSV Processing

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
├── main.py
├── requirements.txt
└── README.md
```

---

## Pipeline Flow

```text
Seed Company
      ↓
Lead Discovery
      ↓
Lead Enrichment
      ↓
Email Generation
      ↓
Safety Check
      ↓
Email Delivery
      ↓
Activity Logging
```

---

## Safety Features

Before any email is sent:

- User confirmation required
- Test email mode supported
- Activity logging enabled
- Controlled lead processing limits

---

## Sample Output

```text
🚀 Automated Outreach Pipeline

Loaded 25 leads from CSV
Processing first 3 leads

✅ Generated email for Maya Subhadra
✅ Generated email for Tyler Groth
✅ Generated email for Ari Hevosmaa

==============================
SAFETY CHECK
==============================

Ready to send 3 emails

Sending...

✅ Email sent for Maya Subhadra
✅ Email sent for Tyler Groth
✅ Email sent for Ari Hevosmaa

✅ Pipeline Completed Successfully
```

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
PROSPEO_API_KEY=your_key
BREVO_API_KEY=your_key
EAZYREACH_CLIENT_ID=your_id
EAZYREACH_CLIENT_SECRET=your_secret
```

Run:

```bash
python main.py
```

---

## Future Improvements

- OpenAI-powered email personalization
- Ocean.io company discovery integration
- Dashboard for campaign analytics
- Email open and click tracking
- Retry and failure recovery mechanisms

---

## Author

Sayali Sali

Built as part of a Software Engineering Outreach Automation Assignment.