"""
Design System Tools
Provides access to patterns, colors, icons, and component schemas
"""
from typing import Dict, List, Optional, Any
from pathlib import Path
import json

# Import from existing modules
from design_system_agent.core.component_types import (
    ACTIVE_COMPONENTS,
    COMPONENT_CATEGORIES,
    get_component_category,
    get_components_by_category
)
from design_system_agent.core.dataset_genertor.crm_dataset.pattern_index import (
    PATTERN_DESCRIPTIONS,
    PATTERN_COMPONENTS,
    PATTERN_CATEGORIES,
    get_pattern_info,
    get_patterns_by_category,
    get_all_patterns
)
from design_system_agent.agent.tools.component_schema_with_values import (
    get_component_schema_with_value,
    get_component_structure,
    create_component_template,
    get_component_example
)


class DesignSystemTools:
    """
    Centralized access to design system resources:
    - Patterns
    - Color palettes
    - Icons
    - Component schemas
    """
    
    def __init__(self):
        """Initialize design system tools"""
        self._load_design_tokens()
    
    def _load_design_tokens(self):
        """Load design tokens (colors, icons, etc.)"""
        # Define color palette structure
        self.colors = {
            "primary": {
                "red": ["red-10", "red-20", "red-30", "red-40", "red-50", "red-60", "red-70", "red-80", "red-90", "red-100"],
                "green": ["green-10", "green-20", "green-30", "green-40", "green-50", "green-60", "green-70", "green-80", "green-90", "green-100"],
                "blue": ["blue-10", "blue-20", "blue-30", "blue-40", "blue-50", "blue-60", "blue-70", "blue-80", "blue-90", "blue-100"],
                "orange": ["orange-10", "orange-20", "orange-30", "orange-40", "orange-50", "orange-60", "orange-70", "orange-80", "orange-90", "orange-100"],
                "yellow": ["yellow-10", "yellow-20", "yellow-30", "yellow-40", "yellow-50", "yellow-60", "yellow-70", "yellow-80", "yellow-90", "yellow-100"],
                "purple": ["purple-10", "purple-20", "purple-30", "purple-40", "purple-50", "purple-60", "purple-70", "purple-80", "purple-90", "purple-100"],
                "pink": ["pink-10", "pink-20", "pink-30", "pink-40", "pink-50", "pink-60", "pink-70", "pink-80", "pink-90", "pink-100"],
                "cyan": ["cyan-10", "cyan-20", "cyan-30", "cyan-40", "cyan-50", "cyan-60", "cyan-70", "cyan-80", "cyan-90", "cyan-100"],
                "teal": ["teal-10", "teal-20", "teal-30", "teal-40", "teal-50", "teal-60", "teal-70", "teal-80", "teal-90", "teal-100"],
                "indigo": ["indigo-10", "indigo-20", "indigo-30", "indigo-40", "indigo-50", "indigo-60", "indigo-70", "indigo-80", "indigo-90", "indigo-100"],
                "gray": ["gray-10", "gray-20", "gray-30", "gray-40", "gray-50", "gray-60", "gray-70", "gray-80", "gray-90", "gray-100"],
            },
            "semantic": {
                "success": ["light-success", "success", "dark-success"],
                "error": ["light-error", "error", "dark-error"],
                "warning": ["light-warning", "warning", "dark-warning"],
                "info": ["light-info", "info", "dark-info"],
            },
            "neutral": {
                "white": "gray-10",
                "primary": "gray-90",
                "secondary": "gray-60",
                "disabled": ["light-disabled", "disabled", "dark-disabled"],
            }
        }
        
        # Define available icons (based on usage in CRM layouts)
        self.icons = [
            # User & People
            "user", "users", "user-plus", "user-check", "user-x",
            # Actions
            "edit", "trash", "save", "plus", "minus", "check", "x", "external-link",
            # Navigation
            "arrow-right", "arrow-left", "arrow-up", "arrow-down", "chevron-right", "chevron-left", "chevron-down", "chevron-up",
            # Data & Lists
            "table", "list", "grid", "columns", "database",
            # Finance
            "dollar-sign", "credit-card", "trending-up", "trending-down", "pie-chart", "bar-chart",
            # Communication
            "mail", "phone", "message-square", "send", "inbox",
            # Files & Documents
            "file", "file-text", "folder", "download", "upload", "paperclip",
            # Status & Indicators
            "check-circle", "alert-circle", "alert-triangle", "info", "help-circle", "bell",
            # Time & Calendar
            "calendar", "clock", "watch",
            # Business
            "briefcase", "target", "award", "star", "heart",
            # Settings & Tools
            "settings", "tool", "filter", "search", "refresh", "more-vertical", "more-horizontal",
            # Media
            "image", "video", "camera",
            # Location
            "map-pin", "globe", "navigation",
            # Other
            "home", "lock", "unlock", "eye", "eye-off", "copy", "share", "link", "tag"
        ]
        
        # Component default properties based on type
        self.component_schemas = {
            "Heading": {
                "type": "Heading",
                "required_props": ["text", "level"],
                "optional_props": ["className", "id"],
                "default": {
                    "text": "Heading Text",
                    "level": 2,
                    "className": "bd-heading"
                }
            },
            "Text": {
                "type": "Text",
                "required_props": ["text"],
                "optional_props": ["className", "id"],
                "default": {
                    "text": "Text content",
                    "className": "bd-text"
                }
            },
            "Label": {
                "type": "Label",
                "required_props": ["text"],
                "optional_props": ["htmlFor", "className"],
                "default": {
                    "text": "Label",
                    "className": "bd-label"
                }
            },
            "Button": {
                "type": "Button",
                "required_props": ["text"],
                "optional_props": ["variant", "size", "icon", "onClick", "disabled", "className"],
                "default": {
                    "text": "Button",
                    "variant": "primary",
                    "size": "medium",
                    "className": "bd-button"
                }
            },
            "Link": {
                "type": "Link",
                "required_props": ["text", "href"],
                "optional_props": ["icon", "external", "className"],
                "default": {
                    "text": "Link",
                    "href": "#",
                    "className": "bd-link"
                }
            },
            "Badge": {
                "type": "Badge",
                "required_props": ["text"],
                "optional_props": ["variant", "icon", "className"],
                "default": {
                    "text": "Badge",
                    "variant": "info",
                    "className": "bd-badge"
                }
            },
            "Chip": {
                "type": "Chip",
                "required_props": ["text"],
                "optional_props": ["icon", "removable", "onClick", "className"],
                "default": {
                    "text": "Chip",
                    "className": "bd-chip"
                }
            },
            "Avatar": {
                "type": "Avatar",
                "required_props": [],
                "optional_props": ["src", "alt", "fallback", "size", "className"],
                "default": {
                    "fallback": "U",
                    "size": "medium",
                    "className": "bd-avatar"
                }
            },
            "Image": {
                "type": "Image",
                "required_props": ["src", "alt"],
                "optional_props": ["width", "height", "className"],
                "default": {
                    "src": "/placeholder.jpg",
                    "alt": "Image",
                    "className": "bd-image"
                }
            },
            "Divider": {
                "type": "Divider",
                "required_props": [],
                "optional_props": ["orientation", "className"],
                "default": {
                    "orientation": "horizontal",
                    "className": "bd-divider"
                }
            },
            "Card": {
                "type": "Card",
                "required_props": [],
                "optional_props": ["title", "children", "className", "actions"],
                "default": {
                    "className": "bd-card"
                }
            },
            "Stack": {
                "type": "Stack",
                "required_props": [],
                "optional_props": ["direction", "spacing", "align", "children", "className"],
                "default": {
                    "direction": "vertical",
                    "spacing": "medium",
                    "className": "bd-stack"
                }
            },
            "List": {
                "type": "List",
                "required_props": ["items"],
                "optional_props": ["ordered", "className"],
                "default": {
                    "items": [],
                    "ordered": False,
                    "className": "bd-list"
                }
            },
            "Table": {
                "type": "Table",
                "required_props": ["headers", "rows"],
                "optional_props": ["striped", "hoverable", "className"],
                "default": {
                    "headers": [],
                    "rows": [],
                    "className": "bd-table"
                }
            },
            "Metric": {
                "type": "Metric",
                "required_props": ["value"],
                "optional_props": ["label", "change", "trend", "icon", "className"],
                "default": {
                    "value": "0",
                    "className": "bd-metric"
                }
            },
            "Dashlet": {
                "type": "Dashlet",
                "required_props": ["title"],
                "optional_props": ["value", "data", "type", "className"],
                "default": {
                    "title": "Dashlet",
                    "type": "chart",
                    "className": "bd-dashlet"
                }
            },
            "ListCard": {
                "type": "ListCard",
                "required_props": ["title"],
                "optional_props": ["description", "avatar", "metadata", "actions", "className"],
                "default": {
                    "title": "Card Title",
                    "className": "bd-listcard"
                }
            },
            "BirthdayCard": {
                "type": "BirthdayCard",
                "required_props": ["name"],
                "optional_props": ["date", "message", "avatar", "className"],
                "default": {
                    "name": "User",
                    "className": "bd-birthdaycard"
                }
            },
            "Insights": {
                "type": "Insights",
                "required_props": ["title", "insights"],
                "optional_props": ["icon", "className"],
                "default": {
                    "title": "Insights",
                    "insights": [],
                    "className": "bd-insights"
                }
            },
            "Alert": {
                "type": "Alert",
                "required_props": ["message"],
                "optional_props": ["title", "variant", "icon", "dismissible", "className"],
                "default": {
                    "message": "Alert message",
                    "variant": "info",
                    "className": "bd-alert"
                }
            }
        }
    
    # ============================================
    # PATTERN METHODS
    # ============================================
    
    def get_pattern(self, pattern_name: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a specific layout pattern
        
        Args:
            pattern_name: Name of the pattern (e.g., "basic_detail", "list")
            
        Returns:
            Pattern information including description, component count, category
        """
        return get_pattern_info(pattern_name)
    
    def get_patterns_by_category(self, category: str) -> List[str]:
        """
        Get all patterns in a specific category
        
        Args:
            category: Category name (detail, list, dashboard, card, timeline, special)
            
        Returns:
            List of pattern names in the category
        """
        return get_patterns_by_category(category)
    
    def get_all_patterns(self) -> List[str]:
        """
        Get list of all available pattern names
        
        Returns:
            List of all pattern names
        """
        return get_all_patterns()
    
    def list_pattern_categories(self) -> List[str]:
        """
        Get list of all pattern categories
        
        Returns:
            List of category names
        """
        return list(PATTERN_CATEGORIES.keys())
    
    # ============================================
    # COLOR PALETTE METHODS
    # ============================================
    
    def get_color_palette(self, palette_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Get color palette(s)
        
        Args:
            palette_name: Optional specific palette (primary, semantic, neutral)
                         If None, returns all palettes
        
        Returns:
            Color palette dictionary
        """
        if palette_name:
            return self.colors.get(palette_name, {})
        return self.colors
    
    def get_color_shades(self, color_name: str) -> List[str]:
        """
        Get all shades of a specific color
        
        Args:
            color_name: Color name (red, green, blue, etc.)
            
        Returns:
            List of color shade classes (e.g., ["red-10", "red-20", ...])
        """
        # Check in primary colors
        if color_name in self.colors["primary"]:
            return self.colors["primary"][color_name]
        
        # Check in semantic colors
        if color_name in self.colors["semantic"]:
            return self.colors["semantic"][color_name]
        
        return []
    
    def get_semantic_colors(self) -> Dict[str, List[str]]:
        """
        Get semantic color mappings (success, error, warning, info)
        
        Returns:
            Dictionary of semantic color variants
        """
        return self.colors["semantic"]
    
    def list_available_colors(self) -> Dict[str, List[str]]:
        """
        List all available color names organized by type
        
        Returns:
            Dictionary with primary, semantic, and neutral colors
        """
        return {
            "primary": list(self.colors["primary"].keys()),
            "semantic": list(self.colors["semantic"].keys()),
            "neutral": list(self.colors["neutral"].keys())
        }
    
    # ============================================
    # ICON METHODS
    # ============================================
    
    def get_icon_by_name(self, icon_name: str) -> Optional[str]:
        """
        Get icon name if it exists in the design system
        
        Args:
            icon_name: Icon name to search for
            
        Returns:
            Icon name if found, None otherwise
        """
        if icon_name in self.icons:
            return icon_name
        return None
    
    def search_icons(self, query: str) -> List[str]:
        """
        Search for icons matching a query
        
        Args:
            query: Search term
            
        Returns:
            List of matching icon names
        """
        query_lower = query.lower()
        return [icon for icon in self.icons if query_lower in icon.lower()]
    
    def get_all_icons(self) -> List[str]:
        """
        Get list of all available icons
        
        Returns:
            List of all icon names
        """
        return self.icons.copy()
    
    def get_icons_by_category(self, category: str) -> List[str]:
        """
        Get icons by category (user, action, navigation, data, etc.)
        
        Args:
            category: Category name
            
        Returns:
            List of icon names in that category
        """
        categories = {
            "user": ["user", "users", "user-plus", "user-check", "user-x"],
            "action": ["edit", "trash", "save", "plus", "minus", "check", "x", "external-link"],
            "navigation": ["arrow-right", "arrow-left", "arrow-up", "arrow-down", "chevron-right", "chevron-left", "chevron-down", "chevron-up"],
            "data": ["table", "list", "grid", "columns", "database"],
            "finance": ["dollar-sign", "credit-card", "trending-up", "trending-down", "pie-chart", "bar-chart"],
            "communication": ["mail", "phone", "message-square", "send", "inbox"],
            "file": ["file", "file-text", "folder", "download", "upload", "paperclip"],
            "status": ["check-circle", "alert-circle", "alert-triangle", "info", "help-circle", "bell"],
            "time": ["calendar", "clock", "watch"],
            "business": ["briefcase", "target", "award", "star", "heart"],
            "settings": ["settings", "tool", "filter", "search", "refresh", "more-vertical", "more-horizontal"],
            "media": ["image", "video", "camera"],
            "location": ["map-pin", "globe", "navigation"],
            "other": ["home", "lock", "unlock", "eye", "eye-off", "copy", "share", "link", "tag"]
        }
        return categories.get(category, [])
    
    # ============================================
    # COMPONENT SCHEMA METHODS
    # ============================================
    
    def get_component_by_type(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get component schema by component type
        
        Args:
            component_type: Component type name (Heading, Button, Card, etc.)
            
        Returns:
            Component schema with required/optional props and defaults
        """
        return self.component_schemas.get(component_type)
    
    def get_component_props(self, component_type: str) -> Optional[Dict[str, List[str]]]:
        """
        Get required and optional props for a component
        
        Args:
            component_type: Component type name
            
        Returns:
            Dictionary with required_props and optional_props lists
        """
        schema = self.component_schemas.get(component_type)
        if schema:
            return {
                "required_props": schema["required_props"],
                "optional_props": schema["optional_props"]
            }
        return None
    
    def get_component_default(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get default props for a component
        
        Args:
            component_type: Component type name
            
        Returns:
            Default props dictionary
        """
        schema = self.component_schemas.get(component_type)
        if schema:
            return schema["default"].copy()
        return None
    
    def get_all_component_types(self) -> List[str]:
        """
        Get list of all available component types
        
        Returns:
            List of component type names
        """
        return ACTIVE_COMPONENTS.copy()
    
    def get_components_by_category(self, category: str) -> List[str]:
        """
        Get components in a specific category
        
        Args:
            category: Category name (typography, interactive, display, containers, data, complex)
            
        Returns:
            List of component types in that category
        """
        return get_components_by_category(category)
    
    def list_component_categories(self) -> List[str]:
        """
        Get list of all component categories
        
        Returns:
            List of category names
        """
        return list(COMPONENT_CATEGORIES.keys())
    
    # ============================================
    # ENHANCED COMPONENT METHODS (WITH VALUES)
    # ============================================
    
    def get_component_with_values(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get component schema with props/value separation
        
        Args:
            component_type: Component type name
            
        Returns:
            Enhanced schema with 'structure' containing 'props' and 'value' sections
        """
        return get_component_schema_with_value(component_type)
    
    def create_component(self, component_type: str, data: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """
        Create a component instance with proper structure for layouts
        
        Args:
            component_type: Component type name
            data: Data to fill in the value section
            
        Returns:
            Component with {'type', 'props', 'value'} structure ready for layouts
            
        Example:
            >>> tools.create_component("Heading", {"text": "Customer Dashboard"})
            {
                "type": "Heading",
                "props": {"level": 2},
                "value": {"text": "Customer Dashboard", "icon": ""}
            }
        """
        return create_component_template(component_type, data)
    
    def get_component_props_schema(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get props configuration schema for a component
        
        Args:
            component_type: Component type name
            
        Returns:
            Props schema with field definitions
        """
        structure = get_component_structure(component_type)
        if structure:
            return structure.get("props")
        return None
    
    def get_component_value_schema(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get value (data) schema for a component
        
        Args:
            component_type: Component type name
            
        Returns:
            Value schema with field definitions
        """
        structure = get_component_structure(component_type)
        if structure:
            return structure.get("value")
        return None
    
    def get_component_example(self, component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get complete usage example for a component
        
        Args:
            component_type: Component type name
            
        Returns:
            Example with type, props, and value filled in
        """
        return get_component_example(component_type)


# Singleton instance
_design_system_tools = None

def get_design_system_tools() -> DesignSystemTools:
    """Get singleton instance of DesignSystemTools"""
    global _design_system_tools
    if _design_system_tools is None:
        _design_system_tools = DesignSystemTools()
    return _design_system_tools


# Convenience functions
def get_pattern(name: str) -> Optional[Dict]:
    """Get pattern info"""
    return get_design_system_tools().get_pattern(name)

def get_color_palette(name: Optional[str] = None) -> Dict:
    """Get color palette"""
    return get_design_system_tools().get_color_palette(name)

def get_icon(name: str) -> Optional[str]:
    """Get icon by name"""
    return get_design_system_tools().get_icon_by_name(name)

def get_component(component_type: str) -> Optional[Dict]:
    """Get basic component schema"""
    return get_design_system_tools().get_component_by_type(component_type)

def get_component_enhanced(component_type: str) -> Optional[Dict]:
    """Get enhanced component schema with props/value separation"""
    return get_design_system_tools().get_component_with_values(component_type)

def create_component(component_type: str, data: Optional[Dict] = None) -> Optional[Dict]:
    """Create component instance with data"""
    return get_design_system_tools().create_component(component_type, data)

