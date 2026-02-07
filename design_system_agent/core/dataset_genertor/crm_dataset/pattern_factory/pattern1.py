"""
Pattern 1: Title + Description
Simple pattern with heading and description text
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder


class Pattern1:
    """
    Title + Description Pattern
    
    LLM Guidance:
    - Use when: Query asks for simple info, basic details, or summary view
    - Data type: Single record with key fields (name, status, priority, owner)
    - Best for: Quick overview without detailed breakdown
    - Keywords: "show details", "get info", "summary", "overview"
    - Example queries: "Show customer info", "Get lead details", "Display case summary"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title and description components
        
        Returns:
            List of components [heading, description]
        """
        title = f"{object_type.title()}: {data.get('name', 'Unknown')}"
        desc_text = f"Status: {data.get('status', 'N/A')} | Priority: {data.get('priority', 'N/A')} | Owner: {data.get('owner', 'N/A')}"
        
        return [
            h1_heading(title),
            DescriptionBuilder(desc_text).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern1"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Description"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return comprehensive LLM guidance for pattern selection"""
        return {
            "pattern_id": "pattern1",
            "pattern_name": "Title + Description",
            "description": "Simple pattern displaying a heading with descriptive text below",
            "use_when": {
                "user_intent": ["view basic info", "quick summary", "simple overview"],
                "query_complexity": "simple",
                "data_requirement": "minimal - just key fields"
            },
            "data_types": {
                "input_structure": "Single record object",
                "required_fields": ["name", "status", "priority", "owner"],
                "optional_fields": ["description", "notes"],
                "data_volume": "1 record"
            },
            "best_for": [
                "Quick status check",
                "Single record summary",
                "Minimal information display",
                "Overview without drill-down"
            ],
            "query_patterns": {
                "keywords": ["show", "get", "display", "view", "info", "details", "summary"],
                "query_types": ["informational", "retrieval", "simple_view"],
                "example_queries": [
                    {"query": "show my lead", "object_type": "lead"},
                    {"query": "get case info", "object_type": "case"},
                    {"query": "display account details", "object_type": "account"},
                    {"query": "view contact summary", "object_type": "contact"}
                ]
            },
            "components": ["Heading", "Description"],
            "layout_characteristics": {
                "complexity": "low",
                "interactivity": "none",
                "visual_density": "sparse"
            }
        }
