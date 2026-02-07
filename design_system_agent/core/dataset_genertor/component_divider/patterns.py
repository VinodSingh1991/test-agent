"""
Divider pattern factory functions for common use cases
"""
from .divider_builder import DividerBuilder
from typing import Dict, Any


def horizontal_divider() -> Dict[str, Any]:
    """Horizontal divider line"""
    return DividerBuilder().horizontal().build()


def vertical_divider() -> Dict[str, Any]:
    """Vertical divider line"""
    return DividerBuilder().vertical().build()
