from fastapi import FastAPI, UploadFile, File, Form
from services.ai_services import GeminiService
from services.pdf_parser import extract_text_from_uploadfile
from models.response_models import AnalysisResponse
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Resume Analyzer API",
    description="An API for uploading and analyzing resumes using AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Resume Analyzer API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """Accept an uploaded PDF resume, extract text, and return combined text."""
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
    
    resume_text = await extract_text_from_uploadfile(resume)

    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="The uploaded PDF appears to be empty or contains no extractable text.")

    ai_service = GeminiService()

    try:
        analysis = ai_service.analyze_resume(resume_text, job_description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI analysis failed!: {str(e)}")

    return analysis
    #{
#       "resume_filename": resume.filename,
#      "analysis": analysis,
        #"content_type": resume.content_type,
        #"job_description": job_description,
        #"resume_text": resume_text,
    #}