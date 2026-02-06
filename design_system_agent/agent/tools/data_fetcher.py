"""
Data Fetcher Tool
Single Responsibility: Fetch CRM data to populate layouts
"""
from typing import Dict, Optional, List
import json
from pathlib import Path


class DataFetcherTool:
    """
    Fetches sample CRM data for populating layouts.
    
    Responsibility:
    - Load sample data from JSON files
    - Match data to entity type(s)
    - Support multi-entity queries
    - Return data in standard format
    """
    
    def __init__(self):
        self.data_file = Path(__file__).parent.parent.parent / "dataset" / "crm_sample_data.json"
        self.sample_data = self._load_sample_data()
    
    def _load_sample_data(self) -> Dict:
        """Load sample CRM data"""
        try:
            if not self.data_file.exists():
                print(f"[DataFetcher] Warning: Sample data file not found at {self.data_file}")
                return {}
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[DataFetcher] Error loading sample data: {e}")
            return {}
    
    def fetch_data(
        self,
        entity_type: str,
        view_type: str = "detail",
        record_id: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Fetch data for a specific entity and view type.
        
        Args:
            entity_type: Entity type (lead, opportunity, account, contact, case, task)
            view_type: View type (detail, list, dashboard)
            record_id: Optional specific record ID
            
        Returns:
            Data dictionary or None if not found
        """
        # Build lookup key
        key = f"{entity_type}_{view_type}_example"
        
        data = self.sample_data.get(key)
        
        if data:
            print(f"[DataFetcher] Fetched data for {entity_type} {view_type}")
            return data
        else:
            print(f"[DataFetcher] No data found for {key}")
            return None
    
    def fetch_multi_entity_data(
        self,
        entities: List[str],
        view_type: str = "detail"
    ) -> Dict:
        """
        Fetch data for multiple entities.
        
        Args:
            entities: List of entity types to fetch
            view_type: View type for each entity
            
        Returns:
            Dictionary with entity data keyed by entity name
        """
        multi_data = {"_entities": entities}
        
        for entity in entities:
            entity_data = self.fetch_data(entity, view_type)
            if entity_data:
                multi_data[entity] = entity_data
        
        print(f"[DataFetcher] Fetched multi-entity data for: {', '.join(entities)}")
        return multi_data
    
    def detect_and_fetch(
        self,
        query: str,
        analysis: Optional[Dict] = None,
        rag_query: Optional[Dict] = None
    ) -> Dict:
        """
        Detect required entities from query/analysis and fetch data.
        
        Args:
            query: User query
            analysis: Query analysis result
            rag_query: RAG query with entity info
            
        Returns:
            Single or multi-entity data
        """
        # Detect entities from query
        detected_entities = self._detect_entities_from_query(query, analysis, rag_query)
        
        # Get view type
        view_type = "detail"
        if rag_query and "view_type" in rag_query:
            view_type = rag_query["view_type"]
        elif analysis and "intent" in analysis:
            intent = analysis["intent"].lower()
            if "list" in intent:
                view_type = "list"
        
        # Fetch data
        if len(detected_entities) == 1:
            # Single entity
            return self.fetch_data(detected_entities[0], view_type) or {}
        elif len(detected_entities) > 1:
            # Multi-entity
            return self.fetch_multi_entity_data(detected_entities, view_type)
        else:
            # No entities detected, use default
            entity = rag_query.get("entity", "lead") if rag_query else "lead"
            return self.fetch_data(entity, view_type) or {}
    
    def _detect_entities_from_query(
        self,
        query: str,
        analysis: Optional[Dict],
        rag_query: Optional[Dict]
    ) -> List[str]:
        """Detect which entities are mentioned in query"""
        entities = []
        query_lower = query.lower()
        
        # Check for entity keywords
        entity_keywords = {
            "account": ["account", "accounts", "company", "companies", "organization"],
            "case": ["case", "cases", "ticket", "tickets", "issue", "issues"],
            "lead": ["lead", "leads", "prospect", "prospects"],
            "task": ["task", "tasks", "todo", "activity", "activities"],
            "contact": ["contact", "contacts", "person", "people"],
            "opportunity": ["opportunity", "opportunities", "deal", "deals"]
        }
        
        for entity, keywords in entity_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                entities.append(entity)
        
        # If no entities found, use rag_query entity
        if not entities and rag_query and "entity" in rag_query:
            entities.append(rag_query["entity"])
        
        # Limit to 3 entities max
        return entities[:3] if entities else []
    
    def get_available_data(self) -> Dict:
        """Get list of available data examples"""
        return {
            "available_examples": list(self.sample_data.keys()),
            "total_count": len(self.sample_data)
        }
