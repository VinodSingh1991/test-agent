"""
Component Layout Builder Module

This module provides a builder pattern for creating hierarchical layouts
with the structure: Tabs → Sections → Rows → Cols → Children
"""

# Data Models
from .builder.models import (
    Component,
    Column,
    Row,
    Section,
    Tab,
    Layout,
    TrainingData,
)

# Layout Builders
from .builder.component_builder import ComponentBuilder
from .builder.column_builder import ColumnBuilder
from .builder.row_builder import RowBuilder
from .builder.section_builder import SectionBuilder
from .builder.tab_builder import TabBuilder
from .builder.layout_builder import LayoutBuilder
from .builder.training_data_builder import TrainingDataBuilder

# Component Builders
from .builder.component_button.button_builder import ButtonBuilder
from .builder.component_heading.heading_builder import HeadingBuilder
from .builder.component_list.list_builder import ListBuilder
from .builder.component_description.description_builder import DescriptionBuilder

# Helper Functions
from .builder.helpers import (
    create_component,
    create_simple_layout,
)

__all__ = [
    # Data Classes
    "Component",
    "Column",
    "Row",
    "Section",
    "Tab",
    "Layout",
    "TrainingData",
    
    # Layout Builders
    "ComponentBuilder",
    "ColumnBuilder",
    "RowBuilder",
    "SectionBuilder",
    "TabBuilder",
    "LayoutBuilder",
    "TrainingDataBuilder",
    
    # Component Builders
    "ButtonBuilder",
    "HeadingBuilder",
    "ListBuilder",
    "DescriptionBuilder",
    
    # Helper Functions
    "create_component",
    "create_simple_layout",
]
