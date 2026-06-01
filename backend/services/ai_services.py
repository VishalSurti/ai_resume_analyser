import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class AIService:
    def analyze_resume(self, resume_text: str, job_description: str) -> dict:
        raise NotImplementedError


class GeminiService(AIService):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def analyze_resume(self, resume_text: str, job_description: str) -> dict:
        prompt = f"""
You are an expert technical recruiter and resume reviewer.

Analyze the resume against the job description.

Return ONLY valid JSON with this exact structure:
{{
  "overall_score": 0,
  "ats_score": 0,
  "strengths": [],
  "weaknesses": [],
  "missing_skills": [],
  "missing_technologies": [],
  "improvements": [],
  "project_suggestions": [],
  "job_match_summary": ""
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned_response = response.text.strip()

        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response.replace("```json", "").replace("```", "").strip()

        return json.loads(cleaned_response)