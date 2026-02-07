"""
Layout Pattern 3: Dashboard Layout

Dashboard view with metrics and detailed information.
Combines overview metrics with detailed record info.
"""

from typing import List, Dict, Any


class LayoutPattern3:
    """
    Dashboard Layout
    
    Layout Structure:
    - Row 1: 3 Dashlets (pattern0)
    - Row 2: Title + Description + List (pattern2)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern0', 'pattern2']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Dashboard with metrics and detailed information"
