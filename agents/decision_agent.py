"""
Decision Agent
Makes final recommendations based on analysis and reasoning
Synthesizes inputs from multiple agents
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentResponse
from config import config
from llm_client import llm_client


class DecisionAgent(BaseAgent):
    """
    Agent that synthesizes analysis and reasoning to make final decisions
    """

    def __init__(self):
        super().__init__(
            name="DecisionAgent",
            description="Synthesizes information and makes final recommendations",
        )
        self.client = llm_client

    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Make final decision based on all inputs

        Args:
            task: {
                "analysis_results": Dict (from AnalysisAgent),
                "reasoning_results": Dict (from ReasoningAgent),
                "context": str (decision context),
                "decision_criteria": Dict (final criteria for decision)
            }

        Returns:
            AgentResponse with final decision and action plan
        """
        try:
            analysis = task.get("analysis_results", {})
            reasoning = task.get("reasoning_results", {})
            context = task.get("context", "")
            criteria = task.get("decision_criteria", {})

            # Synthesize and make decision
            decision = await self._make_decision(analysis, reasoning, context, criteria)

            response = AgentResponse(
                agent_name=self.name,
                status="success",
                data={
                    "decision": decision,
                    "confidence_level": decision.get("confidence", "medium"),
                },
                metadata={
                    "has_analysis": bool(analysis),
                    "has_reasoning": bool(reasoning),
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

    async def _make_decision(
        self,
        analysis: Dict,
        reasoning: Dict,
        context: str,
        criteria: Dict,
    ) -> Dict[str, Any]:
        """Synthesize all inputs and make final decision"""

        prompt = f"""
        You are a senior decision-maker for national-scale operational decisions.

        CONTEXT: {context}

        ANALYSIS SUMMARY:
        {self._format_analysis(analysis)}

        REASONING AND EVALUATION:
        {self._format_reasoning(reasoning)}

        DECISION CRITERIA:
        {self._format_criteria(criteria)}

        TASK:
        Based on all the information above, make a final decision and provide:

        1. RECOMMENDED DECISION: Clear statement of what should be done
        2. CONFIDENCE LEVEL: High/Medium/Low with justification
        3. KEY SUPPORTING FACTORS: Top 3-5 reasons for this decision
        4. IDENTIFIED RISKS: Major risks and mitigation strategies
        5. IMPLEMENTATION PRIORITY: Critical/High/Medium/Low
        6. NEXT STEPS: Concrete action items (5-7 steps)
        7. SUCCESS METRICS: How to measure if this decision is working
        8. CONTINGENCY PLANS: Alternative approaches if primary fails

        Provide response in JSON format with these exact keys.
        """

        result_text = await self.client.chat(
            messages=[
                {
                    "role": "system",
                    "content": "You are a strategic decision-maker with expertise in national operations, policy, and resource allocation.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,  # Lower temperature for more focused decisions
            max_tokens=2500,
        )

        try:
            import json

            result = json.loads(result_text)
        except:
            result = {"decision_summary": result_text, "confidence": "medium"}

        return result

    def _format_analysis(self, analysis: Dict) -> str:
        """Format analysis results for prompt"""
        if not analysis:
            return "No analysis data available"

        import json

        return json.dumps(analysis, indent=2)[:2000]  # Limit size

    def _format_reasoning(self, reasoning: Dict) -> str:
        """Format reasoning results for prompt"""
        if not reasoning:
            return "No reasoning data available"

        import json

        return json.dumps(reasoning, indent=2)[:2000]  # Limit size

    def _format_criteria(self, criteria: Dict) -> str:
        """Format decision criteria"""
        if not criteria:
            return "Standard operational decision criteria apply"

        formatted = []
        for key, value in criteria.items():
            formatted.append(f"- {key}: {value}")
        return "\n".join(formatted)
