"""
Layout RAG Engine - Retrieval system for CRM layouts using embeddings
"""
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from design_system_agent.agent.core.rag_engine import RAGEngine


class LayoutRAGEngine:
    """RAG engine specifically for retrieving similar layout patterns"""
    
    def __init__(self):
        self.layouts_cache: List[Dict[str, Any]] = []
        self.load_layouts()
        print(f"[LayoutRAGEngine] Initialized with {len(self.layouts_cache)} layouts")
    
    def load_layouts(self):
        """Load CRM layouts from JSON dataset"""
        # Find the layouts file
        possible_paths = [
            Path(__file__).parent.parent.parent / "core" / "dataset_genertor" / "crm_dataset" / "crm_layouts.json",
            Path("design_system_agent/core/dataset_genertor/crm_dataset/crm_layouts.json"),
        ]
        
        layouts_path = None
        for path in possible_paths:
            if path.exists():
                layouts_path = path
                break
        
        if not layouts_path:
            print(f"[LayoutRAGEngine] Warning: Layouts file not found. Tried: {possible_paths}")
            return
        
        try:
            with open(layouts_path, 'r', encoding='utf-8') as f:
                self.layouts_cache = json.load(f)
            print(f"[LayoutRAGEngine] Loaded {len(self.layouts_cache)} layouts from {layouts_path}")
        except Exception as e:
            print(f"[LayoutRAGEngine] Error loading layouts: {e}")
    
    def compute_similarity_score(self, layout: Dict[str, Any], search_query: str, entity: str, view_type: str) -> float:
        """
        Compute similarity score between layout and search criteria
        
        Args:
            layout: Layout record
            search_query: RAG search query
            entity: Entity type filter
            view_type: View type filter
            
        Returns:
            Similarity score (0.0 to 1.0)
        """
        score = 0.0
        
        # Exact entity match (40 points)
        if layout.get("entity", "").lower() == entity.lower():
            score += 0.40
        
        # Exact view_type match (40 points)
        if layout.get("view_type", "").lower() == view_type.lower():
            score += 0.40
        
        # Query keyword matching (20 points)
        query_words = set(search_query.lower().split())
        layout_query = layout.get("query", "").lower()
        layout_pattern = layout.get("pattern", "").lower()
        
        # Check query matches
        matched_words = sum(1 for word in query_words if word in layout_query or word in layout_pattern)
        if len(query_words) > 0:
            score += 0.20 * (matched_words / len(query_words))
        
        return min(score, 1.0)
    
    def search_layouts(
        self,
        search_query: str,
        entity: Optional[str] = None,
        view_type: Optional[str] = None,
        top_k: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Search for most relevant layouts
        
        Args:
            search_query: Natural language search query
            entity: Filter by entity type
            view_type: Filter by view type
            top_k: Number of results to return
            
        Returns:
            List of top matching layouts with scores
        """
        print(f"[LayoutRAGEngine] Searching: '{search_query}' | Entity: {entity} | View: {view_type}")
        
        if not self.layouts_cache:
            print("[LayoutRAGEngine] No layouts loaded, returning empty results")
            return []
        
        results = []
        
        for layout in self.layouts_cache:
            score = self.compute_similarity_score(layout, search_query, entity or "", view_type or "")
            
            if score > 0.3:  # Threshold for relevance
                results.append({
                    **layout,
                    "retrieval_score": score
                })
        
        # Sort by score descending
        results.sort(key=lambda x: x["retrieval_score"], reverse=True)
        
        print(f"[LayoutRAGEngine] Found {len(results)} matching layouts, returning top {top_k}")
        if results:
            for i, r in enumerate(results[:top_k], 1):
                print(f"  {i}. {r['pattern']} (score: {r['retrieval_score']:.2f}) - {r['query']}")
        
        return results[:top_k]
    
    def get_layout_by_id(self, layout_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific layout by ID"""
        for layout in self.layouts_cache:
            if layout.get("id") == layout_id:
                return layout
        return None
    
    def get_all_patterns(self) -> List[str]:
        """Get list of all available patterns"""
        return list(set(layout.get("pattern", "") for layout in self.layouts_cache))
    
    def get_all_entities(self) -> List[str]:
        """Get list of all available entities"""
        return list(set(layout.get("entity", "") for layout in self.layouts_cache))


if __name__ == "__main__":
    # Test the engine
    engine = LayoutRAGEngine()
    
    print("\n" + "="*70)
    print("Testing RAG retrieval...")
    print("="*70)
    
    # Test 1: Search for opportunity list
    results = engine.search_layouts(
        search_query="opportunity list with filters",
        entity="opportunity",
        view_type="list",
        top_k=3
    )
    
    print(f"\nTest 1: Found {len(results)} layouts")
    for i, result in enumerate(results, 1):
        print(f"  {i}. Pattern: {result['pattern']}, Score: {result['retrieval_score']:.2f}")
    
    # Test 2: Search for lead form
    results = engine.search_layouts(
        search_query="create new lead form",
        entity="lead",
        view_type="form",
        top_k=3
    )
    
    print(f"\nTest 2: Found {len(results)} layouts")
    for i, result in enumerate(results, 1):
        print(f"  {i}. Pattern: {result['pattern']}, Score: {result['retrieval_score']:.2f}")
    
    # Test 3: Search for dashboard
    results = engine.search_layouts(
        search_query="sales dashboard with metrics",
        entity="dashboard",
        view_type="dashboard",
        top_k=3
    )
    
    print(f"\nTest 3: Found {len(results)} layouts")
    for i, result in enumerate(results, 1):
        print(f"  {i}. Pattern: {result['pattern']}, Score: {result['retrieval_score']:.2f}")
    
    print("\n" + "="*70)
    print(f"Available patterns: {', '.join(engine.get_all_patterns())}")
    print(f"Available entities: {', '.join(engine.get_all_entities())}")
