"""
Layout Pattern 1: Basic Info View

Simple single-row layout for showing basic record information.
Uses Title + Description pattern for clean, minimal presentation.
"""

from typing import List, Dict, Any


class LayoutPattern1:
    """
    Basic Info View Layout
    
    Layout Structure:
    - Row 1: Title + Description (pattern1)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern1']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Basic single-row layout with title and description"
