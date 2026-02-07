"""
Pattern 3: Description Only
Simplest pattern with just description text
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder


class Pattern3:
    """
    Description Only Pattern
    
    LLM Guidance:
    - Use when: Query needs minimal text response or simple message
    - Data type: Very basic info, status message, or single text field
    - Best for: Simple confirmations, single-line summaries
    - Keywords: "what is", "show status", "tell me", "brief info"
    - Example queries: "What is the lead status?", "Show brief info", "Tell me about this case"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate description component
        
        Returns:
            List with single description component
        """
        desc_text = f"Showing details for {object_type}: {data.get('name', 'Unknown')}"
        
        return [
            DescriptionBuilder(desc_text).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern3"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Description"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern3",
            "pattern_name": "Description Only",
            "description": "Minimal text-only response pattern",
            "use_when": {
                "user_intent": ["get brief answer", "simple confirmation", "status check", "minimal response"],
                "query_complexity": "very simple",
                "data_requirement": "single text value, confirmation, or simple message"
            },
            "data_types": {
                "input_structure": "Single text value or simple message",
                "required_fields": ["text content"],
                "optional_fields": [],
                "data_volume": "1 text field only"
            },
            "query_patterns": {
                "keywords": ["what is", "status", "tell me", "brief", "summary", "explain"],
                "query_types": ["simple question", "status check", "single field query", "confirmation"],
                "example_queries": [
                    {"query": "what is the lead status", "object_type": "lead"},
                    {"query": "tell me about this case", "object_type": "case"},
                    {"query": "brief summary", "object_type": "account"},
                    {"query": "show status message", "object_type": "opportunity"}
                ]
            },
            "layout_characteristics": {
                "complexity": "minimal",
                "interactivity": "none",
                "visual_density": "very sparse",
                "components_count": 1,
                "responsive_behavior": "single text block"
            }
        }

