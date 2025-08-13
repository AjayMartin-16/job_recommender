import google.generativeai as genai
import os
import asyncio
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

genai.configure(api_key=GEMINI_API_KEY)

@lru_cache(maxsize=100)
def cached_score(job_desc, skills, experience):
    """Cache identical scoring requests."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    You are a job matching AI. 
    Skills: {skills}
    Experience: {experience} years
    Job Description: {job_desc}
    Return a match score from 0 to 100.
    """
    response = model.generate_content(prompt)
    try:
        return float(response.text.strip())
    except:
        return 0.0

async def async_score(job, skills, experience):
    score = cached_score(job["description"], skills, experience)
    job["score"] = score
    return job

def score_jobs(jobs, skills, experience):
    """Score jobs asynchronously using Gemini."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    scored_jobs = loop.run_until_complete(asyncio.gather(
        *(async_score(job, skills, experience) for job in jobs)
    ))
    return sorted(scored_jobs, key=lambda x: x["score"], reverse=True)
