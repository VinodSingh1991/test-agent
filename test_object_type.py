"""
Test object_type extraction for query: "show my leads"
"""
import sys
import json
sys.path.insert(0, r"e:\design-system-agent")

from design_system_agent.agent.agent_controller import AgentController

def test_lead_query():
    """Test that 'show my leads' extracts object_type='lead'"""
    controller = AgentController()
    
    query = "show my leads"
    print(f"\n{'='*60}")
    print(f"Testing Query: {query}")
    print(f"{'='*60}\n")
    
    result = controller.process_query(query)
    
    print(f"\nResult:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Check object_type
    object_type = result.get("object_type", "NOT_FOUND")
    layout_type = result.get("layout_type", "NOT_FOUND")
    
    print(f"\n{'='*60}")
    print(f"OBJECT TYPE: {object_type}")
    print(f"LAYOUT TYPE: {layout_type}")
    print(f"{'='*60}\n")
    
    # Verify
    if object_type == "lead":
        print("✅ SUCCESS: object_type correctly extracted as 'lead'")
    else:
        print(f"❌ FAILED: Expected object_type='lead', got '{object_type}'")
    
    if layout_type in ["list", "detail"]:
        print(f"✅ SUCCESS: layout_type correctly extracted as '{layout_type}'")
    else:
        print(f"❌ FAILED: Expected layout_type='list' or 'detail', got '{layout_type}'")

if __name__ == "__main__":
    test_lead_query()
