"""
Helper Functions for Component Layout

Utility functions for quickly creating layout elements.
"""

from typing import Dict, List, Any, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def create_component(
    component_type: str,
    classes: List[str] = None,
    props: Dict[str, Any] = None,
    children: Union[str, List[Any], Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Quick helper to create a component dictionary
    
    Args:
        component_type: Component type (e.g., 'div', 'button')
        classes: CSS classes
        props: Component properties
        children: Component children
        
    Returns:
        Component as dictionary
    """
    component = Component(
        type=component_type,
        classes=classes or [],
        props=props or {},
        children=children
    )
    return component.to_dict()


def create_simple_layout(query: str, tab_name: str = "Main") -> Dict[str, Any]:
    """
    Create a simple single-tab, single-section layout structure
    
    Args:
        query: User query
        tab_name: Name for the tab
        
    Returns:
        Basic layout structure as dictionary
    """
    return {
        "query": query,
        "layout": {
            "Tabs": [
                {
                    "TabName": tab_name,
                    "TabId": "tab-main",
                    "Sections": [
                        {
                            "SectionName": "Content",
                            "SectionId": "section-content",
                            "Rows": []
                        }
                    ]
                }
            ]
        }
    }
