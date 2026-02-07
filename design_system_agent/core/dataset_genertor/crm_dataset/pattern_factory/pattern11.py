"""
Pattern 11: Title + Table (Compact)
Pattern with heading and simple table
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h2_heading
from design_system_agent.core.dataset_genertor.component_table.table_builder import TableBuilder


class Pattern11:
    """
    Title + Table (Compact) Pattern
    
    LLM Guidance:
    - Use when: Query asks for simple table view without extra context
    - Data type: Tabular records with multiple columns
    - Best for: Clean data grid with minimal decoration
    - Keywords: "show table", "list in table", "data grid", "simple table"
    - Example queries: "Show leads table", "List cases", "Display records in table"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate heading and table components
        
        Returns:
            List of components [heading, table]
        """
        title = f"{object_type.title()} Records"
        
        columns = [
            {"id": "name", "header": "Name", "accessor": "name"},
            {"id": "status", "header": "Status", "accessor": "status"},
            {"id": "priority", "header": "Priority", "accessor": "priority"},
            {"id": "owner", "header": "Owner", "accessor": "owner"},
        ]
        
        rows = [
            {
                "id": "1",
                "name": data.get('name', 'Unknown'),
                "status": data.get('status', 'N/A'),
                "priority": data.get('priority', 'N/A'),
                "owner": data.get('owner', 'N/A'),
            }
        ]
        
        table = TableBuilder().columns(columns).data(rows).striped().hoverable().build()
        
        return [
            h2_heading(title),
            table
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern11"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Table"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return comprehensive LLM guidance for pattern selection"""
        return {
            "pattern_id": "pattern11",
            "pattern_name": "Title + Table",
            "description": "Tabular pattern displaying multiple records in a structured grid format",
            "use_when": {
                "user_intent": ["view multiple records", "list data", "tabular display"],
                "query_complexity": "moderate",
                "data_requirement": "multiple records with consistent schema"
            },
            "data_types": {
                "input_structure": "Array of record objects",
                "required_fields": ["name", "status", "priority", "owner"],
                "optional_fields": ["created_date", "modified_date", "email", "phone"],
                "data_volume": "1+ records (optimally 5-50)"
            },
            "best_for": [
                "Multi-record display",
                "Data grid presentation",
                "Sortable/filterable lists",
                "Bulk data viewing"
            ],
            "query_patterns": {
                "keywords": ["show", "list", "all", "my", "table", "records", "display multiple"],
                "query_types": ["list_view", "multi_record", "table_display"],
                "example_queries": [
                    {"query": "show my leads", "object_type": "lead"},
                    {"query": "list all cases", "object_type": "case"},
                    {"query": "display accounts table", "object_type": "account"},
                    {"query": "show contact records", "object_type": "contact"}
                ]
            },
            "components": ["Heading", "Table"],
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "medium (sortable, hoverable)",
                "visual_density": "high"
            }
        }
