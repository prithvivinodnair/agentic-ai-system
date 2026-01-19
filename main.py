"""
Main entry point for the Agentic AI System
Demonstrates national-scale operational decision making
"""

import asyncio
from orchestrator import AgenticOrchestrator
from rich.console import Console
from config import config
import json


console = Console()


async def example_emergency_resource_allocation():
    """
    Example: Emergency Resource Allocation During Natural Disaster

    This scenario demonstrates the system making decisions about
    allocating emergency resources across affected regions
    """

    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            EMERGENCY SITUATION REPORT - HURRICANE IMPACT ASSESSMENT

            Region A (Population: 2.5M):
            - 60% power outage
            - 3 hospitals at capacity
            - Emergency shelters: 15 operational, 5 damaged
            - Critical supplies: Water (40% stock), Medical (30% stock)
            - Road access: 70% operational

            Region B (Population: 1.8M):
            - 85% power outage
            - 2 hospitals operational, 1 offline
            - Emergency shelters: 8 operational, 12 damaged
            - Critical supplies: Water (15% stock), Medical (20% stock)
            - Road access: 45% operational

            Region C (Population: 3.2M):
            - 30% power outage
            - 5 hospitals operational
            - Emergency shelters: 25 operational, 2 damaged
            - Critical supplies: Water (70% stock), Medical (60% stock)
            - Road access: 90% operational

            AVAILABLE RESOURCES:
            - Emergency medical teams: 15 teams
            - Water trucks: 30 units
            - Power generators: 25 units (large), 50 units (portable)
            - Medical supplies: 500 pallets
            - Search & rescue teams: 8 teams
            - Emergency budget: $50M immediate release
            """,
        },
        "context": "Emergency resource allocation for hurricane disaster response. Lives are at stake. Immediate decisions required within 24 hours.",
        "objectives": [
            "Minimize loss of life",
            "Restore critical infrastructure",
            "Ensure equitable resource distribution",
            "Maximize impact per dollar spent",
            "Maintain long-term sustainability",
        ],
        "options": [
            {
                "option_id": "opt_1",
                "name": "Proportional Distribution",
                "description": "Distribute resources proportionally based on population size",
                "estimated_cost": "$45M",
                "implementation_time": "12 hours",
            },
            {
                "option_id": "opt_2",
                "name": "Critical Needs Priority",
                "description": "Prioritize regions with most critical conditions (Region B)",
                "estimated_cost": "$48M",
                "implementation_time": "8 hours",
            },
            {
                "option_id": "opt_3",
                "name": "Staged Response",
                "description": "Immediate triage to critical areas, then systematic expansion",
                "estimated_cost": "$50M",
                "implementation_time": "6 hours initial, 48 hours complete",
            },
            {
                "option_id": "opt_4",
                "name": "Hub and Spoke Model",
                "description": "Establish Region C as central hub, distribute from there",
                "estimated_cost": "$42M",
                "implementation_time": "18 hours",
            },
        ],
        "constraints": {
            "budget_limit": "$50M immediate, $200M total",
            "time_constraint": "Critical decisions within 24 hours",
            "resource_capacity": "Limited medical teams and generators",
            "regulatory": "Must follow FEMA guidelines and state emergency protocols",
            "political": "All regions must receive some support for equity",
            "logistical": "Road access varies significantly by region",
        },
        "resources": {
            "personnel": "500 emergency responders available",
            "equipment": "As listed in situation report",
            "budget": "$50M immediate release authorized",
            "coordination": "FEMA coordination available",
        },
        "timeline": "48 hours",
    }

    orchestrator = AgenticOrchestrator()
    results = await orchestrator.execute_workflow(scenario, verbose=True)

    # Export results
    output_file = "emergency_response_decision.json"
    orchestrator.export_results(results["workflow_id"], output_file)
    console.print(f"\n[green]Results exported to: {output_file}[/green]")

    return results


async def example_infrastructure_planning():
    """
    Example: National Infrastructure Investment Decision

    Deciding how to allocate infrastructure budget across
    transportation, energy, and telecommunications
    """

    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            INFRASTRUCTURE ASSESSMENT REPORT

            Transportation:
            - 35% of bridges require major repairs
            - Highway congestion costs: $120B/year in productivity
            - Public transit ridership: Up 15% year-over-year
            - Rural areas lack adequate road infrastructure

            Energy Grid:
            - 60% of grid infrastructure over 30 years old
            - Renewable energy capacity: 25% of total
            - Peak demand blackouts: 15 incidents last year
            - Grid modernization ROI: Estimated 3.2x over 20 years

            Telecommunications:
            - 25M citizens lack broadband access
            - 5G coverage: 60% of urban areas, 10% rural
            - Economic impact of poor connectivity: $80B/year
            - Digital divide affecting education and healthcare

            Available Budget: $300 Billion over 5 years
            """,
        },
        "context": "Long-term national infrastructure investment strategy with multi-generational impact",
        "objectives": [
            "Maximize economic growth and productivity",
            "Ensure national security and resilience",
            "Promote equity and access across all communities",
            "Support climate and sustainability goals",
            "Create high-quality jobs",
        ],
        "options": [
            {
                "option_id": "infra_1",
                "name": "Balanced Approach",
                "transportation": "40%",
                "energy": "35%",
                "telecom": "25%",
            },
            {
                "option_id": "infra_2",
                "name": "Energy Transition Focus",
                "transportation": "25%",
                "energy": "55%",
                "telecom": "20%",
            },
            {
                "option_id": "infra_3",
                "name": "Digital Infrastructure Priority",
                "transportation": "30%",
                "energy": "25%",
                "telecom": "45%",
            },
        ],
        "constraints": {
            "budget": "$300B total, $60B per year maximum",
            "political": "Must show progress within first 2 years for re-election",
            "environmental": "Must align with climate commitments",
            "technical": "Workforce availability for specialized projects",
        },
        "resources": {
            "budget": "$300 Billion",
            "implementation_period": "5 years",
        },
        "timeline": "5 years",
    }

    orchestrator = AgenticOrchestrator()
    results = await orchestrator.execute_workflow(scenario, verbose=True)

    output_file = "infrastructure_decision.json"
    orchestrator.export_results(results["workflow_id"], output_file)
    console.print(f"\n[green]Results exported to: {output_file}[/green]")

    return results


async def main():
    """Main entry point with example scenarios"""

    console.print("[bold cyan]AGENTIC AI SYSTEM - NATIONAL-SCALE OPERATIONAL DECISIONS[/bold cyan]\n")

    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        console.print(f"[bold red]Configuration Error:[/bold red] {str(e)}")
        console.print("\nPlease create a .env file with your API keys.")
        console.print("See .env.example for reference.")
        return

    # Menu
    console.print("Select a scenario to run:\n")
    console.print("1. Emergency Resource Allocation (Hurricane Response)")
    console.print("2. Infrastructure Investment Planning")
    console.print("3. Exit\n")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        console.print("\n[bold]Running Emergency Resource Allocation Scenario...[/bold]\n")
        await example_emergency_resource_allocation()
    elif choice == "2":
        console.print("\n[bold]Running Infrastructure Planning Scenario...[/bold]\n")
        await example_infrastructure_planning()
    elif choice == "3":
        console.print("Exiting...")
        return
    else:
        console.print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    asyncio.run(main())
