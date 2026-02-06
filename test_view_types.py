"""
Test script to demonstrate View Types (List, Card, Table)
and their component mappings
"""

from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    VIEW_TYPES,
    VIEW_TYPE_COMPONENTS,
    PATTERN_TO_VIEW_TYPE,
    PATTERN_TO_VIEW_LEVEL,
    generate_pattern_queries,
    get_query_metadata
)

def show_view_types():
    """Display all available view types and their descriptions"""
    print("=" * 80)
    print("AVAILABLE VIEW TYPES")
    print("=" * 80)
    
    for view_type, description in VIEW_TYPES.items():
        print(f"\n📋 {view_type.upper()} VIEW")
        print(f"   {description}")
        
        components = VIEW_TYPE_COMPONENTS[view_type]
        print(f"\n   Required Components:")
        for comp in components["required"]:
            print(f"      • {comp}")
        
        print(f"\n   Optional Components:")
        for comp in components["optional"]:
            print(f"      • {comp}")
    
    print("\n" + "=" * 80)


def show_pattern_to_view_mapping():
    """Display which patterns use which view types"""
    print("\n" + "=" * 80)
    print("PATTERN → VIEW TYPE MAPPING")
    print("=" * 80)
    
    # Group patterns by view type
    view_type_groups = {}
    for pattern, view_type in PATTERN_TO_VIEW_TYPE.items():
        if view_type not in view_type_groups:
            view_type_groups[view_type] = []
        view_type_groups[view_type].append(pattern)
    
    for view_type, patterns in sorted(view_type_groups.items()):
        print(f"\n{view_type.upper()} VIEW:")
        for pattern in patterns:
            level = PATTERN_TO_VIEW_LEVEL.get(pattern, "basic")
            print(f"   • {pattern:30} → {level} complexity")
    
    print("\n" + "=" * 80)


def show_sample_queries_by_view_type():
    """Generate and display sample queries for each view type"""
    print("\n" + "=" * 80)
    print("SAMPLE QUERIES BY VIEW TYPE")
    print("=" * 80)
    
    # Generate samples for different patterns
    samples = {
        "LIST_SIMPLE": generate_pattern_queries("lead", "LIST_SIMPLE", 3),
        "LIST_ADVANCED": generate_pattern_queries("customer", "LIST_ADVANCED", 3),
        "MULTI_OBJECT": generate_pattern_queries("loan", "MULTI_OBJECT", 3),
        "AGGREGATE": generate_pattern_queries("account", "AGGREGATE", 3),
        "FULL_COMPLEX": generate_pattern_queries("customer", "FULL_COMPLEX", 3),
    }
    
    for pattern, queries in samples.items():
        view_type = PATTERN_TO_VIEW_TYPE.get(pattern, "table")
        view_level = PATTERN_TO_VIEW_LEVEL.get(pattern, "basic")
        
        print(f"\n{'─' * 80}")
        print(f"Pattern: {pattern}")
        print(f"View Type: {view_type.upper()} | Complexity: {view_level.upper()}")
        print(f"{'─' * 80}")
        
        for i, query in enumerate(queries, 1):
            metadata = get_query_metadata(query, pattern)
            print(f"\n{i}. {query}")
            print(f"   Components: {', '.join(metadata['components_required'][:3])}")


def show_component_distribution():
    """Show component usage statistics across view types"""
    print("\n" + "=" * 80)
    print("COMPONENT DISTRIBUTION BY VIEW TYPE")
    print("=" * 80)
    
    for view_type, components in VIEW_TYPE_COMPONENTS.items():
        total_components = len(components["required"]) + len(components["optional"])
        print(f"\n{view_type.upper()} VIEW:")
        print(f"   Total Components: {total_components}")
        print(f"   Required: {len(components['required'])}")
        print(f"   Optional: {len(components['optional'])}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "VIEW TYPES DEMONSTRATION" + " " * 34 + "║")
    print("║" + " " * 15 + "List View | Card View | Table View" + " " * 29 + "║")
    print("╚" + "═" * 78 + "╝")
    
    show_view_types()
    show_pattern_to_view_mapping()
    show_sample_queries_by_view_type()
    show_component_distribution()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ {len(VIEW_TYPES)} view types implemented: Table, List, Card")
    print(f"✓ {len(PATTERN_TO_VIEW_TYPE)} patterns mapped to view types")
    print(f"✓ Component mappings defined for each view type")
    print(f"✓ Complexity levels: basic, medium, advanced")
    print("=" * 80)
    print()
