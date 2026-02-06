"""
API routes for design system agent endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional, List, Dict, TypedDict
from loguru import logger

from design_system_agent.core.dataset_genertor.dataset_generator_controller import DataSetGeneratorController
from design_system_agent.agent.core.vector_layout_rag import VectorLayoutRAGEngine

from ..agent.agent_controller import AgentController

router = APIRouter()
agent = AgentController()
summary_dataset_controller = DataSetGeneratorController()

# RAG Engine (lazy initialization)
_rag_engine: Optional[VectorLayoutRAGEngine] = None


def get_rag_engine() -> VectorLayoutRAGEngine:
    """Get or initialize the RAG engine (singleton pattern)"""
    global _rag_engine
    if _rag_engine is None:
        logger.info("Initializing Vector RAG Engine...")
        _rag_engine = VectorLayoutRAGEngine()
        logger.info("Vector RAG Engine initialized successfully")
    return _rag_engine


class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None
    format: Optional[str] = "json"  # react, html, or json


class RAGSearchRequest(BaseModel):
    query: str
    top_k: int = 10
    rerank: bool = True
    final_k: int = 3


class RAGSearchResponse(BaseModel):
    query: str
    results: List[Dict[str, Any]]
    total_results: int


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


@router.post("/rag/search", response_model=RAGSearchResponse)
async def rag_search(request: RAGSearchRequest):
    """
    Search for similar CRM layouts using Vector RAG with reranking.
    
    Args:
        request: Search parameters including query, filters, and ranking options
        
    Returns:
        RAGSearchResponse with matching layouts
    """
    try:
        logger.info(f"RAG search: '{request.query}'")
        
        # Get RAG engine
        rag_engine = get_rag_engine()
        
        # Perform search (entity and view_type removed)
        results = rag_engine.search(
            query=request.query,
            entity=None,
            view_type=None,
            top_k=request.top_k,
            rerank=request.rerank,
            final_k=request.final_k
        )
        
        logger.info(f"RAG search completed: {len(results)} results found")
        
        return RAGSearchResponse(
            query=request.query,
            results=results,
            total_results=len(results)
        )
        
    except Exception as e:
        logger.error("RAG search error: {}", str(e))
        raise HTTPException(status_code=500, detail=f"RAG search failed: {str(e)}")


@router.get("/rag/stats", response_model=Dict[str, Any])
async def rag_stats():
    """
    Get statistics about the RAG index.
    
    Returns:
        Dictionary with RAG engine statistics
    """
    try:
        logger.info("Fetching RAG statistics")
        
        # Get RAG engine
        rag_engine = get_rag_engine()
        
        # Get statistics
        stats = rag_engine.get_stats()
        
        logger.info(f"RAG stats retrieved: {stats['total_documents']} documents indexed")
        
        return {
            "status": "success",
            "stats": stats
        }
        
    except Exception as e:
        logger.error("RAG stats error: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to get RAG stats: {str(e)}")


@router.post("/rag/reindex", response_model=Dict[str, str])
async def rag_reindex():
    """
    Force reindexing of the CRM layouts dataset.
    Rebuilds the FAISS index from scratch.
    
    Returns:
        Status message
    """
    try:
        logger.info("Starting RAG reindexing...")
        
        # Clear existing RAG engine to force rebuild
        global _rag_engine
        _rag_engine = None
        
        # Reinitialize (will rebuild index)
        rag_engine = get_rag_engine()
        
        stats = rag_engine.get_stats()
        
        logger.info(f"RAG reindexing completed: {stats['total_documents']} documents indexed")
        
        return {
            "status": "success",
            "message": f"RAG index rebuilt successfully. {stats['total_documents']} documents indexed.",
            "documents_indexed": str(stats['total_documents'])
        }
        
    except Exception as e:
        logger.error("RAG reindex error: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to reindex RAG: {str(e)}")
