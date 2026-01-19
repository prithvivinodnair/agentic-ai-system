"""
Data Ingestion Agent
Responsible for ingesting unstructured data from multiple sources
Supports: PDFs, CSV, JSON, APIs, text files
"""

import json
import csv
from typing import Dict, Any, List
from pathlib import Path
import PyPDF2
import pandas as pd
from .base_agent import BaseAgent, AgentResponse


class DataIngestionAgent(BaseAgent):
    """
    Agent specialized in ingesting and preprocessing unstructured data
    """

    def __init__(self):
        super().__init__(
            name="DataIngestionAgent",
            description="Ingests unstructured data from multiple sources and formats",
        )
        self.supported_formats = [".pdf", ".csv", ".json", ".txt", ".xlsx"]

    async def execute(self, task: Dict[str, Any]) -> AgentResponse:
        """
        Ingest data from specified source

        Args:
            task: {
                "source_type": "file" | "api" | "text",
                "source_path": str (file path or API URL),
                "data": str (for direct text input)
            }

        Returns:
            AgentResponse with ingested data
        """
        try:
            source_type = task.get("source_type", "file")

            if source_type == "file":
                data = await self._ingest_file(task["source_path"])
            elif source_type == "text":
                data = {"content": task["data"]}
            elif source_type == "api":
                data = await self._ingest_api(task["source_path"])
            else:
                raise ValueError(f"Unsupported source type: {source_type}")

            response = AgentResponse(
                agent_name=self.name,
                status="success",
                data=data,
                metadata={
                    "source_type": source_type,
                    "source": task.get("source_path", "direct_input"),
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

    async def _ingest_file(self, file_path: str) -> Dict[str, Any]:
        """Ingest data from file based on extension"""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return self._read_pdf(path)
        elif suffix == ".csv":
            return self._read_csv(path)
        elif suffix == ".json":
            return self._read_json(path)
        elif suffix == ".txt":
            return self._read_text(path)
        elif suffix in [".xlsx", ".xls"]:
            return self._read_excel(path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")

    def _read_pdf(self, path: Path) -> Dict[str, Any]:
        """Extract text from PDF"""
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

        return {
            "content": text,
            "format": "pdf",
            "pages": len(reader.pages),
        }

    def _read_csv(self, path: Path) -> Dict[str, Any]:
        """Read CSV file into structured format"""
        df = pd.read_csv(path)
        return {
            "content": df.to_dict(orient="records"),
            "format": "csv",
            "rows": len(df),
            "columns": list(df.columns),
        }

    def _read_json(self, path: Path) -> Dict[str, Any]:
        """Read JSON file"""
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return {
            "content": data,
            "format": "json",
        }

    def _read_text(self, path: Path) -> Dict[str, Any]:
        """Read plain text file"""
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return {
            "content": content,
            "format": "text",
            "length": len(content),
        }

    def _read_excel(self, path: Path) -> Dict[str, Any]:
        """Read Excel file"""
        df = pd.read_excel(path)
        return {
            "content": df.to_dict(orient="records"),
            "format": "excel",
            "rows": len(df),
            "columns": list(df.columns),
        }

    async def _ingest_api(self, api_url: str) -> Dict[str, Any]:
        """Ingest data from API endpoint"""
        import requests

        response = requests.get(api_url, timeout=30)
        response.raise_for_status()

        return {
            "content": response.json(),
            "format": "api",
            "status_code": response.status_code,
        }
