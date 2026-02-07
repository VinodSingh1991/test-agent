"""
Layout Pattern 5: Detailed Overview

Comprehensive view with cards and detailed information.
Rich layout for exploring record details.
"""

from typing import List, Dict, Any


class LayoutPattern5:
    """
    Detailed Overview Layout
    
    Layout Structure:
    - Row 1: Title + Status Badges + Description (pattern8)
    - Row 2: Title + Description + List + Card (pattern5)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern8', 'pattern5']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Comprehensive view with status badges, lists, and cards"
