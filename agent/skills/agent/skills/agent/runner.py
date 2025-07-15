# agent/runner.py

from agent.skills.email_summarizer import summarize_email
from agent.skills.meeting_notes import transcribe_meeting
from agent.skills.job_scraper import scrape_jobs
from agent.skills.resume_autofill import parse_resume

def run_agent(task, payload):
    if task == "summarizeEmail":
        return summarize_email(payload["email"], payload.get("model", "Groq"))

    elif task == "transcribeMeeting":
        return transcribe_meeting(payload)

    elif task == "autoApply":
        return scrape_jobs(payload["job"])

    elif task == "parseResume":
        return parse_resume(payload)

    return "❌ Unknown task"
