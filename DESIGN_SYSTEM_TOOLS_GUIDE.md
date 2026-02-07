# Design System Tools - Quick Reference

## Overview
Enhanced design system tools with comprehensive support for:
- ✅ **Patterns**: Layout pattern information
- ✅ **Color Palettes**: Full color system with semantic colors
- ✅ **Icons**: 90+ icons with categorization
- ✅ **Component Schemas**: Enhanced schemas with props/value separation

## Tools Available

### 1. Pattern Tools

```python
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools

tools = get_design_system_tools()

# Get specific pattern
pattern = tools.get_pattern("basic_detail")
# Returns: {name, description, category, components, component_count, ...}

# Get all patterns
all_patterns = tools.get_all_patterns()
# Returns: ['basic_detail', 'list', 'dashboard', ...]

# Get patterns by category
dashboard_patterns = tools.get_patterns_by_category("dashboard")
# Returns: ['dashboard_metrics', 'dashboard_insights', ...]

# List all categories
categories = tools.list_pattern_categories()
# Returns: ['detail', 'list', 'dashboard', 'card', 'timeline', 'special']
```

### 2. Color Palette Tools

```python
# Get all color palettes
all_colors = tools.get_color_palette()
# Returns: {primary: {...}, semantic: {...}, neutral: {...}}

# Get specific palette
semantic_colors = tools.get_color_palette("semantic")
# Returns: {success: [...], error: [...], warning: [...], info: [...]}

# Get color shades
red_shades = tools.get_color_shades("red")
# Returns: ['red-10', 'red-20', ..., 'red-100']

# List available colors
available = tools.list_available_colors()
# Returns: {primary: ['red', 'green', ...], semantic: ['success', 'error', ...], ...}

# Get semantic colors
semantic = tools.get_semantic_colors()
# Returns: {success: ['light-success', 'success', 'dark-success'], ...}
```

### 3. Icon Tools

```python
# Get icon by name
icon = tools.get_icon_by_name("user")
# Returns: "user" or None

# Search icons
icons = tools.search_icons("arrow")
# Returns: ['arrow-right', 'arrow-left', 'arrow-up', 'arrow-down', ...]

# Get icons by category
action_icons = tools.get_icons_by_category("action")
# Returns: ['edit', 'trash', 'save', 'plus', 'minus', ...]

# Get all icons
all_icons = tools.get_all_icons()
# Returns: ['user', 'edit', 'trash', ...] (90+ icons)
```

**Icon Categories:**
- `user`: user, users, user-plus, user-check, user-x
- `action`: edit, trash, save, plus, minus, check, x
- `navigation`: arrow-*, chevron-*
- `data`: table, list, grid, columns, database
- `finance`: dollar-sign, credit-card, trending-up, trending-down, pie-chart, bar-chart
- `communication`: mail, phone, message-square, send, inbox
- `file`: file, file-text, folder, download, upload, paperclip
- `status`: check-circle, alert-circle, alert-triangle, info, help-circle, bell
- `time`: calendar, clock, watch
- `business`: briefcase, target, award, star, heart
- `settings`: settings, tool, filter, search, refresh, more-*
- `media`: image, video, camera
- `location`: map-pin, globe, navigation
- `other`: home, lock, unlock, eye, eye-off, copy, share, link, tag

### 4. Component Schema Tools (Enhanced with Values)

#### Get Component Schema
```python
# Get enhanced schema with props/value separation
schema = tools.get_component_with_values("Heading")
# Returns: {
#   type: "Heading",
#   description: "...",
#   category: "typography",
#   structure: {
#     props: {...},  # Configuration
#     value: {...}   # Data fields
#   },
#   example: {...}
# }
```

#### Get Props Schema (Configuration)
```python
props_schema = tools.get_component_props_schema("Button")
# Returns: {
#   variant: {type: "string", options: ["primary", "secondary", ...], default: "primary"},
#   size: {type: "string", options: ["small", "medium", "large"], default: "medium"},
#   ...
# }
```

#### Get Value Schema (Data Fields)
```python
value_schema = tools.get_component_value_schema("Metric")
# Returns: {
#   label: {type: "string", required: True, description: "Metric label"},
#   value: {type: "string", required: True, description: "Metric value"},
#   icon: {type: "string", optional: True, default: ""},
#   ...
# }
```

#### Create Component Instance
```python
# Create component with data
heading = tools.create_component("Heading", {
    "text": "Customer Dashboard",
    "icon": "users"
})
# Returns: {
#   "type": "Heading",
#   "props": {"level": 2},
#   "value": {"text": "Customer Dashboard", "icon": "users"}
# }

metric = tools.create_component("Metric", {
    "label": "Total Revenue",
    "value": "$125,000",
    "icon": "trending-up"
})
# Returns: {
#   "type": "Metric",
#   "props": {"size": "md", ...},
#   "value": {"label": "Total Revenue", "value": "$125,000", "icon": "trending-up", ...}
# }
```

#### Get Component Example
```python
example = tools.get_component_example("Badge")
# Returns: Complete working example with type, props, and value filled
```

#### List Components
```python
# Get all component types
all_components = tools.get_all_component_types()
# Returns: ['Heading', 'Text', 'Button', 'Badge', ...] (19 components)

# Get components by category
typography = tools.get_components_by_category("typography")
# Returns: ['Heading', 'Text', 'Label']

# List all categories
categories = tools.list_component_categories()
# Returns: ['typography', 'interactive', 'display', 'containers', 'data', 'complex']
```

## Complete Component List (19 Active Components)

### Typography Components
- **Heading**: H1-H6 headings
- **Text**: Body text, paragraphs
- **Label**: Form labels, metadata

### Interactive Components
- **Button**: Action buttons (primary, secondary, tertiary, danger)
- **Link**: Navigation links

### Display Components
- **Badge**: Status badges (success, warning, danger, info)
- **Chip**: Tags, filters
- **Avatar**: User avatars
- **Image**: Images
- **Divider**: Visual separators

### Container Components
- **Card**: Content panels
- **Stack**: Layout containers

### Data Display Components
- **List**: Item lists
- **Table**: Tabular data
- **Metric**: KPIs, statistics
- **Dashlet**: Dashboard widgets

### Complex/Composite Components
- **ListCard**: List items with avatar + metadata
- **BirthdayCard**: Celebration cards
- **Insights**: AI recommendations
- **Alert**: Notifications, alerts

## Usage in LLM Workflows

### Example: Building a Layout

```python
tools = get_design_system_tools()

# Step 1: Get pattern info
pattern = tools.get_pattern("dashboard_metrics")

# Step 2: Create components based on data
heading = tools.create_component("Heading", {
    "text": "Customer Dashboard"
})

metric1 = tools.create_component("Metric", {
    "label": "Total Revenue",
    "value": "$125,000",
    "icon": "trending-up"
})

metric2 = tools.create_component("Metric", {
    "label": "Active Customers",
    "value": "1,234",
    "icon": "users"
})

table = tools.create_component("Table", {
    "headers": ["Name", "Status", "Amount"],
    "rows": [
        ["John Doe", "Active", "$5,000"],
        ["Jane Smith", "Pending", "$3,500"]
    ]
})

# Step 3: Assemble in layout structure
layout = {
    "rows": [
        {"pattern_info": [heading]},
        {"pattern_info": [metric1, metric2]},
        {"pattern_info": [table]}
    ]
}
```

### Example: Dynamic Component Creation from Data

```python
# Fetch data from CRM
leads = fetch_leads_data()  # Returns: [{name, email, status, value}, ...]

# Create components dynamically
heading = tools.create_component("Heading", {
    "text": f"Leads ({len(leads)})"
})

# Create table with lead data
table = tools.create_component("Table", {
    "headers": ["Name", "Email", "Status", "Value"],
    "rows": [[lead['name'], lead['email'], lead['status'], lead['value']] for lead in leads]
})

# Add badges for each lead status
badges = [
    tools.create_component("Badge", {
        "text": lead['status'],
        "icon": "check-circle" if lead['status'] == "Active" else "clock"
    })
    for lead in leads[:5]
]
```

## Convenience Functions

```python
from design_system_agent.agent.tools.design_system_tools import (
    get_pattern,           # Get pattern info
    get_color_palette,     # Get color palette
    get_icon,              # Get icon by name
    get_component,         # Get basic component schema
    get_component_enhanced,# Get enhanced schema with values
    create_component       # Create component instance
)

# Quick access
pattern = get_pattern("basic_detail")
colors = get_color_palette("semantic")
icon = get_icon("user")
schema = get_component_enhanced("Heading")
heading = create_component("Heading", {"text": "Title"})
```

## Integration with Existing Code

All tools are fully integrated with:
- `component_types.py` - Component type definitions
- `pattern_index.py` - Pattern cataloging
- `component_schema_with_values.py` - Enhanced schemas
- `get_component_schema.py` - Schema utilities

## Testing

Run comprehensive tests:
```bash
python test_enhanced_tools.py
```

This will demonstrate all functionality with real examples.
