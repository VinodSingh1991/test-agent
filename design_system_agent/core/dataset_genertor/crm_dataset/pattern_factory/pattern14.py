"""
Pattern 14: Metrics + Table (Analytics)
Pattern with metrics row followed by detailed table
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading
from design_system_agent.core.dataset_genertor.component_metric.metric_builder import MetricBuilder
from design_system_agent.core.dataset_genertor.component_table.table_builder import TableBuilder


class Pattern14:
    """
    Metrics + Table (Analytics) Pattern
    
    LLM Guidance:
    - Use when: Query asks for analytics view with metrics and supporting data
    - Data type: Summary metrics + detailed breakdown in table
    - Best for: Analytics dashboards, reports with KPIs and details
    - Keywords: "analytics", "metrics and table", "KPIs with details", "performance report"
    - Example queries: "Show analytics report", "Display metrics with data", "Performance dashboard"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate heading, metrics, and table components
        
        Returns:
            List of components [heading, metrics, table]
        """
        title = f"{object_type.title()} Analytics"
        
        # Metrics
        total = data.get(f'total_{object_type}s', 150)
        active = data.get(f'active_{object_type}s', 120)
        
        metric1 = MetricBuilder("Total Records", total).build()
        metric2 = MetricBuilder("Active Records", active).trend(8.0, "up", True).build()
        
        # Table
        columns = [
            {"id": "name", "header": "Name", "accessor": "name"},
            {"id": "status", "header": "Status", "accessor": "status"},
            {"id": "priority", "header": "Priority", "accessor": "priority"},
        ]
        
        rows = [
            {
                "id": "1",
                "name": data.get('name', 'Unknown'),
                "status": data.get('status', 'N/A'),
                "priority": data.get('priority', 'N/A'),
            }
        ]
        
        table = TableBuilder().columns(columns).data(rows).striped().build()
        
        return [
            h1_heading(title),
            metric1,
            metric2,
            table
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern14"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Metric", "Table"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern14",
            "pattern_name": "Metrics + Table (Analytics)",
            "description": "Analytics dashboard with metrics summary and detailed data table",
            "use_when": {
                "user_intent": ["analytics report", "metrics with details", "KPIs and data", "performance report"],
                "query_complexity": "high",
                "data_requirement": "summary metrics plus detailed tabular breakdown"
            },
            "data_types": {
                "input_structure": "Aggregated metrics with supporting detail records",
                "required_fields": ["2-3 summary metrics", "table columns", "table data rows"],
                "optional_fields": ["metric trends", "table sorting/filtering"],
                "data_volume": "2-3 metrics + table with multiple rows"
            },
            "query_patterns": {
                "keywords": ["analytics", "metrics and table", "KPIs with details", "performance report", "dashboard with data"],
                "query_types": ["analytics dashboard", "performance report", "metrics with breakdown", "detailed analytics"],
                "example_queries": [
                    {"query": "show analytics report", "object_type": "lead"},
                    {"query": "display metrics with data", "object_type": "case"},
                    {"query": "performance dashboard", "object_type": "opportunity"},
                    {"query": "KPIs with detailed breakdown", "object_type": "account"}
                ]
            },
            "layout_characteristics": {
                "complexity": "high",
                "interactivity": "table sorting/filtering",
                "visual_density": "dense",
                "components_count": 4,
                "responsive_behavior": "metrics stack, table scrolls horizontally"
            }
        }

