"""
Layout Pattern 8: Comparison View

Side-by-side comparison layout for comparing records.
Uses cards for visual comparison.
"""

from typing import List, Dict, Any


class LayoutPattern8:
    """
    Comparison View Layout
    
    Layout Structure:
    - Row 1: 2 Cards for comparison (pattern10)
    - Row 2: Title + Table for detailed comparison (pattern11)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern10', 'pattern11']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Comparison layout with side-by-side cards and table"
