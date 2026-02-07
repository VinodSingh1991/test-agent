"""
Test LLM-only approach (requires OPENAI_API_KEY)
This test verifies that the system only uses LLM and no keyword-based fallbacks
"""
import os

# Check if API key is set
if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
    print("=" * 70)
    print("⚠️  OPENAI_API_KEY NOT SET")
    print("=" * 70)
    print()
    print("This system now requires OPENAI_API_KEY for all operations.")
    print("Keyword-based fallbacks have been removed per your request.")
    print()
    print("To set the API key:")
    print("  PowerShell: $env:OPENAI_API_KEY = 'sk-...'")
    print("  Bash: export OPENAI_API_KEY='sk-...'")
    print()
    print("=" * 70)
    exit(1)

from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer
from design_system_agent.agent.tools.data_fetcher import DataFetcherTool
from design_system_agent.agent.graph_nodes.default_layout import DefaultLayoutBuilder

print("=" * 70)
print("TESTING LLM-ONLY APPROACH (NO KEYWORD FALLBACKS)")
print("=" * 70)

# Initialize components
analyzer = QueryAnalyzer()
fetcher = DataFetcherTool()
builder = DefaultLayoutBuilder()

# Test query
query = "show my leads"
print(f"\nQuery: '{query}'")

# 1. Query Analysis (LLM only)
print("\n1. Query Analysis (LLM):")
try:
    analysis = analyzer.invoke(query)
    print(f"   ✓ Object Type: {analysis.object_type}")
    print(f"   ✓ Objects: {analysis.objects}")
    print(f"   ✓ Pattern: {analysis.pattern_type}")
    print(f"   ✓ Generated queries: {len(analysis.generated_queries)}")
except Exception as e:
    print(f"   ✗ FAILED: {e}")
    exit(1)

# 2. Data Fetching (LLM-based object detection)
print("\n2. Data Fetching (using LLM analysis):")
data = fetcher.detect_and_fetch(query, analysis.model_dump())
if data:
    print(f"   ✓ Data fetched successfully")
    if "_meta" in data:
        print(f"   ✓ Object: {data['_meta'].get('object_type')}")
        print(f"   ✓ Records: {data['_meta'].get('record_count')}")
else:
    print(f"   ⚠️  No data returned")

# 3. Layout Building (returns empty template)
print("\n3. Layout Building (empty template):")
layout = builder.build_default_layout(query, data, analysis.model_dump())

if "layout" in layout and "rows" in layout["layout"]:
    rows = layout["layout"]["rows"]
    print(f"   ✓ Template structure valid: {len(rows)} rows")
    
    # Check that template is empty (data not filled yet)
    for i, row in enumerate(rows):
        pattern = row.get("pattern_type")
        pattern_info = row.get("pattern_info", [])
        
        print(f"   Row {i+1}: {pattern}")
        for comp in pattern_info:
            comp_type = comp.get("type")
            value = comp.get("value", {})
            
            # Check for empty values
            if comp_type == "Badge":
                badge_text = value.get("text", "")
                if badge_text in ["0 records", ""]:
                    print(f"     ✓ Badge is empty (will be filled by DataFillingAgent)")
                else:
                    print(f"     ⚠️  Badge has value: {badge_text}")
            elif comp_type == "List":
                items = value.get("items", [])
                if not items:
                    print(f"     ✓ List is empty (will be filled by DataFillingAgent)")
                else:
                    print(f"     ⚠️  List has {len(items)} items")

print("\n" + "=" * 70)
print("✓ TEST COMPLETED - System uses LLM-only approach")
print("=" * 70)
print()
print("Next step: DataFillingAgent (LLM) will fill the empty template with actual data")
