"""
Execution Agent
Generates actionable execution plans, reports, and workflows
Prepares outputs for real-world implementation
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta
from .base_agent import BaseAgent, AgentResponse
from config import config
from llm_client import llm_client
import json


class ExecutionAgent(BaseAgent):
    """
    Agent that creates detailed execution plans and implementation workflows
    """

    def __init__(self):
        super().__init__(
            name="ExecutionAgent",
            description="Generates execution plans, timelines, and implementation workflows",
        )
        self.client = llm_client

    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Generate execution plan from decision

        Args:
            task: {
                "decision": Dict (from DecisionAgent),
                "resources": Dict (available resources),
                "timeline": str (timeframe for execution),
                "output_format": "detailed_plan" | "gantt_data" | "report"
            }

        Returns:
            AgentResponse with execution plan
        """
        try:
            decision = task.get("decision", {})
            resources = task.get("resources", {})
            timeline = task.get("timeline", "30 days")
            output_format = task.get("output_format", "detailed_plan")

            # Generate execution plan
            execution_plan = await self._generate_execution_plan(
                decision, resources, timeline, output_format
            )

            # Generate report if requested
            if output_format == "report":
                report = self._generate_report(decision, execution_plan)
                execution_plan["report"] = report

            response = AgentResponse(
                agent_name=self.name,
                status="success",
                data={
                    "execution_plan": execution_plan,
                    "format": output_format,
                },
                metadata={
                    "timeline": timeline,
                    "generated_at": datetime.now().isoformat(),
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

    async def _generate_execution_plan(
        self,
        decision: Dict,
        resources: Dict,
        timeline: str,
        output_format: str,
    ) -> Dict[str, Any]:
        """Generate detailed execution plan using LLM"""

        prompt = f"""
        You are a project manager responsible for executing national-scale operational decisions.

        DECISION TO IMPLEMENT:
        {json.dumps(decision, indent=2)}

        AVAILABLE RESOURCES:
        {json.dumps(resources, indent=2) if resources else "Standard government resources"}

        TIMELINE: {timeline}

        OUTPUT FORMAT: {output_format}

        TASK:
        Create a comprehensive execution plan that includes:

        1. WORK BREAKDOWN STRUCTURE (WBS)
           - Major phases (3-5 phases)
           - Tasks within each phase
           - Dependencies between tasks

        2. TIMELINE & MILESTONES
           - Start and end dates for each phase
           - Key milestones and deliverables
           - Critical path items

        3. RESOURCE ALLOCATION
           - Personnel requirements (roles and FTEs)
           - Budget allocation by phase
           - Technology and infrastructure needs

        4. RISK MANAGEMENT
           - Risk mitigation actions integrated into timeline
           - Contingency buffer allocations
           - Quality checkpoints

        5. STAKEHOLDER COMMUNICATION
           - Communication plan and frequency
           - Reporting structure
           - Approval gates

        6. SUCCESS METRICS & KPIs
           - Measurable outcomes for each phase
           - Monitoring and evaluation framework

        Provide the plan in structured JSON format.
        """

        result_text = await self.client.chat(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert program manager specializing in large-scale government and operational initiatives.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=3000,
        )

        try:
            plan = json.loads(result_text)
        except:
            plan = {
                "execution_summary": result_text,
                "format": "unstructured",
            }

        # Enhance with calculated dates
        plan = self._add_timeline_calculations(plan, timeline)

        return plan

    def _add_timeline_calculations(
        self, plan: Dict, timeline: str
    ) -> Dict[str, Any]:
        """Add calculated start/end dates to plan"""

        # Parse timeline (simple parsing for demo)
        try:
            days = int(timeline.split()[0])
        except:
            days = 30  # Default

        start_date = datetime.now()
        end_date = start_date + timedelta(days=days)

        plan["calculated_timeline"] = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "total_days": days,
            "working_days": days * 5 // 7,  # Approximate working days
        }

        return plan

    def _generate_report(self, decision: Dict, execution_plan: Dict) -> str:
        """Generate executive summary report"""

        report = f"""
        ═══════════════════════════════════════════════════════════════
        NATIONAL-SCALE OPERATIONAL DECISION REPORT
        ═══════════════════════════════════════════════════════════════

        Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        EXECUTIVE SUMMARY
        ─────────────────────────────────────────────────────────────
        Decision: {decision.get('RECOMMENDED DECISION', decision.get('decision_summary', 'N/A'))}

        Confidence Level: {decision.get('CONFIDENCE LEVEL', decision.get('confidence', 'N/A'))}

        Implementation Priority: {decision.get('IMPLEMENTATION PRIORITY', 'N/A')}


        KEY SUPPORTING FACTORS
        ─────────────────────────────────────────────────────────────
        """

        factors = decision.get("KEY SUPPORTING FACTORS", [])
        if factors:
            for i, factor in enumerate(factors, 1):
                report += f"{i}. {factor}\n        "

        report += f"""

        EXECUTION TIMELINE
        ─────────────────────────────────────────────────────────────
        Start Date: {execution_plan.get('calculated_timeline', {}).get('start_date', 'TBD')}
        End Date: {execution_plan.get('calculated_timeline', {}).get('end_date', 'TBD')}
        Duration: {execution_plan.get('calculated_timeline', {}).get('total_days', 'TBD')} days


        NEXT STEPS
        ─────────────────────────────────────────────────────────────
        """

        next_steps = decision.get("NEXT STEPS", [])
        if next_steps:
            for i, step in enumerate(next_steps, 1):
                report += f"{i}. {step}\n        "

        report += f"""

        RISK MITIGATION
        ─────────────────────────────────────────────────────────────
        """

        risks = decision.get("IDENTIFIED RISKS", [])
        if risks:
            for risk in risks:
                if isinstance(risk, dict):
                    report += f"• {risk}\n        "
                else:
                    report += f"• {risk}\n        "

        report += """
        ═══════════════════════════════════════════════════════════════
        END OF REPORT
        ═══════════════════════════════════════════════════════════════
        """

        return report
