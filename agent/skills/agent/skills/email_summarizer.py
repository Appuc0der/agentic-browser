# agent/skills/email_summarizer.py

def summarize_email(email_text, model="Groq"):
    return f"Summary of your email using {model}: {email_text[:75]}..."
