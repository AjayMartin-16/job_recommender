import streamlit as st
from job_search import search_jobs
from ai import score_jobs
from utils import parse_resume
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Job Recommender", layout="wide")
st.title("🔍 AI-Powered Job Recommender (Gemini + SerpAPI)")

# File uploader or manual entry
uploaded_resume = st.file_uploader("Upload your resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
skills = st.text_input("Enter skills (comma-separated)")
experience = st.number_input("Years of experience", min_value=0, max_value=50, value=1)
location = st.text_input("Preferred location (optional)")

if st.button("Find Jobs"):
    with st.spinner("Parsing profile..."):
        if uploaded_resume:
            parsed_data = parse_resume(uploaded_resume)
            user_skills = parsed_data.get("skills", skills)
            user_experience = parsed_data.get("experience", experience)
        else:
            user_skills = skills
            user_experience = experience

    if not user_skills:
        st.error("Please provide skills or upload a resume.")
    else:
        with st.spinner("Searching jobs..."):
            jobs = search_jobs(user_skills, location)

        if not jobs:
            st.warning("No jobs found. Try different skills or location.")
        else:
            with st.spinner("Scoring and recommending jobs..."):
                ranked_jobs = score_jobs(jobs, user_skills, user_experience)

            st.subheader("🏆 Top Job Recommendations")
            for job in ranked_jobs:
                st.markdown(f"### [{job['title']}]({job['link']})")
                st.write(f"**Company:** {job['company']}")
                st.write(f"**Location:** {job['location']}")
                st.write(f"**Score:** {job['score']:.2f}")
                st.write("---")
