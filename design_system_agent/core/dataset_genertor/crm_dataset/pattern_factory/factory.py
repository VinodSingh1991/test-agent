"""
Pattern Factory - Maps pattern types to pattern classes
"""

from typing import Dict, Any, List, Type
from .pattern0 import Pattern0
from .pattern1 import Pattern1
from .pattern2 import Pattern2
from .pattern3 import Pattern3
from .pattern4 import Pattern4
from .pattern5 import Pattern5
from .pattern6 import Pattern6
from .pattern7 import Pattern7
from .pattern8 import Pattern8
from .pattern9 import Pattern9
from .pattern10 import Pattern10
from .pattern11 import Pattern11
from .pattern12 import Pattern12
from .pattern13 import Pattern13
from .pattern14 import Pattern14
from .pattern15 import Pattern15


class PatternFactory:
    """
    Factory to get pattern classes by pattern_type
    
    Central registry for all layout patterns. LLM uses this to:
    1. Discover available patterns
    2. Get pattern metadata (components, description, use cases)
    3. Generate layouts by combining multiple patterns
    
    Pattern Selection Logic for LLM:
    - Analyze query keywords and intent
    - Match query type to pattern use cases
    - Select 1-3 patterns based on complexity
    - Simple queries → 1 pattern (pattern1, pattern3)
    - Detailed queries → 2 patterns (pattern1 + pattern2)
    - Dashboard queries → Multiple patterns (pattern7 + pattern14)
    """
    
    _patterns = {
        "pattern0": Pattern0,
        "pattern1": Pattern1,
        "pattern2": Pattern2,
        "pattern3": Pattern3,
        "pattern4": Pattern4,
        "pattern5": Pattern5,
        "pattern6": Pattern6,
        "pattern7": Pattern7,
        "pattern8": Pattern8,
        "pattern9": Pattern9,
        "pattern10": Pattern10,
        "pattern11": Pattern11,
        "pattern12": Pattern12,
        "pattern13": Pattern13,
        "pattern14": Pattern14,
        "pattern15": Pattern15,
    }
    
    @classmethod
    def get_pattern(cls, pattern_type: str):
        """Get pattern class by type"""
        return cls._patterns.get(pattern_type)
    
    @classmethod
    def generate_layout(cls, query: str, object_type: str, data: Dict[str, Any], pattern_mappings: List[str]) -> Dict[str, Any]:
        """
        Generate layout with rows based on pattern mappings
        
        Args:
            query: User query
            object_type: CRM object type
            data: Sample data
            pattern_mappings: List of pattern types to use ["pattern1", "pattern2", ...]
            
        Returns:
            Layout dict with rows
        """
        rows = []
        
        for idx, pattern_type in enumerate(pattern_mappings):
            pattern_class = cls.get_pattern(pattern_type)
            if pattern_class:
                pattern_info = pattern_class.generate(object_type, data, idx)
                rows.append({
                    "pattern_type": pattern_type,
                    "pattern_info": pattern_info
                })
        
        return {
            "query": query,
            "object_type": object_type,
            "rows": rows
        }
    
    @classmethod
    def list_patterns(cls) -> List[str]:
        """List all available pattern types"""
        return list(cls._patterns.keys())
    
    @classmethod
    def get_all_patterns_guidance(cls) -> Dict[str, Dict[str, Any]]:
        """Get LLM guidance for all available patterns"""
        guidance = {}
        for pattern_type in cls.list_patterns():
            pattern_class = cls.get_pattern(pattern_type)
            if pattern_class and hasattr(pattern_class, 'get_llm_guidance'):
                guidance[pattern_type] = pattern_class.get_llm_guidance()
        return guidance
    
    @classmethod
    def get_pattern_info(cls, pattern_type: str) -> Dict[str, Any]:
        """Get pattern metadata including LLM guidance"""
        pattern_class = cls.get_pattern(pattern_type)
        if pattern_class:
            info = {
                "pattern_type": pattern_type,
                "components": pattern_class.get_components(),
                "description": pattern_class.__doc__
            }
            
            # Add LLM guidance if available
            if hasattr(pattern_class, 'get_llm_guidance'):
                info["llm_guidance"] = pattern_class.get_llm_guidance()
            
            return info
        return None


# Export all patterns
__all__ = [
    'Pattern0',
    'Pattern1',
    'Pattern2',
    'Pattern3',
    'Pattern4',
    'Pattern5',
    'Pattern6',
    'Pattern7',
    'Pattern8',
    'Pattern9',
    'Pattern10',
    'Pattern11',
    'Pattern12',
    'Pattern13',
    'Pattern14',
    'Pattern15',
    'PatternFactory'
]
