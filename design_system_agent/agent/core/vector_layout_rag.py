"""
Vector-based Layout RAG Engine with Reranking
Uses FAISS for vector search and cross-encoder for reranking
Compatible with Python 3.14+
"""
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import pickle
import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np


class VectorLayoutRAGEngine:
    """Advanced RAG engine using FAISS for semantic search with reranking"""
    
    def __init__(self, index_name: str = "crm_layouts"):
        """
        Initialize Vector RAG engine with FAISS
        
        Args:
            index_name: Name for the FAISS index
        """
        print("[VectorLayoutRAGEngine] Initializing...")
        
        # Paths for persistence
        self.index_dir = Path(__file__).parent.parent.parent / "vector_index"
        self.index_dir.mkdir(exist_ok=True)
        self.index_name = index_name
        self.index_path = self.index_dir / f"{index_name}.faiss"
        self.metadata_path = self.index_dir / f"{index_name}_metadata.pkl"
        
        # Initialize embedding model (lightweight and fast)
        print("[VectorLayoutRAGEngine] Loading embedding model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dimensions, fast
        self.embedding_dim = 384
        
        # Initialize reranker (cross-encoder for better precision)
        print("[VectorLayoutRAGEngine] Loading reranker model...")
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')  # Lightweight reranker
        
        # FAISS index and metadata
        self.index = None
        self.layouts_metadata = []
        
        # Load and index layouts
        self.load_and_index_layouts()
        
        print(f"[VectorLayoutRAGEngine] [OK] Initialized with {len(self.layouts_metadata)} indexed layouts")
    
    def load_and_index_layouts(self):
        """Load layouts from JSON and index them in FAISS"""
        # Check if index exists
        if self.index_path.exists() and self.metadata_path.exists():
            print(f"[VectorLayoutRAGEngine] Loading existing index from {self.index_path}...")
            self.index = faiss.read_index(str(self.index_path))
            with open(self.metadata_path, 'rb') as f:
                self.layouts_metadata = pickle.load(f)
            print(f"[VectorLayoutRAGEngine] [OK] Loaded {len(self.layouts_metadata)} layouts from disk")
            return
        
        # Find the layouts file
        possible_paths = [
            Path(__file__).parent.parent.parent / "dataset" / "crm_layouts.json",
            Path("design_system_agent/dataset/crm_layouts.json"),
        ]
        
        layouts_path = None
        for path in possible_paths:
            if path.exists():
                layouts_path = path
                break
        
        if not layouts_path:
            raise FileNotFoundError(f"Layouts file not found. Tried: {possible_paths}")
        
        # Load layouts
        print(f"[VectorLayoutRAGEngine] Loading layouts from {layouts_path}...")
        with open(layouts_path, 'r', encoding='utf-8') as f:
            layouts = json.load(f)
        
        print(f"[VectorLayoutRAGEngine] Loaded {len(layouts)} layouts")
        
        # Create FAISS index (using Inner Product for cosine similarity with normalized vectors)
        print(f"[VectorLayoutRAGEngine] Creating FAISS index...")
        self.index = faiss.IndexFlatIP(self.embedding_dim)  # Inner product for cosine similarity
        
        # Prepare data for indexing
        documents = []
        
        for layout in layouts:
            # Create rich document text for embedding
            doc_text = self._create_document_text(layout)
            documents.append(doc_text)
            
            # Store metadata
            self.layouts_metadata.append({
                "id": layout["id"],
                "pattern": layout["pattern"],
                "entity": layout["entity"],
                "view_type": layout["view_type"],
                "query": layout["query"],
                "components": layout["components"],
                "layout": layout.get("layout", [])
            })
        
        # Generate embeddings
        print(f"[VectorLayoutRAGEngine] Generating embeddings for {len(documents)} documents...")
        embeddings = self.embedding_model.encode(
            documents,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True  # Normalize for cosine similarity
        )
        
        # Add to FAISS index
        self.index.add(embeddings.astype('float32'))
        
        # Save index and metadata
        print(f"[VectorLayoutRAGEngine] Saving index to disk...")
        faiss.write_index(self.index, str(self.index_path))
        with open(self.metadata_path, 'wb') as f:
            pickle.dump(self.layouts_metadata, f)
        
        print(f"[VectorLayoutRAGEngine] [OK] Indexed {len(documents)} layouts in FAISS")
    
    def _create_document_text(self, layout: Dict[str, Any]) -> str:
        """
        Create rich document text for embedding
        Combines query, pattern, entity, and components for better semantic matching
        """
        components_str = ", ".join(layout.get("components", []))
        
        doc_text = f"""
        Query: {layout['query']}
        Pattern: {layout['pattern'].replace('_', ' ')}
        Entity: {layout['entity']}
        View Type: {layout['view_type']}
        Components: {components_str}
        """.strip()
        
        return doc_text
    
    def search(
        self,
        query: str,
        entity: Optional[str] = None,
        view_type: Optional[str] = None,
        top_k: int = 10,
        rerank: bool = True,
        final_k: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Search for relevant layouts with optional reranking
        
        Args:
            query: Natural language search query
            entity: Optional entity filter (e.g., "lead", "opportunity")
            view_type: Optional view type filter (e.g., "list", "dashboard")
            top_k: Number of initial results from vector search
            rerank: Whether to apply reranking
            final_k: Number of final results after reranking
            
        Returns:
            List of top matching layouts with scores
        """
        print(f"[VectorLayoutRAGEngine] Searching: '{query}' (no entity/view filters)")
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        
        # Search in FAISS (get more results for filtering)
        search_k = min(top_k * 5, len(self.layouts_metadata))  # Get 5x for filtering
        distances, indices = self.index.search(query_embedding.astype('float32'), search_k)
        
        # Filter and collect results (entity/view_type filtering disabled for broader results)
        candidate_layouts = []
        for i, (idx, distance) in enumerate(zip(indices[0], distances[0])):
            if idx == -1:  # FAISS returns -1 for empty results
                continue
            
            metadata = self.layouts_metadata[idx]
            
            # Skip entity and view_type filtering - use pure semantic similarity
            # This allows better matching based on query meaning rather than strict filters
            
            # FAISS inner product gives cosine similarity (since vectors are normalized)
            similarity_score = float(distance)
            
            candidate_layouts.append({
                "id": metadata["id"],
                "query": metadata["query"],
                "pattern": metadata["pattern"],
                "entity": metadata["entity"],
                "view_type": metadata["view_type"],
                "components": metadata["components"],
                "layout": metadata["layout"],
                "vector_score": similarity_score
            })
            
            # Stop if we have enough candidates
            if len(candidate_layouts) >= top_k:
                break
        
        if not candidate_layouts:
            print("[VectorLayoutRAGEngine] No results found")
            return []
        
        print(f"[VectorLayoutRAGEngine] Vector search found {len(candidate_layouts)} candidates")
        
        # Apply reranking if requested
        if rerank and len(candidate_layouts) > 0:
            candidate_layouts = self._rerank_results(query, candidate_layouts, final_k)
        else:
            candidate_layouts = candidate_layouts[:final_k]
        
        # Log results
        print(f"[VectorLayoutRAGEngine] Returning {len(candidate_layouts)} results:")
        for i, result in enumerate(candidate_layouts, 1):
            score_type = "rerank_score" if "rerank_score" in result else "vector_score"
            print(f"  {i}. {result['pattern']:20} ({score_type}: {result.get(score_type, 0):.3f}) - {result['query']}")
        
        return candidate_layouts
    
    def _rerank_results(
        self,
        query: str,
        candidates: List[Dict[str, Any]],
        top_k: int
    ) -> List[Dict[str, Any]]:
        """
        Rerank results using cross-encoder for better precision
        
        Args:
            query: User query
            candidates: Candidate results from vector search
            top_k: Number of top results to return
            
        Returns:
            Reranked results
        """
        print(f"[VectorLayoutRAGEngine] Reranking {len(candidates)} candidates...")
        
        # Prepare query-document pairs for reranking
        pairs = []
        for candidate in candidates:
            # Use candidate query as the document for comparison
            pairs.append([query, candidate['query']])
        
        # Get reranking scores
        rerank_scores = self.reranker.predict(pairs)
        
        # Add rerank scores to candidates
        for i, candidate in enumerate(candidates):
            candidate['rerank_score'] = float(rerank_scores[i])
            # Combine vector and rerank scores (weighted)
            candidate['final_score'] = (
                0.4 * candidate['vector_score'] + 
                0.6 * candidate['rerank_score']
            )
        
        # Sort by rerank score
        reranked = sorted(candidates, key=lambda x: x['rerank_score'], reverse=True)
        
        print(f"[VectorLayoutRAGEngine] [OK] Reranked to top {min(top_k, len(reranked))} results")
        
        return reranked[:top_k]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector index"""
        return {
            "total_documents": len(self.layouts_metadata),
            "index_name": self.index_name,
            "embedding_model": "all-MiniLM-L6-v2",
            "reranker_model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
            "embedding_dim": self.embedding_dim,
            "index_type": "FAISS IndexFlatIP (Inner Product)"
        }


if __name__ == "__main__":
    # Test the Vector RAG engine
    print("\n" + "="*80)
    print("TESTING VECTOR RAG ENGINE WITH RERANKING (FAISS)")
    print("="*80 + "\n")
    
    # Initialize engine
    engine = VectorLayoutRAGEngine()
    
    # Test cases
    test_cases = [
        {
            "name": "Test 1: Semantic search - synonyms",
            "query": "lead performance metrics",
            "entity": "lead",
            "view_type": None
        },
        {
            "name": "Test 2: Aggregation query",
            "query": "total revenue sum",
            "entity": "opportunity",
            "view_type": None
        },
        {
            "name": "Test 3: WHERE clause query",
            "query": "filter by status and priority",
            "entity": "lead",
            "view_type": None
        },
        {
            "name": "Test 4: Natural language",
            "query": "show me insights and recommendations",
            "entity": "account",
            "view_type": None
        },
        {
            "name": "Test 5: Pipeline analytics",
            "query": "sales funnel conversion rates",
            "entity": "opportunity",
            "view_type": None
        }
    ]
    
    for test in test_cases:
        print(f"\n{'='*80}")
        print(f"{test['name']}")
        print(f"Query: '{test['query']}'")
        print(f"{'='*80}")
        
        results = engine.search(
            query=test['query'],
            entity=test['entity'],
            view_type=test['view_type'],
            top_k=10,
            rerank=True,
            final_k=3
        )
        
        if results:
            print(f"\n[TOP RESULTS] {len(results)} results:")
            for i, r in enumerate(results, 1):
                print(f"\n{i}. Pattern: {r['pattern']}")
                print(f"   Entity: {r['entity']}")
                print(f"   Query: {r['query']}")
                print(f"   Vector Score: {r['vector_score']:.3f}")
                if 'rerank_score' in r:
                    print(f"   Rerank Score: {r['rerank_score']:.3f}")
                    print(f"   Final Score: {r['final_score']:.3f}")
                print(f"   Components: {', '.join(r['components'][:5])}...")
        else:
            print("\n❌ No results found")
    
    # Show stats
    print(f"\n{'='*80}")
    print("INDEX STATISTICS")
    print(f"{'='*80}")
    stats = engine.get_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
