
from .llm import (
    generate_investigation_plan,
    evaluate_investigation_evidence,
)
from .state import InvestigationState
from .tools.diagnostics import check_device_connectivity

def generate_hypotheses(
    state: InvestigationState,
) -> dict:
    incident = state["incident_description"]

    plan = generate_investigation_plan(incident)

    return {"investigation_plan": plan}

def run_connectivity_check(
    state: InvestigationState,
) -> dict:
    evidence = check_device_connectivity(
        state["device_id"]
    )

    return {"evidence": [evidence]}

def evaluate_evidence_node(
    state: InvestigationState,
) -> dict:

    plan = state["investigation_plan"]

    if plan is None:
        raise ValueError(
            "Cannot evaluate evidence without "
            "an investigation plan."
        )

    evaluation = evaluate_investigation_evidence(
        plan,
        state["evidence"],
    )

    return {"evaluation": evaluation}