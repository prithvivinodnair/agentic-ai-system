"""
Configuration module for the Agentic AI System
Handles environment variables and system-wide settings
"""

import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class Config:
    """Central configuration class for the system"""

    # LLM Provider Selection
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "gemini")  # gemini, ollama, or openai

    # API Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")

    # Ollama Configuration
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama2")

    # Model Configuration
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "2000"))

    # System Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))

    # Agent Configuration
    MAX_AGENT_ITERATIONS: int = 5
    AGENT_TIMEOUT: int = 120

    @classmethod
    def validate(cls) -> bool:
        """Validate that required configuration is present"""
        if cls.LLM_PROVIDER == "openai" and not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set when using OpenAI provider")

        if cls.LLM_PROVIDER == "gemini" and not cls.GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY must be set when using Gemini provider.\n"
                "Get a FREE key at: https://makersuite.google.com/app/apikey"
            )

        if cls.LLM_PROVIDER == "ollama":
            print(f"Using Ollama at {cls.OLLAMA_BASE_URL} with model {cls.OLLAMA_MODEL}")
            print("Make sure Ollama is running: 'ollama serve'")

        if cls.LLM_PROVIDER not in ["openai", "gemini", "ollama"]:
            raise ValueError(f"Invalid LLM_PROVIDER: {cls.LLM_PROVIDER}. Must be 'openai', 'gemini', or 'ollama'")

        return True


config = Config()
