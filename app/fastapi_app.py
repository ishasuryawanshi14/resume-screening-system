from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

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

app = FastAPI()


@app.post("/score_resume")
async def score_resume(

    resume: UploadFile = File(...),

    job_description: str = Form(...)

):

    

    temp_file_path = "temp_resume.pdf"

    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    

    resume_text = extract_text_from_pdf(
        temp_file_path
    )

    resume_text = clean_text(resume_text)

    resume_text = remove_stopwords(resume_text)

    

    job_text = clean_text(job_description)

    job_text = remove_stopwords(job_text)

    

    match_score = calculate_similarity(
        resume_text,
        job_text
    )

   

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_text
    )

    missing_skills = get_missing_skills(
        resume_skills,
        job_skills
    )

    

    return {

        "match_score": match_score,

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "missing_skills": missing_skills
    }