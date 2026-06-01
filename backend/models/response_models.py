from pydantic import BaseModel
from typing import List

class AnalysisResponse(BaseModel):
    overall_score: int
    ats_score: int
    strengths: List[str]
    weaknesses: List[str]
    missing_skills: List[str]
    missing_technologies: List[str]
    improvements: List[str]
    project_suggestions: List[str]
    job_match_summary: str