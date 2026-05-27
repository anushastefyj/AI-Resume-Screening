import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Scanner", layout="wide")

st.title("📄 AI Resume Scanner for Campus Placements")
st.markdown("**Upload a resume and job description to get match score + missing skills**")

st.sidebar.header("📤 Upload")
resume = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.sidebar.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Job Title: Python Developer\nRequired Skills: Python, AWS, Docker, Django..."
)

API_URL = "http://localhost:8000"

if st.sidebar.button("Analyze Resume"):
    if not resume:
        st.sidebar.error("Please upload a resume PDF")
    elif not job_desc:
        st.sidebar.error("Please paste a job description")
    else:
        with st.spinner("Analyzing resume..."):
            try:
                files = {"file": (resume.name, resume.getvalue(), "application/pdf")}
                data = {"job_description": job_desc}
                response = requests.post(f"{API_URL}/match-resume", files=files, data=data, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    score = result["match_score"]
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Match Score", f"{score}%")
                        st.progress(score / 100)
                    
                    with col2:
                        if score >= 75:
                            st.success("✅ Strong Candidate")
                        elif score >= 50:
                            st.warning("⚠️ Moderate Fit")
                        else:
                            st.error("❌ Weak Match")
                    
                    st.subheader("✅ Skills Found in Resume")
                    skills = result["resume_skills"]
                    cols = st.columns(3)
                    for i, skill in enumerate(skills):
                        cols[i % 3].text(f"• {skill}")
                    
                    if result["missing_skills"]:
                        st.subheader("⚠️ Missing Skills")
                        cols = st.columns(3)
                        for i, skill in enumerate(result["missing_skills"][:9]):
                            cols[i % 3].text(f"• {skill}")
                    
                    st.subheader("💡 Recommendation")
                    st.info(f"**{result['recommendation']}** - Match score: {score}%")
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
else:
    st.info("👈 Upload resume and paste job description, then click Analyze")

st.markdown("---")
st.markdown("Made with ❤️ for Campus Placements | B.Tech Final Year Project")