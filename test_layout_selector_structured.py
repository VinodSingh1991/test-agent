"""Test Layout Selector Agent with Pydantic structured output"""
import os
os.environ["OPENAI_API_KEY"] = ""  # Empty to use mock

from design_system_agent.agent.graph_nodes.layout_selector_agent import (
    LayoutSelectorAgent, 
    LayoutSelectionResult
)
from pydantic import ValidationError

print("=" * 80)
print("TESTING LAYOUT SELECTOR AGENT - STRUCTURED OUTPUT")
print("=" * 80)

# Test 1: Verify Pydantic model structure
print("\n[TEST 1] Pydantic Model Validation")
try:
    test_result = LayoutSelectionResult(
        selected_layout_id="test_123",
        confidence=0.9,
        reasoning="Test reasoning",
        is_adapted=False,
        created_from_scratch=False,
        adaptations=["adaptation 1"],
        custom_layout={}
    )
    print(f"✓ Model created successfully: {type(test_result).__name__}")
    print(f"  - selected_layout_id: {test_result.selected_layout_id}")
    print(f"  - confidence: {test_result.confidence}")
    print(f"  - is_adapted: {test_result.is_adapted}")
    print(f"  - adaptations type: {type(test_result.adaptations)}")
except ValidationError as e:
    print(f"✗ Model validation failed: {e}")

# Test 2: Verify agent initialization
print("\n[TEST 2] Agent Initialization")
try:
    agent = LayoutSelectorAgent()
    print(f"✓ Agent initialized successfully")
    print(f"  - LLM type: {type(agent.llm).__name__}")
    print(f"  - Design tools type: {type(agent.design_tools).__name__}")
except Exception as e:
    print(f"✗ Agent initialization failed: {e}")

# Test 3: Verify structured output in _invoke_llm
print("\n[TEST 3] Structured Output Flow")
try:
    # Create a minimal mock prompt
    test_prompt = "Test prompt for layout selection"
    
    # This will use mock LLM since API key is empty
    result = agent._invoke_llm(test_prompt, "fallback_123")
    
    print(f"✓ LLM invocation completed")
    print(f"  - Result type: {type(result).__name__}")
    print(f"  - Is LayoutSelectionResult: {isinstance(result, LayoutSelectionResult)}")
    print(f"  - Selected layout ID: {result.selected_layout_id}")
    print(f"  - Confidence: {result.confidence}")
    
except Exception as e:
    print(f"✗ LLM invocation failed: {e}")

print("\n" + "=" * 80)
print("All tests completed!")
print("=" * 80)
