"""
Layout Pattern 4: Urgent/Alert View

Alert-focused layout for urgent or important records.
Highlights critical information with alerts and table.
"""

from typing import List, Dict, Any


class LayoutPattern4:
    """
    Urgent/Alert View Layout
    
    Layout Structure:
    - Row 1: Alert + Title + Description (pattern12)
    - Row 2: Title + Table (pattern11)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern12', 'pattern11']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Alert-focused layout for urgent/important records"
