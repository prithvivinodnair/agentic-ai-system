"""
FastAPI Server for Agentic AI System
Provides REST API endpoints for the frontend
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import asyncio
from datetime import datetime
import json
import uuid

from orchestrator import AgenticOrchestrator
from config import config

app = FastAPI(
    title="Agentic AI System API",
    description="Multi-agent GenAI system for national-scale operational decisions",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for workflow results (in production, use a database)
workflows: Dict[str, Dict[str, Any]] = {}
workflow_status: Dict[str, str] = {}


class ScenarioRequest(BaseModel):
    """Request model for running a scenario"""
    scenario_type: str  # "emergency" or "infrastructure" or "custom"
    data_source: Optional[Dict[str, Any]] = None
    context: Optional[str] = None
    objectives: Optional[List[str]] = None
    options: Optional[List[Dict[str, Any]]] = None
    constraints: Optional[Dict[str, Any]] = None
    resources: Optional[Dict[str, Any]] = None
    timeline: Optional[str] = "30 days"


class WorkflowResponse(BaseModel):
    """Response model for workflow operations"""
    workflow_id: str
    status: str
    message: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Agentic AI System",
        "version": "1.0.0",
        "provider": config.LLM_PROVIDER
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        config.validate()
        return {
            "status": "healthy",
            "llm_provider": config.LLM_PROVIDER,
            "configuration": "valid"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/scenarios")
async def get_scenarios():
    """Get available pre-built scenarios"""
    return {
        "scenarios": [
            {
                "id": "emergency",
                "name": "Emergency Resource Allocation",
                "description": "Hurricane disaster response across multiple regions",
                "category": "Emergency Management"
            },
            {
                "id": "infrastructure",
                "name": "Infrastructure Investment Planning",
                "description": "National infrastructure budget allocation",
                "category": "Long-term Planning"
            }
        ]
    }


@app.post("/workflow/run", response_model=WorkflowResponse)
async def run_workflow(request: ScenarioRequest, background_tasks: BackgroundTasks):
    """
    Start a workflow execution
    Returns immediately with workflow_id, actual processing happens in background
    """
    workflow_id = str(uuid.uuid4())

    # Get scenario configuration
    if request.scenario_type == "emergency":
        scenario = get_emergency_scenario()
    elif request.scenario_type == "infrastructure":
        scenario = get_infrastructure_scenario()
    elif request.scenario_type == "custom":
        scenario = {
            "data_source": request.data_source,
            "context": request.context,
            "objectives": request.objectives,
            "options": request.options,
            "constraints": request.constraints,
            "resources": request.resources,
            "timeline": request.timeline,
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid scenario type")

    # Initialize workflow status
    workflow_status[workflow_id] = "running"
    workflows[workflow_id] = {
        "workflow_id": workflow_id,
        "status": "running",
        "started_at": datetime.now().isoformat(),
        "scenario_type": request.scenario_type,
        "progress": 0
    }

    # Run workflow in background
    background_tasks.add_task(execute_workflow, workflow_id, scenario)

    return WorkflowResponse(
        workflow_id=workflow_id,
        status="running",
        message="Workflow started successfully"
    )


async def execute_workflow(workflow_id: str, scenario: Dict[str, Any]):
    """Execute the workflow in background"""
    try:
        orchestrator = AgenticOrchestrator()

        # Update progress
        workflows[workflow_id]["progress"] = 10
        workflows[workflow_id]["current_stage"] = "Data Ingestion"

        results = await orchestrator.execute_workflow(scenario, verbose=False)

        # Store results
        workflows[workflow_id].update({
            "status": "completed",
            "completed_at": datetime.now().isoformat(),
            "progress": 100,
            "results": results,
            "current_stage": "Completed"
        })
        workflow_status[workflow_id] = "completed"

    except Exception as e:
        workflows[workflow_id].update({
            "status": "failed",
            "completed_at": datetime.now().isoformat(),
            "error": str(e),
            "current_stage": "Failed"
        })
        workflow_status[workflow_id] = "failed"


@app.get("/workflow/{workflow_id}")
async def get_workflow_status(workflow_id: str):
    """Get workflow status and results"""
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")

    return workflows[workflow_id]


@app.get("/workflows")
async def list_workflows():
    """List all workflows"""
    return {
        "workflows": list(workflows.values()),
        "total": len(workflows)
    }


@app.delete("/workflow/{workflow_id}")
async def delete_workflow(workflow_id: str):
    """Delete a workflow"""
    if workflow_id not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")

    del workflows[workflow_id]
    if workflow_id in workflow_status:
        del workflow_status[workflow_id]

    return {"message": "Workflow deleted successfully"}


def get_emergency_scenario() -> Dict[str, Any]:
    """Get the emergency response scenario"""
    return {
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
        ],
        "constraints": {
            "budget_limit": "$50M immediate, $200M total",
            "time_constraint": "Critical decisions within 24 hours",
            "resource_capacity": "Limited medical teams and generators",
        },
        "resources": {
            "personnel": "500 emergency responders available",
            "equipment": "As listed in situation report",
            "budget": "$50M immediate release authorized",
        },
        "timeline": "48 hours",
    }


def get_infrastructure_scenario() -> Dict[str, Any]:
    """Get the infrastructure planning scenario"""
    return {
        "data_source": {
            "source_type": "text",
            "data": """
            INFRASTRUCTURE ASSESSMENT REPORT

            Transportation:
            - 35% of bridges require major repairs
            - Highway congestion costs: $120B/year in productivity
            - Public transit ridership: Up 15% year-over-year

            Energy Grid:
            - 60% of grid infrastructure over 30 years old
            - Renewable energy capacity: 25% of total
            - Peak demand blackouts: 15 incidents last year

            Telecommunications:
            - 25M citizens lack broadband access
            - 5G coverage: 60% of urban areas, 10% rural
            - Economic impact of poor connectivity: $80B/year

            Available Budget: $300 Billion over 5 years
            """,
        },
        "context": "Long-term national infrastructure investment strategy",
        "objectives": [
            "Maximize economic growth and productivity",
            "Ensure national security and resilience",
            "Promote equity and access",
            "Support climate goals",
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
        ],
        "constraints": {
            "budget": "$300B total",
            "timeline": "5 years",
        },
        "resources": {
            "budget": "$300 Billion",
        },
        "timeline": "5 years",
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Agentic AI System API Server")
    print(f"📡 LLM Provider: {config.LLM_PROVIDER}")
    print("🌐 Server will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")

    uvicorn.run(app, host="0.0.0.0", port=8000)
