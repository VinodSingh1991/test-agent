"""
Type definitions for API requests and responses.
"""
from typing import Optional, List
from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None


class ComponentResponse(BaseModel):
    component_name: str
    code: str
    documentation: str
    confidence: float
