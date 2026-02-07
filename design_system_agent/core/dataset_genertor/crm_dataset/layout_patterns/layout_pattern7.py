"""
Layout Pattern 7: Activity Feed

Activity-focused layout for recent actions and timeline.
Shows recent activities with detailed cards.
"""

from typing import List, Dict, Any


class LayoutPattern7:
    """
    Activity Feed Layout
    
    Layout Structure:
    - Row 1: Title + List + Card (pattern13)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern13']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Activity feed with list and detailed cards"
