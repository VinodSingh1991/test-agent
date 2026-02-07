"""
Test different query patterns with the merged analyze_and_reformulate method
"""
import sys
import json
sys.path.insert(0, r"e:\design-system-agent")

from design_system_agent.agent.agent_controller import AgentController

def test_queries():
    """Test various CRM query patterns"""
    controller = AgentController()
    
    test_cases = [
        ("show my leads", "lead", "list"),
        ("show lead details", "lead", "detail"),
        ("create new opportunity", "opportunity", "form"),
        ("show all accounts", "account", "list"),
        ("view case details", "case", "detail"),
        ("dashboard overview", "unknown", "dashboard"),
        ("show opportunities dashboard", "opportunity", "dashboard"),
    ]
    
    print(f"\n{'='*80}")
    print(f"Testing Query Pattern Extraction")
    print(f"{'='*80}\n")
    
    results = []
    for query, expected_object, expected_layout in test_cases:
        result = controller.process_query(query)
        
        actual_object = result.get("object_type", "NOT_FOUND")
        actual_layout = result.get("layout_type", "NOT_FOUND")
        
        object_match = "✅" if actual_object == expected_object else "❌"
        layout_match = "✅" if actual_layout == expected_layout else "❌"
        
        print(f"Query: '{query}'")
        print(f"  {object_match} Object: {actual_object} (expected: {expected_object})")
        print(f"  {layout_match} Layout: {actual_layout} (expected: {expected_layout})")
        print()
        
        results.append({
            "query": query,
            "object_match": actual_object == expected_object,
            "layout_match": actual_layout == expected_layout
        })
    
    # Summary
    total = len(results)
    object_correct = sum(1 for r in results if r["object_match"])
    layout_correct = sum(1 for r in results if r["layout_match"])
    
    print(f"{'='*80}")
    print(f"Summary:")
    print(f"  Object Type: {object_correct}/{total} correct ({object_correct/total*100:.0f}%)")
    print(f"  Layout Type: {layout_correct}/{total} correct ({layout_correct/total*100:.0f}%)")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    test_queries()
