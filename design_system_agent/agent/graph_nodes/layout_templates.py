"""
Fixed Layout Templates
Pre-defined JSON layouts for fallback scenarios
Structure: layout -> rows -> pattern_type + pattern_info
"""

# Standard fallback layout structure (used when no object type detected)
FALLBACK_LAYOUT_TEMPLATE = {
    "layout": {
        "rows": [
            {
                "pattern_type": "header",
                "pattern_info": [
                    {
                        "type": "Heading",
                        "props": {"level": 1},
                        "value": {"text": "Results", "icon": "list"}
                    },
                    {
                        "type": "Badge",
                        "props": {"variant": "info"},
                        "value": {"text": "No data available"}
                    }
                ]
            },
            {
                "pattern_type": "content",
                "pattern_info": [
                    {
                        "type": "Text",
                        "props": {},
                        "value": {"text": "No records found. Please check your query or data source."}
                    }
                ]
            }
        ]
    }
}

# Object-specific templates
OBJECT_LAYOUT_TEMPLATES = {
    "lead": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Leads", "icon": "user"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Lead information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No leads found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "case": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Cases", "icon": "briefcase"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Case information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No cases found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "account": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Accounts", "icon": "users"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Account information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No accounts found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "contact": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Contacts", "icon": "user"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Contact information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No contacts found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "opportunity": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Opportunities", "icon": "trending-up"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Opportunity information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No opportunities found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "task": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Tasks", "icon": "check-circle"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Task information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No tasks found"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "loan": {
        "layout": {
            "rows": [
                {
                    "pattern_type": "header",
                    "pattern_info": [
                        {
                            "type": "Heading",
                            "props": {"level": 1},
                            "value": {"text": "Loans", "icon": "dollar-sign"}
                        },
                        {
                            "type": "Badge",
                            "props": {"variant": "info"},
                            "value": {"text": "0 records"}
                        }
                    ]
                },
                {
                    "pattern_type": "description",
                    "pattern_info": [
                        {
                            "type": "Text",
                            "props": {},
                            "value": {"text": "Loan information will be displayed here"}
                        }
                    ]
                },
                {
                    "pattern_type": "data_list",
                    "pattern_info": [
                        {
                            "type": "List",
                            "props": {},
                            "value": {
                                "items": [],
                                "emptyMessage": "No loans found"
                            }
                        }
                    ]
                }
            ]
        }
    }
}


def get_fallback_layout(object_type: str = "unknown") -> dict:
    """
    Get fixed fallback layout for object type.
    
    Args:
        object_type: CRM object type (lead, case, account, etc.)
        
    Returns:
        Fixed JSON layout following structure: layout -> rows -> pattern_type + pattern_info
    """
    import copy
    
    # Get template for object type, or use generic fallback
    template = OBJECT_LAYOUT_TEMPLATES.get(object_type, FALLBACK_LAYOUT_TEMPLATE)
    
    # Return deep copy to avoid mutations
    return copy.deepcopy(template)


def get_custom_layout_template() -> dict:
    """
    Get empty template for custom layout creation.
    
    Returns:
        Empty layout structure with correct format
    """
    return {
        "layout": {
            "rows": []
        }
    }


def create_custom_row(pattern_type: str, components: list) -> dict:
    """
    Create a row for custom layout.
    
    Args:
        pattern_type: Type of pattern (header, content, data_list, metrics, etc.)
        components: List of component dicts with type, props, value
        
    Returns:
        Row dict with pattern_type and pattern_info
    """
    return {
        "pattern_type": pattern_type,
        "pattern_info": components
    }


def validate_layout_structure(layout: dict) -> bool:
    """
    Validate layout follows correct structure.
    
    Args:
        layout: Layout dict to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(layout, dict):
        return False
    
    if "layout" not in layout:
        return False
    
    layout_obj = layout["layout"]
    if not isinstance(layout_obj, dict):
        return False
    
    if "rows" not in layout_obj:
        return False
    
    rows = layout_obj["rows"]
    if not isinstance(rows, list):
        return False
    
    # Validate each row
    for row in rows:
        if not isinstance(row, dict):
            return False
        
        if "pattern_type" not in row or "pattern_info" not in row:
            return False
        
        if not isinstance(row["pattern_info"], list):
            return False
        
        # Validate each component in pattern_info
        for comp in row["pattern_info"]:
            if not isinstance(comp, dict):
                return False
            
            required_keys = ["type", "props", "value"]
            if not all(key in comp for key in required_keys):
                return False
    
    return True
