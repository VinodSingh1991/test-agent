"""
Example usage of Layout Pattern Factory

Demonstrates how to use layout patterns to generate complete page layouts
based on user queries.
"""

from design_system_agent.core.dataset_genertor.crm_dataset.layout_patterns import (
    LayoutPatternFactory
)
from design_system_agent.core.dataset_genertor.crm_dataset.pattern_factory import (
    PatternFactory
)


def example_1_basic_lead():
    """Example 1: Basic Lead View"""
    print("=" * 60)
    print("Example 1: Show my basic lead")
    print("=" * 60)
    
    query = "show my basic lead"
    
    # Step 1: LLM selects layout based on query
    # Keywords: "basic", "lead" → layout_pattern1
    layout_type = 'layout_pattern1'
    
    # Step 2: Get patterns for this layout
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern1']
    
    # Step 3: Generate complete layout with components
    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "status": "Active",
        "priority": "High"
    }
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="lead",
        data=data,
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Query: {layout['query']}")
    print(f"Object Type: {layout['object_type']}")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']}")
    print()


def example_2_basic_cases():
    """Example 2: Show my basic cases"""
    print("=" * 60)
    print("Example 2: Show my basic cases")
    print("=" * 60)
    
    query = "show my basic cases"
    
    # Keywords: "basic", "cases" → layout_pattern2
    layout_type = 'layout_pattern2'
    
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern11']
    
    data = [
        {"id": "C001", "subject": "Login Issue", "status": "Open"},
        {"id": "C002", "subject": "Payment Failed", "status": "Pending"}
    ]
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="case",
        data=data,
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Query: {layout['query']}")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']} (Table View)")
    print()


def example_3_lead_dashboard():
    """Example 3: Lead Dashboard"""
    print("=" * 60)
    print("Example 3: Lead dashboard")
    print("=" * 60)
    
    query = "lead dashboard"
    
    # Keywords: "dashboard" → layout_pattern3
    layout_type = 'layout_pattern3'
    
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern0', 'pattern2']
    
    data = {
        "total_leads": 150,
        "active_leads": 89,
        "converted_leads": 45,
        "name": "Lead Overview"
    }
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="lead",
        data=data,
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Query: {layout['query']}")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']} (Metrics Dashlets)")
    print(f"Row 2: {layout['rows'][1]['pattern_type']} (Detailed Info)")
    print()


def example_4_urgent_cases():
    """Example 4: Show urgent cases"""
    print("=" * 60)
    print("Example 4: Show urgent cases")
    print("=" * 60)
    
    query = "show urgent cases"
    
    # Keywords: "urgent" → layout_pattern4
    layout_type = 'layout_pattern4'
    
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern12', 'pattern11']
    
    data = {
        "alert_message": "You have 5 urgent cases requiring immediate attention",
        "cases": [
            {"id": "C100", "subject": "System Down", "priority": "Critical"}
        ]
    }
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="case",
        data=data,
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Query: {layout['query']}")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']} (Alert Banner)")
    print(f"Row 2: {layout['rows'][1]['pattern_type']} (Cases Table)")
    print()


def example_5_llm_guidance():
    """Example 5: Get all layout guidance for LLM"""
    print("=" * 60)
    print("Example 5: Get LLM Guidance for all layouts")
    print("=" * 60)
    
    # Get guidance for all layouts
    all_guidance = LayoutPatternFactory.get_all_layouts_guidance()
    
    print("Available Layouts for LLM Selection:")
    print()
    
    for layout_type, guidance in all_guidance.items():
        print(f"{layout_type}:")
        print(f"  Use when: {guidance['use_when']}")
        print(f"  Keywords: {', '.join(guidance['keywords'][:3])}...")
        print(f"  Example: {guidance['example_queries'][0]}")
        print()


def example_6_detailed_view():
    """Example 6: Detailed account view"""
    print("=" * 60)
    print("Example 6: Detailed account view")
    print("=" * 60)
    
    query = "detailed account view"
    
    # Keywords: "detailed", "account" → layout_pattern5
    layout_type = 'layout_pattern5'
    
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern8', 'pattern5']
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="account",
        data={"name": "Acme Corp", "status": "Active"},
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']} (Status Badges)")
    print(f"Row 2: {layout['rows'][1]['pattern_type']} (Rich Details)")
    print()


def example_7_analytics_report():
    """Example 7: Lead performance report"""
    print("=" * 60)
    print("Example 7: lead performance report")
    print("=" * 60)
    
    query = "lead performance report"
    
    # Keywords: "performance", "report" → layout_pattern6
    layout_type = 'layout_pattern6'
    
    patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
    print(f"Selected Layout: {layout_type}")
    print(f"Patterns in rows: {patterns}")
    # Output: ['pattern9', 'pattern14']
    
    layout = PatternFactory.generate_layout(
        query=query,
        object_type="lead",
        data={"conversion_rate": 32.5, "avg_response_time": 2.3},
        pattern_mappings=patterns
    )
    
    print(f"\nGenerated Layout:")
    print(f"Number of Rows: {len(layout['rows'])}")
    print(f"Row 1: {layout['rows'][0]['pattern_type']} (KPI Metrics)")
    print(f"Row 2: {layout['rows'][1]['pattern_type']} (Analytics Table)")
    print()


def example_8_get_layout_info():
    """Example 8: Get detailed layout information"""
    print("=" * 60)
    print("Example 8: Get layout information")
    print("=" * 60)
    
    layout_type = 'layout_pattern3'
    
    # Get complete layout info
    info = LayoutPatternFactory.get_layout_info(layout_type)
    
    print(f"Layout Type: {info['layout_type']}")
    print(f"Description: {info['description']}")
    print(f"Patterns: {info['patterns']}")
    print(f"LLM Guidance:")
    print(f"  Use when: {info['llm_guidance']['use_when']}")
    print(f"  Best for: {info['llm_guidance']['best_for']}")
    print(f"  Keywords: {info['llm_guidance']['keywords']}")
    print()


if __name__ == "__main__":
    # Run all examples
    example_1_basic_lead()
    example_2_basic_cases()
    example_3_lead_dashboard()
    example_4_urgent_cases()
    example_5_llm_guidance()
    example_6_detailed_view()
    example_7_analytics_report()
    example_8_get_layout_info()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
