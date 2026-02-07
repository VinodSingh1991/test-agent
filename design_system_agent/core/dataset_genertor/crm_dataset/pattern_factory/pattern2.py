"""
Pattern 2: Title + Description + List
Pattern with heading, description, and list of details
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder


class Pattern2:
    """
    Title + Description + List Pattern
    
    LLM Guidance:
    - Use when: Query needs detailed breakdown with itemized information
    - Data type: Single record with multiple fields to display as list items
    - Best for: Detailed view with structured field list
    - Keywords: "detailed view", "show all fields", "complete info", "full details"
    - Example queries: "Show complete lead details", "Display all case information", "Full account view"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title, description, and list components
        
        Returns:
            List of components [heading, description, list]
        """
        title = f"{object_type.title()}: {data.get('name', 'Unknown')}"
        desc_text = f"Detailed information for {object_type} record"
        
        list_items = [
            {"id": "1", "content": f"Status: {data.get('status', 'N/A')}"},
            {"id": "2", "content": f"Priority: {data.get('priority', 'N/A')}"},
            {"id": "3", "content": f"Owner: {data.get('owner', 'N/A')}"},
            {"id": "4", "content": f"Created: {data.get('created_date', 'N/A')}"},
        ]
        
        return [
            h1_heading(title),
            DescriptionBuilder(desc_text).build(),
            ListBuilder().items(list_items).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern2"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Description", "List"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return comprehensive LLM guidance for pattern selection"""
        return {
            "pattern_id": "pattern2",
            "pattern_name": "Title + Description + List",
            "description": "Detailed pattern with heading, description, and itemized list of fields",
            "use_when": {
                "user_intent": ["view detailed info", "see all fields", "complete breakdown"],
                "query_complexity": "moderate",
                "data_requirement": "moderate - multiple fields to display"
            },
            "data_types": {
                "input_structure": "Single record object with multiple attributes",
                "required_fields": ["name", "status", "priority", "owner", "created_date"],
                "optional_fields": ["modified_date", "description", "notes", "tags"],
                "data_volume": "1 record with 4+ fields"
            },
            "best_for": [
                "Complete record view",
                "Field-by-field breakdown",
                "Structured data display",
                "Audit trail viewing"
            ],
            "query_patterns": {
                "keywords": ["detailed", "complete", "full", "all fields", "breakdown", "comprehensive"],
                "query_types": ["detailed_view", "complete_info", "field_listing"],
                "example_queries": [
                    {"query": "show complete lead details", "object_type": "lead"},
                    {"query": "display all case information", "object_type": "case"},
                    {"query": "full account view", "object_type": "account"},
                    {"query": "detailed contact breakdown", "object_type": "contact"}
                ]
            },
            "components": ["Heading", "Description", "List"],
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "low",
                "visual_density": "medium"
            },
            "use_when": "Query needs detailed breakdown with itemized information",
            "data_type": "Single record with multiple fields to display as list items",
            "best_for": "Detailed view with structured field list",
            "keywords": ["detailed view", "show all fields", "complete info", "full details"],
            "example_queries": [
                "Show complete lead details",
                "Display all case information",
                "Full account view"
            ]
        }
