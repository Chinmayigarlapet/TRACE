import json

from abc import ABC, abstractmethod

from ollama import Client
from openai import OpenAI

from .config import settings
from .schemas import (
    InvestigationPlan,
    EvidenceEvaluation,
    DiagnosticEvidence,
)


SYSTEM_PROMPT = """
You are TRACE, an enterprise incident investigation assistant.

Generate up to five plausible root-cause hypotheses.
For each hypothesis, explain why it is plausible and
suggest a diagnostic check.

Do not claim any hypothesis is confirmed.
Do not invent diagnostic results.
Only use information supplied in the incident.
"""
EVIDENCE_EVALUATION_PROMPT = """
You are TRACE, an evidence-driven enterprise incident
investigation assistant.

Evaluate each hypothesis using ONLY the supplied evidence.

STRICT RULES:

1. Do not mark a hypothesis as supported simply because
   it could explain the symptoms.

2. A connectivity timeout confirms communication failure,
   but does not establish the underlying root cause.

3. Mark a hypothesis as supported only when evidence
   specifically favors it over competing explanations.

4. Mark a hypothesis as contradicted only when evidence
   directly conflicts with it.

5. Otherwise, mark the hypothesis as inconclusive.

6. Never invent diagnostic results or device states.

7. Evaluate every hypothesis in the investigation plan.

8. If the root cause is uncertain, set
   additional_checks_required to true.
"""

class LLMProvider(ABC):
    @abstractmethod
    def generate_plan(
        self,
        incident: str,
    ) -> InvestigationPlan:
        pass

    @abstractmethod
    def evaluate_evidence(
        self,
        plan: InvestigationPlan,
        evidence: list[DiagnosticEvidence],
    ) -> EvidenceEvaluation:
        pass

class OllamaProvider(LLMProvider):
    def __init__(self):
        self.client = Client(
            host=settings.ollama_base_url,
            timeout=180,
        )

    def generate_plan(
        self,
        incident: str,
    ) -> InvestigationPlan:

        response = self.client.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": incident,
                },
            ],
            format=InvestigationPlan.model_json_schema(),
            options={"temperature": 0},
            think=False,
        )

        content = response.message.content

        if not content:
            raise RuntimeError(
                "Ollama returned an empty response."
            )

        return InvestigationPlan.model_validate_json(content)

    def evaluate_evidence(
        self,
        plan: InvestigationPlan,
        evidence: list[DiagnosticEvidence],
    ) -> EvidenceEvaluation:

        payload = {
            "investigation_plan": plan.model_dump(),
            "collected_evidence": [
                item.model_dump()
                for item in evidence
            ],
        }

        response = self.client.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "system",
                    "content": EVIDENCE_EVALUATION_PROMPT,
                },
                {
                    "role": "user",
                    "content": json.dumps(payload),
                },
            ],
            format=EvidenceEvaluation.model_json_schema(),
            options={"temperature": 0},
            think=False,
        )

        content = response.message.content

        if not content:
            raise RuntimeError(
                "Ollama returned an empty evaluation."
            )

        return EvidenceEvaluation.model_validate_json(
            content
        )

class OpenAIProvider(LLMProvider):
    def __init__(self):
        if not settings.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is required for OpenAI."
            )

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

    def generate_plan(
        self,
        incident: str,
    ) -> InvestigationPlan:

        response = self.client.responses.parse(
            model=settings.trace_llm_model,
            instructions=SYSTEM_PROMPT,
            input=incident,
            text_format=InvestigationPlan,
        )

        if response.output_parsed is None:
            raise RuntimeError(
                "OpenAI returned no investigation plan."
            )

        return response.output_parsed

    def evaluate_evidence(
        self,
        plan: InvestigationPlan,
        evidence: list[DiagnosticEvidence],
    ) -> EvidenceEvaluation:

        payload = {
            "investigation_plan": plan.model_dump(),
            "collected_evidence": [
                item.model_dump()
                for item in evidence
            ],
        }

        response = self.client.responses.parse(
            model=settings.trace_llm_model,
            instructions=(
                "Evaluate each hypothesis using only the "
                "provided diagnostic evidence. "
                "Classify hypotheses as supported, "
                "contradicted, or inconclusive. "
                "A connectivity timeout alone does not "
                "establish a root cause. "
                "Do not invent diagnostic results."
            ),
            input=json.dumps(payload),
            text_format=EvidenceEvaluation,
        )

        if response.output_parsed is None:
            raise RuntimeError(
                "OpenAI returned no evidence evaluation."
            )

        return response.output_parsed

def create_llm_provider() -> LLMProvider:
    if settings.trace_llm_provider == "ollama":
        return OllamaProvider()

    if settings.trace_llm_provider == "openai":
        return OpenAIProvider()

    raise ValueError("Unsupported LLM provider.")
