"""
Reasoning Agent
Evaluates options against constraints and performs multi-criteria reasoning
Uses LLM for complex reasoning tasks
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentResponse
from config import config
from llm_client import llm_client


class ReasoningAgent(BaseAgent):
    """
    Agent specialized in reasoning about decisions given constraints and objectives
    """

    def __init__(self):
        super().__init__(
            name="ReasoningAgent",
            description="Performs multi-criteria reasoning and constraint evaluation",
        )
        self.client = llm_client

    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Reason about options given constraints

        Args:
            task: {
                "options": List[Dict] (available options/alternatives),
                "constraints": Dict (identified constraints),
                "objectives": List[str] (decision objectives),
                "context": str (decision context)
            }

        Returns:
            AgentResponse with reasoning results and recommendations
        """
        try:
            options = task.get("options", [])
            constraints = task.get("constraints", {})
            objectives = task.get("objectives", [])
            context = task.get("context", "")

            # Perform constraint-based reasoning
            reasoning_result = await self._reason_with_constraints(
                options, constraints, objectives, context
            )

            response = AgentResponse(
                agent_name=self.name,
                status="success",
                data={
                    "reasoning": reasoning_result,
                    "evaluated_options": len(options),
                },
                metadata={
                    "constraints_count": len(constraints) if isinstance(constraints, dict) else 0,
                    "objectives_count": len(objectives),
                },
            )

        except Exception as e:
            response = AgentResponse(
                agent_name=self.name,
                status="error",
                error_message=str(e),
            )

        self.log_execution(response)
        return response

    async def _reason_with_constraints(
        self,
        options: List[Dict],
        constraints: Dict,
        objectives: List[str],
        context: str,
    ) -> Dict[str, Any]:
        """Use LLM to perform constraint-based reasoning"""

        prompt = f"""
        You are a strategic decision-making AI for national-scale operational decisions.

        CONTEXT: {context}

        OBJECTIVES:
        {chr(10).join(f"- {obj}" for obj in objectives)}

        CONSTRAINTS:
        {self._format_constraints(constraints)}

        AVAILABLE OPTIONS:
        {self._format_options(options)}

        TASK:
        1. Evaluate each option against the constraints
        2. Score each option on how well it meets the objectives (0-100 scale)
        3. Identify trade-offs and risks for each option
        4. Provide a ranked recommendation with justification

        Respond in the following JSON format:
        {{
            "evaluation": [
                {{
                    "option_id": "string",
                    "option_name": "string",
                    "constraint_compliance": {{"constraint_name": "pass/fail/partial"}},
                    "objective_scores": {{"objective": score}},
                    "overall_score": number,
                    "pros": ["list"],
                    "cons": ["list"],
                    "risks": ["list"]
                }}
            ],
            "ranked_recommendations": [
                {{
                    "rank": number,
                    "option_id": "string",
                    "justification": "string"
                }}
            ],
            "key_tradeoffs": "string",
            "critical_considerations": ["list"]
        }}
        """

        result_text = await self.client.chat(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in multi-criteria decision analysis and operational planning at national scale.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
        )

        # Parse JSON response
        try:
            import json

            result = json.loads(result_text)
        except:
            # Fallback if not valid JSON
            result = {"raw_reasoning": result_text}

        return result

    def _format_constraints(self, constraints: Dict) -> str:
        """Format constraints for prompt"""
        if not constraints:
            return "No specific constraints provided"

        formatted = []
        for key, value in constraints.items():
            if isinstance(value, dict):
                formatted.append(f"- {key}: {value}")
            else:
                formatted.append(f"- {key}: {value}")
        return "\n".join(formatted)

    def _format_options(self, options: List[Dict]) -> str:
        """Format options for prompt"""
        if not options:
            return "No options provided"

        formatted = []
        for i, option in enumerate(options, 1):
            option_str = f"\nOption {i}:"
            for key, value in option.items():
                option_str += f"\n  - {key}: {value}"
            formatted.append(option_str)
        return "\n".join(formatted)
