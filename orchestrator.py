"""
Orchestrator - Coordinates the multi-agent system
Manages workflow between agents and ensures smooth execution
"""

from typing import Dict, Any, List, Optional
from agents import (
    DataIngestionAgent,
    AnalysisAgent,
    ReasoningAgent,
    DecisionAgent,
    ExecutionAgent,
    AgentResponse,
)
from datetime import datetime
import asyncio
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.tree import Tree


class AgenticOrchestrator:
    """
    Main orchestrator that coordinates all agents in the system
    Implements the workflow for national-scale operational decisions
    """

    def __init__(self):
        self.console = Console()

        # Initialize all agents
        self.data_agent = DataIngestionAgent()
        self.analysis_agent = AnalysisAgent()
        self.reasoning_agent = ReasoningAgent()
        self.decision_agent = DecisionAgent()
        self.execution_agent = ExecutionAgent()

        # Track execution
        self.workflow_history: List[Dict[str, Any]] = []
        self.current_workflow_id: Optional[str] = None

    async def execute_workflow(
        self,
        scenario: Dict[str, Any],
        verbose: bool = True,
    ) -> Dict[str, Any]:
        """
        Execute the complete decision-making workflow

        Args:
            scenario: {
                "data_source": Dict (source configuration),
                "context": str (decision context),
                "objectives": List[str],
                "options": List[Dict] (available options),
                "constraints": Dict (constraints),
                "resources": Dict (available resources),
                "timeline": str
            }
            verbose: Whether to display detailed progress

        Returns:
            Complete workflow results
        """
        workflow_id = f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.current_workflow_id = workflow_id

        if verbose:
            self._display_header()

        results = {
            "workflow_id": workflow_id,
            "timestamp": datetime.now().isoformat(),
            "scenario": scenario,
            "stages": {},
        }

        try:
            # Stage 1: Data Ingestion
            if verbose:
                self.console.print("\n[bold cyan]Stage 1: Data Ingestion[/bold cyan]")

            ingestion_result = await self._stage_data_ingestion(
                scenario.get("data_source", {}), verbose
            )
            results["stages"]["ingestion"] = ingestion_result

            # Stage 2: Analysis
            if verbose:
                self.console.print("\n[bold cyan]Stage 2: Data Analysis[/bold cyan]")

            analysis_result = await self._stage_analysis(
                ingestion_result, scenario.get("context", ""), verbose
            )
            results["stages"]["analysis"] = analysis_result

            # Stage 3: Reasoning
            if verbose:
                self.console.print("\n[bold cyan]Stage 3: Constraint-Based Reasoning[/bold cyan]")

            reasoning_result = await self._stage_reasoning(
                scenario.get("options", []),
                scenario.get("constraints", {}),
                scenario.get("objectives", []),
                scenario.get("context", ""),
                verbose,
            )
            results["stages"]["reasoning"] = reasoning_result

            # Stage 4: Decision Making
            if verbose:
                self.console.print("\n[bold cyan]Stage 4: Decision Making[/bold cyan]")

            decision_result = await self._stage_decision(
                analysis_result,
                reasoning_result,
                scenario.get("context", ""),
                scenario.get("decision_criteria", {}),
                verbose,
            )
            results["stages"]["decision"] = decision_result

            # Stage 5: Execution Planning
            if verbose:
                self.console.print("\n[bold cyan]Stage 5: Execution Planning[/bold cyan]")

            execution_result = await self._stage_execution(
                decision_result,
                scenario.get("resources", {}),
                scenario.get("timeline", "30 days"),
                verbose,
            )
            results["stages"]["execution"] = execution_result

            results["status"] = "success"

            if verbose:
                self._display_summary(results)

        except Exception as e:
            results["status"] = "error"
            results["error"] = str(e)
            if verbose:
                self.console.print(f"\n[bold red]Error:[/bold red] {str(e)}")

        self.workflow_history.append(results)
        return results

    async def _stage_data_ingestion(
        self, data_source: Dict[str, Any], verbose: bool
    ) -> AgentResponse:
        """Execute data ingestion stage"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            if verbose:
                progress.add_task("Ingesting data...", total=None)

            result = await self.data_agent.execute(data_source)

        if verbose and result.status == "success":
            self.console.print("✓ Data ingested successfully", style="green")

        return result

    async def _stage_analysis(
        self, ingestion_result: AgentResponse, context: str, verbose: bool
    ) -> Dict[str, AgentResponse]:
        """Execute analysis stage with multiple analysis types"""
        analyses = {}

        analysis_types = ["constraints", "insights", "risks", "summary"]

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            for analysis_type in analysis_types:
                if verbose:
                    task = progress.add_task(
                        f"Analyzing {analysis_type}...", total=None
                    )

                result = await self.analysis_agent.execute({
                    "data": ingestion_result.data,
                    "analysis_type": analysis_type,
                    "context": context,
                })

                analyses[analysis_type] = result

                if verbose:
                    progress.remove_task(task)
                    if result.status == "success":
                        self.console.print(
                            f"✓ {analysis_type.capitalize()} analysis complete",
                            style="green",
                        )

        return analyses

    async def _stage_reasoning(
        self,
        options: List[Dict],
        constraints: Dict,
        objectives: List[str],
        context: str,
        verbose: bool,
    ) -> AgentResponse:
        """Execute reasoning stage"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            if verbose:
                progress.add_task("Evaluating options against constraints...", total=None)

            result = await self.reasoning_agent.execute({
                "options": options,
                "constraints": constraints,
                "objectives": objectives,
                "context": context,
            })

        if verbose and result.status == "success":
            self.console.print("✓ Reasoning complete", style="green")

        return result

    async def _stage_decision(
        self,
        analysis_results: Dict[str, AgentResponse],
        reasoning_result: AgentResponse,
        context: str,
        criteria: Dict,
        verbose: bool,
    ) -> AgentResponse:
        """Execute decision-making stage"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            if verbose:
                progress.add_task("Synthesizing decision...", total=None)

            # Combine all analysis results
            combined_analysis = {
                k: v.data for k, v in analysis_results.items()
            }

            result = await self.decision_agent.execute({
                "analysis_results": combined_analysis,
                "reasoning_results": reasoning_result.data,
                "context": context,
                "decision_criteria": criteria,
            })

        if verbose and result.status == "success":
            self.console.print("✓ Decision finalized", style="green")

        return result

    async def _stage_execution(
        self,
        decision_result: AgentResponse,
        resources: Dict,
        timeline: str,
        verbose: bool,
    ) -> AgentResponse:
        """Execute execution planning stage"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            if verbose:
                progress.add_task("Generating execution plan...", total=None)

            result = await self.execution_agent.execute({
                "decision": decision_result.data.get("decision", {}),
                "resources": resources,
                "timeline": timeline,
                "output_format": "report",
            })

        if verbose and result.status == "success":
            self.console.print("✓ Execution plan ready", style="green")

        return result

    def _display_header(self):
        """Display workflow header"""
        header = Panel(
            "[bold white]AGENTIC AI SYSTEM FOR NATIONAL-SCALE OPERATIONAL DECISIONS[/bold white]\n"
            "[dim]Multi-Agent GenAI System for Automated Decision Making[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
        self.console.print(header)

    def _display_summary(self, results: Dict[str, Any]):
        """Display workflow summary"""
        self.console.print("\n" + "=" * 70)
        self.console.print("[bold green]WORKFLOW COMPLETED SUCCESSFULLY[/bold green]")
        self.console.print("=" * 70)

        # Display decision
        decision = results["stages"]["decision"].data.get("decision", {})

        if "RECOMMENDED DECISION" in decision:
            self.console.print(
                f"\n[bold]Recommended Decision:[/bold] {decision['RECOMMENDED DECISION']}"
            )

        if "CONFIDENCE LEVEL" in decision:
            self.console.print(
                f"[bold]Confidence Level:[/bold] {decision['CONFIDENCE LEVEL']}"
            )

        # Display execution report if available
        execution = results["stages"]["execution"].data.get("execution_plan", {})
        if "report" in execution:
            self.console.print("\n[bold cyan]EXECUTIVE REPORT:[/bold cyan]")
            self.console.print(execution["report"])

    def get_workflow_history(self) -> List[Dict[str, Any]]:
        """Get complete workflow history"""
        return self.workflow_history

    def export_results(self, workflow_id: str, output_path: str) -> bool:
        """Export workflow results to JSON file"""
        import json

        workflow = next(
            (w for w in self.workflow_history if w["workflow_id"] == workflow_id),
            None,
        )

        if not workflow:
            return False

        # Convert AgentResponse objects to dicts for serialization
        exportable = self._make_serializable(workflow)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(exportable, f, indent=2)

        return True

    def _make_serializable(self, obj: Any) -> Any:
        """Convert objects to JSON-serializable format"""
        if isinstance(obj, AgentResponse):
            return obj.to_dict()
        elif isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        else:
            return obj
