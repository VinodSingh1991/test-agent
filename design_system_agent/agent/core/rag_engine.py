"""
RAG (Retrieval Augmented Generation) engine for design system queries.
Basic keyword-based version - will be upgraded to vector embeddings later.
"""
from pathlib import Path
from typing import List, Dict, Any


class RAGEngine:
    """Handles retrieval for design system queries using keyword matching."""
    
    def __init__(self):
        self.documents_cache = {}
        self._load_documents()
        print(f"RAGEngine initialized with {len(self.documents_cache)} documents")
    
    def _load_documents(self):
        """Load all design system documentation."""
        # Try multiple potential paths
        base_paths = [
            Path(__file__).parent.parent.parent / "documents",  # From package root
            Path(__file__).parent.parent / "documents",  # Original path
            Path("documents"),  # Current directory
        ]
        
        docs_path = None
        for path in base_paths:
            if path.exists():
                docs_path = path
                break
        
        if not docs_path:
            print(f"Documents path does not exist. Tried: {[str(p) for p in base_paths]}")
            return
        
        for file_path in docs_path.rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    doc_type = file_path.parent.name
                    doc_name = file_path.stem
                    self.documents_cache[f"{doc_type}/{doc_name}"] = {
                        "content": content,
                        "type": doc_type,
                        "name": doc_name,
                        "path": str(file_path)
                    }
                print(f"Loaded document: {doc_type}/{doc_name}")
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
    
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant documents for the query using keyword matching.
        
        Args:
            query: Search query
            top_k: Number of top results to return
            
        Returns:
            List of relevant documents with scores
        """
        query_lower = query.lower()
        results = []
        
        for doc_id, doc in self.documents_cache.items():
            content_lower = doc["content"].lower()
            # Score based on keyword matches
            score = 0
            for word in query_lower.split():
                if len(word) > 2:  # Skip very short words
                    score += content_lower.count(word)
            
            if score > 0:
                results.append({
                    "id": doc_id,
                    "content": doc["content"],
                    "type": doc["type"],
                    "name": doc["name"],
                    "score": score
                })
        
        # Sort by score and return top_k
        results.sort(key=lambda x: x["score"], reverse=True)
        print(f"Retrieved {len(results[:top_k])} documents for query: {query}")
        return results[:top_k]
    
    def get_all_documents(self) -> List[Dict[str, Any]]:
        """Get all cached documents."""
        return [
            {"id": doc_id, **doc}
            for doc_id, doc in self.documents_cache.items()
        ]
