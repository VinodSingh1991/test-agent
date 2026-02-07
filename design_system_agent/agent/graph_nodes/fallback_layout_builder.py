"""
Fallback Layout Builder
Creates generic layouts when no good match found
Uses fixed JSON templates for consistency
Data will be filled by LLM agents (DataFillingAgent)
"""
from typing import Dict, List, Any, Optional
from design_system_agent.agent.graph_nodes.layout_templates import (
    get_fallback_layout,
    validate_layout_structure
)


class FallbackLayoutBuilder:
    """
    Builds fallback layouts when no suitable layout found.
    Uses fixed JSON templates following structure: layout -> rows -> pattern_type + pattern_info
    """
    
    def build_fallback_layout(
        self,
        query: str,
        data: Dict[str, Any],
        analysis: Optional[Dict] = None
    ) -> Dict:
        """
        Build fallback layout using fixed JSON templates.
        
        Args:
            query: User query
            data: Fetched data (should be dict)
            analysis: Query analysis
            
        Returns:
            Fixed JSON layout following structure: layout -> rows -> pattern_type + pattern_info
        """
        # Ensure data is a dict
        if not isinstance(data, dict):
            print(f"[FallbackLayoutBuilder] ⚠️  Data is not a dict (type: {type(data).__name__}), converting to empty dict")
            data = {}
        
        # Detect object type from multiple sources
        object_type = self._detect_object_type(query, data, analysis)
        
        # Get fixed template for object type
        layout = get_fallback_layout(object_type)
        
        print(f"[FallbackLayoutBuilder] ✓ Using fixed JSON template for object: '{object_type}'")
        print(f"[FallbackLayoutBuilder] ✓ Structure: layout -> rows -> pattern_type + pattern_info")
        
        # Validate structure
        if validate_layout_structure(layout):
            print(f"[FallbackLayoutBuilder] ✓ Layout structure validated successfully")
        else:
            print(f"[FallbackLayoutBuilder] ⚠️  Layout structure validation failed, using emergency fallback")
            layout = get_fallback_layout("unknown")
        
        print(f"[FallbackLayoutBuilder] ℹ️  Returning empty template - data will be filled by DataFillingAgent (LLM)")
        return layout
    
    def _detect_object_type(self, query: str, data: Dict, analysis: Optional[Dict]) -> str:
        """
        Detect single object type from query, data, or analysis.
        
        Priority order:
        1. analysis.objects or analysis.object_type
        2. Data keys (_objects, object_type, etc.)
        3. Query keywords (lead, case, account, etc.)
        
        Returns:
            Single object type string (lead, case, account, etc.) or "unknown"
        """
        # Priority 1: Check analysis
        if analysis:
            # Check objects field (list)
            objects = analysis.get("objects", [])
            if isinstance(objects, list) and objects:
                obj_type = objects[0]
                print(f"[FallbackLayoutBuilder] Object type from analysis.objects: {obj_type}")
                return obj_type
            
            # Check object_type field (string)
            obj_type = analysis.get("object_type")
            if obj_type and obj_type != "unknown":
                print(f"[FallbackLayoutBuilder] Object type from analysis.object_type: {obj_type}")
                return obj_type
        
        # Priority 2: Check data for object keys
        objects = self._detect_objects_from_data(data)
        if objects and objects != ["unknown"]:
            obj_type = objects[0]
            print(f"[FallbackLayoutBuilder] Object type from data keys: {obj_type}")
            return obj_type
        
        # Priority 3: Detect from query keywords
        obj_type = self._detect_object_from_query(query)
        if obj_type != "unknown":
            print(f"[FallbackLayoutBuilder] Object type from query keywords: {obj_type}")
            return obj_type
        
        print(f"[FallbackLayoutBuilder] ⚠️  Could not detect object type, using 'unknown' template")
        return "unknown"
    
    def _detect_object_from_query(self, query: str) -> str:
        """Detect single object from query keywords (returns first match)"""
        query_lower = query.lower()
        object_keywords = {
            "lead": ["lead", "leads"],
            "case": ["case", "cases", "ticket", "tickets"],
            "account": ["account", "accounts", "customer", "customers"],
            "contact": ["contact", "contacts"],
            "opportunity": ["opportunity", "opportunities", "deal", "deals"],
            "task": ["task", "tasks"],
            "loan": ["loan", "loans"],
            "policy": ["policy", "policies"]
        }
        
        for obj_type, keywords in object_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                return obj_type
        
        return "unknown"
    
    def _detect_objects_from_data(self, data: Dict) -> List[str]:
        """Detect objects in data (helper for _detect_object_type)"""
        # Ensure data is a dict
        if not isinstance(data, dict) or not data:
            return ["unknown"]
        
        # Check _objects metadata
        if "_objects" in data:
            return data["_objects"]
        
        # Check for object keys
        object_keys = ["lead", "case", "account", "contact", "opportunity", "task", "loan", "policy"]
        objects = []
        
        for key in object_keys:
            if key in data or f"{key}_data" in data:
                objects.append(key)
        
        # Check _meta.object_type
        if not objects and "_meta" in data:
            object_type = data["_meta"].get("object_type")
            if object_type and object_type != "unknown":
                objects.append(object_type)
        
        return objects if objects else ["unknown"]
