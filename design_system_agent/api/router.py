"""
API routes for design system agent endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional, List, Dict, TypedDict
from loguru import logger

from design_system_agent.core.dataset_genertor.dataset_generator_controller import DataSetGeneratorController

from ..agent.agent_controller import AgentController

router = APIRouter()
agent = AgentController()
summary_dataset_controller = DataSetGeneratorController()


class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None
    format: Optional[str] = "json"  # react, html, or json


@router.post("/query", response_model=Dict[str, Any])
async def process_query(request: QueryRequest):
    """Process a design system query and generate code in specified format."""
    try:
        print(f"Processing query: {request.query} (format: {request.format})")
        result = agent.process_query(request.query)
        print(f"Query processed successfully")
        return result
    except Exception as e:
        print(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/generate_dataset", response_model=Dict[str, str])
async def generate_dataset():
    """Generate the summary dataset."""
    try:
        summary_dataset_controller.generate_summary_dataset()
        return {"status": "success", "message": "Summary dataset generated successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
