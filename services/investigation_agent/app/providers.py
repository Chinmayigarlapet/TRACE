
from abc import ABC, abstractmethod

from ollama import Client
from openai import OpenAI

from .config import settings
from .schemas import InvestigationPlan


SYSTEM_PROMPT = """
You are TRACE, an enterprise incident investigation assistant.

Generate up to five plausible root-cause hypotheses.
For each hypothesis, explain why it is plausible and
suggest a diagnostic check.

Do not claim any hypothesis is confirmed.
Do not invent diagnostic results.
Only use information supplied in the incident.
"""


class LLMProvider(ABC):
    @abstractmethod
    def generate_plan(
        self,
        incident: str,
    ) -> InvestigationPlan:
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


def create_llm_provider() -> LLMProvider:
    if settings.trace_llm_provider == "ollama":
        return OllamaProvider()

    if settings.trace_llm_provider == "openai":
        return OpenAIProvider()

    raise ValueError("Unsupported LLM provider.")
