"""
Pattern 15: Detailed Field View
Pattern with title and detailed field-by-field breakdown using list
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading, h3_heading
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder
from design_system_agent.core.dataset_genertor.component_badge.patterns import info_badge


class Pattern15:
    """
    Detailed Field View Pattern
    
    LLM Guidance:
    - Use when: Query asks for complete field details, all properties, or full record view
    - Data type: Single record with all available fields
    - Best for: Inspection view, debugging, complete record display
    - Keywords: "all fields", "complete details", "full record", "every property", "show everything"
    - Example queries: "Show all lead fields", "Display complete record", "Full details of case"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate detailed field view components
        
        Returns:
            List of components with all available fields
        """
        main_title = f"{object_type.title()} Complete Details"
        section1_title = "Basic Information"
        section2_title = "Additional Data"
        
        basic_items = [
            {"id": "1", "content": f"Name: {data.get('name', 'N/A')}"},
            {"id": "2", "content": f"Status: {data.get('status', 'N/A')}"},
            {"id": "3", "content": f"Priority: {data.get('priority', 'N/A')}"},
            {"id": "4", "content": f"Owner: {data.get('owner', 'N/A')}"},
        ]
        
        additional_items = [
            {"id": "5", "content": f"Email: {data.get('email', 'N/A')}"},
            {"id": "6", "content": f"Phone: {data.get('phone', 'N/A')}"},
            {"id": "7", "content": f"Created Date: {data.get('created_date', 'N/A')}"},
        ]
        
        badge = info_badge(f"Record ID: {idx}")
        
        return [
            h1_heading(main_title),
            badge,
            h3_heading(section1_title),
            ListBuilder().items(basic_items).build(),
            h3_heading(section2_title),
            ListBuilder().items(additional_items).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern15"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Badge", "List"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern15",
            "pattern_name": "Detailed Field View",
            "description": "Complete field breakdown with all available record properties",
            "use_when": {
                "user_intent": ["view all fields", "complete details", "full record", "every property", "inspection"],
                "query_complexity": "simple with verbose output",
                "data_requirement": "single record with all fields displayed"
            },
            "data_types": {
                "input_structure": "Single record with comprehensive field list",
                "required_fields": ["all available record fields"],
                "optional_fields": ["metadata fields", "system fields"],
                "data_volume": "1 record with 6+ fields displayed"
            },
            "query_patterns": {
                "keywords": ["all fields", "complete", "full record", "every property", "show everything", "detailed", "inspect"],
                "query_types": ["complete record view", "all fields display", "inspection view", "full details"],
                "example_queries": [
                    {"query": "show all lead fields", "object_type": "lead"},
                    {"query": "display complete record", "object_type": "account"},
                    {"query": "full details of case", "object_type": "case"},
                    {"query": "every property of contact", "object_type": "contact"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "none",
                "visual_density": "dense",
                "components_count": 6,
                "responsive_behavior": "vertical stacking of sections"
            }
        }

