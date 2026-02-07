"""Test structured LLM fix"""
import os
# Use empty key to trigger mock LLM
os.environ["OPENAI_API_KEY"] = ""

from design_system_agent.agent.core.llm_factory import LLMFactory
from pydantic import BaseModel, Field

class TestModel(BaseModel):
    test_field: str = Field(description="Test field")

print("Testing LLMFactory.open_ai_structured_llm()...")

# Test without structured output
try:
    llm1 = LLMFactory.open_ai_structured_llm(structured_output=None)
    print("✓ LLM without structured output created successfully")
    print(f"  Type: {type(llm1).__name__}")
except Exception as e:
    print(f"✗ Error creating LLM without structured output: {e}")

# Test with structured output
try:
    llm2 = LLMFactory.open_ai_structured_llm(structured_output=TestModel)
    print("✓ LLM with structured output created successfully")
    print(f"  Type: {type(llm2).__name__}")
except Exception as e:
    print(f"✗ Error creating LLM with structured output: {e}")

print("\nAll tests completed!")

