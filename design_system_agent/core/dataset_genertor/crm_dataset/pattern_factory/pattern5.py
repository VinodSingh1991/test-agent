"""
Pattern 5: Title + Description + List + Card
Pattern with heading, description, list, and card
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder
from design_system_agent.core.dataset_genertor.component_card.card_builder import CardBuilder


class Pattern5:
    """
    Title + Description + List + Card Pattern
    
    LLM Guidance:
    - Use when: Query needs rich detailed view with card-based information
    - Data type: Record with main fields (list) + additional details (card)
    - Best for: Comprehensive view mixing list and card layouts
    - Keywords: "complete view", "detailed overview", "full information with card"
    - Example queries: "Show complete customer view", "Display detailed account info", "Full lead overview with card"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title, description, list, and card components
        
        Returns:
            List of components [heading, description, list, card]
        """
        title = f"{object_type.title()} Overview"
        desc_text = f"Comprehensive view of {data.get('name', 'Unknown')}"
        
        list_items = [
            {"id": "1", "content": f"Status: {data.get('status', 'N/A')}"},
            {"id": "2", "content": f"Priority: {data.get('priority', 'N/A')}"},
        ]
        
        card_content = [
            f"Owner: {data.get('owner', 'N/A')}",
            f"Email: {data.get('email', 'N/A')}"
        ]
        
        card = CardBuilder(data.get('name', 'Unknown')) \
            .title(f"{object_type.title()} Card") \
            .content(card_content) \
            .footer(f"Created: {data.get('created_date', 'N/A')}") \
            .elevated() \
            .build()
        
        return [
            h2_heading(title),
            DescriptionBuilder(desc_text).build(),
            ListBuilder().items(list_items).build(),
            card
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern5"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Description", "List", "Card"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern5",
            "pattern_name": "Title + Description + List + Card",
            "description": "Rich detailed view combining list and card layouts",
            "use_when": {
                "user_intent": ["comprehensive view", "complete details", "full information", "detailed overview"],
                "query_complexity": "medium to high",
                "data_requirement": "record with both list-worthy fields and card-worthy details"
            },
            "data_types": {
                "input_structure": "Single record with multiple sections",
                "required_fields": ["name", "key fields for list", "additional details for card"],
                "optional_fields": ["footer metadata", "created/updated dates"],
                "data_volume": "1 record with 4+ components"
            },
            "query_patterns": {
                "keywords": ["complete", "full", "detailed", "comprehensive", "overview", "all info", "card"],
                "query_types": ["comprehensive view", "detailed display", "full record view", "rich information"],
                "example_queries": [
                    {"query": "show complete customer view", "object_type": "contact"},
                    {"query": "display detailed account info", "object_type": "account"},
                    {"query": "full lead overview with card", "object_type": "lead"},
                    {"query": "comprehensive case details", "object_type": "case"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium-high",
                "interactivity": "potential card interactions",
                "visual_density": "dense",
                "components_count": 4,
                "responsive_behavior": "card stacking on mobile"
            }
        }

