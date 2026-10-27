from typing import TypedDict

from .schemas import (
    InvestigationPlan,
    DiagnosticEvidence,
    EvidenceEvaluation,
)


class InvestigationState(TypedDict):
    incident_description: str
    device_id: str
    investigation_plan: InvestigationPlan | None
    evidence: list[DiagnosticEvidence]
    evaluation: EvidenceEvaluation | None