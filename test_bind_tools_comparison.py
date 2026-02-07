"""
Test comparison between legacy prompts vs bind_tools approach
Shows how bind_tools reduces prompt size significantly
"""

# Initialize agents with different modes
from design_system_agent.agent.graph_nodes.layout_selector_agent import LayoutSelectorAgent

print("=" * 80)
print("BIND_TOOLS APPROACH COMPARISON")
print("=" * 80)

# Test 1: Agent with bind_tools (NEW)
print("\n[TEST 1] Initializing with bind_tools (RECOMMENDED)")
print("-" * 80)
agent_with_tools = LayoutSelectorAgent(use_tools=True)

# Test 2: Agent without bind_tools (LEGACY)
print("\n[TEST 2] Initializing without bind_tools (LEGACY)")
print("-" * 80)
agent_legacy = LayoutSelectorAgent(use_tools=False)

# Compare prompt sizes
print("\n" + "=" * 80)
print("PROMPT SIZE COMPARISON")
print("=" * 80)

query = "show customers with balance > 100000"
normalized_query = "customers balance greater than 100000"
candidate_layouts = [{
    "id": "layout_1",
    "layout": {"rows": [{"pattern_type": "header", "pattern_info": [{"type": "Heading", "props": {"level": 1}, "value": {"text": "Customers"}}]}]},
    "patterns_used": ["header"],
    "query": "show customers"
}]
data_summary = "Sample data: 10 customer records"
analysis = {
    "pattern_type": "LIST_ADVANCED",
    "complexity_level": "medium",
    "view_type": "table",
    "has_conditions": True
}

# Build prompts
prompt_with_tools = agent_with_tools._build_prompt(
    query, normalized_query, candidate_layouts, data_summary, analysis
)
prompt_legacy = agent_legacy._build_prompt(
    query, normalized_query, candidate_layouts, data_summary, analysis
)

print(f"\n✓ With bind_tools:    {len(prompt_with_tools):,} characters")
print(f"✓ Legacy (no tools):  {len(prompt_legacy):,} characters")
print(f"\n📊 Token savings:      ~{len(prompt_legacy) - len(prompt_with_tools):,} characters")
print(f"📊 Size reduction:     {((len(prompt_legacy) - len(prompt_with_tools)) / len(prompt_legacy) * 100):.1f}%")

print("\n" + "=" * 80)
print("AVAILABLE TOOLS (when use_tools=True)")
print("=" * 80)

if agent_with_tools.llm_with_tools:
    tools = agent_with_tools.llm_with_tools.__dict__.get('bound_tools', [])
    if tools:
        print(f"\n✓ {len(tools)} tools bound to LLM:")
        for tool in tools:
            tool_name = getattr(tool, 'name', str(tool))
            print(f"  - {tool_name}")
    else:
        print("\nTools available:")
        print("  - search_icons(query)")
        print("  - get_icons_by_category(category)")
        print("  - get_all_icons()")
        print("  - get_color_shades(color)")
        print("  - get_semantic_colors()")
        print("  - get_all_colors()")
        print("  - get_component_schema(type)")
        print("  - get_components_by_category(category)")
        print("  - list_all_components()")
        print("  - get_pattern_info(name)")
        print("  - get_patterns_by_category(category)")
        print("  - list_all_patterns()")

print("\n" + "=" * 80)
print("RECOMMENDATION")
print("=" * 80)
print("\n✅ USE bind_tools=True (default) for:")
print("  - Production deployments")
print("  - Complex queries with many patterns")
print("  - Cost optimization (shorter prompts = fewer tokens)")
print("  - Dynamic icon/color selection")
print("  - Scalable design system (easily add more colors/icons)")

print("\n⚠️  USE bind_tools=False (legacy) for:")
print("  - Testing without OpenAI API key")
print("  - Simple queries with fixed color/icon sets")
print("  - When function calling is disabled")

print("\n" + "=" * 80)
print("✓ Comparison complete!")
print("=" * 80)
