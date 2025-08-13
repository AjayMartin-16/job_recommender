# AI Job Recommender

This is a small project I built to recommend jobs based on a resume or skills you give it.  
You can either upload your resume (PDF) or type in your skills, years of experience, and optionally a location.  
It will search jobs from LinkedIn (via SerpAPI) and then use Google's Gemini AI to score the jobs based on your profile.

---

## What it does
- Lets you upload a resume OR enter details manually
- Pulls job listings from LinkedIn using SerpAPI
- Uses Gemini to figure out which jobs match your profile best
- Shows you the top jobs in a simple Streamlit UI
- Runs scoring in parallel (async) so it’s faster when there are many jobs
- Avoids rescoring the same job twice (caching)

---

## Tech I used
- **Python** for the main logic
- **Streamlit** for the interface
- **LangChain** to parse resumes
- **Google Generative AI (Gemini)** for job scoring
- **SerpAPI** for job scraping from LinkedIn
- **asyncio** for concurrent scoring
- **joblib** for caching

---

## How to run it

1. Clone the repo
```bash
git clone https://github.com/yourusername/AI_JOB_RECOMMENDER.git
cd AI_JOB_RECOMMENDER
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv myenv
myenv\Scripts\activate  # On Windows
source myenv/bin/activate  # On Mac/Linux
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create a .env.local file in the project folder with your API keys:

ini
Copy
Edit
SERPAPI_KEY=your_serpapi_key
GOOGLE_API_KEY=your_google_api_key
Run the app

bash
Copy
Edit
streamlit run app.py
File structure
bash
Copy
Edit
app.py              # Main Streamlit app
ai.py               # Gemini scoring logic (async + cache)
job_search.py       # LinkedIn job fetching
resume_parser.py    # Resume parsing with LangChain
requirements.txt    # Dependencies
.env.local          # Your API keys
README.md           # This file
Notes / Gotchas
SerpAPI needs a valid API key and you may need a paid plan for many searches

Gemini models keep changing names — I used gemini-1.5-pro, but check your account for the latest available models

If you see “404 model not found” errors, just swap the model name in ai.py

The async batching makes a big difference when there are lots of jobs to score
