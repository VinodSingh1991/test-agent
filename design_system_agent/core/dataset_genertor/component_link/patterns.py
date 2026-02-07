"""
Link pattern factory functions for common use cases
"""
from typing import Optional, Dict, Any
from .link_builder import LinkBuilder



def standard_link(text: str, url: str = "#") -> Dict[str, Any]:
    """Standard hyperlink"""
    return LinkBuilder(text, url).build()


def external_link(text: str, url: str) -> Dict[str, Any]:
    """External link (opens in new tab)"""
    return LinkBuilder(text, url).external().build()


def primary_link(text: str, url: str = "#") -> Dict[str, Any]:
    """Primary colored link"""
    return LinkBuilder(text, url).primary().build()
