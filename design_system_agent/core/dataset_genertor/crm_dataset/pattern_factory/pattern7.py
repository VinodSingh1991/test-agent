"""
Pattern 7: Dashlet 4 Columns
Pattern with 4 dashlets in a row
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_dashlet.dashlet_builder import DashletBuilder


class Pattern7:
    """
    Dashlet 4 Columns Pattern
    
    LLM Guidance:
    - Use when: Query asks for comprehensive dashboard with multiple metrics
    - Data type: 4 different aggregate metrics (Total, Active, Completed, Pending)
    - Best for: Full-width analytics dashboard with detailed KPIs
    - Keywords: "full dashboard", "complete metrics", "all statistics", "analytics view"
    - Example queries: "Show complete dashboard", "Display all metrics", "Full analytics view"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate 4 dashlet components
        
        Returns:
            List of 4 dashlet components
        """
        total_count = data.get(f'total_{object_type}s', data.get('total_leads', 150))
        active_count = data.get(f'active_{object_type}s', data.get('active_leads', 89))
        completed_count = data.get('converted_leads', data.get('resolved_cases', 45))
        pending_count = data.get('open_cases', 15)
        
        dashlet1 = DashletBuilder(f"Total {object_type.title()}s") \
            .with_description(str(total_count)) \
            .default() \
            .build()
        
        dashlet2 = DashletBuilder("Active") \
            .with_description(str(active_count)) \
            .accent() \
            .build()
        
        dashlet3 = DashletBuilder("Completed") \
            .with_description(str(completed_count)) \
            .primary() \
            .build()
        
        dashlet4 = DashletBuilder("Pending") \
            .with_description(str(pending_count)) \
            .outlined() \
            .build()
        
        return [dashlet1, dashlet2, dashlet3, dashlet4]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern7"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Dashlet"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern7",
            "pattern_name": "Dashlet 4 Columns",
            "description": "Full-width dashboard with 4 metric cards",
            "use_when": {
                "user_intent": ["complete dashboard", "full metrics", "all KPIs", "comprehensive analytics"],
                "query_complexity": "medium",
                "data_requirement": "4 different aggregate metrics (Total, Active, Completed, Pending)"
            },
            "data_types": {
                "input_structure": "Aggregated data with 4 distinct metric values",
                "required_fields": ["total count", "active count", "completed count", "pending/other count"],
                "optional_fields": ["trend indicators", "comparison values"],
                "data_volume": "4 metrics (aggregate values)"
            },
            "query_patterns": {
                "keywords": ["complete dashboard", "full metrics", "all statistics", "analytics", "comprehensive", "4 metrics"],
                "query_types": ["full dashboard", "comprehensive metrics", "complete analytics", "all KPIs"],
                "example_queries": [
                    {"query": "show complete dashboard", "object_type": "lead"},
                    {"query": "display all metrics", "object_type": "case"},
                    {"query": "full analytics view", "object_type": "opportunity"},
                    {"query": "comprehensive KPI dashboard", "object_type": "account"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "none",
                "visual_density": "medium",
                "components_count": 4,
                "responsive_behavior": "4-column grid to 2x2 to stacked"
            }
        }

