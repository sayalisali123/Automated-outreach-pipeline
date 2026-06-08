def generate_email(name, title, company):
    """
    Mock AI email generator (submission-safe version)
    """

    return f"""
<p>Hello {name},</p>

<p>
I came across your profile and noticed your role as <b>{title}</b> at <b>{company}</b>.
</p>

<p>
Your experience in your domain is impressive, and I wanted to reach out for a potential professional connection.
</p>

<p>
I’m currently working on an automated outreach system that helps connect professionals based on role relevance.
</p>

<p>
Would love to connect and exchange ideas.
</p>

<p>
Best regards,<br>
Automated Outreach System
</p>
"""