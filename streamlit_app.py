import streamlit as st
from playwright.sync_api import sync_playwright
from agent.scraper import scrape_tesla_jobs
import pandas as pd

st.set_page_config(page_title="Agentic Tesla Intern Finder", layout="wide")
st.title("🚀 Tesla Internship Agent")
st.markdown("Search Tesla Careers and scrape internships using AI agent.")

query = st.text_input("🔍 Search Keywords", "AI internship")
location = st.selectbox("📍 Location Filter", ["United States", "India", "Germany", "Any"])
category = st.selectbox("📂 Category Filter", ["Internship", "Full-time", "Any"])
search = st.button("Run Agent")

if search:
    st.info("Launching Tesla scraper agent...")
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.tesla.com/careers/search/", timeout=60000)

        jobs = scrape_tesla_jobs(page, query=query, location_filter=location, category_filter=category)
        browser.close()

    if jobs:
        df = pd.DataFrame(jobs)
        st.success(f"✅ Found {len(df)} jobs")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Results as CSV", csv, "tesla_jobs.csv", "text/csv")
    else:
        st.warning("No jobs found for that query.")
