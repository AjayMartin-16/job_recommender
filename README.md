# AI Job Recommender

## Project Description
The **AI Job Recommender** is a smart job search assistant I built to make finding relevant opportunities faster and less frustrating.  
Instead of scrolling endlessly through LinkedIn, you can upload your resume or type your skills, and the app will:
- Fetch real job listings from LinkedIn
- Score them based on your profile using Google Gemini AI
- Show you the best matches first

It combines **resume parsing, job scraping, and AI-based scoring** into a single, easy-to-use Streamlit dashboard.

---

## Features
- **Resume Upload or Manual Input** – works for both PDF resumes and direct skill entry
- **LinkedIn Job Fetching** – powered by SerpAPI for live job data
- **AI Scoring** – Google Gemini evaluates job relevance based on your skills & experience
- **Async Processing** – scores multiple jobs in parallel for speed
- **Caching** – avoids rescoring duplicate job descriptions
- **Clean UI** – quick, interactive interface built with Streamlit

---

## How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-job-recommender.git
   cd ai-job-recommender
Create and activate a virtual environment

bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set environment variables in .env (create this file in the project root)

ini
Copy
Edit
SERPAPI_API_KEY=your_serpapi_key
GOOGLE_API_KEY=your_google_api_key
Run the app

bash
Copy
Edit
streamlit run app.py
Sample Input/Output
Sample Input (Manual entry)

makefile
Copy
Edit
Skills: Python, Data Analysis, SQL, Machine Learning
Experience: 3
Location: Remote
Sample Output (AI-ranked jobs)

Rank	Job Title	Company	Match Score
1	Data Analyst (Remote)	TechCorp Ltd	92%
2	Machine Learning Eng.	AI Solutions	88%
3	SQL Data Specialist	DataWorks	83%

Screenshots
<img width="1897" height="862" alt="image" src="https://github.com/user-attachments/assets/c7ccbe06-9159-45e4-9e41-705faa37db8a" />
<img width="1792" height="741" alt="image" src="https://github.com/user-attachments/assets/0344d8fa-d181-4999-bfe5-92e8545ae45d" />



AI Scored Results

#Tech Stack
Python

Streamlit – frontend UI

LangChain – resume parsing

SerpAPI – LinkedIn job scraping

Google Gemini – AI scoring

AsyncIO – parallel processing

Author
Built by B.Ajay MArtin Ferdinand as a portfolio project to combine AI with practical job searching.
