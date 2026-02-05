"""
Component Layout Builder Module

This module provides a builder pattern for creating hierarchical layouts
with the structure: Tabs → Sections → Rows → Cols → Children
"""

# Data Models
from .models import (
    Component,
    Column,
    Row,
    Section,
    Tab,
    Layout,
    TrainingData,
)

# Layout Builders
from .component_builder import ComponentBuilder
from .column_builder import ColumnBuilder
from .row_builder import RowBuilder
from .section_builder import SectionBuilder
from .tab_builder import TabBuilder
from .layout_builder import LayoutBuilder
from .training_data_builder import TrainingDataBuilder

# Helper Functions
from .helpers import (
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
    
    # Helper Functions
    "create_component",
    "create_simple_layout",
]
