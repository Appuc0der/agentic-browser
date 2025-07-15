def scrape_tesla_jobs(page, query="AI internship", location_filter="United States", category_filter="Internship"):
    print(f"🔍 Searching Tesla Careers for: {query}")

    jobs = []

    try:
        # 1. Search by keyword
        page.wait_for_selector("input[placeholder='Search jobs']", timeout=10000)
        page.fill("input[placeholder='Search jobs']", query)
        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)

        # 2. Filter: Category → Internship
        try:
            page.click(f"text={category_filter}")
            page.wait_for_timeout(2000)
        except:
            print(f"⚠️ Could not click category '{category_filter}'")

        # 3. Filter: Location → United States
        try:
            page.click(f"text={location_filter}")
            page.wait_for_timeout(2000)
        except:
            print(f"⚠️ Could not click location '{location_filter}'")

        # 4. Scrape job results
        job_cards = page.locator(".tds-accordion-item")
        count = job_cards.count()
        print(f"📄 Found {count} listings.")
        
        for i in range(min(count, 15)):
            job = job_cards.nth(i)
            title = job.locator("h4").inner_text()
            location = job.locator(".location").inner_text()
            team = job.locator("div.tds-list--unordered div").nth(0).inner_text()
            job_id = job.get_attribute("data-job-id")
            apply_link = f"https://www.tesla.com/careers/search/job/{job_id}" if job_id else "N/A"

            jobs.append({
                "Title": title,
                "Location": location,
                "Team": team,
                "Apply Link": apply_link
            })

    except Exception as e:
        print(f"❌ Error scraping Tesla: {e}")

    return jobs
