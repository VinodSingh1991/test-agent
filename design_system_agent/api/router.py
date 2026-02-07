"""
API routes for design system agent endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Optional, List, Dict
from loguru import logger

from design_system_agent.agent.core.vector_layout_rag import VectorLayoutRAGEngine

from ..agent.agent_controller import AgentController
from ..core.dataset_genertor.dataset_generator_controller import DataSetGeneratorController

router = APIRouter()
agent = AgentController()

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


class DatasetGenerateRequest(BaseModel):
    total_records: Optional[int] = 2000
    force_regenerate: bool = False


class DatasetGenerateResponse(BaseModel):
    status: str
    message: str
    total_records: int
    jsonl_path: str
    json_path: str
    patterns_used: List[str]
    object_types: List[str]


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
        
        # Perform search with query variations
        results = rag_engine.search(
            query=request.query,
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
        rag_engine = get_rag_engine()
        
        stats = {
            "total_indexed_layouts": len(rag_engine.layouts_metadata),
            "index_path": str(rag_engine.index_path),
            "metadata_path": str(rag_engine.metadata_path),
            "embedding_model": "all-MiniLM-L6-v2",
            "embedding_dimension": rag_engine.embedding_dim,
            "reranker_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"
        }
        
        logger.info("RAG stats retrieved")
        return stats
        
    except Exception as e:
        logger.error("Error getting RAG stats: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")


@router.post("/rag/rebuild", response_model=Dict[str, Any])
async def rebuild_rag_index():
    """
    Rebuild the RAG index from the dataset file.
    This will delete existing index and create a new one.
    
    Returns:
        Status information about the rebuild
    """
    try:
        global _rag_engine
        
        logger.info("Starting RAG index rebuild...")
        
        # Delete existing index files if they exist
        import shutil
        from pathlib import Path
        
        index_dir = Path(__file__).parent.parent / "vector_index"
        if index_dir.exists():
            logger.info(f"Removing existing index directory: {index_dir}")
            shutil.rmtree(index_dir)
        
        # Reset RAG engine (will rebuild on next access)
        _rag_engine = None
        
        # Initialize new RAG engine (this will rebuild the index)
        logger.info("Rebuilding index...")
        rag_engine = get_rag_engine()
        
        result = {
            "status": "success",
            "message": "RAG index rebuilt successfully",
            "total_layouts_indexed": len(rag_engine.layouts_metadata),
            "index_path": str(rag_engine.index_path)
        }
        
        logger.info("RAG index rebuild completed")
        return result
        
    except Exception as e:
        logger.error("Error rebuilding RAG index: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to rebuild index: {str(e)}")


@router.post("/dataset/generate", response_model=DatasetGenerateResponse)
async def generate_dataset(request: DatasetGenerateRequest):
    """
    Generate CRM layouts dataset with patterns.
    
    This endpoint generates a comprehensive dataset of CRM layouts using all 16 patterns.
    The dataset includes layouts for various CRM objects (Lead, Account, Contact, Case, etc.)
    with different query types and pattern combinations.
    
    Args:
        request: Generation parameters including total_records and force_regenerate flag
        
    Returns:
        DatasetGenerateResponse with generation statistics and file paths
    """
    try:
        logger.info(f"Starting dataset generation (total_records={request.total_records}, force={request.force_regenerate})")
        
        # Initialize dataset generator controller
        dataset_controller = DataSetGeneratorController()
        
        # Check if dataset already exists
        from pathlib import Path
        dataset_dir = Path(__file__).parent.parent / "dataset"
        json_file = dataset_dir / "crm_layouts.json"
        jsonl_file = dataset_dir / "crm_layouts.jsonl"
        
        if json_file.exists() and jsonl_file.exists() and not request.force_regenerate:
            logger.warning("Dataset already exists. Use force_regenerate=true to regenerate.")
            
            # Read existing dataset to get stats
            import json
            with open(json_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
            
            patterns = list(set(r.get("patterns_used", [r.get("pattern", "unknown")])[0] if isinstance(r.get("patterns_used", [r.get("pattern", "unknown")]), list) else r.get("pattern", "unknown") for r in existing_data))
            object_types = list(set(r.get("object_type", r.get("entity", "unknown")) for r in existing_data))
            
            return DatasetGenerateResponse(
                status="exists",
                message="Dataset already exists. Use force_regenerate=true to regenerate.",
                total_records=len(existing_data),
                jsonl_path=str(jsonl_file),
                json_path=str(json_file),
                patterns_used=patterns,
                object_types=object_types
            )
        
        # Generate the dataset
        logger.info("Generating new dataset...")
        result = dataset_controller.generate_summary_dataset()
        
        # Read the generated dataset to get detailed stats
        import json
        with open(json_file, 'r', encoding='utf-8') as f:
            generated_data = json.load(f)
        
        # Extract patterns and object types from generated data
        patterns = list(set(r.get("patterns_used", [r.get("pattern", "unknown")])[0] if isinstance(r.get("patterns_used", [r.get("pattern", "unknown")]), list) else r.get("pattern", "unknown") for r in generated_data))
        object_types = list(set(r.get("object_type", r.get("entity", "unknown")) for r in generated_data))
        
        logger.info(f"Dataset generation completed: {len(generated_data)} records, {len(patterns)} patterns, {len(object_types)} object types")
        
        return DatasetGenerateResponse(
            status="success",
            message="Dataset generated successfully",
            total_records=len(generated_data),
            jsonl_path=str(jsonl_file),
            json_path=str(json_file),
            patterns_used=sorted(patterns),
            object_types=sorted(object_types)
        )
        
    except Exception as e:
        logger.error("Dataset generation error: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to generate dataset: {str(e)}")


@router.get("/dataset/info", response_model=Dict[str, Any])
async def get_dataset_info():
    """
    Get information about the current dataset.
    
    Returns statistics about the existing dataset including:
    - Total records
    - Patterns used
    - Object types covered
    - File paths
    - File sizes
    
    Returns:
        Dictionary with dataset information
    """
    try:
        from pathlib import Path
        import json
        import os
        
        dataset_dir = Path(__file__).parent.parent / "dataset"
        json_file = dataset_dir / "crm_layouts.json"
        jsonl_file = dataset_dir / "crm_layouts.jsonl"
        
        if not json_file.exists():
            return {
                "status": "not_found",
                "message": "Dataset does not exist. Generate it using POST /dataset/generate",
                "exists": False
            }
        
        # Read dataset
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract statistics
        patterns = list(set(r.get("patterns_used", [r.get("pattern", "unknown")])[0] if isinstance(r.get("patterns_used", [r.get("pattern", "unknown")]), list) else r.get("pattern", "unknown") for r in data))
        object_types = list(set(r.get("object_type", r.get("entity", "unknown")) for r in data))
        layout_types = list(set(r.get("layout_type", r.get("view_type", "unknown")) for r in data))
        
        # Count patterns and object types
        pattern_counts = {}
        for r in data:
            p = r.get("patterns_used", [r.get("pattern", "unknown")])[0] if isinstance(r.get("patterns_used", [r.get("pattern", "unknown")]), list) else r.get("pattern", "unknown")
            pattern_counts[p] = pattern_counts.get(p, 0) + 1
        
        object_type_counts = {}
        for r in data:
            obj = r.get("object_type", r.get("entity", "unknown"))
            object_type_counts[obj] = object_type_counts.get(obj, 0) + 1
        
        # Get file sizes
        json_size = os.path.getsize(json_file)
        jsonl_size = os.path.getsize(jsonl_file) if jsonl_file.exists() else 0
        
        logger.info(f"Dataset info retrieved: {len(data)} records")
        
        return {
            "status": "success",
            "exists": True,
            "total_records": len(data),
            "patterns": sorted(patterns),
            "pattern_counts": pattern_counts,
            "object_types": sorted(object_types),
            "object_type_counts": object_type_counts,
            "layout_types": sorted(layout_types),
            "files": {
                "json": {
                    "path": str(json_file),
                    "size_bytes": json_size,
                    "size_mb": round(json_size / (1024 * 1024), 2)
                },
                "jsonl": {
                    "path": str(jsonl_file),
                    "size_bytes": jsonl_size,
                    "size_mb": round(jsonl_size / (1024 * 1024), 2)
                }
            }
        }
        
    except Exception as e:
        logger.error("Error getting dataset info: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to get dataset info: {str(e)}")
