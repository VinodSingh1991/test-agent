"""
Pattern 6: Title + Description + Table + Summary
Pattern with heading, description, table, and summary description
"""

from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading, h2_heading
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_table.table_builder import TableBuilder


class Pattern6:
    """
    Title + Description + Table + Summary Pattern
    
    LLM Guidance:
    - Use when: Query asks for tabular data view with context
    - Data type: Records that work well in table format (rows and columns)
    - Best for: Structured data display with header and footer summary
    - Keywords: "table view", "show in table", "list records", "data grid"
    - Example queries: "Show leads in table", "Display cases as table", "List accounts in grid"
    """
    
    @staticmethod
    def generate(object_type: str, data: Dict[str, Any], idx: int = 0) -> List[Dict[str, Any]]:
        """
        Generate title, description, table, and summary components
        
        Returns:
            List of components [heading, description, table, summary]
        """
        title = f"{object_type.title()} Complete View"
        desc_text = f"Detailed table view for {object_type} records"
        
        # Table
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
        
        summary_text = f"Total records: 1 | Active: {data.get('status', 'N/A')}"
        
        return [
            h1_heading(title),
            DescriptionBuilder(desc_text).build(),
            table,
            h2_heading("Summary"),
            DescriptionBuilder(summary_text).build()
        ]
    
    @staticmethod
    def get_pattern_type() -> str:
        return "pattern6"
    
    @staticmethod
    def get_components() -> List[str]:
        return ["Heading", "Description", "Table"]
    
    @staticmethod
    def get_llm_guidance() -> Dict[str, Any]:
        """Return structured guidance for LLM pattern selection"""
        return {
            "pattern_id": "pattern6",
            "pattern_name": "Title + Description + Table + Summary",
            "description": "Tabular data view with contextual header and footer",
            "use_when": {
                "user_intent": ["view table", "see grid", "structured data", "tabular view"],
                "query_complexity": "medium",
                "data_requirement": "records suitable for tabular display with rows and columns"
            },
            "data_types": {
                "input_structure": "Structured records with consistent fields",
                "required_fields": ["column headers", "row data", "summary information"],
                "optional_fields": ["sortable columns", "filterable data"],
                "data_volume": "1+ records in table format"
            },
            "query_patterns": {
                "keywords": ["table", "grid", "list records", "data view", "show in table", "tabular"],
                "query_types": ["table display", "grid view", "structured data", "record listing"],
                "example_queries": [
                    {"query": "show leads in table", "object_type": "lead"},
                    {"query": "display cases as table", "object_type": "case"},
                    {"query": "list accounts in grid", "object_type": "account"},
                    {"query": "table view of contacts", "object_type": "contact"}
                ]
            },
            "layout_characteristics": {
                "complexity": "medium",
                "interactivity": "potential sorting/filtering",
                "visual_density": "dense",
                "components_count": 5,
                "responsive_behavior": "horizontal scroll on mobile"
            }
        }

