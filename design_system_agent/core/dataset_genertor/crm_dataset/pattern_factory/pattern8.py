"""
Pattern 8: Title + Badges + Description
Pattern with heading, status badges, and description
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_badge.patterns import success_badge, warning_badge, info_badge, danger_badge


class Pattern8:
    """
    Title + Badges + Description Pattern
    
    LLM Guidance:
    - Use when: Query asks for status view with visual indicators
    - Data type: Record with status/priority fields that need badge representation
    - Best for: Status-focused views with color-coded indicators
    - Keywords: "show status", "display priority", "status view", "with badges"
    - Example queries: "Show lead status", "Display case priority", "Account status view"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title, badges, and description components
        
        Returns:
            List of components [heading, badges, description]
        """
        title = f"{object_type.title()} Status View"
        desc_text = f"Current information for {data.get('name', 'Unknown')}"
        
        # Create badges based on data
        status_badge = success_badge(data.get('status', 'Unknown'))
        priority_map = {"High": danger_badge, "Medium": warning_badge, "Low": info_badge}
        priority_fn = priority_map.get(data.get('priority', 'Medium'), info_badge)
        priority_badge = priority_fn(data.get('priority', 'Medium'))
        
        return [
            h2_heading(title),
            status_badge,
            priority_badge,
            DescriptionBuilder(desc_text).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern8"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Badge", "Description"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern8",
            "pattern_name": "Title + Badges + Description",
            "description": "Status-focused view with color-coded badge indicators",
            "use_when": {
                "user_intent": ["check status", "view priority", "see badges", "visual indicators"],
                "query_complexity": "simple",
                "data_requirement": "record with status/priority fields needing visual emphasis"
            },
            "data_types": {
                "input_structure": "Single record with status-type fields",
                "required_fields": ["name", "status", "priority or category"],
                "optional_fields": ["additional badge fields"],
                "data_volume": "1 record with 2-3 badge indicators"
            },
            "query_patterns": {
                "keywords": ["status", "priority", "badges", "view with indicators", "color coded"],
                "query_types": ["status check", "priority view", "badge display", "visual status"],
                "example_queries": [
                    {"query": "show lead status", "object_type": "lead"},
                    {"query": "display case priority", "object_type": "case"},
                    {"query": "account status view", "object_type": "account"},
                    {"query": "priority with badges", "object_type": "opportunity"}
                ]
            },
            "layout_characteristics": {
                "complexity": "low",
                "interactivity": "none",
                "visual_density": "sparse",
                "components_count": 4,
                "responsive_behavior": "vertical stacking"
            }
        }

