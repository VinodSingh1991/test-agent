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
        object_type: str,
        layout_type: str = "detail",
        record_id: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Fetch data for a specific object and layout type.
        
        Args:
            object_type: Object type (lead, opportunity, account, contact, case, task)
            layout_type: Layout type (detail, list, dashboard)
            record_id: Optional specific record ID
            
        Returns:
            Data dictionary or None if not found
        """
        # Build lookup key - map to old format for compatibility
        key = f"{object_type}_{layout_type}_example"
        
        data = self.sample_data.get(key)
        
        if data:
            print(f"[DataFetcher] Fetched data for {object_type} {layout_type}")
            return data
        else:
            print(f"[DataFetcher] No data found for {key}")
            return None
    
    def fetch_multi_entity_data(
        self,
        objects: List[str],
        layout_type: str = "detail"
    ) -> Dict:
        """
        Fetch data for multiple objects.
        
        Args:
            objects: List of object types to fetch
            layout_type: Layout type for each object
            
        Returns:
            Dictionary with object data keyed by object name
        """
        multi_data = {"_objects": objects}
        
        for obj in objects:
            obj_data = self.fetch_data(obj, layout_type)
            if obj_data:
                multi_data[obj] = obj_data
        
        print(f"[DataFetcher] Fetched multi-object data for: {', '.join(objects)}")
        return multi_data
    
    def detect_and_fetch(
        self,
        query: str,
        analysis: Optional[Dict] = None,
        rag_query: Optional[Dict] = None
    ) -> Dict:
        """
        Detect required objects from query/analysis and fetch data.
        
        Args:
            query: User query
            analysis: Query analysis result
            rag_query: RAG query with object info
            
        Returns:
            Single or multi-object data
        """
        # Detect objects from query
        detected_objects = self._detect_objects_from_query(query, analysis, rag_query)
        
        # Get layout type
        layout_type = "detail"
        if rag_query and "layout_type" in rag_query:
            layout_type = rag_query["layout_type"]
        elif analysis and "intent" in analysis:
            intent = analysis["intent"].lower()
            if "list" in intent:
                layout_type = "list"
        
        # Fetch data
        if len(detected_objects) == 1:
            # Single object
            return self.fetch_data(detected_objects[0], layout_type) or {}
        elif len(detected_objects) > 1:
            # Multi-object
            return self.fetch_multi_entity_data(detected_objects, layout_type)
        else:
            # No objects detected, use default
            obj_type = rag_query.get("object_type", "lead") if rag_query else "lead"
            return self.fetch_data(obj_type, layout_type) or {}
    
    def _detect_objects_from_query(
        self,
        query: str,
        analysis: Optional[Dict],
        rag_query: Optional[Dict]
    ) -> List[str]:
        """Detect which objects are mentioned in query"""
        objects = []
        query_lower = query.lower()
        
        # Check for object keywords
        object_keywords = {
            "account": ["account", "accounts", "company", "companies", "organization"],
            "case": ["case", "cases", "ticket", "tickets", "issue", "issues"],
            "lead": ["lead", "leads", "prospect", "prospects"],
            "task": ["task", "tasks", "todo", "activity", "activities"],
            "contact": ["contact", "contacts", "person", "people"],
            "opportunity": ["opportunity", "opportunities", "deal", "deals"]
        }
        
        for obj_type, keywords in object_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                objects.append(obj_type)
        
        # If no objects found, use rag_query object_type
        if not objects and rag_query and "object_type" in rag_query:
            objects.append(rag_query["object_type"])
        
        # Limit to 3 objects max
        return objects[:3] if objects else []
    
    def get_available_data(self) -> Dict:
        """Get list of available data examples"""
        return {
            "available_examples": list(self.sample_data.keys()),
            "total_count": len(self.sample_data)
        }
