
from pydantic import BaseModel, Field


class Hypothesis(BaseModel):
    cause: str = Field(
        description="A possible explanation for the incident"
    )
    reasoning: str = Field(
        description="Why this cause is worth investigating"
    )
    diagnostic_check: str = Field(
        description="A diagnostic check that could test this hypothesis"
    )


class InvestigationPlan(BaseModel):
    incident_summary: str
    hypotheses: list[Hypothesis] = Field(
        min_length=1,
        max_length=5,
    )
