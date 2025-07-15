from agent.skills.job_scraper import scrape_jobs
from agent.skills.email_summarizer import summarize_email
from agent.skills.meeting_notes import transcribe_audio
from agent.skills.resume_autofill import parse_resume_pdf

def run_agent(task, data):
    if task == "summarizeEmail":
        return summarize_email(data["email"], data.get("model", "Groq"))
    elif task == "transcribeMeeting":
        return transcribe_audio(data)
    elif task == "autoApply":
        return f"Auto-applying to jobs related to: {data['job']}"
    elif task == "parseResume":
        return parse_resume_pdf(data)
    else:
        return "Unknown task."
