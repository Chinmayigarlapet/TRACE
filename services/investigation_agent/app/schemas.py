
from pydantic import BaseModel, Field
from typing import Any
from typing import Literal

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

class DiagnosticEvidence(BaseModel):
    device_id: str
    check_name: str
    result: dict[str, Any]
    source: str = "mock_simulator"


class HypothesisEvaluation(BaseModel):
    cause: str
    status: Literal[
        "supported",
        "contradicted",
        "inconclusive"
    ]
    explanation: str


class EvidenceEvaluation(BaseModel):
    evaluations: list[HypothesisEvaluation]
    investigation_summary: str
    additional_checks_required: bool    