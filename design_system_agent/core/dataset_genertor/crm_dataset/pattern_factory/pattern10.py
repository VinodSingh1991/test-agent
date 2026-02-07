"""
Pattern 10: Card Grid (2 Cards)
Pattern with 2 cards side by side
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_card.card_builder import CardBuilder


class Pattern10:
    """
    Card Grid (2 Cards) Pattern
    
    LLM Guidance:
    - Use when: Query asks for comparison view or side-by-side information
    - Data type: Two related entities or aspects to compare
    - Best for: Before/after, comparison, related items display
    - Keywords: "compare", "side by side", "two cards", "dual view"
    - Example queries: "Compare leads", "Show related accounts", "Side by side view"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate 2 card components
        
        Returns:
            List of 2 card components
        """
        card1_content = [
            f"Status: {data.get('status', 'N/A')}",
            f"Priority: {data.get('priority', 'N/A')}",
            f"Owner: {data.get('owner', 'N/A')}"
        ]
        
        card1 = CardBuilder(f"{data.get('name', 'Unknown')} - Details") \
            .title("Primary Information") \
            .content(card1_content) \
            .elevated() \
            .build()
        
        card2_content = [
            f"Email: {data.get('email', 'N/A')}",
            f"Phone: {data.get('phone', 'N/A')}"
        ]
        
        card2 = CardBuilder(f"{data.get('name', 'Unknown')} - Contact") \
            .title("Contact Information") \
            .content(card2_content) \
            .footer(f"Created: {data.get('created_date', 'N/A')}") \
            .elevated() \
            .build()
        
        return [card1, card2]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern10"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Card"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern10",
            "pattern_name": "Card Grid (2 Cards)",
            "description": "Side-by-side card layout for comparison or related items",
            "use_when": {
                "user_intent": ["compare", "side by side view", "related items", "dual display"],
                "query_complexity": "medium",
                "data_requirement": "two related entities, aspects, or sections to display"
            },
            "data_types": {
                "input_structure": "Single record with divisible information or 2 related records",
                "required_fields": ["primary info for card 1", "secondary info for card 2"],
                "optional_fields": ["card footers", "metadata"],
                "data_volume": "2 cards worth of information"
            },
            "query_patterns": {
                "keywords": ["compare", "side by side", "two cards", "dual view", "related", "both"],
                "query_types": ["comparison view", "related items", "dual display", "side-by-side"],
                "example_queries": [
                    {"query": "compare leads", "object_type": "lead"},
                    {"query": "show related accounts", "object_type": "account"},
                    {"query": "side by side view", "object_type": "contact"},
                    {"query": "display both sections", "object_type": "case"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "potential card interactions",
                "visual_density": "medium-dense",
                "components_count": 2,
                "responsive_behavior": "side-by-side to stacked"
            }
        }

