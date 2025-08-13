import os
from serpapi.google_search import GoogleSearch

from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_jobs(skills, location=""):
    """Search jobs from Google Jobs via SerpAPI."""
    if not SERP_API_KEY:
        raise ValueError("Missing SERPAPI_API_KEY in .env file")

    query = f"{skills} jobs {location}".strip()
    search = GoogleSearch({
        "engine": "google_jobs",
        "q": query,
        "api_key": SERP_API_KEY
    })
    results = search.get_dict()

    jobs = []
    for job in results.get("jobs_results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "link": job.get("related_links", [{}])[0].get("link", "#"),
            "description": job.get("description", "")
        })
    return jobs
