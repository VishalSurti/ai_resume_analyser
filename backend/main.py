from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI(
    title="AI Resume Analyzer API",
    description="An API for uploading and analyzing resumes using AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Resume Analyzer API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze_resume")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    return {
        "resume_filename": resume.filename,
        "content_type": resume.content_type,
        "job_description": job_description
    }