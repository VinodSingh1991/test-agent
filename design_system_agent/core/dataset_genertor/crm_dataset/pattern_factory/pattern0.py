"""
Pattern 0: Dashlet 3 Columns
Pattern with 3 dashlets in a row
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_dashlet.dashlet_builder import DashletBuilder


class Pattern0:
    """
    Dashlet 3 Columns Pattern
    
    LLM Guidance:
    - Use when: Query asks for "dashboard", "overview", "metrics", "summary stats"
    - Data type: Aggregate counts, totals, statistics (Total, Active, Priority counts)
    - Best for: High-level KPI display with 3 key metrics
    - Keywords: "show metrics", "display stats", "overview dashboard", "key numbers"
    - Example queries: "Show lead metrics", "Display case statistics", "Account overview"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate 3 dashlet components
        
        Returns:
            List of 3 dashlet components
        """
        total_count = data.get(f'total_{object_type}s', data.get('total_leads', 150))
        active_count = data.get(f'active_{object_type}s', data.get('active_leads', 120))
        priority_count = data.get('converted_leads', data.get('open_cases', 30))
        
        dashlet1 = DashletBuilder(f"Total {object_type.title()}s") \
            .with_description(str(total_count)) \
            .default() \
            .build()
        
        dashlet2 = DashletBuilder(f"Active {object_type.title()}s") \
            .with_description(str(active_count)) \
            .accent() \
            .build()
        
        dashlet3 = DashletBuilder(f"Priority {object_type.title()}s") \
            .with_description(str(priority_count)) \
            .primary() \
            .build()
        
        return [dashlet1, dashlet2, dashlet3]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern0"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Dashlet"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern0",
            "pattern_name": "Dashboard Metrics (3 Dashlets)",
            "description": "Dashboard view with 3 metric cards showing key statistics",
            "use_when": {
                "user_intent": ["view dashboard", "see metrics", "check statistics", "monitor KPIs"],
                "query_complexity": "simple to medium",
                "data_requirement": "aggregate counts or statistics (total, active, completed)"
            },
            "data_types": {
                "input_structure": "Aggregated data with numeric counts",
                "required_fields": ["total count", "active count", "completed/converted count"],
                "optional_fields": ["trend data", "percentage changes"],
                "data_volume": "3 metrics (aggregate values, not individual records)"
            },
            "query_patterns": {
                "keywords": ["metrics", "dashboard", "stats", "statistics", "overview", "summary", "total", "count"],
                "query_types": ["dashboard view", "metrics display", "statistics summary", "KPI overview"],
                "example_queries": [
                    {"query": "show lead metrics", "object_type": "lead"},
                    {"query": "display case dashboard", "object_type": "case"},
                    {"query": "account statistics overview", "object_type": "account"},
                    {"query": "total count of opportunities", "object_type": "opportunity"}
                ]
            },
            "layout_characteristics": {
                "complexity": "low",
                "interactivity": "none",
                "visual_density": "sparse",
                "components_count": 3,
                "responsive_behavior": "3-column grid on desktop, stacked on mobile"
            }
        }

