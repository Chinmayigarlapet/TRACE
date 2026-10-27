from .providers import create_llm_provider

from .schemas import (
    InvestigationPlan,
    DiagnosticEvidence,
    EvidenceEvaluation,
)


# Function 1: Generate initial investigation hypotheses
def generate_investigation_plan(
    incident_description: str,
) -> InvestigationPlan:

    provider = create_llm_provider()

    return provider.generate_plan(
        incident_description
    )


# Function 2: Evaluate collected diagnostic evidence
def evaluate_investigation_evidence(
    plan: InvestigationPlan,
    evidence: list[DiagnosticEvidence],
) -> EvidenceEvaluation:

    provider = create_llm_provider()

    return provider.evaluate_evidence(
        plan,
        evidence,
    )