
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    trace_llm_provider: Literal["ollama", "openai"] = "ollama"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"

    openai_api_key: str | None = None
    trace_llm_model: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        extra="ignore",
    )


settings = Settings()
