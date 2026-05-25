import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import matplotlib.pyplot as plt

from src.preprocessing import (
    extract_text_from_pdf,
    clean_text,
    remove_stopwords
)

from src.matcher import calculate_similarity

from src.skill_extractor import (
    extract_skills,
    get_missing_skills
)



st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)



st.markdown("""
<style>

.main {
    background-color: #FFF7F3;
}

section[data-testid="stSidebar"] {
    background-color: #FFE5EC;
}

h1 {
    color: #6D6875;
    font-size: 48px !important;
    font-weight: bold;
}

h2, h3 {
    color: #6D6875;
}

.stButton > button {
    background-color: #B8C0FF;
    color: black;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #A0C4FF;
    color: black;
}

.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #2B2D42 !important;
    border-radius: 12px;
    border: 2px solid #C7C7C7 !important;
    font-size: 16px !important;
}
            

textarea:focus {
    outline: none !important;
    box-shadow: none !important;
    border-color: #C7C7C7 !important;
}

textarea:focus-visible {
    outline: none !important;
    box-shadow: none !important;
    border-color: #C7C7C7 !important;
}

[data-baseweb="textarea"] {
    border: none !important;
    box-shadow: none !important;
}

.stFileUploader {
    background-color: #FFFFFF;
    padding: 10px;
    border-radius: 10px;
}

[data-testid="stMetricValue"] {
    color: #6D6875;
}

</style>
""", unsafe_allow_html=True)

 

with st.sidebar:

    st.title("About")

    st.info("""
This system analyzes resumes using:

✔ TF-IDF Similarity  
✔ Skill Extraction  
✔ NLP Preprocessing  
✔ Keyword Matching  
""")

    st.markdown("---")

    st.title("Built With")

    st.write("""
• Python  
• Streamlit  
• Scikit-learn  
• NLTK  
• Matplotlib  
""")



st.title("📄 RESUME SCREENING SYSTEM")

st.write("An intelligent platform for resume screening, skill analysis, and job matching.")



col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )



analyze_button = st.button("Analyze Resume")



if analyze_button and uploaded_file and job_description:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    
    resume_text = extract_text_from_pdf("temp_resume.pdf")
    resume_text = clean_text(resume_text)
    resume_text = remove_stopwords(resume_text)

    
    job_text = clean_text(job_description)
    job_text = remove_stopwords(job_text)

    
    match_score = calculate_similarity(
        resume_text,
        job_text
    )

    
    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_text)

    missing_skills = get_missing_skills(
        resume_skills,
        job_skills
    )

    matched_skills = len(
        set(resume_skills).intersection(set(job_skills))
    )

    skill_match_score = (
        matched_skills / len(job_skills)
    ) * 100 if job_skills else 0

    

    st.markdown("---")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.subheader("TF-IDF Score")
        st.success(f"{round(match_score, 2)}% Match")

    with result_col2:
        st.subheader("Skill Match Score")
        st.info(f"{round(skill_match_score, 2)}% Skill Match")

    
    skill_col1, skill_col2 = st.columns(2)

    with skill_col1:
        st.subheader("✅ Resume Skills")

        if resume_skills:
            for skill in resume_skills:
               st.markdown(f"• {skill}")

    with skill_col2:
        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.markdown(f"• {skill}")
        else:
            st.success("No Missing Skills")

    

    st.subheader("Skill Match Visualization")

    labels = [
        "Matched Skills",
        "Missing Skills"
    ]

    sizes = [
        matched_skills,
        len(missing_skills)
    ]

    fig, ax = plt.subplots(figsize=(7,7))

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 8},
        radius=1.1
    )

    chart_col1, chart_col2, chart_col3 = st.columns([1,3,1])

    with chart_col2:
       st.pyplot(
           fig,
           use_container_width=False
    )

    

    st.subheader("Final Recommendation")

    if match_score >= 75:

        st.success(
            "Excellent match! Candidate is highly suitable for this role."
        )

    elif match_score >= 50:

        st.warning(
            "Moderate match score. Candidate meets some requirements but can improve further."
        )

    else:

        st.error(
            "Low match score. Resume needs improvement for this role."
        )