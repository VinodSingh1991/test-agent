"""
Pattern 13: List with Cards
Pattern with list of items followed by related cards
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder
from design_system_agent.core.dataset_genertor.component_card.card_builder import CardBuilder


class Pattern13:
    """
    List with Cards Pattern
    
    LLM Guidance:
    - Use when: Query asks for activity list with detailed card view
    - Data type: List of items + detailed card for highlighted item
    - Best for: Activity feeds, timeline with detail, recent items with focus
    - Keywords: "recent activity", "timeline with details", "activity list", "recent with card"
    - Example queries: "Show recent activities", "Display timeline with details", "Recent leads with info"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate heading, list, and card components
        
        Returns:
            List of components [heading, list, card]
        """
        title = f"Recent {object_type.title()} Activity"
        
        list_items = [
            {"id": "1", "content": f"Created: {data.get('name', 'Unknown')}"},
            {"id": "2", "content": f"Status changed to: {data.get('status', 'N/A')}"},
            {"id": "3", "content": f"Priority set to: {data.get('priority', 'N/A')}"},
            {"id": "4", "content": f"Assigned to: {data.get('owner', 'N/A')}"},
        ]
        
        card_content = [
            f"Current Status: {data.get('status', 'N/A')}",
            f"Priority Level: {data.get('priority', 'N/A')}"
        ]
        
        card = CardBuilder("Highlighted Item") \
            .title(data.get('name', 'Unknown')) \
            .content(card_content) \
            .footer(f"Last Updated: {data.get('created_date', 'N/A')}") \
            .elevated() \
            .build()
        
        return [
            h2_heading(title),
            ListBuilder().items(list_items).build(),
            card
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern13"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "List", "Card"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern13",
            "pattern_name": "List with Cards",
            "description": "Activity list with detailed card view for highlighted item",
            "use_when": {
                "user_intent": ["view recent activity", "see timeline", "activity feed", "list with details"],
                "query_complexity": "medium",
                "data_requirement": "activity/event list plus detailed card for one item"
            },
            "data_types": {
                "input_structure": "Activity list with focus item details",
                "required_fields": ["activity events list", "highlighted item details"],
                "optional_fields": ["timestamps", "metadata"],
                "data_volume": "activity list (3-5 items) + 1 detailed card"
            },
            "query_patterns": {
                "keywords": ["recent activity", "timeline", "activity list", "history", "events", "recent with card"],
                "query_types": ["activity feed", "timeline view", "event list", "recent items with focus"],
                "example_queries": [
                    {"query": "show recent activities", "object_type": "lead"},
                    {"query": "display timeline with details", "object_type": "case"},
                    {"query": "recent leads with info", "object_type": "lead"},
                    {"query": "activity feed for account", "object_type": "account"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "potential card expansion",
                "visual_density": "medium-dense",
                "components_count": 3,
                "responsive_behavior": "vertical flow maintained"
            }
        }

