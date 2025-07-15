def summarize_email(email_text, model="Groq"):
    return f"Summary from {model}: {email_text[:100]}"
