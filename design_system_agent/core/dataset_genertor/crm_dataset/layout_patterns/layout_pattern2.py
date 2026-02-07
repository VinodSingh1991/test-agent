"""
Layout Pattern 2: Basic List/Table View

Clean table layout for displaying multiple records.
Uses Title + Table pattern for structured data presentation.
"""

from typing import List, Dict, Any


class LayoutPattern2:
    """
    Basic List/Table View Layout
    
    Layout Structure:
    - Row 1: Title + Table (pattern11)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern11']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Table layout for displaying multiple records"
