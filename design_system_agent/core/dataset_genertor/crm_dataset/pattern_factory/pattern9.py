"""
Pattern 9: Metrics Row (3 Metrics)
Pattern with 3 metrics showing KPIs with trends
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_metric.metric_builder import MetricBuilder


class Pattern9:
    """
    Metrics Row (3 Metrics) Pattern
    
    LLM Guidance:
    - Use when: Query asks for KPIs or performance metrics with trends
    - Data type: Numeric metrics with trend indicators (up/down percentages)
    - Best for: Performance tracking, conversion rates, response times
    - Keywords: "show KPIs", "metrics with trends", "performance indicators", "conversion rates"
    - Example queries: "Show conversion metrics", "Display performance KPIs", "Response time metrics"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate 3 metric components with trends
        
        Returns:
            List of 3 metric components
        """
        conversion_rate = data.get('conversion_rate', 68.0)
        response_time = data.get('avg_response_time', 2.5)
        
        metric1 = MetricBuilder("Conversion Rate", f"{conversion_rate}%").trend(5.0, "up", True).build()
        metric2 = MetricBuilder("Avg Response Time", f"{response_time}h").trend(10.0, "down", True).build()
        metric3 = MetricBuilder("Satisfaction Score", "4.8/5").trend(2.0, "up", True).build()
        
        return [metric1, metric2, metric3]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern9"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Metric"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern9",
            "pattern_name": "Metrics Row (3 Metrics)",
            "description": "KPI metrics with trend indicators (up/down changes)",
            "use_when": {
                "user_intent": ["view KPIs", "check performance", "see trends", "monitor metrics"],
                "query_complexity": "medium",
                "data_requirement": "3 numeric metrics with trend/change indicators"
            },
            "data_types": {
                "input_structure": "Performance metrics with trend data",
                "required_fields": ["3 metric values", "trend directions", "percentage changes"],
                "optional_fields": ["time period", "comparison baseline"],
                "data_volume": "3 KPI metrics with trends"
            },
            "query_patterns": {
                "keywords": ["KPIs", "metrics with trends", "performance", "conversion", "indicators", "growth"],
                "query_types": ["KPI display", "performance metrics", "trend analysis", "conversion tracking"],
                "example_queries": [
                    {"query": "show conversion metrics", "object_type": "lead"},
                    {"query": "display performance KPIs", "object_type": "case"},
                    {"query": "response time metrics", "object_type": "ticket"},
                    {"query": "growth indicators", "object_type": "account"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "none",
                "visual_density": "medium",
                "components_count": 3,
                "responsive_behavior": "3-column to stacked"
            }
        }

