
from .providers import create_llm_provider
from .schemas import InvestigationPlan


def generate_investigation_plan(
    incident_description: str,
) -> InvestigationPlan:

    provider = create_llm_provider()

    return provider.generate_plan(
        incident_description
    )
