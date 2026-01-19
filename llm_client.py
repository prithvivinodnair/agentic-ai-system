"""
Universal LLM Client
Supports multiple providers: OpenAI (paid), Google Gemini (free), Ollama (free, local)
"""

from typing import Dict, Any, List
from config import config
import json


class LLMClient:
    """Universal client that works with multiple LLM providers"""

    def __init__(self):
        self.provider = config.LLM_PROVIDER

        if self.provider == "openai":
            from openai import AsyncOpenAI
            self.client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
            self.model = "gpt-4-turbo-preview"

        elif self.provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=config.GOOGLE_API_KEY)
            self.model = "gemini-pro"
            self.client = genai

        elif self.provider == "ollama":
            import ollama
            self.client = ollama
            self.model = config.OLLAMA_MODEL

    async def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = None,
        max_tokens: int = None,
    ) -> str:
        """
        Universal chat method that works across all providers

        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Randomness (0-1)
            max_tokens: Maximum response length

        Returns:
            str: The LLM response content
        """
        temp = temperature if temperature is not None else config.TEMPERATURE
        max_tok = max_tokens if max_tokens is not None else config.MAX_TOKENS

        if self.provider == "openai":
            return await self._chat_openai(messages, temp, max_tok)
        elif self.provider == "gemini":
            return await self._chat_gemini(messages, temp, max_tok)
        elif self.provider == "ollama":
            return await self._chat_ollama(messages, temp, max_tok)

    async def _chat_openai(
        self, messages: List[Dict[str, str]], temperature: float, max_tokens: int
    ) -> str:
        """OpenAI chat completion"""
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    async def _chat_gemini(
        self, messages: List[Dict[str, str]], temperature: float, max_tokens: int
    ) -> str:
        """Google Gemini chat completion"""
        # Gemini uses a different format - convert messages
        model = self.client.GenerativeModel(self.model)

        # Combine messages into a single prompt for Gemini
        prompt = self._convert_messages_to_prompt(messages)

        # Configure generation
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }

        # Generate response
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
        )

        return response.text

    async def _chat_ollama(
        self, messages: List[Dict[str, str]], temperature: float, max_tokens: int
    ) -> str:
        """Ollama local LLM chat completion"""
        import asyncio

        # Ollama doesn't have async support, so we run in executor
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self.client.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": temperature,
                    "num_predict": max_tokens,
                },
            ),
        )

        return response["message"]["content"]

    def _convert_messages_to_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Convert OpenAI-style messages to a single prompt for Gemini"""
        prompt_parts = []

        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            if role == "system":
                prompt_parts.append(f"Instructions: {content}\n")
            elif role == "user":
                prompt_parts.append(f"User: {content}\n")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}\n")

        return "\n".join(prompt_parts)


# Create a singleton instance
llm_client = LLMClient()
