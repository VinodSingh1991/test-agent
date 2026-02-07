"""
Heading pattern factory functions for common use cases
"""
from typing import Optional, Dict, Any
from .heading_builder import HeadingBuilder



# Level-based patterns
def h1_heading(text: str) -> Dict[str, Any]:
    """H1 page title heading"""
    return HeadingBuilder(text, 1).build()


def h2_heading(text: str) -> Dict[str, Any]:
    """H2 section heading"""
    return HeadingBuilder(text, 2).build()


def h3_heading(text: str) -> Dict[str, Any]:
    """H3 subsection heading"""
    return HeadingBuilder(text, 3).build()


def h4_heading(text: str) -> Dict[str, Any]:
    """H4 detail heading"""
    return HeadingBuilder(text, 4).build()


def h5_heading(text: str) -> Dict[str, Any]:
    """H5 minor heading"""
    return HeadingBuilder(text, 5).build()


def h6_heading(text: str) -> Dict[str, Any]:
    """H6 small heading"""
    return HeadingBuilder(text, 6).build()


# Common use cases
def page_title(text: str) -> Dict[str, Any]:
    """Bold page title (H1)"""
    return HeadingBuilder(text, 1).build()


def section_title(text: str) -> Dict[str, Any]:
    """Section title (H2)"""
    return HeadingBuilder(text, 2).build()


def card_title(text: str) -> Dict[str, Any]:
    """Card title (H3)"""
    return HeadingBuilder(text, 3).build()
