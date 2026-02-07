"""
Default Layout Builder
Creates a simple default layout when no RAG matches are found.
Uses fixed JSON template: layout -> rows -> pattern_type + pattern_info
Data will be filled by LLM agents (DataFillingAgent)
"""
from typing import Dict, Any, Optional
from design_system_agent.agent.graph_nodes.layout_templates import (
    get_fallback_layout,
    validate_layout_structure
)


class DefaultLayoutBuilder:
    """
    Builds a default layout when no RAG matches are found.
    Uses fixed JSON templates following structure: layout -> rows -> pattern_type + pattern_info
    """
    
    def build_default_layout(
        self,
        query: str,
        data: Optional[Dict[str, Any]] = None,
        analysis: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Build fixed default layout using templates.
        Data will be filled by DataFillingAgent (LLM-based).
        
        Args:
            query: User's query
            data: Fetched data (optional)
            analysis: Query analysis (optional)
            
        Returns:
            Fixed JSON layout template (empty): layout -> rows -> pattern_type + pattern_info
        """
        # Detect object type
        obj_type = self._extract_object_type(data, analysis)
        
        # Get fixed template (empty, to be filled by LLM)
        layout = get_fallback_layout(obj_type)
        
        print(f"[DefaultLayoutBuilder] ✓ Using fixed template for object: '{obj_type}'")
        print(f"[DefaultLayoutBuilder] ✓ Structure: layout -> rows -> pattern_type + pattern_info")
        print(f"[DefaultLayoutBuilder] ℹ️  Data will be filled by DataFillingAgent (LLM)")
        
        # Validate structure
        if validate_layout_structure(layout):
            print(f"[DefaultLayoutBuilder] ✓ Layout structure validated")
        else:
            print(f"[DefaultLayoutBuilder] ⚠️  Validation failed, using emergency fallback")
            layout = get_fallback_layout("unknown")
        
        return layout
    
    def _extract_object_type(self, data: Optional[Dict], analysis: Optional[Dict]) -> str:
        """Extract object type from data or analysis"""
        if data and "_meta" in data:
            obj_type = data["_meta"].get("object_type", "data")
            if obj_type:
                return obj_type
        
        # Fallback: detect from keywords
        keywords = ["lead", "account", "opportunity", "case", "task", "contact", "loan", "policy"]
        if analysis and "intent" in analysis:
            intent_str = str(analysis["intent"]).lower()
            for keyword in keywords:
                if keyword in intent_str:
                    return keyword
        
        return "data"

