"""
Design System Tools Demo
Demonstrates usage of all design system utility functions
"""
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools
import json


def demo_patterns():
    """Demonstrate pattern retrieval functions"""
    print("\n" + "="*80)
    print("PATTERN TOOLS DEMO")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get all patterns
    print("\n1. All Available Patterns:")
    patterns = tools.get_all_patterns()
    print(f"   Total: {len(patterns)} patterns")
    print(f"   Patterns: {', '.join(patterns[:5])}...")
    
    # Get pattern info
    print("\n2. Pattern Details - 'basic_detail':")
    pattern_info = tools.get_pattern("basic_detail")
    print(f"   {json.dumps(pattern_info, indent=3)}")
    
    # Get patterns by category
    print("\n3. Patterns by Category - 'dashboard':")
    dashboard_patterns = tools.get_patterns_by_category("dashboard")
    print(f"   Patterns: {dashboard_patterns}")
    
    # List all categories
    print("\n4. All Pattern Categories:")
    categories = tools.list_pattern_categories()
    print(f"   Categories: {categories}")


def demo_colors():
    """Demonstrate color palette functions"""
    print("\n" + "="*80)
    print("COLOR PALETTE TOOLS DEMO")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # List available colors
    print("\n1. Available Color Names:")
    colors = tools.list_available_colors()
    print(f"   Primary colors: {colors['primary']}")
    print(f"   Semantic colors: {colors['semantic']}")
    print(f"   Neutral colors: {list(colors['neutral'].keys())}")
    
    # Get color shades
    print("\n2. Blue Color Shades:")
    blue_shades = tools.get_color_shades("blue")
    print(f"   Shades: {blue_shades}")
    
    # Get semantic colors
    print("\n3. Semantic Colors:")
    semantic = tools.get_semantic_colors()
    for name, variants in semantic.items():
        print(f"   {name}: {variants}")
    
    # Get specific palette
    print("\n4. Primary Color Palette:")
    primary_palette = tools.get_color_palette("primary")
    print(f"   Available: {list(primary_palette.keys())}")


def demo_icons():
    """Demonstrate icon retrieval functions"""
    print("\n" + "="*80)
    print("ICON TOOLS DEMO")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get specific icon
    print("\n1. Get Specific Icon:")
    icon = tools.get_icon_by_name("user")
    print(f"   Icon 'user': {icon}")
    
    # Search icons
    print("\n2. Search Icons - 'arrow':")
    arrow_icons = tools.search_icons("arrow")
    print(f"   Found {len(arrow_icons)} icons: {arrow_icons[:5]}...")
    
    # Get icons by category
    print("\n3. Icons by Category - 'finance':")
    finance_icons = tools.get_icons_by_category("finance")
    print(f"   Finance icons: {finance_icons}")
    
    # Get all icons
    print("\n4. Total Available Icons:")
    all_icons = tools.get_all_icons()
    print(f"   Total: {len(all_icons)} icons")
    print(f"   Sample: {all_icons[:10]}...")


def demo_components():
    """Demonstrate component schema functions"""
    print("\n" + "="*80)
    print("COMPONENT SCHEMA TOOLS DEMO")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Get all component types
    print("\n1. All Component Types:")
    components = tools.get_all_component_types()
    print(f"   Total: {len(components)} components")
    print(f"   Components: {components}")
    
    # Get component schema
    print("\n2. Component Schema - 'Button':")
    button_schema = tools.get_component_by_type("Button")
    print(f"   {json.dumps(button_schema, indent=3)}")
    
    # Get component props
    print("\n3. Component Props - 'Table':")
    table_props = tools.get_component_props("Table")
    print(f"   {json.dumps(table_props, indent=3)}")
    
    # Get component default
    print("\n4. Component Default - 'Badge':")
    badge_default = tools.get_component_default("Badge")
    print(f"   {json.dumps(badge_default, indent=3)}")
    
    # Get components by category
    print("\n5. Components by Category - 'data':")
    data_components = tools.get_components_by_category("data")
    print(f"   Data components: {data_components}")
    
    # List component categories
    print("\n6. All Component Categories:")
    categories = tools.list_component_categories()
    print(f"   Categories: {categories}")


def demo_complete_workflow():
    """Demonstrate a complete workflow using all tools"""
    print("\n" + "="*80)
    print("COMPLETE WORKFLOW DEMO - Building a Dashboard Layout")
    print("="*80)
    
    tools = get_design_system_tools()
    
    # Step 1: Choose a pattern
    print("\n1. Choose Pattern:")
    pattern = tools.get_pattern("metrics_dashboard")
    print(f"   Pattern: {pattern['name']}")
    print(f"   Description: {pattern['description']}")
    print(f"   Components needed: {pattern['component_count']}")
    
    # Step 2: Get components for the pattern
    print("\n2. Get Required Components:")
    components_needed = ["Heading", "Metric", "Dashlet", "Divider"]
    for comp in components_needed:
        schema = tools.get_component_by_type(comp)
        print(f"   - {comp}: {schema['description']}")
    
    # Step 3: Choose colors for the dashboard
    print("\n3. Choose Color Scheme:")
    colors = tools.get_color_shades("blue")
    print(f"   Primary color: blue-50")
    print(f"   Background: blue-10")
    print(f"   Text: gray-90")
    
    # Step 4: Choose icons
    print("\n4. Choose Icons:")
    finance_icons = tools.get_icons_by_category("finance")
    print(f"   Using icons: {finance_icons[:3]}")
    
    # Step 5: Build the layout structure
    print("\n5. Build Layout Structure:")
    layout = {
        "pattern": "metrics_dashboard",
        "sections": [
            {
                "type": "Heading",
                "props": {
                    "text": "Sales Dashboard",
                    "level": 1,
                    "className": "bd-heading bd-blue-70"
                }
            },
            {
                "type": "Stack",
                "props": {
                    "direction": "horizontal",
                    "spacing": "medium",
                    "children": [
                        {
                            "type": "Metric",
                            "props": {
                                "label": "Total Revenue",
                                "value": "$125,000",
                                "change": "+12%",
                                "trend": "up",
                                "icon": "dollar-sign"
                            }
                        },
                        {
                            "type": "Metric",
                            "props": {
                                "label": "Active Deals",
                                "value": "48",
                                "change": "+8",
                                "trend": "up",
                                "icon": "briefcase"
                            }
                        },
                        {
                            "type": "Metric",
                            "props": {
                                "label": "Conversion Rate",
                                "value": "23%",
                                "change": "-2%",
                                "trend": "down",
                                "icon": "trending-down"
                            }
                        }
                    ]
                }
            },
            {
                "type": "Divider",
                "props": {
                    "orientation": "horizontal"
                }
            },
            {
                "type": "Dashlet",
                "props": {
                    "title": "Sales Pipeline",
                    "type": "chart",
                    "icon": "bar-chart"
                }
            }
        ]
    }
    
    print(f"   Layout built with {len(layout['sections'])} sections")
    print(f"   {json.dumps(layout, indent=3)}")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("DESIGN SYSTEM TOOLS - COMPREHENSIVE DEMO")
    print("="*80)
    
    # Run all demos
    demo_patterns()
    demo_colors()
    demo_icons()
    demo_components()
    demo_complete_workflow()
    
    print("\n" + "="*80)
    print("DEMO COMPLETE")
    print("="*80)
    print("\nAll design system tools are now available:")
    print("  - get_pattern(name)")
    print("  - get_color_palette(name)")
    print("  - get_icon(name)")
    print("  - get_component(type)")
    print("\nFor detailed usage, see the functions above!")
    print("="*80 + "\n")
