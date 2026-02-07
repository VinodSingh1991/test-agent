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
            Path(__file__).parent.parent.parent / "dataset" / "crm_query_dataset.json",
            Path("dataset/crm_query_dataset.json"),
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
        
        for entry in layouts:
            # Create rich document text for embedding
            doc_text = self._create_document_text(entry)
            documents.append(doc_text)
            
            # Store metadata
            self.layouts_metadata.append({
                "query": entry["query"],
                "object_type": entry["object_type"],
                "layout_type": entry["layout_type"],
                "patterns_used": entry["patterns_used"],
                "layout": entry["layout"],
                "metadata": entry["metadata"]
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
    
    def _create_document_text(self, entry: Dict[str, Any]) -> str:
        """
        Create rich document text for embedding
        Combines query, object type, layout type, and patterns for better semantic matching
        """
        patterns_str = ", ".join(entry.get("patterns_used", []))
        
        # Extract component types from layout
        components = []
        for row in entry["layout"].get("rows", []):
            for component in row.get("pattern_info", []):
                comp_type = component.get("type", "")
                if comp_type and comp_type not in components:
                    components.append(comp_type)
        
        components_str = ", ".join(components)
        
        doc_text = f"""
        Query: {entry['query']}
        Object Type: {entry['object_type']}
        Layout Type: {entry['layout_type'].replace('_', ' ')}
        Patterns: {patterns_str}
        Components: {components_str}
        Rows: {entry['metadata'].get('num_rows', 0)}
        Total Components: {entry['metadata'].get('num_components', 0)}
        """.strip()
        
        return doc_text
    
    def search(
        self,
        query: str | List[str],
        top_k: int = 10,
        rerank: bool = True,
        final_k: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Search for relevant layouts with optional reranking
        
        Args:
            query: Natural language search query or list of query variations
            top_k: Number of initial results from vector search
            rerank: Whether to apply reranking
            final_k: Number of final results after reranking
            
        Returns:
            List of top matching layouts with scores
        """
        # Handle both single query and list of queries
        queries = [query] if isinstance(query, str) else query
        primary_queries = queries[:3]  # Use top 3 query variations
        print(f"[VectorLayoutRAGEngine] Searching with {len(primary_queries)} query variation(s)")
        
        # Search with each query variation and collect unique results
        all_candidates = {}  # Use dict to track unique layouts by index
        
        for i, q in enumerate(primary_queries, 1):
            print(f"  Query {i}: '{q}'")
            
            # Generate query embedding
            query_embedding = self.embedding_model.encode(
                [q],
                convert_to_numpy=True,
                normalize_embeddings=True
            )
            
            # Search in FAISS (get more results for filtering)
            search_k = min(top_k * 2, len(self.layouts_metadata))  # Get 2x for each query
            distances, indices = self.index.search(query_embedding.astype('float32'), search_k)
            
            # Collect results from this query
            for idx, distance in zip(indices[0], distances[0]):
                if idx == -1:  # FAISS returns -1 for empty results
                    continue
                
                similarity_score = float(distance)
                
                # Track best score for each unique layout
                if idx not in all_candidates or similarity_score > all_candidates[idx]['vector_score']:
                    metadata = self.layouts_metadata[idx]
                    all_candidates[idx] = {
                        "query": metadata["query"],
                        "object_type": metadata["object_type"],
                        "layout_type": metadata["layout_type"],
                        "patterns_used": metadata["patterns_used"],
                        "layout": metadata["layout"],
                        "metadata_info": metadata["metadata"],
                        "vector_score": similarity_score,
                        "matched_query": q  # Track which variation matched
                    }
        
        # Convert to list and sort by score
        candidate_layouts = sorted(
            all_candidates.values(),
            key=lambda x: x['vector_score'],
            reverse=True
        )[:top_k]
        
        if not candidate_layouts:
            print("[VectorLayoutRAGEngine] No results found")
            return []
        
        print(f"[VectorLayoutRAGEngine] Vector search found {len(candidate_layouts)} unique candidates")
        
        # Apply reranking if requested
        if rerank and len(candidate_layouts) > 0:
            candidate_layouts = self._rerank_results(primary_queries[0], candidate_layouts, final_k)
        else:
            candidate_layouts = candidate_layouts[:final_k]
        
        # Log results
        print(f"[VectorLayoutRAGEngine] Returning {len(candidate_layouts)} results:")
        for i, result in enumerate(candidate_layouts, 1):
            score_type = "rerank_score" if "rerank_score" in result else "vector_score"
            pattern = result['patterns_used'][0] if result.get('patterns_used') else 'unknown'
            print(f"  {i}. {pattern:20} ({score_type}: {result.get(score_type, 0):.3f}) - {result['query']}")
        
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
            "object_type": "lead",
            "layout_type": None
        },
        {
            "name": "Test 2: Aggregation query",
            "query": "total revenue sum",
            "object_type": "opportunity",
            "layout_type": None
        },
        {
            "name": "Test 3: WHERE clause query",
            "query": "filter by status and priority",
            "object_type": "lead",
            "layout_type": None
        },
        {
            "name": "Test 4: Natural language",
            "query": "show me insights and recommendations",
            "object_type": "account",
            "layout_type": None
        },
        {
            "name": "Test 5: Pipeline analytics",
            "query": "sales funnel conversion rates",
            "object_type": "opportunity",
            "layout_type": None
        }
    ]
    
    for test in test_cases:
        print(f"\n{'='*80}")
        print(f"{test['name']}")
        print(f"Query: '{test['query']}'")
        print(f"{'='*80}")
        
        results = engine.search(
            query=test['query'],
            top_k=10,
            rerank=True,
            final_k=3
        )
        
        if results:
            print(f"\n[TOP RESULTS] {len(results)} results:")
            for i, r in enumerate(results, 1):
                pattern = r['patterns_used'][0] if r.get('patterns_used') else 'unknown'
                print(f"\n{i}. Pattern: {pattern}")
                print(f"   Object Type: {r.get('object_type', 'N/A')}")
                print(f"   Layout Type: {r.get('layout_type', 'N/A')}")
                print(f"   Query: {r['query']}")
                print(f"   Vector Score: {r['vector_score']:.3f}")
                if 'rerank_score' in r:
                    print(f"   Rerank Score: {r['rerank_score']:.3f}")
                    print(f"   Final Score: {r['final_score']:.3f}")
        else:
            print("\n❌ No results found")
    
    # Show stats
    print(f"\n{'='*80}")
    print("INDEX STATISTICS")
    print(f"{'='*80}")
    stats = engine.get_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
