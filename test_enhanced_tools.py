"""
Test Enhanced Design System Tools
Demonstrates the new tools for patterns, colors, icons, and component schemas with values
"""
import json
from design_system_agent.agent.tools.design_system_tools import (
    get_design_system_tools,
    get_pattern,
    get_color_palette,
    get_icon,
    get_component_enhanced,
    create_component
)


def test_patterns():
    """Test pattern retrieval"""
    print("\n" + "="*80)
    print("PATTERN TOOLS")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get specific pattern
    print("\n1. Get Pattern Info:")
    pattern = tools.get_pattern("basic_detail")
    if pattern:
        print(f"   Pattern: {pattern.get('name')}")
        print(f"   Description: {pattern.get('description')}")
        print(f"   Category: {pattern.get('category')}")
        print(f"   Components: {pattern.get('components')}")
    
    # Get all patterns
    print("\n2. All Patterns:")
    all_patterns = tools.get_all_patterns()
    print(f"   Total: {len(all_patterns)} patterns")
    print(f"   Sample: {', '.join(all_patterns[:5])}...")
    
    # Get patterns by category
    print("\n3. Patterns by Category (dashboard):")
    dashboard_patterns = tools.get_patterns_by_category("dashboard")
    print(f"   {dashboard_patterns}")


def test_colors():
    """Test color palette retrieval"""
    print("\n" + "="*80)
    print("COLOR PALETTE TOOLS")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get all color palettes
    print("\n1. All Color Palettes:")
    all_colors = tools.get_color_palette()
    print(f"   Primary colors: {list(all_colors['primary'].keys())}")
    print(f"   Semantic colors: {list(all_colors['semantic'].keys())}")
    
    # Get specific palette
    print("\n2. Semantic Color Palette:")
    semantic = tools.get_color_palette("semantic")
    print(json.dumps(semantic, indent=2))
    
    # Get color shades
    print("\n3. Red Color Shades:")
    red_shades = tools.get_color_shades("red")
    print(f"   {red_shades}")
    
    # List available colors
    print("\n4. List All Available Colors:")
    available = tools.list_available_colors()
    print(json.dumps(available, indent=2))


def test_icons():
    """Test icon retrieval"""
    print("\n" + "="*80)
    print("ICON TOOLS")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get specific icon
    print("\n1. Get Icon by Name:")
    icon = tools.get_icon_by_name("user")
    print(f"   Icon 'user': {icon}")
    
    icon = tools.get_icon_by_name("non-existent")
    print(f"   Icon 'non-existent': {icon}")
    
    # Search icons
    print("\n2. Search Icons (query: 'arrow'):")
    arrow_icons = tools.search_icons("arrow")
    print(f"   Found: {arrow_icons}")
    
    # Get icons by category
    print("\n3. Icons by Category (action):")
    action_icons = tools.get_icons_by_category("action")
    print(f"   {action_icons}")
    
    # Get all icons
    print("\n4. All Icons:")
    all_icons = tools.get_all_icons()
    print(f"   Total: {len(all_icons)} icons")
    print(f"   Sample: {', '.join(all_icons[:10])}...")


def test_components():
    """Test component schema retrieval"""
    print("\n" + "="*80)
    print("COMPONENT SCHEMA TOOLS")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get enhanced component schema
    print("\n1. Enhanced Component Schema (with values) - Heading:")
    heading_schema = tools.get_component_with_values("Heading")
    print(json.dumps(heading_schema, indent=2))
    
    # Get props schema only
    print("\n2. Component Props Schema - Button:")
    button_props = tools.get_component_props_schema("Button")
    print(json.dumps(button_props, indent=2))
    
    # Get value schema only
    print("\n3. Component Value Schema - Metric:")
    metric_value = tools.get_component_value_schema("Metric")
    print(json.dumps(metric_value, indent=2))
    
    # Get component example
    print("\n4. Component Example - Badge:")
    badge_example = tools.get_component_example("Badge")
    print(json.dumps(badge_example, indent=2))


def test_create_components():
    """Test creating component instances"""
    print("\n" + "="*80)
    print("CREATE COMPONENT INSTANCES")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Create Heading component
    print("\n1. Create Heading Component:")
    heading = tools.create_component("Heading", {
        "text": "Customer Dashboard",
        "icon": "users"
    })
    print(json.dumps(heading, indent=2))
    
    # Create Metric component
    print("\n2. Create Metric Component:")
    metric = tools.create_component("Metric", {
        "label": "Total Revenue",
        "value": "$125,000",
        "icon": "trending-up",
        "description": "Year to date"
    })
    print(json.dumps(metric, indent=2))
    
    # Create Badge component
    print("\n3. Create Badge Component:")
    badge = tools.create_component("Badge", {
        "text": "Active",
        "icon": "check-circle"
    })
    print(json.dumps(badge, indent=2))
    
    # Create Table component
    print("\n4. Create Table Component:")
    table = tools.create_component("Table", {
        "headers": ["Name", "Status", "Amount"],
        "rows": [
            ["John Doe", "Active", "$1,000"],
            ["Jane Smith", "Pending", "$2,500"]
        ]
    })
    print(json.dumps(table, indent=2))
    
    # Create ListCard component
    print("\n5. Create ListCard Component:")
    listcard = tools.create_component("ListCard", {
        "title": "John Doe",
        "description": "Senior Account Manager",
        "metadata": ["john@example.com", "+1 234-567-8900"]
    })
    print(json.dumps(listcard, indent=2))


def test_all_component_types():
    """Test all available component types"""
    print("\n" + "="*80)
    print("ALL COMPONENT TYPES")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get all component types
    print("\n1. All Available Component Types:")
    all_types = tools.get_all_component_types()
    print(f"   Total: {len(all_types)} components")
    for comp_type in all_types:
        print(f"   - {comp_type}")
    
    # Get components by category
    print("\n2. Components by Category:")
    categories = tools.list_component_categories()
    for category in categories:
        components = tools.get_components_by_category(category)
        print(f"   {category}: {components}")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("TESTING ENHANCED DESIGN SYSTEM TOOLS")
    print("="*80)
    
    # Run all tests
    test_patterns()
    test_colors()
    test_icons()
    test_components()
    test_create_components()
    test_all_component_types()
    
    print("\n" + "="*80)
    print("ALL TESTS COMPLETED")
    print("="*80 + "\n")
