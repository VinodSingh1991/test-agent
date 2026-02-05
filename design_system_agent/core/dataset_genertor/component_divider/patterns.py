"""
Divider pattern factory functions for common use cases
"""
from .divider_builder import DividerBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def horizontal_divider() -> Component:
    """Horizontal divider line"""
    return DividerBuilder().horizontal().build()


def vertical_divider() -> Component:
    """Vertical divider line"""
    return DividerBuilder().vertical().build()
