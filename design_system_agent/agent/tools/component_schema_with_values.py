"""
Enhanced Component Schema with Props and Value Separation
Provides schemas that separate configuration (props) from data (value)
Based on CRM layout dataset structure
"""
from typing import Dict, Optional, Any, List


# Enhanced component schemas with props and value sections
COMPONENT_SCHEMAS_WITH_VALUES = {
    "Heading": {
        "type": "Heading",
        "description": "Heading component for titles (H1-H6)",
        "category": "typography",
        "structure": {
            "props": {
                "level": {"type": "number", "range": "1-6", "default": 2, "description": "Heading level (H1-H6)"},
                "className": {"type": "string", "optional": True, "default": "bd-heading"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Heading text content"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Optional icon name"}
            }
        },
        "example": {
            "type": "Heading",
            "props": {"level": 1},
            "value": {"icon": "", "text": "Customer Dashboard"}
        }
    },
    
    "Text": {
        "type": "Text",
        "description": "Text component for body content and paragraphs  ",
        "category": "typography",
        "structure": {
            "props": {
                "size": {"type": "string", "options": ["small", "medium", "large"], "default": "medium", "optional": True},
                "color": {"type": "string", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-text"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Text content"}
            }
        },
        "example": {
            "type": "Text",
            "props": {},
            "value": {"text": "This is the customer account description."}
        }
    },
    
    "Label": {
        "type": "Label",
        "description": "Label component for form labels and metadata",
        "category": "typography",
        "structure": {
            "props": {
                "htmlFor": {"type": "string", "optional": True},
                "required": {"type": "boolean", "optional": True, "default": False},
                "className": {"type": "string", "optional": True, "default": "bd-label"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Label text"}
            }
        },
        "example": {
            "type": "Label",
            "props": {"required": True},
            "value": {"text": "Email Address"}
        }
    },
    
    "Button": {
        "type": "Button",
        "description": "Button component for actions",
        "category": "interactive",
        "structure": {
            "props": {
                "variant": {"type": "string", "options": ["primary", "secondary", "tertiary", "danger"], "default": "primary"},
                "size": {"type": "string", "options": ["small", "medium", "large"], "default": "medium"},
                "disabled": {"type": "boolean", "optional": True, "default": False},
                "iconPosition": {"type": "string", "options": ["left", "right"], "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-button"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Button text"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Icon name"}
            }
        },
        "example": {
            "type": "Button",
            "props": {"variant": "primary", "size": "medium"},
            "value": {"text": "Save Changes", "icon": "save"}
        }
    },
    
    "Link": {
        "type": "Link",
        "description": "Link component for navigation",
        "category": "interactive",
        "structure": {
            "props": {
                "external": {"type": "boolean", "optional": True, "default": False},
                "target": {"type": "string", "options": ["_blank", "_self"], "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-link"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Link text"},
                "href": {"type": "string", "required": True, "description": "URL"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Icon name"}
            }
        },
        "example": {
            "type": "Link",
            "props": {"external": True, "target": "_blank"},
            "value": {"text": "View Details", "href": "/customer/123", "icon": "external-link"}
        }
    },
    
    "Badge": {
        "type": "Badge",
        "description": "Badge component for status indicators",
        "category": "display",
        "structure": {
            "props": {
                "variant": {"type": "string", "options": ["success", "warning", "danger", "info", "default"], "default": "info"},
                "size": {"type": "string", "options": ["small", "medium", "large"], "default": "medium", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-badge"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Badge text"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Icon name"}
            }
        },
        "example": {
            "type": "Badge",
            "props": {"variant": "success"},
            "value": {"text": "Active", "icon": "check-circle"}
        }
    },
    
    "Chip": {
        "type": "Chip",
        "description": "Chip component for tags and filters",
        "category": "display",
        "structure": {
            "props": {
                "removable": {"type": "boolean", "optional": True, "default": False},
                "className": {"type": "string", "optional": True, "default": "bd-chip"}
            },
            "value": {
                "text": {"type": "string", "required": True, "description": "Chip text"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Icon name"}
            }
        },
        "example": {
            "type": "Chip",
            "props": {"removable": True},
            "value": {"text": "Marketing", "icon": "tag"}
        }
    },
    
    "Avatar": {
        "type": "Avatar",
        "description": "Avatar component for user profile images",
        "category": "display",
        "structure": {
            "props": {
                "size": {"type": "string", "options": ["small", "medium", "large", "xlarge"], "default": "medium"},
                "shape": {"type": "string", "options": ["circle", "square"], "default": "circle"},
                "className": {"type": "string", "optional": True, "default": "bd-avatar"}
            },
            "value": {
                "src": {"type": "string", "optional": True, "description": "Image URL"},
                "alt": {"type": "string", "optional": True, "description": "Alt text"},
                "fallback": {"type": "string", "optional": True, "default": "U", "description": "Fallback initials"}
            }
        },
        "example": {
            "type": "Avatar",
            "props": {"size": "large", "shape": "circle"},
            "value": {"src": "/images/user.jpg", "alt": "John Doe", "fallback": "JD"}
        }
    },
    
    "Image": {
        "type": "Image",
        "description": "Image component for displaying images",
        "category": "display",
        "structure": {
            "props": {
                "loading": {"type": "string", "options": ["lazy", "eager"], "default": "lazy", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-image"}
            },
            "value": {
                "src": {"type": "string", "required": True, "description": "Image source URL"},
                "alt": {"type": "string", "required": True, "description": "Alt text"},
                "width": {"type": "string | number", "optional": True, "description": "Image width"},
                "height": {"type": "string | number", "optional": True, "description": "Image height"}
            }
        },
        "example": {
            "type": "Image",
            "props": {"loading": "lazy"},
            "value": {"src": "/products/product.jpg", "alt": "Product", "width": "300", "height": "200"}
        }
    },
    
    "Divider": {
        "type": "Divider",
        "description": "Divider component for visual separation",
        "category": "display",
        "structure": {
            "props": {
                "orientation": {"type": "string", "options": ["horizontal", "vertical"], "default": "horizontal"},
                "spacing": {"type": "string", "options": ["small", "medium", "large"], "default": "medium", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-divider"}
            },
            "value": {}
        },
        "example": {
            "type": "Divider",
            "props": {"orientation": "horizontal", "spacing": "medium"},
            "value": {}
        }
    },
    
    "Card": {
        "type": "Card",
        "description": "Card container for grouped content",
        "category": "containers",
        "structure": {
            "props": {
                "bordered": {"type": "boolean", "optional": True, "default": True},
                "shadow": {"type": "string", "options": ["none", "small", "medium", "large"], "default": "small", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-card"}
            },
            "value": {
                "title": {"type": "string", "optional": True, "description": "Card title"},
                "children": {"type": "array", "optional": True, "description": "Card content"}
            }
        },
        "example": {
            "type": "Card",
            "props": {"bordered": True, "shadow": "medium"},
            "value": {"title": "Customer Information"}
        }
    },
    
    "Stack": {
        "type": "Stack",
        "description": "Stack container for layout",
        "category": "containers",
        "structure": {
            "props": {
                "direction": {"type": "string", "options": ["vertical", "horizontal"], "default": "vertical"},
                "spacing": {"type": "string", "options": ["none", "small", "medium", "large"], "default": "medium"},
                "align": {"type": "string", "options": ["start", "center", "end", "stretch"], "default": "start", "optional": True},
                "justify": {"type": "string", "options": ["start", "center", "end", "between", "around"], "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-stack"}
            },
            "value": {
                "children": {"type": "array", "optional": True, "description": "Stack children"}
            }
        },
        "example": {
            "type": "Stack",
            "props": {"direction": "horizontal", "spacing": "medium", "align": "center"},
            "value": {}
        }
    },
    
    "List": {
        "type": "List",
        "description": "List component for items",
        "category": "data",
        "structure": {
            "props": {
                "ordered": {"type": "boolean", "default": False},
                "icon": {"type": "string", "optional": True, "description": "Icon for list items"},
                "className": {"type": "string", "optional": True, "default": "bd-list"}
            },
            "value": {
                "items": {"type": "array", "required": True, "description": "List of item strings"}
            }
        },
        "example": {
            "type": "List",
            "props": {"ordered": False, "icon": "check"},
            "value": {"items": ["Complete task 1", "Review task 2", "Submit task 3"]}
        }
    },
    
    "Table": {
        "type": "Table",
        "description": "Table component for tabular data",
        "category": "data",
        "structure": {
            "props": {
                "striped": {"type": "boolean", "optional": True, "default": False},
                "hoverable": {"type": "boolean", "optional": True, "default": True},
                "bordered": {"type": "boolean", "optional": True, "default": True},
                "className": {"type": "string", "optional": True, "default": "bd-table"}
            },
            "value": {
                "headers": {"type": "array", "required": True, "description": "Table column headers"},
                "rows": {"type": "array", "required": True, "description": "Table row data"}
            }
        },
        "example": {
            "type": "Table",
            "props": {"striped": True, "hoverable": True},
            "value": {
                "headers": ["Name", "Status", "Amount"],
                "rows": [["John Doe", "Active", "$1,000"], ["Jane Smith", "Pending", "$2,500"]]
            }
        }
    },
    
    "Metric": {
        "type": "Metric",
        "description": "Metric component for KPIs",
        "category": "data",
        "structure": {
            "props": {
                "size": {"type": "string", "options": ["sm", "md", "lg"], "default": "md"},
                "color": {"type": "string", "optional": True, "description": "Color theme"},
                "trend": {
                    "type": "object",
                    "optional": True,
                    "schema": {
                        "value": {"type": "number", "description": "Trend percentage"},
                        "direction": {"type": "string", "options": ["up", "down", "neutral"]},
                        "isPositive": {"type": "boolean"}
                    }
                },
                "className": {"type": "string", "optional": True, "default": "bd-metric"}
            },
            "value": {
                "label": {"type": "string", "required": True, "description": "Metric label"},
                "value": {"type": "string", "required": True, "description": "Metric value (formatted)"},
                "icon": {"type": "string", "optional": True, "default": "", "description": "Icon name"},
                "description": {"type": "string", "optional": True, "default": ""},
                "additionalInfo": {"type": "string", "optional": True, "default": ""}
            }
        },
        "example": {
            "type": "Metric",
            "props": {
                "size": "md",
                "color": "brand",
                "trend": {"value": 12.0, "direction": "up", "isPositive": True}
            },
            "value": {
                "label": "Total Revenue",
                "value": "$125K",
                "icon": "trending-up",
                "description": "",
                "additionalInfo": ""
            }
        }
    },
    
    "Dashlet": {
        "type": "Dashlet",
        "description": "Dashlet component for dashboard widgets",
        "category": "data",
        "structure": {
            "props": {
                "type": {"type": "string", "options": ["chart", "metric", "list"], "default": "chart"},
                "size": {"type": "string", "options": ["small", "medium", "large"], "default": "medium", "optional": True},
                "className": {"type": "string", "optional": True, "default": "bd-dashlet"}
            },
            "value": {
                "title": {"type": "string", "required": True, "description": "Dashlet title"},
                "value": {"type": "string | number", "optional": True, "description": "Dashlet value"},
                "data": {"type": "array", "optional": True, "description": "Chart data"},
                "icon": {"type": "string", "optional": True, "description": "Icon name"}
            }
        },
        "example": {
            "type": "Dashlet",
            "props": {"type": "chart", "size": "medium"},
            "value": {"title": "Sales Pipeline", "data": [10, 20, 30, 40], "icon": "pie-chart"}
        }
    },
    
    "ListCard": {
        "type": "ListCard",
        "description": "ListCard component for list items with metadata",
        "category": "complex",
        "structure": {
            "props": {
                "interactive": {"type": "boolean", "optional": True, "default": True},
                "className": {"type": "string", "optional": True, "default": "bd-listcard"}
            },
            "value": {
                "title": {"type": "string", "required": True, "description": "Card title"},
                "description": {"type": "string", "optional": True, "description": "Card description"},
                "avatar": {"type": "object", "optional": True, "description": "Avatar config"},
                "metadata": {"type": "array", "optional": True, "description": "Array of metadata strings"},
                "badge": {"type": "object", "optional": True, "description": "Badge config"}
            }
        },
        "example": {
            "type": "ListCard",
            "props": {"interactive": True},
            "value": {
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
        "structure": {
            "props": {
                "theme": {"type": "string", "optional": True, "description": "Card theme"},
                "className": {"type": "string", "optional": True, "default": "bd-birthdaycard"}
            },
            "value": {
                "name": {"type": "string", "required": True, "description": "Person name"},
                "date": {"type": "string", "optional": True, "description": "Birthday date"},
                "message": {"type": "string", "optional": True, "description": "Birthday message"},
                "avatar": {"type": "object", "optional": True, "description": "Avatar config"}
            }
        },
        "example": {
            "type": "BirthdayCard",
            "props": {},
            "value": {
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
        "structure": {
            "props": {
                "expandable": {"type": "boolean", "optional": True, "default": True},
                "className": {"type": "string", "optional": True, "default": "bd-insights"}
            },
            "value": {
                "title": {"type": "string", "required": True, "description": "Insights title"},
                "insights": {"type": "array", "required": True, "description": "Array of insight strings"},
                "icon": {"type": "string", "optional": True, "description": "Icon name"}
            }
        },
        "example": {
            "type": "Insights",
            "props": {"expandable": True},
            "value": {
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
        "structure": {
            "props": {
                "variant": {"type": "string", "options": ["success", "warning", "danger", "info"], "default": "info"},
                "dismissible": {"type": "boolean", "optional": True, "default": False},
                "className": {"type": "string", "optional": True, "default": "bd-alert"}
            },
            "value": {
                "title": {"type": "string", "optional": True, "description": "Alert title"},
                "message": {"type": "string", "required": True, "description": "Alert message"},
                "icon": {"type": "string", "optional": True, "description": "Icon name"}
            }
        },
        "example": {
            "type": "Alert",
            "props": {"variant": "success", "dismissible": True},
            "value": {
                "title": "Success",
                "message": "Customer record updated successfully",
                "icon": "check-circle"
            }
        }
    }
}


def get_component_schema_with_value(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get enhanced component schema with props/value separation
    
    Args:
        component_type: Component type name
        
    Returns:
        Component schema with structure containing props and value sections
    """
    return COMPONENT_SCHEMAS_WITH_VALUES.get(component_type)


def get_component_structure(component_type: str) -> Optional[Dict[str, Any]]:
    """
    Get the props and value structure for a component
    
    Args:
        component_type: Component type name
        
    Returns:
        Dictionary with 'props' and 'value' schemas
    """
    schema = COMPONENT_SCHEMAS_WITH_VALUES.get(component_type)
    if schema:
        return schema.get("structure")
    return None


def create_component_template(component_type: str, fill_values: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
    """
    Create a component template with default structure
    
    Args:
        component_type: Component type name
        fill_values: Optional dictionary with values to fill in
        
    Returns:
        Component template with type, props, and value
    """
    schema = COMPONENT_SCHEMAS_WITH_VALUES.get(component_type)
    if not schema:
        return None
    
    structure = schema.get("structure", {})
    props_schema = structure.get("props", {})
    value_schema = structure.get("value", {})
    
    # Build props with defaults
    props = {}
    for prop_name, prop_config in props_schema.items():
        if "default" in prop_config:
            props[prop_name] = prop_config["default"]
    
    # Build value with defaults and fill with provided values
    value = {}
    for value_name, value_config in value_schema.items():
        if "default" in value_config:
            value[value_name] = value_config["default"]
        elif value_config.get("required"):
            value[value_name] = ""  # Empty placeholder for required fields
    
    # Override with provided fill_values
    if fill_values:
        value.update(fill_values)
    
    return {
        "type": component_type,
        "props": props,
        "value": value
    }


def list_all_component_types() -> List[str]:
    """Get list of all component types with value schemas"""
    return list(COMPONENT_SCHEMAS_WITH_VALUES.keys())


def get_component_example(component_type: str) -> Optional[Dict[str, Any]]:
    """Get example usage for a component"""
    schema = COMPONENT_SCHEMAS_WITH_VALUES.get(component_type)
    if schema:
        return schema.get("example")
    return None
