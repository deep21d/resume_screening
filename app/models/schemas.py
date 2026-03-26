from pydantic import BaseModel, Field
from typing import List


class EvaluationResult(BaseModel):
    score: int = Field(..., ge=0, le=100, description="Match score between 0 and 100")

    summary: str = Field(..., description="Short summary of candidate profile")

    strengths: List[str] = Field(
        default_factory=list,
        description="Key strengths of the candidate relevant to the job"
    )

    gaps: List[str] = Field(
        default_factory=list,
        description="Missing skills or experience gaps"
    )

    risks: List[str] = Field(
        default_factory=list,
        description="Potential concerns or red flags"
    )

    explanation: str = Field(
        ...,
        description="Detailed explanation of scoring"
    )