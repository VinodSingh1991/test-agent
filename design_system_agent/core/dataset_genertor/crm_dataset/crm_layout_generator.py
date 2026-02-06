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
from design_system_agent.core.dataset_genertor.component_badge.patterns import success_badge, warning_badge, info_badge, primary_badge, secondary_badge, danger_badge
from design_system_agent.core.dataset_genertor.component_chip.patterns import primary_chip, secondary_chip
from design_system_agent.core.dataset_genertor.component_divider.patterns import horizontal_divider
from design_system_agent.core.dataset_genertor.component_label.patterns import form_label
from design_system_agent.core.dataset_genertor.component_text.patterns import body_text
from design_system_agent.core.dataset_genertor.component_link.patterns import standard_link

# Pattern and query configurations
from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    generate_full_dataset,
    get_query_metadata,
    get_layout_for_query,
    get_components_for_view_type,
    VIEW_TYPES,
    PATTERN_TO_VIEW_TYPE,
    VIEW_TYPE_COMPONENTS,
    OBJECTS,
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
        col1_1 = ColumnBuilder("Title", f"col-{idx}-1-1").add_component(heading)
        col1_2 = ColumnBuilder("Badges", f"col-{idx}-1-2") \
            .add_component(status_badge) \
            .add_component(priority_badge)
        col1_3 = ColumnBuilder("Avatar", f"col-{idx}-1-3").add_component(avatar)
        row1.add_column(col1_1).add_column(col1_2).add_column(col1_3)
        
        # Row 2: Divider
        row2 = RowBuilder(f"row-{idx}-2", "Divider")
        col2_1 = ColumnBuilder("Divider", f"col-{idx}-2-1").add_component(divider1)
        row2.add_column(col2_1)
        
        # Row 3: Fields
        row3 = RowBuilder(f"row-{idx}-3", "Fields")
        col3_1 = ColumnBuilder("Labels", f"col-{idx}-3-1") \
            .add_component(owner_label) \
            .add_component(owner_text) \
            .add_component(created_label) \
            .add_component(created_text)
        col3_2 = ColumnBuilder("Tags", f"col-{idx}-3-2") \
            .add_component(tag_chip1) \
            .add_component(tag_chip2)
        row3.add_column(col3_1).add_column(col3_2)
        
        # Row 4: Table
        row4 = RowBuilder(f"row-{idx}-4", "Table")
        col4_1 = ColumnBuilder("Details", f"col-{idx}-4-1").add_component(details_table)
        row4.add_column(col4_1)
        
        # Row 5: Actions
        row5 = RowBuilder(f"row-{idx}-5", "Actions")
        col5_1 = ColumnBuilder("Divider", f"col-{idx}-5-1").add_component(divider2)
        row5.add_column(col5_1)
        
        row6 = RowBuilder(f"row-{idx}-6", "Buttons")
        col6_1 = ColumnBuilder("Buttons", f"col-{idx}-6-1") \
            .add_component(edit_btn) \
            .add_component(delete_btn) \
            .add_component(related_link)
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
        col1 = ColumnBuilder("Heading", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        # Row 2: Metrics
        row2 = RowBuilder(f"row-{idx}-2", "Metrics")
        col2_1 = ColumnBuilder("Metric1", f"col-{idx}-2-1").add_component(revenue_metric)
        col2_2 = ColumnBuilder("Metric2", f"col-{idx}-2-2").add_component(count_metric)
        col2_3 = ColumnBuilder("Metric3", f"col-{idx}-2-3").add_component(rate_metric)
        row2.add_column(col2_1).add_column(col2_2).add_column(col2_3)
        
        # Row 3: Dashlets
        row3 = RowBuilder(f"row-{idx}-3", "Dashlets")
        col3_1 = ColumnBuilder("Dashlet1", f"col-{idx}-3-1").add_component(dashlet1)
        col3_2 = ColumnBuilder("Dashlet2", f"col-{idx}-3-2").add_component(dashlet2)
        row3.add_column(col3_1).add_column(col3_2)
        
        # Row 4: Card and Badge
        row4 = RowBuilder(f"row-{idx}-4", "Card")
        col4_1 = ColumnBuilder("Card", f"col-{idx}-4-1").add_component(card)
        col4_2 = ColumnBuilder("Badge", f"col-{idx}-4-2").add_component(up_badge)
        row4.add_column(col4_1).add_column(col4_2)
        
        # Row 5: Divider
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Divider", f"col-{idx}-5").add_component(divider)
        row5.add_column(col5)
        
        # Row 6: Buttons
        row6 = RowBuilder(f"row-{idx}-6", "Buttons")
        col6 = ColumnBuilder("Actions", f"col-{idx}-6") \
            .add_component(refresh_btn) \
            .add_component(export_btn)
        row6.add_column(col6)
        
        # Row 7: Table
        row7 = RowBuilder(f"row-{idx}-7", "Table")
        col7 = ColumnBuilder("Breakdown", f"col-{idx}-7").add_component(table)
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
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "ListCard")
        col2 = ColumnBuilder("Contacts", f"col-{idx}-2").add_component(listcard)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Details")
        col3 = ColumnBuilder("ContactInfo", f"col-{idx}-3") \
            .add_component(avatar) \
            .add_component(status_badge) \
            .add_component(role_text) \
            .add_component(profile_link)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Tags")
        col4 = ColumnBuilder("Tags", f"col-{idx}-4") \
            .add_component(tag1) \
            .add_component(tag2)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Div", f"col-{idx}-5").add_component(divider)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Actions")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(add_btn)
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
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Insights")
        col2 = ColumnBuilder("AI", f"col-{idx}-2").add_component(insights)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Alert")
        col3 = ColumnBuilder("Opportunity", f"col-{idx}-3").add_component(alert)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Badges")
        col4 = ColumnBuilder("Status", f"col-{idx}-4") \
            .add_component(priority_badge) \
            .add_component(confidence_badge) \
            .add_component(desc_text)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Categories")
        col5 = ColumnBuilder("Types", f"col-{idx}-5") \
            .add_component(chip1) \
            .add_component(chip2)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Divider")
        col6 = ColumnBuilder("Div", f"col-{idx}-6").add_component(divider)
        row6.add_column(col6)
        
        row7 = RowBuilder(f"row-{idx}-7", "Action")
        col7 = ColumnBuilder("Button", f"col-{idx}-7").add_component(apply_btn)
        row7.add_column(col7)
        
        section.add_rows(row1, row2, row3, row4, row5, row6, row7)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_list_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate list pattern - Tabular data display (7 components)"""
        # Components: Heading, Table, Badge, Chip, Button, Avatar, Link
        
        heading = h1_heading(f"All {object_type}s")
        
        # Filter chips
        chip1 = primary_chip("Active")
        chip2 = secondary_chip("All Statuses")
        
        # Data table with status badges
        table = TableBuilder() \
            .set_headers("Name", "Owner", "Status", "Priority", "Actions") \
            .add_row([f"{object_type} 1", self.sample_names[0], "Active", "High", "View"]) \
            .add_row([f"{object_type} 2", self.sample_names[1], "Pending", "Medium", "View"]) \
            .add_row([f"{object_type} 3", self.sample_names[2], "Closed", "Low", "View"]) \
            .add_row([f"{object_type} 4", self.sample_names[3], "Active", "High", "View"]) \
            .striped().build()
        
        # Row action buttons
        view_btn = primary_button("View Selected")
        export_btn = secondary_button("Export")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder(f"{object_type} List", f"tab-{idx}")
        section = SectionBuilder("List View", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Filters")
        col2 = ColumnBuilder("Chips", f"col-{idx}-2") \
            .add_component(chip1) \
            .add_component(chip2)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Table")
        col3 = ColumnBuilder("Data", f"col-{idx}-3").add_component(table)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Actions")
        col4 = ColumnBuilder("Buttons", f"col-{idx}-4") \
            .add_component(view_btn) \
            .add_component(export_btn)
        row4.add_column(col4)
        
        section.add_rows(row1, row2, row3, row4)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_list_summary_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate list_summary pattern - List with summary metrics (7 components)"""
        # Components: Heading, Metric, Divider, Table, Badge, Chip, Button
        
        heading = h2_heading(f"{object_type} Overview")
        
        # Summary metrics
        total_metric = MetricBuilder("1,234", f"Total {object_type}s").with_change("+15%", "up").build()
        active_metric = MetricBuilder("856", "Active").with_change("+8%", "up").build()
        closed_metric = MetricBuilder("378", "Closed").with_change("-3%", "down").build()
        
        divider = horizontal_divider()
        
        # Filter chips
        filter_chip = primary_chip("This Quarter")
        
        # Summary table
        table = TableBuilder() \
            .set_headers("Status", "Count", "Revenue", "%") \
            .add_row(["Active", "856", "$2.5M", "69%"]) \
            .add_row(["Pending", "234", "$850K", "19%"]) \
            .add_row(["Closed", "144", "$320K", "12%"]) \
            .striped().build()
        
        refresh_btn = primary_button("Refresh")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Summary", f"tab-{idx}")
        section = SectionBuilder("Overview", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Metrics")
        col2_1 = ColumnBuilder("M1", f"col-{idx}-2-1").add_component(total_metric)
        col2_2 = ColumnBuilder("M2", f"col-{idx}-2-2").add_component(active_metric)
        col2_3 = ColumnBuilder("M3", f"col-{idx}-2-3").add_component(closed_metric)
        row2.add_column(col2_1).add_column(col2_2).add_column(col2_3)
        
        row3 = RowBuilder(f"row-{idx}-3", "Divider")
        col3 = ColumnBuilder("Div", f"col-{idx}-3").add_component(divider)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Filter")
        col4 = ColumnBuilder("Chip", f"col-{idx}-4").add_component(filter_chip)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Table")
        col5 = ColumnBuilder("Data", f"col-{idx}-5").add_component(table)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Action")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(refresh_btn)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_grid_card_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate grid_card pattern - Multiple cards in grid (8 components)"""
        # Components: Heading, Card, Image, Badge, Text, Button, Chip, Avatar
        
        heading = h1_heading(f"{object_type} Card View")
        
        # Grid of cards
        card1 = CardBuilder(f"{object_type} Alpha").elevated() \
            .with_header("High Priority") \
            .add_body_content(f"Owner: {self.sample_names[0]}") \
            .add_body_content("Status: Active") \
            .with_footer("View Details") \
            .build()
        
        card2 = CardBuilder(f"{object_type} Beta").elevated() \
            .with_header("Medium Priority") \
            .add_body_content(f"Owner: {self.sample_names[1]}") \
            .add_body_content("Status: Pending") \
            .with_footer("View Details") \
            .build()
        
        card3 = CardBuilder(f"{object_type} Gamma").elevated() \
            .with_header("Low Priority") \
            .add_body_content(f"Owner: {self.sample_names[2]}") \
            .add_body_content("Status: Closed") \
            .with_footer("View Details") \
            .build()
        
        # Filter controls
        filter_chip1 = primary_chip("All")
        filter_chip2 = secondary_chip("Active Only")
        
        add_btn = primary_button(f"Add {object_type}")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Card View", f"tab-{idx}")
        section = SectionBuilder("Cards", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Filters")
        col2 = ColumnBuilder("Chips", f"col-{idx}-2") \
            .add_component(filter_chip1) \
            .add_component(filter_chip2)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Grid")
        col3_1 = ColumnBuilder("Card1", f"col-{idx}-3-1").add_component(card1)
        col3_2 = ColumnBuilder("Card2", f"col-{idx}-3-2").add_component(card2)
        col3_3 = ColumnBuilder("Card3", f"col-{idx}-3-3").add_component(card3)
        row3.add_column(col3_1).add_column(col3_2).add_column(col3_3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Action")
        col4 = ColumnBuilder("Button", f"col-{idx}-4").add_component(add_btn)
        row4.add_column(col4)
        
        section.add_rows(row1, row2, row3, row4)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_timeline_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate timeline pattern - Chronological activity (8 components)"""
        # Components: Heading, Stack, Avatar, Text, Badge, Divider, Link, Chip
        
        heading = h2_heading(f"{object_type} Timeline")
        
        # Timeline entries
        avatar1 = AvatarBuilder("/user1.jpg").small().build()
        activity1 = body_text(f"Created {object_type.lower()} record")
        badge1 = info_badge("Created")
        time1 = body_text("2 hours ago")
        
        divider1 = horizontal_divider()
        
        avatar2 = AvatarBuilder("/user2.jpg").small().build()
        activity2 = body_text(f"Updated status to Active")
        badge2 = success_badge("Updated")
        time2 = body_text("1 hour ago")
        
        divider2 = horizontal_divider()
        
        avatar3 = AvatarBuilder("/user3.jpg").small().build()
        activity3 = body_text(f"Added comment")
        badge3 = primary_badge("Comment")
        time3 = body_text("30 minutes ago")
        
        filter_chip = primary_chip("All Activity")
        load_more_btn = secondary_button("Load More")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Timeline", f"tab-{idx}")
        section = SectionBuilder("Activity", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Filter")
        col2 = ColumnBuilder("Chip", f"col-{idx}-2").add_component(filter_chip)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Activity1")
        col3 = ColumnBuilder("Entry1", f"col-{idx}-3") \
            .add_component(avatar1) \
            .add_component(activity1) \
            .add_component(badge1) \
            .add_component(time1) \
            .add_component(divider1)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Activity2")
        col4 = ColumnBuilder("Entry2", f"col-{idx}-4") \
            .add_component(avatar2) \
            .add_component(activity2) \
            .add_component(badge2) \
            .add_component(time2) \
            .add_component(divider2)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Activity3")
        col5 = ColumnBuilder("Entry3", f"col-{idx}-5") \
            .add_component(avatar3) \
            .add_component(activity3) \
            .add_component(badge3) \
            .add_component(time3)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "LoadMore")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(load_more_btn)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_hierarchy_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate hierarchy pattern - Tree structure (7 components)"""
        # Components: Heading, Stack, Divider, Badge, Text, Avatar, Button
        
        heading = h2_heading(f"{object_type} Hierarchy")
        
        # Root level
        root_text = body_text(f"Root: {data['name']}")
        root_badge = primary_badge("Level 1")
        root_avatar = AvatarBuilder("/root.jpg").small().build()
        expand_btn = secondary_button("Expand All")
        
        divider1 = horizontal_divider()
        
        # Child level
        child1_text = body_text(f"Child: {self.sample_companies[0]}")
        child1_badge = secondary_badge("Level 2")
        
        divider2 = horizontal_divider()
        
        child2_text = body_text(f"Child: {self.sample_companies[1]}")
        child2_badge = secondary_badge("Level 2")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Hierarchy", f"tab-{idx}")
        section = SectionBuilder("Tree", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Controls")
        col2 = ColumnBuilder("Button", f"col-{idx}-2").add_component(expand_btn)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Root")
        col3 = ColumnBuilder("RootNode", f"col-{idx}-3") \
            .add_component(root_avatar) \
            .add_component(root_text) \
            .add_component(root_badge) \
            .add_component(divider1)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Child1")
        col4 = ColumnBuilder("ChildNode1", f"col-{idx}-4") \
            .add_component(child1_text) \
            .add_component(child1_badge) \
            .add_component(divider2)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Child2")
        col5 = ColumnBuilder("ChildNode2", f"col-{idx}-5") \
            .add_component(child2_text) \
            .add_component(child2_badge)
        row5.add_column(col5)
        
        section.add_rows(row1, row2, row3, row4, row5)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_analytics_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate analytics pattern - Data insights (8 components)"""
        # Components: Heading, Metric, Dashlet, Table, Badge, Divider, Button, Chip
        
        heading = h1_heading(f"{object_type} Analytics")
        
        # KPI metrics
        metric1 = MetricBuilder(data['revenue'], "Total Revenue").with_change("+18%", "up").build()
        metric2 = MetricBuilder(f"{data['confidence']}%", "Success Rate").with_change("+5%", "up").build()
        
        # Dashlets
        dashlet1 = DashletBuilder("Top Performers").add_content("5 active records").with_action("View").build()
        dashlet2 = DashletBuilder("Trend Analysis").add_content("Growth: +15%").build()
        
        trend_badge = success_badge("Trending Up")
        
        divider = horizontal_divider()
        
        # Analytics table
        table = TableBuilder() \
            .set_headers("Metric", "Current", "Previous", "Change") \
            .add_row(["Conversion Rate", "42%", "38%", "+4%"]) \
            .add_row(["Avg Deal Size", "$125K", "$110K", "+14%"]) \
            .add_row(["Time to Close", "45 days", "52 days", "-7 days"]) \
            .striped().build()
        
        filter_chip = primary_chip("Last Quarter")
        export_btn = secondary_button("Export Report")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Analytics", f"tab-{idx}")
        section = SectionBuilder("Insights", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "KPIs")
        col2_1 = ColumnBuilder("M1", f"col-{idx}-2-1").add_component(metric1)
        col2_2 = ColumnBuilder("M2", f"col-{idx}-2-2").add_component(metric2)
        row2.add_column(col2_1).add_column(col2_2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Widgets")
        col3_1 = ColumnBuilder("D1", f"col-{idx}-3-1").add_component(dashlet1)
        col3_2 = ColumnBuilder("D2", f"col-{idx}-3-2").add_component(dashlet2)
        col3_3 = ColumnBuilder("Badge", f"col-{idx}-3-3").add_component(trend_badge)
        row3.add_column(col3_1).add_column(col3_2).add_column(col3_3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Divider")
        col4 = ColumnBuilder("Div", f"col-{idx}-4").add_component(divider)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Filter")
        col5 = ColumnBuilder("Chip", f"col-{idx}-5").add_component(filter_chip)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Table")
        col6 = ColumnBuilder("Data", f"col-{idx}-6").add_component(table)
        row6.add_column(col6)
        
        row7 = RowBuilder(f"row-{idx}-7", "Action")
        col7 = ColumnBuilder("Button", f"col-{idx}-7").add_component(export_btn)
        row7.add_column(col7)
        
        section.add_rows(row1, row2, row3, row4, row5, row6, row7)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_related_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate related pattern - Connected entities (8 components)"""
        # Components: Heading, ListCard, Avatar, Badge, Link, Button, Chip, Divider
        
        heading = h2_heading(f"Related to {object_type}")
        
        # Related items list
        listcard = ListCardBuilder(f"Related {object_type}s") \
            .add_item("/rel1.jpg", "Related Record 1", "Opportunity", "Active") \
            .add_item("/rel2.jpg", "Related Record 2", "Account", "Pending") \
            .add_item("/rel3.jpg", "Related Record 3", "Contact", "Active") \
            .build()
        
        # Relationship type chips
        chip1 = primary_chip("Parent")
        chip2 = secondary_chip("Child")
        chip3 = info_badge("Sibling")
        
        divider = horizontal_divider()
        
        # Actions
        add_relation_btn = primary_button("Add Relation")
        view_all_link = standard_link("View All Related")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Related", f"tab-{idx}")
        section = SectionBuilder("Relationships", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Types")
        col2 = ColumnBuilder("Chips", f"col-{idx}-2") \
            .add_component(chip1) \
            .add_component(chip2) \
            .add_component(chip3)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "List")
        col3 = ColumnBuilder("Items", f"col-{idx}-3").add_component(listcard)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Divider")
        col4 = ColumnBuilder("Div", f"col-{idx}-4").add_component(divider)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Actions")
        col5 = ColumnBuilder("Controls", f"col-{idx}-5") \
            .add_component(add_relation_btn) \
            .add_component(view_all_link)
        row5.add_column(col5)
        
        section.add_rows(row1, row2, row3, row4, row5)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_alerts_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate alerts pattern - Important messages (7 components)"""
        # Components: Heading, Alert, Badge, Button, Divider, Avatar, Link
        
        heading = h2_heading(f"{object_type} Alerts")
        
        # Alert messages
        alert1 = AlertBuilder(f"High priority {object_type.lower()} requires attention").danger().dismissible().with_action("Review").build()
        alert2 = AlertBuilder(f"{object_type} status updated successfully").success().dismissible().build()
        alert3 = AlertBuilder(f"Upcoming deadline for {object_type.lower()}").warning().with_action("View").build()
        
        # Severity badges
        critical_badge = danger_button("Critical")
        
        divider = horizontal_divider()
        
        # Actions
        view_all_btn = secondary_button("View All Alerts")
        settings_link = standard_link("Alert Settings")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Alerts", f"tab-{idx}")
        section = SectionBuilder("Notifications", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Alert1")
        col2 = ColumnBuilder("A1", f"col-{idx}-2").add_component(alert1)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Alert2")
        col3 = ColumnBuilder("A2", f"col-{idx}-3").add_component(alert2)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Alert3")
        col4 = ColumnBuilder("A3", f"col-{idx}-4").add_component(alert3)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Severity")
        col5 = ColumnBuilder("Badge", f"col-{idx}-5").add_component(critical_badge)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Divider")
        col6 = ColumnBuilder("Div", f"col-{idx}-6").add_component(divider)
        row6.add_column(col6)
        
        row7 = RowBuilder(f"row-{idx}-7", "Actions")
        col7 = ColumnBuilder("Controls", f"col-{idx}-7") \
            .add_component(view_all_btn) \
            .add_component(settings_link)
        row7.add_column(col7)
        
        section.add_rows(row1, row2, row3, row4, row5, row6, row7)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_activity_feed_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate activity_feed pattern - Recent updates (9 components)"""
        # Components: Heading, Stack, Avatar, Badge, Text, Link, Divider, Button, Chip
        
        heading = h2_heading(f"{object_type} Activity Feed")
        
        # Filter chip
        filter_chip = primary_chip("All Activity")
        
        # Activity entries
        avatar1 = AvatarBuilder("/user1.jpg").small().build()
        activity1_text = body_text(f"{self.sample_names[0]} created {object_type.lower()}")
        activity1_badge = success_badge("Created")
        activity1_link = standard_link("View")
        
        divider1 = horizontal_divider()
        
        avatar2 = AvatarBuilder("/user2.jpg").small().build()
        activity2_text = body_text(f"{self.sample_names[1]} updated status")
        activity2_badge = info_badge("Updated")
        
        divider2 = horizontal_divider()
        
        avatar3 = AvatarBuilder("/user3.jpg").small().build()
        activity3_text = body_text(f"{self.sample_names[2]} added comment")
        activity3_badge = primary_badge("Comment")
        
        load_more_btn = secondary_button("Load More")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Activity", f"tab-{idx}")
        section = SectionBuilder("Feed", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Filter")
        col2 = ColumnBuilder("Chip", f"col-{idx}-2").add_component(filter_chip)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Entry1")
        col3 = ColumnBuilder("Act1", f"col-{idx}-3") \
            .add_component(avatar1) \
            .add_component(activity1_text) \
            .add_component(activity1_badge) \
            .add_component(activity1_link) \
            .add_component(divider1)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Entry2")
        col4 = ColumnBuilder("Act2", f"col-{idx}-4") \
            .add_component(avatar2) \
            .add_component(activity2_text) \
            .add_component(activity2_badge) \
            .add_component(divider2)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Entry3")
        col5 = ColumnBuilder("Act3", f"col-{idx}-5") \
            .add_component(avatar3) \
            .add_component(activity3_text) \
            .add_component(activity3_badge)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "LoadMore")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(load_more_btn)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_celebrations_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate celebrations pattern - Special occasions (7 components)"""
        # Components: Heading, BirthdayCard, Avatar, Badge, Card, Button, Divider
        
        heading = h2_heading(f"{object_type} Celebrations")
        
        # Birthday cards
        birthday_card = BirthdayCardBuilder(self.sample_names[0], "Feb 15") \
            .with_message("Happy Birthday!") \
            .with_avatar("/birthday.jpg") \
            .build()
        
        # Occasion cards
        card = CardBuilder("Work Anniversary").elevated() \
            .add_body_content(f"{self.sample_names[1]} - 5 years") \
            .with_footer("Send Wishes") \
            .build()
        
        occasion_badge = success_badge("Birthday")
        anniversary_badge = info_badge("Anniversary")
        
        divider = horizontal_divider()
        
        send_wishes_btn = primary_button("Send Wishes")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Celebrations", f"tab-{idx}")
        section = SectionBuilder("Occasions", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Birthday")
        col2 = ColumnBuilder("BCard", f"col-{idx}-2").add_component(birthday_card)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Anniversary")
        col3 = ColumnBuilder("ACard", f"col-{idx}-3").add_component(card)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Badges")
        col4 = ColumnBuilder("Types", f"col-{idx}-4") \
            .add_component(occasion_badge) \
            .add_component(anniversary_badge)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Div", f"col-{idx}-5").add_component(divider)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Action")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(send_wishes_btn)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_dashlet_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate dashlet pattern - Compact widget (6 components)"""
        # Components: Dashlet, Metric, Badge, Button, Avatar, Link
        
        # Main dashlet
        dashlet = DashletBuilder(f"{object_type} Summary") \
            .add_content(f"Total: {data['revenue']}") \
            .add_content(f"Status: {data['status']}") \
            .with_action("View Details") \
            .build()
        
        # Metric widget
        metric = MetricBuilder("1,234", f"{object_type}s").with_change("+12%", "up").build()
        
        status_badge = success_badge(data['status'])
        avatar = AvatarBuilder(data['avatar']).small().build()
        
        view_btn = primary_button("Open")
        details_link = standard_link("Full View")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Widget", f"tab-{idx}")
        section = SectionBuilder("Dashlet", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Dashlet")
        col1 = ColumnBuilder("Widget", f"col-{idx}-1").add_component(dashlet)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Metric")
        col2 = ColumnBuilder("KPI", f"col-{idx}-2").add_component(metric)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Status")
        col3_1 = ColumnBuilder("Badge", f"col-{idx}-3-1").add_component(status_badge)
        col3_2 = ColumnBuilder("Avatar", f"col-{idx}-3-2").add_component(avatar)
        row3.add_column(col3_1).add_column(col3_2)
        
        row4 = RowBuilder(f"row-{idx}-4", "Actions")
        col4 = ColumnBuilder("Controls", f"col-{idx}-4") \
            .add_component(view_btn) \
            .add_component(details_link)
        row4.add_column(col4)
        
        section.add_rows(row1, row2, row3, row4)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_summarize_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate summarize pattern - Quick overview (6 components)"""
        # Components: Heading, Text, Metric, Badge, Divider, Button
        
        heading = h2_heading(f"{object_type} Summary")
        
        summary_text = body_text(f"Quick overview of {object_type.lower()} {data['name']} with key highlights")
        
        # Key metrics
        revenue_metric = MetricBuilder(data['revenue'], "Value").build()
        confidence_metric = MetricBuilder(f"{data['confidence']}%", "Confidence").build()
        
        status_badge = success_badge(data['status'])
        priority_badge = warning_badge(data['priority'])
        
        divider = horizontal_divider()
        
        view_full_btn = primary_button("View Full Details")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Summary", f"tab-{idx}")
        section = SectionBuilder("Overview", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Description")
        col2 = ColumnBuilder("Text", f"col-{idx}-2").add_component(summary_text)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Metrics")
        col3_1 = ColumnBuilder("M1", f"col-{idx}-3-1").add_component(revenue_metric)
        col3_2 = ColumnBuilder("M2", f"col-{idx}-3-2").add_component(confidence_metric)
        row3.add_column(col3_1).add_column(col3_2)
        
        row4 = RowBuilder(f"row-{idx}-4", "Badges")
        col4 = ColumnBuilder("Status", f"col-{idx}-4") \
            .add_component(status_badge) \
            .add_component(priority_badge)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Div", f"col-{idx}-5").add_component(divider)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Action")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(view_full_btn)
        row6.add_column(col6)
        
        section.add_rows(row1, row2, row3, row4, row5, row6)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_detail_card_layout(self, object_type: str, data: Dict, idx: int) -> LayoutBuilder:
        """Generate detail_card pattern - Card-based detail (10 components)"""
        # Components: Card, Heading, Avatar, Badge, Text, Divider, Label, Chip, Button, Link
        
        # Main detail card
        card = CardBuilder(f"{object_type}: {data['name']}").elevated() \
            .with_header(f"Priority: {data['priority']}") \
            .add_body_content(f"Owner: {data['owner']}") \
            .add_body_content(f"Status: {data['status']}") \
            .add_body_content(f"Created: {data['created']}") \
            .with_footer("Edit | Delete") \
            .build()
        
        heading = h2_heading(f"{object_type} Details")
        avatar = AvatarBuilder(data['avatar']).large().build()
        status_badge = success_badge(data['status'])
        priority_badge = warning_badge(data['priority'])
        
        desc_text = body_text(f"Detailed information for {object_type.lower()} record")
        
        divider = horizontal_divider()
        
        owner_label = form_label("Record Owner")
        
        tag1 = primary_chip("Enterprise")
        tag2 = secondary_chip("High Value")
        
        edit_btn = primary_button("Edit Card")
        view_link = standard_link("View Full Record")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Card Details", f"tab-{idx}")
        section = SectionBuilder("CardView", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1_1 = ColumnBuilder("Title", f"col-{idx}-1-1").add_component(heading)
        col1_2 = ColumnBuilder("Avatar", f"col-{idx}-1-2").add_component(avatar)
        row1.add_column(col1_1).add_column(col1_2)
        
        row2 = RowBuilder(f"row-{idx}-2", "Card")
        col2 = ColumnBuilder("MainCard", f"col-{idx}-2").add_component(card)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Badges")
        col3 = ColumnBuilder("Status", f"col-{idx}-3") \
            .add_component(status_badge) \
            .add_component(priority_badge)
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Description")
        col4 = ColumnBuilder("Text", f"col-{idx}-4") \
            .add_component(owner_label) \
            .add_component(desc_text)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Tags")
        col5 = ColumnBuilder("Chips", f"col-{idx}-5") \
            .add_component(tag1) \
            .add_component(tag2)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Divider")
        col6 = ColumnBuilder("Div", f"col-{idx}-6").add_component(divider)
        row6.add_column(col6)
        
        row7 = RowBuilder(f"row-{idx}-7", "Actions")
        col7 = ColumnBuilder("Controls", f"col-{idx}-7") \
            .add_component(edit_btn) \
            .add_component(view_link)
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
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Desc")
        col2 = ColumnBuilder("Description", f"col-{idx}-2").add_component(desc)
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Action")
        col3 = ColumnBuilder("Button", f"col-{idx}-3").add_component(button)
        row3.add_column(col3)
        
        section.add_rows(row1, row2, row3)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    # ============ GENERATION METHODS ============
    
    def generate_table_view_layout(self, query: str, metadata: Dict, data: Dict, object_type: str, idx: int) -> LayoutBuilder:
        """Generate table view layout - Uses Table component"""
        heading = h1_heading(query)
        
        # Filter chips based on complexity
        if metadata['view_level'] in ['medium', 'advanced']:
            filter_chip = primary_chip("Filter Active")
        
        # Table with data - using sample primitive format
        table = {
            "type": "Table",
            "additional_info": {
                "total_value": 3,
                "description": f"Table view for {object_type} data"
            },
            "header": {
                "image_url": "",
                "action_url": "",
                "icon": "table",
                "text": f"{object_type.capitalize()} Records",
                "description": f"List of {object_type} records"
            },
            "footer": {
                "view_more_url": f"/view-all-{object_type}",
                "icon": "arrow-right",
                "text": "View All",
                "description": "View all records"
            },
            "cells": [
                {"cell_key": "cell_1", "cell_type": "text", "cell_display_name": "Name"},
                {"cell_key": "cell_2", "cell_type": "text", "cell_display_name": "Owner"},
                {"cell_key": "cell_3", "cell_type": "badge", "cell_display_name": "Status"},
                {"cell_key": "cell_4", "cell_type": "text", "cell_display_name": "Revenue"},
                {"cell_key": "cell_5", "cell_type": "link", "cell_display_name": "Actions"}
            ],
            "data": [
                {
                    "cell_1": {"icon": "", "text": data['name']},
                    "cell_2": {"icon": "user", "text": data['owner']},
                    "cell_3": {"icon": "", "text": data['status']},
                    "cell_4": {"icon": "dollar-sign", "text": data['revenue']},
                    "cell_5": {"icon": "external-link", "text": "View Details", "url": f"/details/{idx}"}
                },
                {
                    "cell_1": {"icon": "", "text": self.sample_names[1]},
                    "cell_2": {"icon": "user", "text": "Manager"},
                    "cell_3": {"icon": "", "text": "Active"},
                    "cell_4": {"icon": "dollar-sign", "text": "$75,000"},
                    "cell_5": {"icon": "external-link", "text": "View Details", "url": f"/details/{idx+1}"}
                },
                {
                    "cell_1": {"icon": "", "text": self.sample_names[2]},
                    "cell_2": {"icon": "user", "text": data['owner']},
                    "cell_3": {"icon": "", "text": data['priority']},
                    "cell_4": {"icon": "dollar-sign", "text": "$125,000"},
                    "cell_5": {"icon": "external-link", "text": "View Details", "url": f"/details/{idx+2}"}
                }
            ]
        }
        
        # Status badges
        status_badge = success_badge(data['status'])
        
        # Action buttons
        export_btn = secondary_button("Export")
        refresh_btn = primary_button("Refresh")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Table View", f"tab-{idx}")
        section = SectionBuilder("Data", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        if metadata['view_level'] in ['medium', 'advanced']:
            row2 = RowBuilder(f"row-{idx}-2", "Filters")
            col2 = ColumnBuilder("Chips", f"col-{idx}-2").add_component(filter_chip)
            row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Table")
        col3 = ColumnBuilder("Data", f"col-{idx}-3")
        col3._children = table  # Direct assignment for custom component
        row3.add_column(col3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Actions")
        col4 = ColumnBuilder("Buttons", f"col-{idx}-4") \
            .add_component(export_btn) \
            .add_component(refresh_btn)
        row4.add_column(col4)
        
        if metadata['view_level'] in ['medium', 'advanced']:
            section.add_rows(row1, row2, row3, row4)
        else:
            section.add_rows(row1, row3, row4)
        
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_list_view_layout(self, query: str, metadata: Dict, data: Dict, object_type: str, idx: int) -> LayoutBuilder:
        """Generate list view layout - Uses ListCard component"""
        heading = h2_heading(query)
        
        # ListCard with items - using sample primitive format
        listcard = {
            "type": "Listcard",
            "additional_info": {
                "total_value": 3,
                "description": f"List of {object_type} related items"
            },
            "header": {
                "image_url": "",
                "action_url": f"/manage-{object_type}",
                "icon": "list",
                "text": f"{object_type.capitalize()} Activities",
                "description": f"Recent {object_type} activities and updates"
            },
            "footer": {
                "view_more_url": f"/all-{object_type}-activities",
                "icon": "arrow-right",
                "text": "Load More",
                "description": "View all activities"
            },
            "cells": [
                {"cell_key": "cell_1", "cell_type": "text", "cell_display_name": "Title"},
                {"cell_key": "cell_2", "cell_type": "text", "cell_display_name": "Description"},
                {"cell_key": "cell_3", "cell_type": "badge", "cell_display_name": "Status"},
                {"cell_key": "cell_4", "cell_type": "text", "cell_display_name": "Owner"}
            ],
            "data": [
                {
                    "cell_1": {"icon": "user", "text": data['name']},
                    "cell_2": {"icon": "", "text": f"Updated {object_type} information"},
                    "cell_3": {"icon": "", "text": data['status']},
                    "cell_4": {"icon": "user-circle", "text": data['owner']}
                },
                {
                    "cell_1": {"icon": "activity", "text": self.sample_names[1]},
                    "cell_2": {"icon": "", "text": "New activity logged"},
                    "cell_3": {"icon": "", "text": "Active"},
                    "cell_4": {"icon": "user-circle", "text": "Manager"}
                },
                {
                    "cell_1": {"icon": "check-circle", "text": self.sample_names[2]},
                    "cell_2": {"icon": "", "text": "Review completed"},
                    "cell_3": {"icon": "", "text": "Pending"},
                    "cell_4": {"icon": "user-circle", "text": "Analyst"}
                }
            ]
        }
        
        # Supporting components based on complexity
        avatar = AvatarBuilder(data['avatar']).medium().build()
        status_badge = success_badge(data['status'])
        divider = horizontal_divider()
        
        if metadata['view_level'] == 'advanced':
            detail_link = standard_link("View Full Details")
            chip = primary_chip("Active Items")
        
        add_btn = primary_button("Add Item")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("List View", f"tab-{idx}")
        section = SectionBuilder("Items", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "ListCard")
        col2 = ColumnBuilder("Items", f"col-{idx}-2")
        col2._children = listcard  # Direct assignment for custom component
        row2.add_column(col2)
        
        row3 = RowBuilder(f"row-{idx}-3", "Details")
        col3 = ColumnBuilder("Info", f"col-{idx}-3") \
            .add_component(avatar) \
            .add_component(status_badge)
        row3.add_column(col3)
        
        if metadata['view_level'] == 'advanced':
            row4 = RowBuilder(f"row-{idx}-4", "Advanced")
            col4 = ColumnBuilder("Extra", f"col-{idx}-4") \
                .add_component(chip) \
                .add_component(detail_link)
            row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Divider")
        col5 = ColumnBuilder("Div", f"col-{idx}-5").add_component(divider)
        row5.add_column(col5)
        
        row6 = RowBuilder(f"row-{idx}-6", "Action")
        col6 = ColumnBuilder("Button", f"col-{idx}-6").add_component(add_btn)
        row6.add_column(col6)
        
        if metadata['view_level'] == 'advanced':
            section.add_rows(row1, row2, row3, row4, row5, row6)
        else:
            section.add_rows(row1, row2, row3, row5, row6)
        
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_card_view_layout(self, query: str, metadata: Dict, data: Dict, object_type: str, idx: int) -> LayoutBuilder:
        """Generate card view layout - Uses Card and Metric components"""
        heading = h1_heading(query)
        
        # Metrics (required for card view)
        metric1 = MetricBuilder(data['revenue'], "Total Value").with_change("+12%", "up").build()
        metric2 = MetricBuilder(f"{data['confidence']}%", "Confidence").with_change("+5%", "up").build()
        
        # Cards
        card1 = CardBuilder("Summary Card").elevated() \
            .add_body_content(f"Status: {data['status']}") \
            .add_body_content(f"Owner: {data['owner']}") \
            .with_footer("View Details") \
            .build()
        
        # Advanced components
        if metadata['view_level'] == 'advanced':
            dashlet = DashletBuilder("Quick Stats") \
                .add_content(f"Total: {data['revenue']}") \
                .with_action("Expand") \
                .build()
            
            card2 = CardBuilder("Insights").elevated() \
                .add_body_content("Growth trending upward") \
                .add_body_content("Performance exceeds target") \
                .build()
        
        status_badge = success_badge(data['status'])
        divider = horizontal_divider()
        
        refresh_btn = primary_button("Refresh")
        export_btn = secondary_button("Export")
        
        # Build layout
        layout = LayoutBuilder()
        tab = TabBuilder("Card View", f"tab-{idx}")
        section = SectionBuilder("Dashboard", f"sec-{idx}")
        
        row1 = RowBuilder(f"row-{idx}-1", "Header")
        col1 = ColumnBuilder("Title", f"col-{idx}-1").add_component(heading)
        row1.add_column(col1)
        
        row2 = RowBuilder(f"row-{idx}-2", "Metrics")
        col2_1 = ColumnBuilder("M1", f"col-{idx}-2-1").add_component(metric1)
        col2_2 = ColumnBuilder("M2", f"col-{idx}-2-2").add_component(metric2)
        col2_3 = ColumnBuilder("Badge", f"col-{idx}-2-3").add_component(status_badge)
        row2.add_column(col2_1).add_column(col2_2).add_column(col2_3)
        
        row3 = RowBuilder(f"row-{idx}-3", "Cards")
        col3_1 = ColumnBuilder("C1", f"col-{idx}-3-1").add_component(card1)
        row3.add_column(col3_1)
        
        if metadata['view_level'] == 'advanced':
            col3_2 = ColumnBuilder("C2", f"col-{idx}-3-2").add_component(card2)
            col3_3 = ColumnBuilder("Dashlet", f"col-{idx}-3-3").add_component(dashlet)
            row3.add_column(col3_2).add_column(col3_3)
        
        row4 = RowBuilder(f"row-{idx}-4", "Divider")
        col4 = ColumnBuilder("Div", f"col-{idx}-4").add_component(divider)
        row4.add_column(col4)
        
        row5 = RowBuilder(f"row-{idx}-5", "Actions")
        col5 = ColumnBuilder("Buttons", f"col-{idx}-5") \
            .add_component(refresh_btn) \
            .add_component(export_btn)
        row5.add_column(col5)
        
        section.add_rows(row1, row2, row3, row4, row5)
        tab.add_section(section)
        layout.add_tab(tab)
        
        return layout
    
    def generate_all_layouts(self) -> List[Dict[str, Any]]:
        """Generate layouts using new query generation system with view types"""
        records = []
        
        # Generate queries using the new system
        queries = generate_full_dataset(2000)
        
        print(f"Generated {len(queries)} queries from new query system")
        
        # View type to generator mapping
        view_type_generators = {
            "table": self.generate_table_view_layout,
            "list": self.generate_list_view_layout,
            "card": self.generate_card_view_layout,
        }
        
        for idx, query in enumerate(queries, 1):
            # Get metadata for this query (includes view type, components, etc.)
            metadata = get_query_metadata(query)
            layout_info = get_layout_for_query(query)
            
            # Determine object type from query
            object_type = "lead"  # default
            for obj in OBJECTS.keys():
                if obj in query.lower():
                    object_type = obj
                    break
            
            # Get sample data
            data = self.get_sample_data(object_type, idx)
            
            # Get the appropriate generator for this view type
            view_type = metadata['view_type']
            generator = view_type_generators.get(view_type, self.generate_table_view_layout)
            
            # Generate layout
            layout = generator(query, metadata, data, object_type, idx)
            
            # Create record with metadata
            records.append({
                "id": f"crm_{idx}",
                "query": query,
                "pattern": metadata['pattern'],
                "view_type": view_type,
                "view_level": metadata['view_level'],
                "primary_component": metadata['primary_component'],
                "components_required": metadata['components_required'],
                "components_optional": metadata['components_optional'],
                "components": metadata['all_components'],
                "entity": object_type,
                "layout_structure": layout_info['layout_structure'],
                "layout": layout.to_dict(),
                "score": 0.95
            })
            
            # Progress indicator
            if idx % 500 == 0:
                print(f"  Processed {idx} queries...")
        
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
