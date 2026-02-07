"""
Layout Pattern Factory

Central registry and management for layout patterns.
Maps user queries to complete page layouts.
"""

from typing import Dict, List, Any, Optional
from .layout_pattern1 import LayoutPattern1
from .layout_pattern2 import LayoutPattern2
from .layout_pattern3 import LayoutPattern3
from .layout_pattern4 import LayoutPattern4
from .layout_pattern5 import LayoutPattern5
from .layout_pattern6 import LayoutPattern6
from .layout_pattern7 import LayoutPattern7
from .layout_pattern8 import LayoutPattern8


class LayoutPatternFactory:
    """
    Factory for managing and generating layout patterns.
    
    Layout patterns define complete page structures by combining multiple component patterns.
    Each layout pattern specifies which component patterns to use in rows.
    
    Available Layout Patterns:
    - layout_pattern1: Basic Info View (simple single record)
    - layout_pattern2: Basic List/Table View (multiple records)
    - layout_pattern3: Dashboard Layout (metrics + details)
    - layout_pattern4: Urgent/Alert View (critical items)
    - layout_pattern5: Detailed Overview (comprehensive view)
    - layout_pattern6: Analytics Report (metrics + tables)
    - layout_pattern7: Activity Feed (timeline/history)
    - layout_pattern8: Comparison View (side-by-side)
    """
    
    _layouts = {
        'layout_pattern1': LayoutPattern1,
        'layout_pattern2': LayoutPattern2,
        'layout_pattern3': LayoutPattern3,
        'layout_pattern4': LayoutPattern4,
        'layout_pattern5': LayoutPattern5,
        'layout_pattern6': LayoutPattern6,
        'layout_pattern7': LayoutPattern7,
        'layout_pattern8': LayoutPattern8,
    }
    
    @classmethod
    def get_layout(cls, layout_type: str):
        """Get a layout pattern class by type"""
        return cls._layouts.get(layout_type)
    
    @classmethod
    def list_layouts(cls) -> List[str]:
        """List all available layout types"""
        return list(cls._layouts.keys())
    
    @classmethod
    def get_layout_info(cls, layout_type: str) -> Optional[Dict[str, Any]]:
        """Get metadata about a specific layout"""
        layout_class = cls.get_layout(layout_type)
        if layout_class:
            info = {
                "layout_type": layout_type,
                "description": layout_class.get_description(),
                "patterns": layout_class.get_patterns()
            }
            return info
        return None
    
    @classmethod
    def get_patterns_for_layout(cls, layout_type: str) -> Optional[List[str]]:
        """Get list of pattern types for a specific layout"""
        layout_class = cls.get_layout(layout_type)
        if layout_class:
            return layout_class.get_patterns()
        return None
    
    @classmethod
    def generate_layout_structure(cls, layout_type: str, query: str, object_type: str) -> Optional[Dict[str, Any]]:
        """
        Generate the layout structure for a given layout type.
        Returns the structure without actual component data (use PatternFactory for that).
        """
        layout_class = cls.get_layout(layout_type)
        if not layout_class:
            return None
        
        patterns = layout_class.get_patterns()
        
        return {
            "layout_type": layout_type,
            "query": query,
            "object_type": object_type,
            "rows": [
                {
                    "row_index": idx,
                    "pattern_type": pattern_type
                }
                for idx, pattern_type in enumerate(patterns)
            ]
        }


# Export layout patterns
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
