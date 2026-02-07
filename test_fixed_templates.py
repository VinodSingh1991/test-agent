"""
Test script to verify fixed JSON templates work correctly.
Tests layout_templates.py, fallback_layout_builder.py, and default_layout.py
"""
from design_system_agent.agent.graph_nodes.layout_templates import (
    get_fallback_layout,
    validate_layout_structure,
    OBJECT_LAYOUT_TEMPLATES
)
from design_system_agent.agent.graph_nodes.fallback_layout_builder import FallbackLayoutBuilder
from design_system_agent.agent.graph_nodes.default_layout import DefaultLayoutBuilder


def test_template_structure():
    """Test that all templates have correct structure"""
    print("\n=== Testing Template Structure ===")
    
    for obj_type in OBJECT_LAYOUT_TEMPLATES.keys():
        layout = get_fallback_layout(obj_type)
        is_valid = validate_layout_structure(layout)
        
        status = "✓" if is_valid else "✗"
        print(f"{status} {obj_type}: {'Valid' if is_valid else 'INVALID'}")
        
        if not is_valid:
            print(f"   ERROR: Template structure invalid for {obj_type}")
            print(f"   Layout: {layout}")
    
    # Test unknown fallback
    layout = get_fallback_layout("unknown")
    is_valid = validate_layout_structure(layout)
    status = "✓" if is_valid else "✗"
    print(f"{status} unknown (fallback): {'Valid' if is_valid else 'INVALID'}")


def test_fallback_builder():
    """Test FallbackLayoutBuilder with fixed templates"""
    print("\n=== Testing FallbackLayoutBuilder ===")
    
    builder = FallbackLayoutBuilder()
    
    test_cases = [
        {
            "name": "Lead query with analysis",
            "query": "show me all leads",
            "data": {},
            "analysis": {
                "object_type": "lead",
                "pattern_type": "LIST_SIMPLE"
            },
            "expected_type": "lead"
        },
        {
            "name": "Case query with data",
            "query": "show cases",
            "data": {
                "_meta": {"object_type": "case"}
            },
            "analysis": None,
            "expected_type": "case"
        },
        {
            "name": "Loan query from keywords",
            "query": "sum of loan amount grouped by branch",
            "data": {},
            "analysis": None,
            "expected_type": "loan"
        },
        {
            "name": "Unknown query",
            "query": "show me data",
            "data": {},
            "analysis": None,
            "expected_type": "data"
        }
    ]
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        layout = builder.build_fallback_layout(
            test_case["query"],
            test_case["data"],
            test_case["analysis"]
        )
        is_valid = validate_layout_structure(layout)
        
        if is_valid:
            print(f"  ✓ Layout structure valid")
            print(f"  ✓ Has {len(layout['layout']['rows'])} row(s)")
            
            # Check pattern types
            for i, row in enumerate(layout['layout']['rows']):
                print(f"  ✓ Row {i+1}: {row['pattern_type']}")
        else:
            print(f"  ✗ INVALID layout structure")
            print(f"  Layout: {layout}")


def test_default_builder():
    """Test DefaultLayoutBuilder with fixed templates"""
    print("\n=== Testing DefaultLayoutBuilder ===")
    
    builder = DefaultLayoutBuilder()
    
    test_cases = [
        {
            "name": "Lead with data",
            "query": "show lead details",
            "data": {"_meta": {"object_type": "lead"}},
            "analysis": None
        },
        {
            "name": "Opportunity from keywords",
            "query": "show opportunity pipeline",
            "data": None,
            "analysis": {"intent": "Show opportunity information"}
        },
        {
            "name": "Unknown object",
            "query": "show random data",
            "data": None,
            "analysis": None
        }
    ]
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        layout = builder.build_default_layout(
            test_case["query"],
            test_case["data"],
            test_case["analysis"]
        )
        is_valid = validate_layout_structure(layout)
        
        if is_valid:
            print(f"  ✓ Layout structure valid")
            print(f"  ✓ Has {len(layout['layout']['rows'])} row(s)")
        else:
            print(f"  ✗ INVALID layout structure")


def test_structure_details():
    """Test detailed structure of a template"""
    print("\n=== Testing Detailed Structure ===")
    
    layout = get_fallback_layout("lead")
    
    print(f"✓ Has 'layout' key: {'layout' in layout}")
    print(f"✓ Has 'rows' key: {'rows' in layout['layout']}")
    print(f"✓ Rows is list: {isinstance(layout['layout']['rows'], list)}")
    print(f"✓ Number of rows: {len(layout['layout']['rows'])}")
    
    for i, row in enumerate(layout['layout']['rows']):
        print(f"\nRow {i+1}:")
        print(f"  ✓ Has 'pattern_type': {'pattern_type' in row}")
        print(f"  ✓ Has 'pattern_info': {'pattern_info' in row}")
        print(f"  ✓ Pattern type: {row.get('pattern_type', 'N/A')}")
        print(f"  ✓ Number of components: {len(row.get('pattern_info', []))}")
        
        for j, component in enumerate(row.get('pattern_info', [])):
            comp_type = component.get('component', 'unknown')
            print(f"    Component {j+1}: {comp_type}")


def test_all_object_types():
    """Test all supported object types"""
    print("\n=== Testing All Object Types ===")
    
    object_types = list(OBJECT_LAYOUT_TEMPLATES.keys())
    print(f"Total object types: {len(object_types)}")
    print(f"Object types: {', '.join(object_types)}")
    
    all_valid = True
    for obj_type in object_types:
        layout = get_fallback_layout(obj_type)
        is_valid = validate_layout_structure(layout)
        if not is_valid:
            all_valid = False
            print(f"✗ FAILED: {obj_type}")
    
    if all_valid:
        print(f"\n✓ All {len(object_types)} object types have valid templates!")
    else:
        print(f"\n✗ Some templates are invalid")


if __name__ == "__main__":
    print("=" * 60)
    print("FIXED TEMPLATE SYSTEM TESTS")
    print("=" * 60)
    
    try:
        test_template_structure()
        test_all_object_types()
        test_structure_details()
        test_fallback_builder()
        test_default_builder()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS COMPLETED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
