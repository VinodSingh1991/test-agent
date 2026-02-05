"""
Heading pattern factory functions for common use cases
"""
from typing import Optional
from .heading_builder import HeadingBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


# Level-based patterns
def h1_heading(text: str) -> Component:
    """H1 page title heading"""
    return HeadingBuilder(text, 1).build()


def h2_heading(text: str) -> Component:
    """H2 section heading"""
    return HeadingBuilder(text, 2).build()


def h3_heading(text: str) -> Component:
    """H3 subsection heading"""
    return HeadingBuilder(text, 3).build()


def h4_heading(text: str) -> Component:
    """H4 detail heading"""
    return HeadingBuilder(text, 4).build()


def h5_heading(text: str) -> Component:
    """H5 minor heading"""
    return HeadingBuilder(text, 5).build()


def h6_heading(text: str) -> Component:
    """H6 small heading"""
    return HeadingBuilder(text, 6).build()


# Common use cases
def page_title(text: str) -> Component:
    """Bold page title (H1)"""
    return HeadingBuilder(text, 1).build()


def section_title(text: str) -> Component:
    """Section title (H2)"""
    return HeadingBuilder(text, 2).build()


def card_title(text: str) -> Component:
    """Card title (H3)"""
    return HeadingBuilder(text, 3).build()
