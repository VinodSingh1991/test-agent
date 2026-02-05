"""
Summary Data Generator

Generates summary records using builder pattern with full layout hierarchy.
Layout → Tab → Section → Row → Column → Component

Supports multiple component patterns:
- Pattern 1: Title + Description
- Pattern 2: Title + List + Description
- Pattern 3: Title + List
- Pattern 4: Title + Description + Button
- Pattern 5: Title + Button
- Pattern 6: Title + List + Button
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from design_system_agent.core.dataset_genertor.component_heading.heading_builder import HeadingBuilder
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder
from design_system_agent.core.dataset_genertor.component_button.button_builder import ButtonBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.layout_builder import LayoutBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.tab_builder import TabBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.section_builder import SectionBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.row_builder import RowBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.column_builder import ColumnBuilder

basic_query_to_get_summary = [
    "show my basic notifications",
    "show my tasks",
    "show upcoming events",
    "show system update",
    "quick action",
    "show pending approvals",
    "show account status",
    "security alert",
    "weekly summary",
    "show my teams",
]

modrate_query_to_get_summary = [
    "show my notifications",
    "show my tasks for today",
    "show upcoming events this week",
    "show latest system update",
    "perform quick action",
    "show pending approvals",
    "show account status overview",
    "show security alert",
    "show weekly summary",
    "show my teams and groups",
]

advanced_query_to_get_summary = [
    "show my notifications and alerts",
    "show my tasks with deadlines",
    "show upcoming events and meetings",
    "show detailed system update",
    "perform advanced quick action",
    "show pending approvals with details",
    "show comprehensive account status",
    "show recent security alerts",
    "show detailed weekly summary",
    "show all my teams and projects",
]

class SummaryDataGenerator:
    """Generator for creating summary records using builder pattern with multiple patterns"""
    
    def __init__(self):
        self.output_dir = Path("design_system_agent/dataset")
        self.output_file_jsonl = self.output_dir / "summary_records.jsonl"
        self.output_file_json = self.output_dir / "summary_records.json"

    def generate_title_description(self, idx: int, title: str, description: str) -> LayoutBuilder:
        """Generate layout with title and description"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        desc = DescriptionBuilder(description).large().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        desc_col = ColumnBuilder("Description Column", f"col-desc-{idx}").add_component(
            desc.type, desc.children, desc.classes, desc.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        desc_row = RowBuilder(f"row-desc-{idx}", "Description Row").add_column(desc_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_row(heading_row).add_row(desc_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_title_list_description(self, idx: int, title: str, list_items: List[str], description: str) -> LayoutBuilder:
        """Generate layout with title, list, and description"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        list_comp = ListBuilder(*list_items).unordered().with_disc().with_padding().build()
        desc = DescriptionBuilder(description).large().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        list_col = ColumnBuilder("List Column", f"col-list-{idx}").add_component(
            list_comp.type, list_comp.children, list_comp.classes, list_comp.props
        )
        desc_col = ColumnBuilder("Description Column", f"col-desc-{idx}").add_component(
            desc.type, desc.children, desc.classes, desc.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        list_row = RowBuilder(f"row-list-{idx}", "List Row").add_column(list_col)
        desc_row = RowBuilder(f"row-desc-{idx}", "Description Row").add_column(desc_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_rows(heading_row, list_row, desc_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_title_list(self, idx: int, title: str, list_items: List[str]) -> LayoutBuilder:
        """Generate layout with title and list"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        list_comp = ListBuilder(*list_items).unordered().with_disc().with_padding().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        list_col = ColumnBuilder("List Column", f"col-list-{idx}").add_component(
            list_comp.type, list_comp.children, list_comp.classes, list_comp.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        list_row = RowBuilder(f"row-list-{idx}", "List Row").add_column(list_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_rows(heading_row, list_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_title_description_button(self, idx: int, title: str, description: str, button_text: str) -> LayoutBuilder:
        """Generate layout with title, description, and button"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        desc = DescriptionBuilder(description).large().build()
        button = ButtonBuilder(button_text).primary().medium().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        desc_col = ColumnBuilder("Description Column", f"col-desc-{idx}").add_component(
            desc.type, desc.children, desc.classes, desc.props
        )
        button_col = ColumnBuilder("Button Column", f"col-button-{idx}").add_component(
            button.type, button.children, button.classes, button.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        desc_row = RowBuilder(f"row-desc-{idx}", "Description Row").add_column(desc_col)
        button_row = RowBuilder(f"row-button-{idx}", "Button Row").add_column(button_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_rows(heading_row, desc_row, button_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_title_button(self, idx: int, title: str, button_text: str) -> LayoutBuilder:
        """Generate layout with title and button"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        button = ButtonBuilder(button_text).primary().medium().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        button_col = ColumnBuilder("Button Column", f"col-button-{idx}").add_component(
            button.type, button.children, button.classes, button.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        button_row = RowBuilder(f"row-button-{idx}", "Button Row").add_column(button_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_rows(heading_row, button_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_title_list_button(self, idx: int, title: str, list_items: List[str], button_text: str) -> LayoutBuilder:
        """Generate layout with title, list, and button"""
        # Build components
        heading = HeadingBuilder(title, level=2).bold().build()
        list_comp = ListBuilder(*list_items).unordered().with_disc().with_padding().build()
        button = ButtonBuilder(button_text).primary().medium().build()
        
        # Build columns
        heading_col = ColumnBuilder("Heading Column", f"col-heading-{idx}").add_component(
            heading.type, heading.children, heading.classes, heading.props
        )
        list_col = ColumnBuilder("List Column", f"col-list-{idx}").add_component(
            list_comp.type, list_comp.children, list_comp.classes, list_comp.props
        )
        button_col = ColumnBuilder("Button Column", f"col-button-{idx}").add_component(
            button.type, button.children, button.classes, button.props
        )
        
        # Build rows
        heading_row = RowBuilder(f"row-heading-{idx}", "Heading Row").add_column(heading_col)
        list_row = RowBuilder(f"row-list-{idx}", "List Row").add_column(list_col)
        button_row = RowBuilder(f"row-button-{idx}", "Button Row").add_column(button_col)
        
        # Build section
        section = SectionBuilder("Main Content", f"section-main-{idx}").add_rows(heading_row, list_row, button_row)
        
        # Build tab
        tab = TabBuilder("Summary", f"tab-summary-{idx}").add_section(section)
        
        # Build and return layout
        return LayoutBuilder().add_tab(tab)
    
    def generate_records(self, count: int = 10) -> List[Dict[str, Any]]:
        """Generate multiple records using different patterns"""
        data = []

        # Pattern 1: Title + Description
        for idx, q in enumerate(basic_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_description(
                    idx=idx,
                    title="Recent Notifications",
                    description="You have 5 unread notifications. 2 require immediate attention."
                ).to_dict()
            })

        # Pattern 2: Title + List + Description
        for idx, q in enumerate(modrate_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_list_description(
                    idx=idx,
                    title="Today's Tasks",
                    list_items=["Review pull requests", "Update documentation", "Fix bug #234"],
                    description="Complete these tasks by end of day for maximum productivity."
                ).to_dict()
            })

        # Pattern 3: Title + List
        for idx, q in enumerate(modrate_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_list(
                    idx=idx,
                    title="Upcoming Events",
                    list_items=["Team meeting at 2 PM", "Client call at 4 PM", "Code review at 5 PM"]
                ).to_dict()
            })

        # Pattern 4: Title + Description + Button
        for idx, q in enumerate(advanced_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_description_button(
                    idx=idx,
                    title="System Update Available",
                    description="A new version 2.5.0 is available with bug fixes and performance improvements.",
                    button_text="Update Now"
                ).to_dict()
            })

        # Pattern 5: Title + Button
        for idx, q in enumerate(advanced_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_button(
                    idx=idx,
                    title="Quick Actions",
                    button_text="Start New Project"
                ).to_dict()
            })

        # Pattern 6: Title + List + Button
        for idx, q in enumerate(advanced_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_list_button(
                    idx=idx,
                    title="Pending Approvals",
                    list_items=["Invoice #1234", "Expense report #567", "Time-off request"],
                    button_text="Review All"
                ).to_dict()
            })

        # More Pattern 1 examples
        for idx, q in enumerate(basic_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_description(
                    idx=idx,
                    title="Account Overview",
                    description="Your account balance is $1,234.56 with 3 pending transactions."
                ).to_dict()
            })

        # More Pattern 4 examples
        for idx, q in enumerate(advanced_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_description_button(
                    idx=idx,
                    title="Security Alert",
                    description="Unusual login activity detected from a new device. Please verify your account.",
                    button_text="Verify Account"
                ).to_dict()
            })

        # More Pattern 2 examples
        for idx, q in enumerate(modrate_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_list_description(
                    idx=idx,
                    title="Weekly Summary",
                    list_items=["15 tasks completed", "3 meetings attended", "2 projects delivered"],
                    description="Great progress this week! Keep up the good work."
                ).to_dict()
            })

        # More Pattern 3 examples
        for idx, q in enumerate(modrate_query_to_get_summary, start=1):
            data.append({
                "query": q,
                "layout": self.generate_title_list(
                    idx=idx,
                    title="My Teams",
                    list_items=["Frontend Team", "Backend Team", "DevOps Team", "QA Team"]
                ).to_dict()
            })

        return data[:count]
    
    def generate_and_save(self, count: int = 10):
        """
        Generate records using different patterns and save to both JSONL and JSON files
        
        Args:
            count: Number of records to generate (default: 10)
        """
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate records
        records = self.generate_records(count)
        
        # Write to JSONL file using writelines and map (no explicit for loop)
        with open(self.output_file_jsonl, 'w', encoding='utf-8') as f:
            f.writelines(map(lambda r: json.dumps(r, ensure_ascii=False) + '\n', records))
        
        # Write to JSON file as array
        with open(self.output_file_json, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Generated {len(records)} record(s) using multiple patterns")
        print(f"✓ Patterns: Title+Desc, Title+List+Desc, Title+List, Title+Desc+Button, Title+Button, Title+List+Button")
        print(f"✓ Saved to JSONL: {self.output_file_jsonl}")
        print(f"✓ Saved to JSON: {self.output_file_json}")
        
        return {"jsonl": str(self.output_file_jsonl), "json": str(self.output_file_json)}


if __name__ == "__main__":
    generator = SummaryDataGenerator()
    
    # Generate records with all patterns in loops (default 100 records possible)
    print("=== Generating records with multiple patterns in loops ===")
    output_paths = generator.generate_and_save(count=100)  # Generate all available records
    print(f"\nOutput files:")
    print(f"  JSONL: {output_paths['jsonl']}")
    print(f"  JSON: {output_paths['json']}\n")
    
    # Example: Generate limited number of records
    # output_paths = generator.generate_and_save(count=30)
