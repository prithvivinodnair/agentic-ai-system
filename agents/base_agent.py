"""
Base Agent class that all specialized agents inherit from
Provides core functionality for agent communication and execution
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import json


class AgentResponse(BaseModel):
    """Standardized response format for all agents"""

    agent_name: str
    status: str  # success, error, pending
    data: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    error_message: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary"""
        return self.model_dump()

    def to_json(self) -> str:
        """Convert response to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the system
    Defines the interface that all agents must implement
    """

    def __init__(self, name: str, description: str, tools: Optional[List[Any]] = None):
        self.name = name
        self.description = description
        self.tools = tools or []
        self.execution_history: List[AgentResponse] = []

    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Execute the agent's primary function
        Must be implemented by all child classes

        Args:
            task: Dictionary containing task parameters and data

        Returns:
            AgentResponse with execution results
        """
        pass

    def log_execution(self, response: AgentResponse) -> None:
        """Log the execution for audit trail"""
        self.execution_history.append(response)

    def get_history(self) -> List[AgentResponse]:
        """Retrieve execution history"""
        return self.execution_history

    def clear_history(self) -> None:
        """Clear execution history"""
        self.execution_history = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
