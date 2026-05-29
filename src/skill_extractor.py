SKILLS = [

    # Programming Languages
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",

    # Frontend
    "html",
    "css",
    "react",
    "nextjs",
    "angular",
    "vue",
    "bootstrap",
    "tailwind css",

    # Backend
    "nodejs",
    "express",
    "django",
    "flask",
    "fastapi",
    "spring boot",
    "php",

    # Database
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "supabase",
    "firebase",

    # Cloud & DevOps
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "jenkins",
    "github actions",
    "linux",

    # Data Science
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "tableau",
    "power bi",
    "excel",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",

    # Tools
    "git",
    "github",
    "gitlab",
    "vercel",
    "postman",
    "jupyter",
    "vscode",

    # Web Technologies
    "rest api",
    "graphql",
    "json",
    "xml",

    # Mobile Development
    "android",
    "flutter",
    "react native",

    # Software Engineering
    "oop",
    "data structures",
    "algorithms",
    "system design",

    # Analytics
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