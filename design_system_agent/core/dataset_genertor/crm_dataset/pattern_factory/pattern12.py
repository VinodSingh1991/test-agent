"""
Pattern 12: Alert + Title + Description
Pattern with alert message, heading, and description
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_alert.alert_builder import AlertBuilder


class Pattern12:
    """
    Alert + Title + Description Pattern
    
    LLM Guidance:
    - Use when: Query needs attention/warning about important information
    - Data type: Critical information, warnings, important notices
    - Best for: Highlighting urgent or important records
    - Keywords: "urgent", "important", "alert", "warning", "attention needed"
    - Example queries: "Show urgent cases", "Display important leads", "Alert for overdue tasks"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate alert, title, and description components
        
        Returns:
            List of components [alert, heading, description]
        """
        # Determine alert type based on priority
        alert_map = {
            "High": ("error", "High Priority Item Requires Attention"),
            "Medium": ("warning", "Medium Priority Item"),
            "Low": ("info", "Low Priority Item")
        }
        alert_type, alert_msg = alert_map.get(data.get('priority', 'Medium'), ("info", "Item Information"))
        
        alert = AlertBuilder(alert_msg).variant(alert_type).build()
        title = f"{object_type.title()}: {data.get('name', 'Unknown')}"
        desc_text = f"Status: {data.get('status', 'N/A')} | Owner: {data.get('owner', 'N/A')}"
        
        return [
            alert,
            h2_heading(title),
            DescriptionBuilder(desc_text).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern12"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Alert", "Heading", "Description"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern12",
            "pattern_name": "Alert + Title + Description",
            "description": "Attention-grabbing layout with alert message banner",
            "use_when": {
                "user_intent": ["urgent info", "important notice", "warning", "critical alert"],
                "query_complexity": "simple to medium",
                "data_requirement": "record with priority/urgency requiring visual attention"
            },
            "data_types": {
                "input_structure": "Single record with urgency indicator",
                "required_fields": ["name", "priority/urgency level", "status"],
                "optional_fields": ["owner", "due date"],
                "data_volume": "1 record with alert context"
            },
            "query_patterns": {
                "keywords": ["urgent", "important", "alert", "warning", "critical", "attention", "priority"],
                "query_types": ["urgent display", "important notice", "alert view", "critical information"],
                "example_queries": [
                    {"query": "show urgent cases", "object_type": "case"},
                    {"query": "display important leads", "object_type": "lead"},
                    {"query": "alert for overdue tasks", "object_type": "task"},
                    {"query": "critical opportunities", "object_type": "opportunity"}
                ]
            },
            "layout_characteristics": {
                "complexity": "low-medium",
                "interactivity": "alert dismissal possible",
                "visual_density": "sparse",
                "components_count": 3,
                "responsive_behavior": "vertical stacking"
            }
        }

