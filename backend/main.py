from fastapi import FastAPI

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