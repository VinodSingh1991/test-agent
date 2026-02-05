"""
Link pattern factory functions for common use cases
"""
from typing import Optional
from .link_builder import LinkBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def standard_link(text: str, url: str = "#") -> Component:
    """Standard hyperlink"""
    return LinkBuilder(text, url).build()


def external_link(text: str, url: str) -> Component:
    """External link (opens in new tab)"""
    return LinkBuilder(text, url).external().build()


def primary_link(text: str, url: str = "#") -> Component:
    """Primary colored link"""
    return LinkBuilder(text, url).primary().build()
