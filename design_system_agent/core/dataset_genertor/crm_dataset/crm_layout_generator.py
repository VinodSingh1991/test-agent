"""
CRM Layout Generator - Generates comprehensive CRM layouts using Pattern-Based Components
Uses PATTERN_BASED_QUERIES and PATTERN_COMPONENTS for rich, realistic layouts
"""
import json
from pathlib import Path
from typing import Dict, Any, List
import random

# Layout builders
from design_system_agent.core.dataset_genertor.component_layout.builder.layout_builder import LayoutBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.tab_builder import TabBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.section_builder import SectionBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.row_builder import RowBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.column_builder import ColumnBuilder

# All 21 Component Builders
from design_system_agent.core.dataset_genertor.component_heading.heading_builder import HeadingBuilder
from design_system_agent.core.dataset_genertor.component_description.description_builder import DescriptionBuilder
from design_system_agent.core.dataset_genertor.component_text.text_builder import TextBuilder
from design_system_agent.core.dataset_genertor.component_link.link_builder import LinkBuilder
from design_system_agent.core.dataset_genertor.component_label.label_builder import LabelBuilder
from design_system_agent.core.dataset_genertor.component_button.button_builder import ButtonBuilder
from design_system_agent.core.dataset_genertor.component_avatar.avatar_builder import AvatarBuilder
from design_system_agent.core.dataset_genertor.component_badge.badge_builder import BadgeBuilder
from design_system_agent.core.dataset_genertor.component_list.list_builder import ListBuilder
from design_system_agent.core.dataset_genertor.component_table.table_builder import TableBuilder
from design_system_agent.core.dataset_genertor.component_image.image_builder import ImageBuilder
from design_system_agent.core.dataset_genertor.component_chip.chip_builder import ChipBuilder
from design_system_agent.core.dataset_genertor.component_card.card_builder import CardBuilder
from design_system_agent.core.dataset_genertor.component_dashlet.dashlet_builder import DashletBuilder
from design_system_agent.core.dataset_genertor.component_listcard.listcard_builder import ListCardBuilder
from design_system_agent.core.dataset_genertor.component_birthdaycard.birthdaycard_builder import BirthdayCardBuilder
from design_system_agent.core.dataset_genertor.component_alert.alert_builder import AlertBuilder
from design_system_agent.core.dataset_genertor.component_insights.insights_builder import InsightsBuilder
from design_system_agent.core.dataset_genertor.component_divider.divider_builder import DividerBuilder
from design_system_agent.core.dataset_genertor.component_stack.stack_builder import StackBuilder
from design_system_agent.core.dataset_genertor.component_metric.metric_builder import MetricBuilder

# Import pattern factory functions for cleaner component creation
from design_system_agent.core.dataset_genertor.component_heading.patterns import h1_heading, h2_heading
from design_system_agent.core.dataset_genertor.component_button.patterns import primary_button, secondary_button, danger_button
from design_system_agent.core.dataset_genertor.component_badge.patterns import success_badge, warning_badge, info_badge
from design_system_agent.core.dataset_genertor.component_chip.patterns import primary_chip, secondary_chip
from design_system_agent.core.dataset_genertor.component_divider.patterns import horizontal_divider
from design_system_agent.core.dataset_genertor.component_label.patterns import form_label
from design_system_agent.core.dataset_genertor.component_text.patterns import body_text
from design_system_agent.core.dataset_genertor.component_link.patterns import standard_link

# Pattern and query configurations
from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    PATTERN_BASED_QUERIES,
    PATTERN_COMPONENTS,
)


class CRMLayoutGenerator:
    """Generates CRM-specific layouts using pattern-based component combinations"""
    
    def __init__(self):
        # Save to design_system_agent/dataset/ folder
        self.output_dir = Path(__file__).parent.parent.parent.parent / "dataset"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Sample data for realistic layouts
        self.sample_names = ["John Doe", "Jane Smith", "Bob Wilson", "Alice Johnson", "Mike Brown"]
        self.sample_companies = ["Acme Corp", "Tech Solutions", "Global Industries", "StartUp Inc", "Enterprise Ltd"]
        self.sample_statuses = ["Active", "Pending", "Closed", "Qualified", "New", "Working"]
        self.sample_priorities = ["High", "Medium", "Low"]
    
    def get_sample_data(self, object_type: str, idx: int) -> Dict[str, Any]:
        """Generate sample CRM data for an object"""
        return {
            "name": f"{object_type} {random.choice(self.sample_companies)}",
            "owner": random.choice(self.sample_names),
            "status": random.choice(self.sample_statuses),
            "priority": random.choice(self.sample_priorities),
            "created": f"2026-01-{(idx % 28) + 1:02d}",
            "revenue": f"${random.randint(10, 500)}K",
            "confidence": random.randint(70, 99),
            "avatar": f"/avatar{(idx % 5) + 1}.jpg",
            "email": f"{random.choice(self.sample_names).lower().replace(' ', '.')}@example.com",
            "phone": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
        }
    
    # ============ PATTERN-SPECIFIC LAYOUT GENERATORS ============
    
    def generate_basic_detail_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate basic_detail pattern - Comprehensive record detail view (10 components)"""
        # Components: Heading, Badge, Divider, Label, Text, Table, Avatar, Button, Link, Chip
        
        # Header section - using pattern functions
        heading = h1_heading(f"{object_type}: {data['name']}")
        status_badge = success_badge(data['status'])
        priority_badge = warning_badge(data['priority'])
        avatar = AvatarBuilder(data['avatar']).large().build()
        
        # Info section - using pattern functions
        divider1 = horizontal_divider()
        owner_label = form_label("Owner")
        owner_text = body_text(data['owner'])
        created_label = form_label("Created")
        created_text = body_text(data['created'])
        
        # Tags - using pattern functions
        tag_chip1 = primary_chip("Enterprise")
        tag_chip2 = secondary_chip("Q1 2026")
        
        # Details table
        details_table = TableBuilder() \
            .set_headers("Field", "Value") \
            .add_row(["Revenue", data['revenue']]) \
            .add_row(["Email", data['email']]) \
            .add_row(["Phone", data['phone']]) \
            .striped().build()
        
        # Actions - using pattern functions
        divider2 = horizontal_divider()
        edit_btn = primary_button("Edit")
        delete_btn = danger_button("Delete")
        related_link = standard_link("View Related Records")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder(f"{object_type} Details", f"tab-{idx}")
        section = SectionBuilder("Overview", f"sec-{idx}")
        
        # Row 1: Header
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1_1 = ColumnBuilder("Title", f"col-{idx}-1-1").add_component(heading.type, heading.children, heading.classes, heading.props)
        col1_2 = ColumnBuilder("Badges", f"col-{idx}-1-2") \
            .add_component(status_badge.type, status_badge.children, status_badge.classes, status_badge.props) \
            .add_component(priority_badge.type, priority_badge.children, priority_badge.classes, priority_badge.props)
        col1_3 = ColumnBuilder("Avatar", f"col-{idx}-1-3").add_component(avatar.type, avatar.children, avatar.classes, avatar.props)
        row1.add_column(col1_1).add_column(col1_2).add_column(col1_3)
        
        # Row 2: Divider
        row2 = RowBuilder(f"row-{idx}-2", "Divider")
        col2_1 = ColumnBuilder("Divider", f"col-{idx}-2-1").add_component(divider1.type, divider1.children, divider1.classes, divider1.props)
        row2.add_column(col2_1)
        
        # Row 3: Fields
        row3 = RowBuilder(f"row-{idx}-3", "Fields")
        col3_1 = ColumnBuilder("Labels", f"col-{idx}-3-1") \
            .add_component(owner_label.type, owner_label.children, owner_label.classes, owner_label.props) \
            .add_component(owner_text.type, owner_text.children, owner_text.classes, owner_text.props) \
            .add_component(created_label.type, created_label.children, created_label.classes, created_label.props) \
            .add_component(created_text.type, created_text.children, created_text.classes, created_text.props)
        col3_2 = ColumnBuilder("Tags", f"col-{idx}-3-2") \
            .add_component(tag_chip1.type, tag_chip1.children, tag_chip1.classes, tag_chip1.props) \
            .add_component(tag_chip2.type, tag_chip2.children, tag_chip2.classes, tag_chip2.props)
        row3.add_column(col3_1).add_column(col3_2)
        
        # Row 4: Table
        row4 = RowBuilder(f"row-{idx}-4", "Table")
        col4_1 = ColumnBuilder("Details", f"col-{idx}-4-1").add_component(details_table.type, details_table.children, details_table.classes, details_table.props)
        row4.add_column(col4_1)
        
        # Row 5: Actions
        row5 = RowBuilder(f"row-{idx}-5", "Actions")
        col5_1 = ColumnBuilder("Divider", f"col-{idx}-5-1").add_component(divider2.type, divider2.children, divider2.classes, divider2.props)
        row5.add_column(col5_1)
        
        row6 = RowBuilder(f"row-{idx}-6", "Buttons")
        col6_1 = ColumnBuilder("Buttons", f"col-{idx}-6-1") \
            .add_component(edit_btn.type, edit_btn.children, edit_btn.classes, edit_btn.props) \
            .add_component(delete_btn.type, delete_btn.children, delete_btn.classes, delete_btn.props) \
            .add_component(related_link.type, related_link.children, related_link.classes, related_link.props)
        row6.add_column(col6_1)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_metrics_dashboard_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate metrics_dashboard pattern - KPI dashboard (8 components)"""
        # Components: Heading, Metric, Dashlet, Card, Badge, Divider, Button, Table
        
        heading = HeadingBuilder(f"{object_type} Performance Dashboard", 1).build()
        
        # Metrics
        revenue_metric = MetricBuilder(data['revenue'], "Total Revenue").with_change("+12%", "up").build()
        count_metric = MetricBuilder("1,234", f"Total {object_type}s").with_change("+5%", "up").build()
        rate_metric = MetricBuilder("42%", "Win Rate").with_change("0%", "neutral").build()
        
        # Dashlets
        dashlet1 = DashletBuilder(f"Top {object_type}s").add_content("5 high-value records").with_action("View All").build()
        dashlet2 = DashletBuilder("Recent Activity").add_content("12 updates today").build()
        
        # Card with grouped metrics
        card = CardBuilder("Team Performance").elevated() \
            .add_body_content("Team A: $500K") \
            .add_body_content("Team B: $350K") \
            .build()
        
        # Trend badges
        up_badge = BadgeBuilder("Trending Up").success().build()
        
        divider = DividerBuilder().horizontal().build()
        
        # Actions
        refresh_btn = ButtonBuilder("Refresh").primary().build()
        export_btn = ButtonBuilder("Export").secondary().build()
        
        # Breakdown table
        table = TableBuilder() \
            .set_headers("Region", "Revenue", "Growth") \
            .add_row(["North", "$500K", "+15%"]) \
            .add_row(["South", "$350K", "+8%"]) \
            .add_row(["East", "$400K", "+12%"]) \
            .striped().build()
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Dashboard", f"tab-{idx}")
        section = SectionBuilder("Metrics", f"sec-{idx}")
        
        # Row 1: Title
        row1 = RowBuilder(f"row-{idx}-1", "Title")
        col1 = ColumnBuilder("Heading", f"col-{idx}-1").add_component(heading.type, heading.children, heading.classes, heading.props)
        row1.add_column(col1)
        
        # Row 2: Metrics
        row2 = RowBuilder(f"row-{idx}-2", "Metrics")
        col2_1 = ColumnBuilder("Metric1", f"col-{idx}-2-1").add_component(revenue_metric.type, revenue_metric.children, revenue_metric.classes, revenue_metric.props)
        col2_2 = ColumnBuilder("Metric2", f"col-{idx}-2-2").add_component(count_metric.type, count_metric.children, count_metric.classes, count_metric.props)
        col2_3 = ColumnBuilder("Metric3", f"col-{idx}-2-3").add_component(rate_metric.type, rate_metric.children, rate_metric.classes, rate_metric.props)
        row2.add_column(col2_1).add_column(col2_2).add_column(col2_3)
        
        # Row 3: Dashlets
        row3 = RowBuilder(f"row-{idx}-3", "Dashlets")
        col3_1 = ColumnBuilder("Dashlet1", f"col-{idx}-3-1").add_component(dashlet1.type, dashlet1.children, dashlet1.classes, dashlet1.props)
        col3_2 = ColumnBuilder("Dashlet2", f"col-{idx}-3-2").add_component(dashlet2.type, dashlet2.children, dashlet2.classes, dashlet2.props)
        row3.add_column(col3_1).add_column(col3_2)
        
        # Row 4: Card and Badge
        row4 = RowBuilder(f"row-{idx}-4", "Card")
        col4_1 = ColumnBuilder("Card", f"col-{idx}-4-1").add_component(card.type, card.children, card.classes, card.props)
        col4_2 = ColumnBuilder("Badge", f"col-{idx}-4-2").add_component(up_badge.type, up_badge.children, up_badge.classes, up_badge.props)
        row4.add_column(col4_1).add_column(col4_2)
        
        # Row 5: Divider
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Divider", f"col-{idx}-5").add_component(divider.type, divider.children, divider.classes, divider.props)
        row5.add_column(col5)
        
        # Row 6: Buttons
        row6 = RowBuilder(f"row-{idx}-6", "Buttons")
        col6 = ColumnBuilder("Actions", f"col-{idx}-6") \
            .add_component(refresh_btn.type, refresh_btn.children, refresh_btn.classes, refresh_btn.props) \
            .add_component(export_btn.type, export_btn.children, export_btn.classes, export_btn.props)
        row6.add_column(col6)
        
        # Row 7: Table
        row7 = RowBuilder(f"row-{idx}-7", "Table")
        col7 = ColumnBuilder("Breakdown", f"col-{idx}-7").add_component(table.type, table.children, table.classes, table.props)
        row7.add_column(col7)
        
        section.add_rows(row1, row2, row3, row4, row5, row6, row7)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_contact_list_card_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate contact_list_card pattern - People/stakeholders (9 components)"""
        # Components: Heading, ListCard, Avatar, Badge, Text, Link, Chip, Button, Divider
        
        heading = HeadingBuilder(f"{object_type} Team Members", 2).build()
        
        # ListCard with contacts
        listcard = ListCardBuilder(f"{object_type} Stakeholders") \
            .add_item("/user1.jpg", self.sample_names[0], "Project Manager", "Online") \
            .add_item("/user2.jpg", self.sample_names[1], "Sales Rep", "Away") \
            .add_item("/user3.jpg", self.sample_names[2], "Engineer", "Busy") \
            .build()
        
        # Individual contact components
        avatar = AvatarBuilder("/avatar.jpg").medium().with_status("online").build()
        status_badge = BadgeBuilder("Online").success().pill_shape().build()
        role_text = TextBuilder("Key Contact").small().build()
        profile_link = LinkBuilder("View Full Profile").build()
        
        # Tags
        tag1 = ChipBuilder("Decision Maker").primary().build()
        tag2 = ChipBuilder("Technical").secondary().build()
        
        divider = DividerBuilder().horizontal().build()
        add_btn = ButtonBuilder("Add Contact").primary().build()
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Contacts", f"tab-{idx}")
        section = SectionBuilder("Team", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading.type, heading.children, heading.classes, heading.props)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "ListCard")
        col2 = ColumnBuilder("Contacts", f"col-{idx}-2").add_component(listcard.type, listcard.children, listcard.classes, listcard.props)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Details")
        col3 = ColumnBuilder("ContactInfo", f"col-{idx}-3") \
            .add_component(avatar.type, avatar.children, avatar.classes, avatar.props) \
            .add_component(status_badge.type, status_badge.children, status_badge.classes, status_badge.props) \
            .add_component(role_text.type, role_text.children, role_text.classes, role_text.props) \
            .add_component(profile_link.type, profile_link.children, profile_link.classes, profile_link.props)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Tags")
        col4 = ColumnBuilder("Tags", f"col-{idx}-4") \
            .add_component(tag1.type, tag1.children, tag1.classes, tag1.props) \
            .add_component(tag2.type, tag2.children, tag2.classes, tag2.props)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Div", f"col-{idx}-5").add_component(divider.type, divider.children, divider.classes, divider.props)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Actions")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(add_btn.type, add_btn.children, add_btn.classes, add_btn.props)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_insights_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate insights pattern - AI suggestions (8 components)"""
        # Components: Heading, Insights, Alert, Badge, Button, Divider, Text, Chip
        
        heading = HeadingBuilder(f"{object_type} Intelligence", 2).build()
        
        # Insights component
        insights = InsightsBuilder(f"{object_type} Recommendations") \
            .with_description(f"AI-powered insights for this {object_type.lower()}") \
            .add_recommendation("Focus on high-value activities") \
            .add_recommendation("Schedule follow-up within 2 days") \
            .add_recommendation("Engage decision maker") \
            .info() \
            .with_confidence("92%") \
            .build()
        
        # Alert
        alert = AlertBuilder("New opportunity detected").success().dismissible().with_action("Review").build()
        
        # Priority badge
        priority_badge = BadgeBuilder("High Priority").danger().build()
        confidence_badge = BadgeBuilder("92% Confidence").info().pill_shape().build()
        
        # Description
        desc_text = TextBuilder("Based on historical data and current trends").small().build()
        
        # Category chips
        chip1 = ChipBuilder("Predictive").primary().build()
        chip2 = ChipBuilder("Actionable").success().build()
        
        divider = DividerBuilder().horizontal().build()
        apply_btn = ButtonBuilder("Apply Recommendations").primary().build()
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Insights", f"tab-{idx}")
        section = SectionBuilder("AI Insights", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading.type, heading.children, heading.classes, heading.props)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Insights")
        col2 = ColumnBuilder("AI", f"col-{idx}-2").add_component(insights.type, insights.children, insights.classes, insights.props)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Alert")
        col3 = ColumnBuilder("Opportunity", f"col-{idx}-3").add_component(alert.type, alert.children, alert.classes, alert.props)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Badges")
        col4 = ColumnBuilder("Status", f"col-{idx}-4") \
            .add_component(priority_badge.type, priority_badge.children, priority_badge.classes, priority_badge.props) \
            .add_component(confidence_badge.type, confidence_badge.children, confidence_badge.classes, confidence_badge.props) \
            .add_component(desc_text.type, desc_text.children, desc_text.classes, desc_text.props)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Categories")
        col5 = ColumnBuilder("Types", f"col-{idx}-5") \
            .add_component(chip1.type, chip1.children, chip1.classes, chip1.props) \
            .add_component(chip2.type, chip2.children, chip2.classes, chip2.props)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Divider")
        col6 = ColumnBuilder("Div", f"col-{idx}-6").add_component(divider.type, divider.children, divider.classes, divider.props)
        row6.add_column(col6)
        
        row7 = RowBuilder(f"row-{idx}-7", "Action")
        col7 = ColumnBuilder("Button", f"col-{idx}-7").add_component(apply_btn.type, apply_btn.children, apply_btn.classes, apply_btn.props)
        row7.add_column(col7)
        
        section.add_rows(row1, row2, row3, row4, row5, row6, row7)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_generic_pattern_layout(self, pattern: str, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generic pattern layout generator for patterns without specific implementation"""
        components = PATTERN_COMPONENTS.get(pattern, ["Heading", "Description", "Button"])
        
        heading = HeadingBuilder(f"{object_type} - {pattern.replace('_', ' ').title()}", 2).build()
        desc = DescriptionBuilder(f"This is a {pattern} view for {object_type}").build()
        button = ButtonBuilder("Action").primary().build()
        
        layout = LayoutBuilder()
        tab = TabBuilder(pattern.title(), f"tab-{idx}")
        section = SectionBuilder("Content", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading.type, heading.children, heading.classes, heading.props)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Desc")
        col2 = ColumnBuilder("Description", f"col-{idx}-2").add_component(desc.type, desc.children, desc.classes, desc.props)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Action")
        col3 = ColumnBuilder("Button", f"col-{idx}-3").add_component(button.type, button.children, button.classes, button.props)
        row3.add_column(col3)
        
        section.add_rows(row1, row2, row3)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    # ============ GENERATION METHODS ============
    
    def generate_all_layouts(self) -> List[Dict[str, Any]]:
        """Generate pattern-based CRM dataset using PATTERN_BASED_QUERIES"""
        records = []
        idx = 1
        
        # Pattern to generator mapping
        pattern_generators = {
            "basic_detail": self.generate_basic_detail_layout,
            "metrics_dashboard": self.generate_metrics_dashboard_layout,
            "contact_list_card": self.generate_contact_list_card_layout,
            "insights": self.generate_insights_layout,
        }
        
        # Iterate through all pattern-based queries (6 objects × patterns)
        for object_type, patterns in PATTERN_BASED_QUERIES.items():
            for pattern, queries in patterns.items():
                for query in queries:
                    # Get sample data for this object
                    data = self.get_sample_data(object_type, idx)
                    
                    # Get the appropriate generator for this pattern
                    if pattern in pattern_generators:
                        layout = pattern_generators[pattern](object_type, data, idx)
                    else:
                        layout = self.generate_generic_pattern_layout(pattern, object_type, data, idx)
                    
                    # Get components for this pattern
                    components_used = PATTERN_COMPONENTS.get(pattern, ["Heading", "Description", "Button"])
                    
                    # Create record
                    records.append({
                        "id": f"crm_{idx}",
                        "query": query,
                        "pattern": pattern,
                        "components": components_used,
                        "entity": object_type.lower(),
                        "view_type": pattern,
                        "layout": layout.to_dict(),
                        "score": 0.95
                    })
                    
                    idx += 1
        
        return records
    
    def save_dataset(self):
        """Save dataset in both JSONL and JSON formats"""
        records = self.generate_all_layouts()
        
        # Save as JSONL
        jsonl_path = self.output_dir / "crm_layouts.jsonl"
        with open(jsonl_path, 'w', encoding='utf-8') as f:
            f.writelines(map(lambda r: json.dumps(r) + '\n', records))
        
        # Save as JSON
        json_path = self.output_dir / "crm_layouts.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(records, f, indent=2, ensure_ascii=False)
        
        return {
            "total_records": len(records),
            "jsonl_path": str(jsonl_path),
            "json_path": str(json_path),
            "patterns": list(set(r["pattern"] for r in records)),
            "entities": list(set(r["entity"] for r in records))
        }


if __name__ == "__main__":
    print("Generating CRM dataset...")
    generator = CRMLayoutGenerator()
    result = generator.save_dataset()
    
    print(f"\n✅ Dataset generated successfully!")
    print(f"Total records: {result['total_records']}")
    print(f"JSONL file: {result['jsonl_path']}")
    print(f"JSON file: {result['json_path']}")
    print(f"\nPatterns: {', '.join(result['patterns'])}")
    print(f"Entities: {', '.join(result['entities'])}")
