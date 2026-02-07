"""
Pattern Index - Quick reference for all CRM layout patterns

This module provides constants and utilities for working with CRM layout patterns.
"""

# Pattern descriptions
PATTERN_DESCRIPTIONS = {
    # Detail patterns
    "basic_detail": "Comprehensive record detail view with 10 components",
    "detail_card": "Card-based detail view with avatars and chips",
    "summarize": "Quick overview with metrics and badges",
    
    # List patterns
    "contact_list_card": "Contact/stakeholder list with avatars",
    "list": "Tabular data display with table component",
    "list_summary": "List with summary metrics at top",
    
    # Dashboard patterns
    "metrics_dashboard": "KPI dashboard with metrics and dashlets",
    "analytics": "Data insights with metrics and tables",
    "dashlet": "Compact dashboard widget",
    
    # Card patterns
    "grid_card": "Multiple cards in responsive grid",
    
    # Timeline patterns
    "timeline": "Chronological activity timeline with stack",
    "activity_feed": "Recent updates and activity stream",
    "hierarchy": "Tree structure with nested stacks",
    
    # Special patterns
    "insights": "AI suggestions with insights component",
    "alerts": "Important messages and notifications",
    "celebrations": "Birthday cards and special occasions",
    "related": "Connected entities and relationships",
}

# Component count by pattern
PATTERN_COMPONENTS = {
    "basic_detail": 10,
    "detail_card": 10,
    "insights": 8,
    "metrics_dashboard": 8,
    "analytics": 8,
    "grid_card": 8,
    "timeline": 8,
    "related": 8,
    "contact_list_card": 9,
    "activity_feed": 9,
    "list": 7,
    "list_summary": 7,
    "hierarchy": 7,
    "alerts": 7,
    "celebrations": 7,
    "dashlet": 6,
    "summarize": 6,
}

# Pattern categories
PATTERN_CATEGORIES = {
    "detail": ["basic_detail", "detail_card", "summarize"],
    "list": ["contact_list_card", "list", "list_summary"],
    "dashboard": ["metrics_dashboard", "analytics", "dashlet"],
    "card": ["grid_card"],
    "timeline": ["timeline", "activity_feed", "hierarchy"],
    "special": ["insights", "alerts", "celebrations", "related"],
}

# View types
VIEW_TYPES = ["table", "list", "card"]

def get_pattern_info(pattern_name: str) -> dict:
    """Get information about a specific pattern"""
    return {
        "name": pattern_name,
        "description": PATTERN_DESCRIPTIONS.get(pattern_name, "Unknown pattern"),
        "component_count": PATTERN_COMPONENTS.get(pattern_name, 0),
        "category": next((cat for cat, patterns in PATTERN_CATEGORIES.items() if pattern_name in patterns), "unknown")
    }

def get_patterns_by_category(category: str) -> list:
    """Get all patterns in a specific category"""
    return PATTERN_CATEGORIES.get(category, [])

def get_all_patterns() -> list:
    """Get list of all available pattern names"""
    return list(PATTERN_DESCRIPTIONS.keys())
