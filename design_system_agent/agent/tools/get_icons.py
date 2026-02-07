"""
Icon Registry for Design System
Provides access to all available icons in the BusinessNext design system
"""
from typing import List, Optional


# Complete icon list based on Feather Icons (commonly used in CRM systems)
ICONS = [
    # User & People
    "user", "users", "user-plus", "user-check", "user-x", "user-minus",
    
    # Actions
    "edit", "edit-2", "edit-3", "trash", "trash-2", "save", "plus", "minus", 
    "check", "x", "external-link", "copy", "cut", "clipboard",
    
    # Navigation
    "arrow-right", "arrow-left", "arrow-up", "arrow-down",
    "chevron-right", "chevron-left", "chevron-down", "chevron-up",
    "chevrons-right", "chevrons-left", "chevrons-down", "chevrons-up",
    "corner-down-left", "corner-down-right", "corner-up-left", "corner-up-right",
    
    # Data & Lists
    "table", "list", "grid", "columns", "database", "layers", "package",
    
    # Finance & Business
    "dollar-sign", "credit-card", "trending-up", "trending-down", 
    "pie-chart", "bar-chart", "bar-chart-2", "activity", "briefcase",
    "target", "award", "shopping-cart", "shopping-bag",
    
    # Communication
    "mail", "phone", "phone-call", "phone-incoming", "phone-outgoing",
    "message-square", "message-circle", "send", "inbox", "at-sign",
    
    # Files & Documents
    "file", "file-text", "file-plus", "file-minus", "folder",
    "folder-plus", "folder-minus", "download", "upload", "paperclip",
    
    # Status & Indicators
    "check-circle", "check-square", "alert-circle", "alert-triangle", 
    "alert-octagon", "info", "help-circle", "bell", "bell-off",
    "star", "heart", "thumbs-up", "thumbs-down",
    
    # Time & Calendar
    "calendar", "clock", "watch",
    
    # Settings & Tools
    "settings", "tool", "filter", "search", "refresh", "refresh-cw",
    "more-vertical", "more-horizontal", "menu", "sliders",
    
    # Media
    "image", "video", "camera", "camera-off", "film", "music",
    "mic", "mic-off", "volume", "volume-2", "volume-x",
    
    # Location & Navigation
    "map-pin", "map", "globe", "navigation", "compass",
    
    # UI Elements
    "home", "lock", "unlock", "eye", "eye-off", "maximize",
    "minimize", "maximize-2", "minimize-2", "zoom-in", "zoom-out",
    "share", "share-2", "link", "link-2", "anchor", "tag",
    
    # Status Indicators  
    "circle", "disc", "square", "octagon", "triangle",
    "zap", "zap-off", "power",
    
    # Miscellaneous
    "book", "bookmark", "calendar-plus", "code", "command",
    "cpu", "flag", "gift", "percent", "printer", "server",
    "shield", "shield-off", "sidebar", "smartphone", "tablet",
    "terminal", "thermometer", "toggle-left", "toggle-right",
    "truck", "tv", "umbrella", "wifi", "wifi-off"
]


# Icon categories for easy discovery
ICON_CATEGORIES = {
    "user": [
        "user", "users", "user-plus", "user-check", "user-x", "user-minus"
    ],
    "action": [
        "edit", "edit-2", "edit-3", "trash", "trash-2", "save", "plus", 
        "minus", "check", "x", "external-link", "copy", "cut", "clipboard"
    ],
    "navigation": [
        "arrow-right", "arrow-left", "arrow-up", "arrow-down",
        "chevron-right", "chevron-left", "chevron-down", "chevron-up",
        "chevrons-right", "chevrons-left", "chevrons-down", "chevrons-up"
    ],
    "data": [
        "table", "list", "grid", "columns", "database", "layers", "package"
    ],
    "finance": [
        "dollar-sign", "credit-card", "trending-up", "trending-down",
        "pie-chart", "bar-chart", "bar-chart-2", "activity"
    ],
    "communication": [
        "mail", "phone", "phone-call", "message-square", "message-circle",
        "send", "inbox", "at-sign"
    ],
    "file": [
        "file", "file-text", "file-plus", "folder", "download", 
        "upload", "paperclip"
    ],
    "status": [
        "check-circle", "alert-circle", "alert-triangle", "info", 
        "help-circle", "bell", "star", "heart"
    ],
    "time": [
        "calendar", "clock", "watch"
    ],
    "business": [
        "briefcase", "target", "award", "shopping-cart", "shopping-bag"
    ],
    "settings": [
        "settings", "tool", "filter", "search", "refresh", 
        "more-vertical", "more-horizontal", "menu", "sliders"
    ],
    "media": [
        "image", "video", "camera", "film", "music", "mic"
    ],
    "location": [
        "map-pin", "map", "globe", "navigation", "compass"
    ],
    "ui": [
        "home", "lock", "unlock", "eye", "eye-off", "maximize",
        "minimize", "zoom-in", "zoom-out", "share", "link", "tag"
    ]
}


def get_icon(icon_name: str) -> Optional[str]:
    """
    Get icon name if it exists
    
    Args:
        icon_name: Icon name to retrieve
        
    Returns:
        Icon name if found, None otherwise
    """
    return icon_name if icon_name in ICONS else None


def search_icons(query: str) -> List[str]:
    """
    Search icons by name
    
    Args:
        query: Search query
        
    Returns:
        List of matching icon names
    """
    query_lower = query.lower()
    return [icon for icon in ICONS if query_lower in icon]


def get_icons_by_category(category: str) -> List[str]:
    """
    Get all icons in a category
    
    Args:
        category: Category name
        
    Returns:
        List of icon names
    """
    return ICON_CATEGORIES.get(category, [])


def get_all_icons() -> List[str]:
    """Get all available icons"""
    return ICONS.copy()


def list_icon_categories() -> List[str]:
    """Get list of all icon categories"""
    return list(ICON_CATEGORIES.keys())
