"""
LangChain Design System Tools
Wrapper to expose design system tools as LangChain tools for LLM function calling
"""
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool

from design_system_agent.agent.tools.design_system_tools import get_design_system_tools


# ===========================
# COLOR TOOLS
# ===========================

@tool
def get_all_colors() -> Dict[str, List[str]]:
    """
    Get all available colors in the design system organized by family.
    Returns dict with color families (red, blue, green, etc.) and their shades.
    Use this when you need to see all color options.
    """
    return get_design_system_tools().list_available_colors()


@tool
def get_color_shades(color_name: str) -> List[str]:
    """
    Get all shades for a specific color (e.g., 'blue' returns ['blue-10', 'blue-20', ..., 'blue-100']).
    
    Args:
        color_name: Base color name (red, blue, green, orange, yellow, purple, pink, cyan, teal, indigo, gray)
    
    Returns:
        List of color shades like ['blue-10', 'blue-20', ..., 'blue-100']
    """
    return get_design_system_tools().get_color_shades(color_name)


@tool
def get_semantic_colors() -> Dict[str, List[str]]:
    """
    Get semantic colors for status indication.
    Returns colors for success, error, warning, and info states.
    Use for badges, alerts, status indicators.
    """
    return get_design_system_tools().get_semantic_colors()


# ===========================
# ICON TOOLS
# ===========================

@tool
def search_icons(query: str) -> List[str]:
    """
    Search for icons by keyword or description.
    
    Args:
        query: Search term (e.g., "trending", "user", "money", "calendar")
    
    Returns:
        List of matching icon names
    
    Examples:
        - search_icons("trending") → ["trending-up", "trending-down"]
        - search_icons("user") → ["user", "users", "user-plus", "user-check"]
        - search_icons("money") → ["dollar-sign", "credit-card"]
    """
    return get_design_system_tools().search_icons(query)


@tool
def get_icons_by_category(category: str) -> List[str]:
    """
    Get all icons in a specific category.
    
    Args:
        category: Icon category (user, action, navigation, data, finance, status, 
                 communication, file, time, business, settings, media, location)
    
    Returns:
        List of icon names in that category
    """
    return get_design_system_tools().get_icons_by_category(category)


@tool
def get_all_icons() -> List[str]:
    """
    Get complete list of all available icons (90+ icons).
    Only use this if you need to see ALL icons. For specific needs, use search_icons() or get_icons_by_category().
    """
    return get_design_system_tools().get_all_icons()


# ===========================
# PATTERN TOOLS
# ===========================

@tool
def get_pattern_info(pattern_name: str) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a specific UI pattern.
    
    Args:
        pattern_name: Pattern name (header, content, footer, table, card_grid, list_group, 
                     stat_cards, filter_bar, action_bar, form, tabs, sidebar, etc.)
    
    Returns:
        Dict with pattern description, components, use cases, and example structure
    """
    return get_design_system_tools().get_pattern(pattern_name)


@tool
def get_patterns_by_category(category: str) -> List[str]:
    """
    Get patterns in a specific category.
    
    Args:
        category: Pattern category (layout, navigation, data_display, input, feedback, etc.)
    
    Returns:
        List of pattern names in that category
    """
    return get_design_system_tools().get_patterns_by_category(category)


@tool
def list_all_patterns() -> List[str]:
    """
    Get names of all available UI patterns.
    Returns simple list of pattern names. Use get_pattern_info() for details.
    """
    return get_design_system_tools().get_all_patterns()


# ===========================
# COMPONENT TOOLS
# ===========================

@tool
def get_component_schema(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get complete schema for a component including props and value structure.
    
    Args:
        component_type: Component type (Heading, Button, Badge, List, Card, Avatar, 
                       Label, Icon, Divider, Text, Link, Image, Chip, Alert, etc.)
    
    Returns:
        Dict with component structure, required props, and value fields
    """
    return get_design_system_tools().get_component_with_values(component_type)


@tool
def get_components_by_category(category: str) -> List[str]:
    """
    Get all components in a specific category.
    
    Args:
        category: Component category (typography, layout, navigation, data_display, 
                 input, feedback, media, overlay)
    
    Returns:
        List of component names in that category
    
    Examples:
        - get_components_by_category("typography") → ["Heading", "Text", "Label"]
        - get_components_by_category("data_display") → ["Badge", "Chip", "Avatar", "List"]
    """
    return get_design_system_tools().get_components_by_category(category)


@tool
def list_all_components() -> List[str]:
    """
    Get list of all 19 available component types.
    Use this to see what components are available for building layouts.
    """
    return get_design_system_tools().get_all_component_types()


# ===========================
# TOOL COLLECTION
# ===========================

def get_langchain_design_tools() -> List:
    """
    Get all LangChain design system tools for binding to LLM.
    
    Returns:
        List of @tool decorated functions for colors, icons, patterns, components
    """
    return [
        # Color tools
        get_all_colors,
        get_color_shades,
        get_semantic_colors,
        # Icon tools
        search_icons,
        get_icons_by_category,
        get_all_icons,
        # Pattern tools
        get_pattern_info,
        get_patterns_by_category,
        list_all_patterns,
        # Component tools
        get_component_schema,
        get_components_by_category,
        list_all_components,
    ]
