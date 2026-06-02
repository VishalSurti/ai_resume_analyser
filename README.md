# ai_resume_analyser

AI Resume Analyzer is a web application that analyzes a candidate's resume against a job description using Google's Gemini AI.

The application extracts text from uploaded PDF resumes, compares the content with a target job description, and generates structured feedback including ATS score, strengths, weaknesses, missing skills, missing technologies, improvement suggestions, and project recommendations.

## Features

- Upload PDF resumes
- Extract resume text using PDF parsing
- Analyze resumes using Gemini AI
- ATS score calculation
- Resume strengths and weaknesses analysis
- Missing skills identification
- Missing technology recommendations
- Personalized project suggestions
- Responsive frontend interface
- Error handling and validation

## Tech Stack

### Backend
- FastAPI
- Python
- Pydantic
- PyPDF
- Gemini API

### Frontend
- HTML
- CSS
- JavaScript

### Tools
- Git
- GitHub
- VS Code

## Project Structure
```text
ai_resume_analyzer/
│
├── backend/
│   ├── main.py
│   ├── services/
│   │   ├── ai_service.py
│   │   └── pdf_parser.py
│   ├── models/
│   │   └── response_models.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```


## Installation

### Clone Repository

```bash
git clone <your-github-url>
cd ai_resume_analyzer
```

### Create virtual Enviornment
```bash
python -m venv venv
source venv/bin/activate (For MacOS)
venv\Scripts\activate (For Windows)

pip install -r requirements.txt
```

## Environment Variables

Create a '.env' file inside the backend directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

Start FastAPI:
```bash
uvicorn backend.main:app --reload
```

Open frontend/index.html


## API Endpoint

POST /analyze

Inputs:
- PDF Resume
- Job Description

Output:
- Overall Score
- ATS Score
- Strengths
- Weaknesses
- Missing Skills
- Missing Technologies
- Improvement Suggestions
- Project Suggestions
- Job Match Summary

## Future Improvements

- React frontend
- Resume keyword highlighting
- Resume comparison feature
- DOCX support
- User authentication
- Download analysis as PDF
- Cloud deployment