from playwright.sync_api import sync_playwright
from agent.scraper import scrape_tesla_jobs

def execute_action(action):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context()

        print("🧭 Opening job search portals...")

        # --- 1. Tesla ---
        tesla_page = context.new_page()
        tesla_page.goto("https://www.tesla.com/careers/search/", timeout=60000)
        print("✅ Tesla page opened.")
        jobs = scrape_tesla_jobs(tesla_page)
        print("\n📢 Top Tesla AI Internships:")
        for job in jobs:
            print("•", job)

        # --- 2. Other tabs (optional) ---
        other_sites = {
            "Indeed": "https://www.indeed.com",
            "LinkedIn": "https://www.linkedin.com/jobs",
            "Glassdoor": "https://www.glassdoor.com/index.htm"
        }

        for name, url in other_sites.items():
            page = context.new_page()
            page.goto(url, timeout=60000)
            print(f"✅ {name} opened at {url}")

        input("\n🌐 All tabs opened. Press Enter to close browser.")
        browser.close()
        return "✅ Job tabs loaded and Tesla jobs scraped"
