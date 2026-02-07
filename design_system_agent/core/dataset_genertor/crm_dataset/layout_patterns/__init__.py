"""
Layout Patterns Module

This module provides complete page layout patterns that combine multiple component patterns.
Each layout pattern defines a full page structure for specific query types.
"""

from .layout_pattern1 import LayoutPattern1
from .layout_pattern2 import LayoutPattern2
from .layout_pattern3 import LayoutPattern3
from .layout_pattern4 import LayoutPattern4
from .layout_pattern5 import LayoutPattern5
from .layout_pattern6 import LayoutPattern6
from .layout_pattern7 import LayoutPattern7
from .layout_pattern8 import LayoutPattern8
from .factory import LayoutPatternFactory

__all__ = [
    'LayoutPattern1',
    'LayoutPattern2',
    'LayoutPattern3',
    'LayoutPattern4',
    'LayoutPattern5',
    'LayoutPattern6',
    'LayoutPattern7',
    'LayoutPattern8',
    'LayoutPatternFactory'
]
