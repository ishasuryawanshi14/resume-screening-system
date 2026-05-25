SKILLS = [

    # Programming
    "python",
    "java",
    "javascript",
    "c",
    "c++",

    # Web
    "html",
    "css",
    "react",
    "nextjs",

    # Database
    "sql",
    "mysql",
    "mongodb",
    "supabase",

    # Data Analytics
    "excel",
    "power bi",
    "tableau",
    "pandas",
    "numpy",

    # Tools
    "git",
    "github",
    "vercel",
    "jupyter",

    # AI/ML
    "machine learning",
    "data analysis",
    "data visualization"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills

def get_missing_skills(resume_skills, job_skills):

    missing = []

    for skill in job_skills:

        if skill not in resume_skills:
            missing.append(skill)

    return missing