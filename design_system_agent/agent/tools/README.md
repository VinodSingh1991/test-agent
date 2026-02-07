# Design System Tools

Comprehensive toolkit for accessing design system resources including patterns, colors, icons, and component schemas.

## Overview

The Design System Tools provide a unified interface to query and retrieve:
- **Layout Patterns**: 17 pre-built CRM layout patterns
- **Color Palettes**: 11 color families with 10 shades each + semantic colors
- **Icons**: 100+ Feather icons organized by category
- **Component Schemas**: Detailed schemas for all 19 active components

## Quick Start

```python
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools

# Get the tools instance
tools = get_design_system_tools()

# Get a pattern
pattern = tools.get_pattern("basic_detail")

# Get color shades
blue_shades = tools.get_color_shades("blue")

# Find icons
icons = tools.search_icons("arrow")

# Get component schema
button_schema = tools.get_component_by_type("Button")
```

## Available Tools

### 1. Pattern Tools

#### `get_pattern(pattern_name: str) -> Dict`
Get detailed information about a specific layout pattern.

```python
pattern = tools.get_pattern("metrics_dashboard")
# Returns: {
#   "name": "metrics_dashboard",
#   "description": "KPI dashboard with metrics and dashlets",
#   "component_count": 8,
#   "category": "dashboard"
# }
```

#### `get_patterns_by_category(category: str) -> List[str]`
Get all patterns in a category.

**Categories**: `detail`, `list`, `dashboard`, `card`, `timeline`, `special`

```python
dashboard_patterns = tools.get_patterns_by_category("dashboard")
# Returns: ["metrics_dashboard", "analytics", "dashlet"]
```

#### `get_all_patterns() -> List[str]`
Get list of all 17 available patterns.

#### `list_pattern_categories() -> List[str]`
Get list of all pattern categories.

---

### 2. Color Tools

#### `get_color_palette(palette_name: Optional[str]) -> Dict`
Get color palette(s).

```python
# Get all palettes
all_colors = tools.get_color_palette()

# Get specific palette
primary_colors = tools.get_color_palette("primary")
```

**Palettes**: `primary`, `semantic`, `neutral`

#### `get_color_shades(color_name: str) -> List[str]`
Get all 10 shades of a color.

```python
blue_shades = tools.get_color_shades("blue")
# Returns: ["blue-10", "blue-20", ..., "blue-100"]
```

**Available Colors**:
- **Primary**: red, green, blue, orange, yellow, purple, pink, cyan, teal, indigo, gray
- **Semantic**: success, error, warning, info
- **Neutral**: white, primary, secondary, disabled

#### `get_semantic_colors() -> Dict`
Get semantic color mappings.

```python
semantic = tools.get_semantic_colors()
# Returns: {
#   "success": ["light-success", "success", "dark-success"],
#   "error": ["light-error", "error", "dark-error"],
#   ...
# }
```

#### `list_available_colors() -> Dict`
List all color names organized by type.

---

### 3. Icon Tools

#### `get_icon_by_name(icon_name: str) -> Optional[str]`
Get icon if it exists.

```python
icon = tools.get_icon_by_name("user")
# Returns: "user" if exists, None otherwise
```

#### `search_icons(query: str) -> List[str]`
Search icons by keyword.

```python
arrow_icons = tools.search_icons("arrow")
# Returns: ["arrow-right", "arrow-left", "arrow-up", "arrow-down", ...]
```

#### `get_icons_by_category(category: str) -> List[str]`
Get all icons in a category.

**Categories**: `user`, `action`, `navigation`, `data`, `finance`, `communication`, `file`, `status`, `time`, `business`, `settings`, `media`, `location`, `ui`

```python
finance_icons = tools.get_icons_by_category("finance")
# Returns: ["dollar-sign", "credit-card", "trending-up", ...]
```

#### `get_all_icons() -> List[str]`
Get list of all 100+ available icons.

---

### 4. Component Schema Tools

#### `get_component_by_type(component_type: str) -> Dict`
Get complete component schema including props, defaults, and examples.

```python
button = tools.get_component_by_type("Button")
# Returns: {
#   "type": "Button",
#   "required_props": ["text"],
#   "optional_props": ["variant", "size", "icon", ...],
#   "default": {"text": "Button", "variant": "primary", ...}
# }
```

#### `get_component_props(component_type: str) -> Dict`
Get just the required and optional props.

```python
props = tools.get_component_props("Table")
# Returns: {
#   "required_props": ["headers", "rows"],
#   "optional_props": ["striped", "hoverable", "bordered", ...]
# }
```

#### `get_component_default(component_type: str) -> Dict`
Get default prop values for a component.

```python
defaults = tools.get_component_default("Badge")
# Returns: {"text": "Badge", "variant": "info", "className": "bd-badge"}
```

#### `get_all_component_types() -> List[str]`
Get list of all 19 active component types.

**Component Types**: Heading, Text, Label, Button, Link, Badge, Chip, Avatar, Image, Divider, Card, Stack, List, Table, Metric, Dashlet, ListCard, BirthdayCard, Insights, Alert

#### `get_components_by_category(category: str) -> List[str]`
Get components in a specific category.

**Categories**: `typography`, `interactive`, `display`, `containers`, `data`, `complex`

```python
data_components = tools.get_components_by_category("data")
# Returns: ["List", "Table", "Metric", "Dashlet"]
```

#### `list_component_categories() -> List[str]`
Get list of all component categories.

---

## Convenience Functions

Direct access functions without creating tools instance:

```python
from design_system_agent.agent.tools.design_system_tools import (
    get_pattern,
    get_color_palette,
    get_icon,
    get_component
)

# Use directly
pattern = get_pattern("basic_detail")
colors = get_color_palette("primary")
icon = get_icon("user")
component = get_component("Button")
```

---

## Complete Workflow Example

```python
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools

tools = get_design_system_tools()

# 1. Choose a pattern
pattern = tools.get_pattern("metrics_dashboard")

# 2. Get components needed
button = tools.get_component_by_type("Button")
metric = tools.get_component_by_type("Metric")

# 3. Choose colors
primary_color = "blue-50"
background_color = "gray-10"

# 4. Choose icons
icon = tools.get_icon_by_name("dollar-sign")

# 5. Build layout
layout = {
    "pattern": pattern["name"],
    "components": [
        {
            "type": "Metric",
            "props": {
                **metric["default"],
                "value": "$125,000",
                "label": "Revenue",
                "icon": icon,
                "className": f"bd-metric bd-bg-{background_color}"
            }
        }
    ]
}
```

---

## Testing

Run the comprehensive demo:

```bash
python test_design_system_tools.py
```

This demonstrates:
- Pattern retrieval
- Color palette usage
- Icon searching
- Component schema access
- Complete workflow building a dashboard

---

## File Structure

```
design_system_agent/agent/tools/
├── design_system_tools.py      # Main unified API
├── get_icons.py                # Icon registry
├── get_component_schema.py     # Component schemas
└── data_fetcher.py             # Data fetching (existing)
```

---

## Integration with Component Types

These tools integrate with:
- `design_system_agent.core.component_types` - Component type definitions
- `design_system_agent.core.dataset_genertor.crm_dataset.pattern_index` - Pattern definitions

---

## API Summary

| Tool | Purpose | Key Methods |
|------|---------|-------------|
| **Patterns** | Layout patterns | `get_pattern()`, `get_patterns_by_category()` |
| **Colors** | Color palettes | `get_color_shades()`, `get_semantic_colors()` |
| **Icons** | Icon library | `search_icons()`, `get_icons_by_category()` |
| **Components** | Component schemas | `get_component_by_type()`, `get_component_props()` |

---

## Next Steps

1. **Use in LLM Prompts**: Include tool outputs in prompts for layout generation
2. **Validate Components**: Use schemas to validate generated layouts
3. **Color Consistency**: Use color palettes for consistent theming
4. **Icon Selection**: Use icon search to find appropriate icons
5. **Pattern Matching**: Use patterns to guide layout structure

---

## Notes

- All 19 component types have complete schemas with examples
- Color system supports 11 color families with 10 shades each (10-100)
- Icon library based on Feather Icons (100+ icons)
- Pattern system covers 17 pre-built CRM layout patterns
- Tools are singleton-based for efficient reuse

---

*Last Updated: Design System Tools v1.0*
