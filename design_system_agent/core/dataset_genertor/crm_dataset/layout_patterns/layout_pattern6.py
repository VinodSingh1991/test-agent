"""
Layout Pattern 6: Analytics Report

Analytics-focused layout with metrics and data tables.
Perfect for performance reports and KPI tracking.
"""

from typing import List, Dict, Any


class LayoutPattern6:
    """
    Analytics Report Layout
    
    Layout Structure:
    - Row 1: 3 Metrics with trends (pattern9)
    - Row 2: Metrics + Table (pattern14)
    """
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of pattern types to use in rows"""
        return ['pattern9', 'pattern14']
    
    @staticmethod
    def get_description() -> str:
        """Return layout description"""
        return "Analytics layout with KPI metrics and data tables"
