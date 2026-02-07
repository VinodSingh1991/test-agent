"""
Pattern 4: Title + List
Pattern with heading and list
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder


class Pattern4:
    """
    Title + List Pattern
    
    LLM Guidance:
    - Use when: Query asks for field list without extra description
    - Data type: Record with multiple fields to display as list
    - Best for: Clean field listing with title
    - Keywords: "list fields", "show properties", "display attributes"
    - Example queries: "List lead fields", "Show account properties", "Display contact attributes"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title and list components
        
        Returns:
            List of components [heading, list]
        """
        title = f"{object_type.title()} Details"
        
        list_items = [
            {"id": "1", "content": f"Name: {data.get('name', 'Unknown')}"},
            {"id": "2", "content": f"Status: {data.get('status', 'N/A')}"},
            {"id": "3", "content": f"Priority: {data.get('priority', 'N/A')}"},
            {"id": "4", "content": f"Owner: {data.get('owner', 'N/A')}"},
        ]
        
        return [
            h2_heading(title),
            ListBuilder().items(list_items).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern4"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "List"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern4",
            "pattern_name": "Title + List",
            "description": "Heading with bulleted list of fields",
            "use_when": {
                "user_intent": ["list properties", "show fields", "display attributes", "enumerate values"],
                "query_complexity": "simple",
                "data_requirement": "single record with multiple fields for list display"
            },
            "data_types": {
                "input_structure": "Single record object",
                "required_fields": ["name", "3-6 key properties"],
                "optional_fields": ["additional attributes"],
                "data_volume": "1 record with 3-6 list items"
            },
            "query_patterns": {
                "keywords": ["list", "fields", "properties", "attributes", "show", "display"],
                "query_types": ["field enumeration", "property list", "attribute display"],
                "example_queries": [
                    {"query": "list lead fields", "object_type": "lead"},
                    {"query": "show account properties", "object_type": "account"},
                    {"query": "display contact attributes", "object_type": "contact"},
                    {"query": "enumerate case fields", "object_type": "case"}
                ]
            },
            "layout_characteristics": {
                "complexity": "low",
                "interactivity": "none",
                "visual_density": "medium",
                "components_count": 2,
                "responsive_behavior": "vertical stacking"
            }
        }

