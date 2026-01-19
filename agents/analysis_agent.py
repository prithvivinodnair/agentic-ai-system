"""
Analysis Agent
Extracts insights, identifies constraints, and performs data analysis
Uses LLM for intelligent analysis of unstructured data
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentResponse
from config import config
from llm_client import llm_client


class AnalysisAgent(BaseAgent):
    """
    Agent specialized in analyzing data and extracting actionable insights
    """

    def __init__(self):
        super().__init__(
            name="AnalysisAgent",
            description="Analyzes data to extract insights, constraints, and key information",
        )
        self.client = llm_client

    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Analyze data and extract insights

        Args:
            task: {
                "data": Any (data to analyze),
                "analysis_type": "constraints" | "insights" | "risks" | "summary",
                "context": str (optional context about the operational decision)
            }

        Returns:
            AgentResponse with analysis results
        """
        try:
            data = task.get("data")
            analysis_type = task.get("analysis_type", "insights")
            context = task.get("context", "")

            # Perform LLM-based analysis
            analysis_result = await self._analyze_with_llm(data, analysis_type, context)

            response = AgentResponse(
                agent_name=self.name,
                status="success",
                data={
                    "analysis": analysis_result,
                    "analysis_type": analysis_type,
                },
                metadata={
                    "provider": config.LLM_PROVIDER,
                    "context_provided": bool(context),
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

    async def _analyze_with_llm(
        self, data: Any, analysis_type: str, context: str
    ) -> Dict[str, Any]:
        """Use LLM to perform intelligent analysis"""

        # Create appropriate prompt based on analysis type
        prompts = {
            "constraints": """
            Analyze the following data and identify all operational constraints, limitations, and requirements.
            Focus on: budget constraints, resource limitations, regulatory requirements, time constraints, and dependencies.

            Data: {data}
            Context: {context}

            Provide a structured analysis with:
            1. Identified constraints (list each with severity: high/medium/low)
            2. Dependencies between constraints
            3. Critical path items

            Format as JSON.
            """,
            "insights": """
            Analyze the following data and extract key insights relevant to operational decision-making.
            Focus on: trends, patterns, anomalies, opportunities, and risks.

            Data: {data}
            Context: {context}

            Provide:
            1. Key insights (top 5)
            2. Data patterns observed
            3. Recommendations

            Format as JSON.
            """,
            "risks": """
            Conduct a risk assessment on the following data for operational decision-making.

            Data: {data}
            Context: {context}

            Identify:
            1. Potential risks (with probability: high/medium/low and impact: high/medium/low)
            2. Mitigation strategies
            3. Risk prioritization

            Format as JSON.
            """,
            "summary": """
            Provide a concise executive summary of the following data for decision-makers.

            Data: {data}
            Context: {context}

            Include:
            1. Executive summary (2-3 sentences)
            2. Key facts and figures
            3. Critical information for decision-making

            Format as JSON.
            """,
        }

        prompt = prompts.get(analysis_type, prompts["insights"]).format(
            data=str(data)[:4000],  # Limit data size
            context=context,
        )

        # Call LLM API (works with any provider)
        result_text = await self.client.chat(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert data analyst specialized in operational decision-making at national scale. Provide structured, actionable analysis.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
        )

        # Try to parse as JSON, fallback to text
        try:
            import json

            result = json.loads(result_text)
        except:
            result = {"analysis": result_text}

        return result
