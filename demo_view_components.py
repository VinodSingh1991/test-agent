"""
Demonstration: View Types automatically use their corresponding components
- Card View → Card component
- Table View → Table component
- List View → ListCard component
"""

from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    get_components_for_view_type,
    get_query_metadata,
    get_layout_for_query,
    PATTERN_TO_VIEW_TYPE
)

def demo_view_type_components():
    """Show that each view type uses its corresponding component"""
    print("=" * 80)
    print("VIEW TYPE → COMPONENT MAPPING")
    print("=" * 80)
    
    view_types = ["table", "list", "card"]
    
    for view_type in view_types:
        components = get_components_for_view_type(view_type)
        print(f"\n📋 {view_type.upper()} VIEW")
        print(f"   Primary Component: ✓ {components['primary_component']}")
        print(f"   Required: {', '.join(components['required_components'])}")
        print(f"   Optional: {', '.join(components['optional_components'][:5])}...")
    
    print("\n" + "=" * 80)


def demo_query_to_component():
    """Show that queries automatically get the right component based on view type"""
    print("\n" + "=" * 80)
    print("QUERIES → AUTOMATIC COMPONENT SELECTION")
    print("=" * 80)
    
    sample_queries = [
        ("show all customers", "LIST_SIMPLE", "table"),
        ("show top 10 leads where status is open", "LIST_ADVANCED", "table"),
        ("show customer with related account", "MULTI_OBJECT", "list"),
        ("show sum of loan_amount for customers", "AGGREGATE", "card"),
        ("show branch wise loan + account balance summary", "FULL_COMPLEX", "card"),
    ]
    
    for query, pattern, expected_view in sample_queries:
        metadata = get_query_metadata(query, pattern)
        
        print(f"\n{'─' * 80}")
        print(f"Query: {query}")
        print(f"Pattern: {pattern}")
        print(f"View Type: {metadata['view_type'].upper()}")
        print(f"✓ Primary Component: {metadata['primary_component']}")
        print(f"All Components: {', '.join(metadata['all_components'][:6])}...")
    
    print("\n" + "=" * 80)


def demo_layout_generation():
    """Show complete layout structure with primary component highlighted"""
    print("\n" + "=" * 80)
    print("LAYOUT GENERATION - PRIMARY COMPONENT USAGE")
    print("=" * 80)
    
    scenarios = [
        ("show all customers", "LIST_SIMPLE"),
        ("show customer with related loan", "MULTI_OBJECT"),
        ("show sum of account balance grouped by branch", "AGGREGATE"),
    ]
    
    for query, pattern in scenarios:
        layout = get_layout_for_query(query, pattern)
        
        print(f"\n{'─' * 80}")
        print(f"Query: {query}")
        print(f"View: {layout['view_type'].upper()} ({layout['view_level']} complexity)")
        print(f"\nLayout Structure:")
        print(f"   Header: {', '.join(layout['layout_structure']['header'])}")
        print(f"   Main: ✓ {', '.join(layout['layout_structure']['main'])} ← PRIMARY")
        print(f"   Supporting: {', '.join(layout['layout_structure']['supporting'])}")
    
    print("\n" + "=" * 80)


def show_user_request_examples():
    """Show what happens when user asks for specific view types"""
    print("\n" + "=" * 80)
    print("USER REQUEST → COMPONENT USAGE")
    print("=" * 80)
    
    print("\n✓ User asks for CARD VIEW:")
    card_info = get_components_for_view_type("card")
    print(f"   → Uses {card_info['primary_component']} component (Card)")
    print(f"   → Also includes: Metric, Dashlet, Badge, etc.")
    
    print("\n✓ User asks for TABLE VIEW:")
    table_info = get_components_for_view_type("table")
    print(f"   → Uses {table_info['primary_component']} component (Table)")
    print(f"   → Also includes: Badge, Button, Link, Chip, etc.")
    
    print("\n✓ User asks for LIST VIEW:")
    list_info = get_components_for_view_type("list")
    print(f"   → Uses {list_info['primary_component']} component (ListCard)")
    print(f"   → Also includes: Avatar, Badge, Divider, etc.")
    
    print("\n" + "=" * 80)


def show_pattern_view_mapping():
    """Show which patterns use which view types and components"""
    print("\n" + "=" * 80)
    print("PATTERN → VIEW TYPE → COMPONENT")
    print("=" * 80)
    
    # Group patterns by view type
    view_groups = {}
    for pattern, view_type in PATTERN_TO_VIEW_TYPE.items():
        if view_type not in view_groups:
            view_groups[view_type] = []
        view_groups[view_type].append(pattern)
    
    for view_type, patterns in sorted(view_groups.items()):
        primary_comp = get_components_for_view_type(view_type)['primary_component']
        print(f"\n{view_type.upper()} VIEW → Uses {primary_comp} component:")
        for pattern in patterns:
            print(f"   • {pattern}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 12 + "VIEW TYPE COMPONENT MAPPING DEMONSTRATION" + " " * 25 + "║")
    print("║" + " " * 10 + "Card View → Card | Table View → Table | List View → ListCard" + " " * 9 + "║")
    print("╚" + "═" * 78 + "╝")
    
    demo_view_type_components()
    demo_query_to_component()
    demo_layout_generation()
    show_user_request_examples()
    show_pattern_view_mapping()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("✓ Card View automatically includes Card component")
    print("✓ Table View automatically includes Table component")  
    print("✓ List View automatically includes ListCard component")
    print("✓ Each view type has primary + required + optional components")
    print("✓ Layout generation ensures primary component is always used")
    print("=" * 80)
    print()
