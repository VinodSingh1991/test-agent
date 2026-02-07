"""
Component Schema Utilities
Provides detailed schemas for all design system components
"""
from typing import Dict, Optional, Any, List
from design_system_agent.core.component_types import ACTIVE_COMPONENTS, COMPONENT_CATEGORIES
from design_system_agent.agent.tools.component_schema_with_values import (
    COMPONENT_SCHEMAS_WITH_VALUES,
    get_component_schema_with_value,
    get_component_structure,
    create_component_template,
    get_component_example as get_example_with_values
)


# Comprehensive component schemas with all properties
COMPONENT_SCHEMAS = {
    "Heading": {
        "type": "Heading",
        "description": "Heading component for titles (H1-H6)",
        "category": "typography",
        "required_props": ["text", "level"],
        "optional_props": ["className", "id", "color"],
        "prop_types": {
            "text": "string",
            "level": "number (1-6)",
            "className": "string",
            "id": "string",
            "color": "string"
        },
        "default": {
            "text": "Heading Text",
            "level": 2,
            "className": "bd-heading"
        },
        "example": {
            "type": "Heading",
            "props": {
                "text": "Customer Details",
                "level": 2,
                "className": "bd-heading bd-primary"
            }
        }
    },
    "Text": {
        "type": "Text",
        "description": "Text component for body content and paragraphs",
        "category": "typography",
        "required_props": ["text"],
        "optional_props": ["className", "id", "color", "size"],
        "prop_types": {
            "text": "string",
            "className": "string",
            "id": "string",
            "color": "string",
            "size": "string (small, medium, large)"
        },
        "default": {
            "text": "Text content",
            "className": "bd-text"
        },
        "example": {
            "type": "Text",
            "props": {
                "text": "This is a detailed description of the customer account.",
                "className": "bd-text bd-secondary"
            }
        }
    },
    "Label": {
        "type": "Label",
        "description": "Label component for form labels and metadata",
        "category": "typography",
        "required_props": ["text"],
        "optional_props": ["htmlFor", "className", "required"],
        "prop_types": {
            "text": "string",
            "htmlFor": "string",
            "className": "string",
            "required": "boolean"
        },
        "default": {
            "text": "Label",
            "className": "bd-label"
        },
        "example": {
            "type": "Label",
            "props": {
                "text": "Email Address",
                "htmlFor": "email-input",
                "required": True
            }
        }
    },
    "Button": {
        "type": "Button",
        "description": "Button component for actions",
        "category": "interactive",
        "required_props": ["text"],
        "optional_props": ["variant", "size", "icon", "onClick", "disabled", "className", "iconPosition"],
        "prop_types": {
            "text": "string",
            "variant": "string (primary, secondary, tertiary, danger)",
            "size": "string (small, medium, large)",
            "icon": "string",
            "onClick": "function",
            "disabled": "boolean",
            "className": "string",
            "iconPosition": "string (left, right)"
        },
        "default": {
            "text": "Button",
            "variant": "primary",
            "size": "medium",
            "className": "bd-button"
        },
        "example": {
            "type": "Button",
            "props": {
                "text": "Save Changes",
                "variant": "primary",
                "icon": "save",
                "iconPosition": "left"
            }
        }
    },
    "Link": {
        "type": "Link",
        "description": "Link component for navigation",
        "category": "interactive",
        "required_props": ["text", "href"],
        "optional_props": ["icon", "external", "className", "target"],
        "prop_types": {
            "text": "string",
            "href": "string",
            "icon": "string",
            "external": "boolean",
            "className": "string",
            "target": "string (_blank, _self)"
        },
        "default": {
            "text": "Link",
            "href": "#",
            "className": "bd-link"
        },
        "example": {
            "type": "Link",
            "props": {
                "text": "View Details",
                "href": "/customer/123",
                "icon": "external-link"
            }
        }
    },
    "Badge": {
        "type": "Badge",
        "description": "Badge component for status indicators",
        "category": "display",
        "required_props": ["text"],
        "optional_props": ["variant", "icon", "className"],
        "prop_types": {
            "text": "string",
            "variant": "string (success, warning, danger, info, default)",
            "icon": "string",
            "className": "string"
        },
        "default": {
            "text": "Badge",
            "variant": "info",
            "className": "bd-badge"
        },
        "example": {
            "type": "Badge",
            "props": {
                "text": "Active",
                "variant": "success",
                "icon": "check-circle"
            }
        }
    },
    "Chip": {
        "type": "Chip",
        "description": "Chip component for tags and filters",
        "category": "display",
        "required_props": ["text"],
        "optional_props": ["icon", "removable", "onRemove", "onClick", "className"],
        "prop_types": {
            "text": "string",
            "icon": "string",
            "removable": "boolean",
            "onRemove": "function",
            "onClick": "function",
            "className": "string"
        },
        "default": {
            "text": "Chip",
            "className": "bd-chip"
        },
        "example": {
            "type": "Chip",
            "props": {
                "text": "Marketing",
                "icon": "tag",
                "removable": True
            }
        }
    },
    "Avatar": {
        "type": "Avatar",
        "description": "Avatar component for user profile images",
        "category": "display",
        "required_props": [],
        "optional_props": ["src", "alt", "fallback", "size", "className", "shape"],
        "prop_types": {
            "src": "string (image URL)",
            "alt": "string",
            "fallback": "string (initials)",
            "size": "string (small, medium, large, xlarge)",
            "className": "string",
            "shape": "string (circle, square)"
        },
        "default": {
            "fallback": "U",
            "size": "medium",
            "shape": "circle",
            "className": "bd-avatar"
        },
        "example": {
            "type": "Avatar",
            "props": {
                "src": "/images/user.jpg",
                "alt": "John Doe",
                "fallback": "JD",
                "size": "large"
            }
        }
    },
    "Image": {
        "type": "Image",
        "description": "Image component for displaying images",
        "category": "display",
        "required_props": ["src", "alt"],
        "optional_props": ["width", "height", "className", "loading"],
        "prop_types": {
            "src": "string",
            "alt": "string",
            "width": "string | number",
            "height": "string | number",
            "className": "string",
            "loading": "string (lazy, eager)"
        },
        "default": {
            "src": "/placeholder.jpg",
            "alt": "Image",
            "className": "bd-image"
        },
        "example": {
            "type": "Image",
            "props": {
                "src": "/products/product-123.jpg",
                "alt": "Product Image",
                "width": "300",
                "height": "200"
            }
        }
    },
    "Divider": {
        "type": "Divider",
        "description": "Divider component for visual separation",
        "category": "display",
        "required_props": [],
        "optional_props": ["orientation", "className", "spacing"],
        "prop_types": {
            "orientation": "string (horizontal, vertical)",
            "className": "string",
            "spacing": "string (small, medium, large)"
        },
        "default": {
            "orientation": "horizontal",
            "className": "bd-divider"
        },
        "example": {
            "type": "Divider",
            "props": {
                "orientation": "horizontal",
                "spacing": "medium"
            }
        }
    },
    "Card": {
        "type": "Card",
        "description": "Card container for grouped content",
        "category": "containers",
        "required_props": [],
        "optional_props": ["title", "children", "className", "actions", "footer"],
        "prop_types": {
            "title": "string",
            "children": "array",
            "className": "string",
            "actions": "array",
            "footer": "object"
        },
        "default": {
            "className": "bd-card"
        },
        "example": {
            "type": "Card",
            "props": {
                "title": "Customer Information",
                "className": "bd-card"
            }
        }
    },
    "Stack": {
        "type": "Stack",
        "description": "Stack container for layout",
        "category": "containers",
        "required_props": [],
        "optional_props": ["direction", "spacing", "align", "justify", "children", "className"],
        "prop_types": {
            "direction": "string (vertical, horizontal)",
            "spacing": "string (none, small, medium, large)",
            "align": "string (start, center, end, stretch)",
            "justify": "string (start, center, end, between, around)",
            "children": "array",
            "className": "string"
        },
        "default": {
            "direction": "vertical",
            "spacing": "medium",
            "className": "bd-stack"
        },
        "example": {
            "type": "Stack",
            "props": {
                "direction": "horizontal",
                "spacing": "medium",
                "align": "center"
            }
        }
    },
    "List": {
        "type": "List",
        "description": "List component for items",
        "category": "data",
        "required_props": ["items"],
        "optional_props": ["ordered", "className", "icon"],
        "prop_types": {
            "items": "array",
            "ordered": "boolean",
            "className": "string",
            "icon": "string"
        },
        "default": {
            "items": [],
            "ordered": False,
            "className": "bd-list"
        },
        "example": {
            "type": "List",
            "props": {
                "items": ["Item 1", "Item 2", "Item 3"],
                "ordered": False,
                "icon": "check"
            }
        }
    },
    "Table": {
        "type": "Table",
        "description": "Table component for tabular data",
        "category": "data",
        "required_props": ["headers", "rows"],
        "optional_props": ["striped", "hoverable", "bordered", "className", "actions"],
        "prop_types": {
            "headers": "array",
            "rows": "array",
            "striped": "boolean",
            "hoverable": "boolean",
            "bordered": "boolean",
            "className": "string",
            "actions": "array"
        },
        "default": {
            "headers": [],
            "rows": [],
            "className": "bd-table"
        },
        "example": {
            "type": "Table",
            "props": {
                "headers": ["Name", "Status", "Amount"],
                "rows": [
                    ["John Doe", "Active", "$1,000"],
                    ["Jane Smith", "Pending", "$2,500"]
                ],
                "striped": True,
                "hoverable": True
            }
        }
    },
    "Metric": {
        "type": "Metric",
        "description": "Metric component for KPIs",
        "category": "data",
        "required_props": ["value"],
        "optional_props": ["label", "change", "trend", "icon", "className", "format"],
        "prop_types": {
            "value": "string | number",
            "label": "string",
            "change": "string | number",
            "trend": "string (up, down, neutral)",
            "icon": "string",
            "className": "string",
            "format": "string (currency, percentage, number)"
        },
        "default": {
            "value": "0",
            "className": "bd-metric"
        },
        "example": {
            "type": "Metric",
            "props": {
                "value": "$125,000",
                "label": "Total Revenue",
                "change": "+12%",
                "trend": "up",
                "icon": "trending-up"
            }
        }
    },
    "Dashlet": {
        "type": "Dashlet",
        "description": "Dashlet component for dashboard widgets",
        "category": "data",
        "required_props": ["title"],
        "optional_props": ["value", "data", "type", "className", "icon"],
        "prop_types": {
            "title": "string",
            "value": "string | number",
            "data": "array",
            "type": "string (chart, metric, list)",
            "className": "string",
            "icon": "string"
        },
        "default": {
            "title": "Dashlet",
            "type": "chart",
            "className": "bd-dashlet"
        },
        "example": {
            "type": "Dashlet",
            "props": {
                "title": "Sales Pipeline",
                "type": "chart",
                "data": [10, 20, 30, 40],
                "icon": "pie-chart"
            }
        }
    },
    "ListCard": {
        "type": "ListCard",
        "description": "ListCard component for list items with metadata",
        "category": "complex",
        "required_props": ["title"],
        "optional_props": ["description", "avatar", "metadata", "actions", "className", "badge"],
        "prop_types": {
            "title": "string",
            "description": "string",
            "avatar": "object",
            "metadata": "array",
            "actions": "array",
            "className": "string",
            "badge": "object"
        },
        "default": {
            "title": "Card Title",
            "className": "bd-listcard"
        },
        "example": {
            "type": "ListCard",
            "props": {
                "title": "John Doe",
                "description": "Senior Account Manager",
                "avatar": {"fallback": "JD"},
                "metadata": ["john@example.com", "+1 234-567-8900"],
                "badge": {"text": "VIP", "variant": "success"}
            }
        }
    },
    "BirthdayCard": {
        "type": "BirthdayCard",
        "description": "BirthdayCard component for celebrations",
        "category": "complex",
        "required_props": ["name"],
        "optional_props": ["date", "message", "avatar", "className"],
        "prop_types": {
            "name": "string",
            "date": "string",
            "message": "string",
            "avatar": "object",
            "className": "string"
        },
        "default": {
            "name": "User",
            "className": "bd-birthdaycard"
        },
        "example": {
            "type": "BirthdayCard",
            "props": {
                "name": "Sarah Johnson",
                "date": "Today",
                "message": "Wishing you a wonderful year ahead!",
                "avatar": {"src": "/avatars/sarah.jpg", "fallback": "SJ"}
            }
        }
    },
    "Insights": {
        "type": "Insights",
        "description": "Insights component for AI recommendations",
        "category": "complex",
        "required_props": ["title", "insights"],
        "optional_props": ["icon", "className", "actions"],
        "prop_types": {
            "title": "string",
            "insights": "array",
            "icon": "string",
            "className": "string",
            "actions": "array"
        },
        "default": {
            "title": "Insights",
            "insights": [],
            "className": "bd-insights"
        },
        "example": {
            "type": "Insights",
            "props": {
                "title": "AI Recommendations",
                "insights": [
                    "Follow up with 3 high-priority leads",
                    "Revenue forecast up 15% this quarter"
                ],
                "icon": "zap"
            }
        }
    },
    "Alert": {
        "type": "Alert",
        "description": "Alert component for notifications",
        "category": "complex",
        "required_props": ["message"],
        "optional_props": ["title", "variant", "icon", "dismissible", "className", "actions"],
        "prop_types": {
            "message": "string",
            "title": "string",
            "variant": "string (success, warning, danger, info)",
            "icon": "string",
            "dismissible": "boolean",
            "className": "string",
            "actions": "array"
        },
        "default": {
            "message": "Alert message",
            "variant": "info",
            "className": "bd-alert"
        },
        "example": {
            "type": "Alert",
            "props": {
                "title": "Success",
                "message": "Customer record updated successfully",
                "variant": "success",
                "icon": "check-circle",
                "dismissible": True
            }
        }
    }
}


def get_component_schema(component_type: str) -> Optional[Dict[str, Any]]:
    """Get complete schema for a component type"""
    return COMPONENT_SCHEMAS.get(component_type)


def get_component_props(component_type: str) -> Optional[Dict[str, List[str]]]:
    """Get required and optional props"""
    schema = COMPONENT_SCHEMAS.get(component_type)
    if schema:
        return {
            "required_props": schema["required_props"],
            "optional_props": schema["optional_props"]
        }
    return None


def get_component_default(component_type: str) -> Optional[Dict[str, Any]]:
    """Get default props"""
    schema = COMPONENT_SCHEMAS.get(component_type)
    if schema:
        return schema["default"].copy()
    return None


def get_component_example(component_type: str) -> Optional[Dict[str, Any]]:
    """Get example usage"""
    schema = COMPONENT_SCHEMAS.get(component_type)
    if schema:
        return schema.get("example")
    return None


def get_all_schemas() -> Dict[str, Dict[str, Any]]:
    """Get all component schemas"""
    return COMPONENT_SCHEMAS.copy()


def list_components_by_category(category: str) -> List[str]:
    """List components in a category"""
    return [
        comp_type for comp_type, schema in COMPONENT_SCHEMAS.items()
        if schema.get("category") == category
    ]


# ============================================
# ENHANCED SCHEMA METHODS (WITH VALUE SUPPORT)
# ============================================

def get_component_with_values(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get component schema with props/value separation
    
    Args:
        component_type: Component type name
        
    Returns:
        Enhanced schema with 'structure' containing 'props' and 'value' sections
    """
    return get_component_schema_with_value(component_type)


def create_component(component_type: str, data: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
    """
    Create a component instance with proper structure
    
    Args:
        component_type: Component type name
        data: Data to fill in the value section
        
    Returns:
        Component with {'type', 'props', 'value'} structure ready for layouts
    """
    return create_component_template(component_type, data)


def get_component_props_schema(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get props schema (configuration) for a component
    
    Args:
        component_type: Component type name
        
    Returns:
        Props schema with field definitions
    """
    structure = get_component_structure(component_type)
    if structure:
        return structure.get("props")
    return None


def get_component_value_schema(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get value schema (data fields) for a component
    
    Args:
        component_type: Component type name
        
    Returns:
        Value schema with field definitions
    """
    structure = get_component_structure(component_type)
    if structure:
        return structure.get("value")
    return None

