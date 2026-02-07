"""
Test template data filling
"""
import os
import sys

# Ensure no API key is set
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer
from design_system_agent.agent.tools.data_fetcher import DataFetcherTool
from design_system_agent.agent.graph_nodes.default_layout import DefaultLayoutBuilder

print("=" * 70)
print("TESTING TEMPLATE DATA FILLING")
print("=" * 70)

# Initialize components
analyzer = QueryAnalyzer()
fetcher = DataFetcherTool()
builder = DefaultLayoutBuilder()

# Test query
query = "show my leads"
print(f"\nQuery: '{query}'")

# 1. Analyze query
print("\n1. Query Analysis:")
analysis = analyzer.invoke(query)
print(f"   Object Type: {analysis.object_type}")
print(f"   Objects: {analysis.objects}")
print(f"   Pattern: {analysis.pattern_type}")

# 2. Fetch data
print("\n2. Data Fetching:")
data = fetcher.detect_and_fetch(query, analysis.model_dump())
if data:
    print(f"   ✓ Data fetched")
    if "_meta" in data:
        print(f"   ✓ Object: {data['_meta'].get('object_type')}")
        print(f"   ✓ Records: {data['_meta'].get('record_count')}")
    if "records" in data:
        print(f"   ✓ Record count: {len(data['records'])}")
        print(f"   ✓ First record: {data['records'][0] if data['records'] else 'None'}")
else:
    print(f"   ✗ No data")

# 3. Build and fill layout
print("\n3. Layout Building with Data Filling:")
layout = builder.build_default_layout(query, data, analysis.model_dump())

# 4. Verify filled data
print("\n4. Verification:")
if "layout" in layout and "rows" in layout["layout"]:
    rows = layout["layout"]["rows"]
    print(f"   ✓ Structure valid: {len(rows)} rows")
    
    for i, row in enumerate(rows):
        pattern = row.get("pattern_type")
        pattern_info = row.get("pattern_info", [])
        
        print(f"\n   Row {i+1}: {pattern}")
        for j, comp in enumerate(pattern_info):
            comp_type = comp.get("type")
            value = comp.get("value", {})
            
            print(f"     Component {j+1} ({comp_type}):")
            if comp_type == "Badge":
                print(f"       Text: {value.get('text')}")
            elif comp_type == "List":
                items = value.get("items", [])
                print(f"       Items count: {len(items)}")
                if items:
                    print(f"       First item: {items[0][:80]}...")
            elif comp_type == "Text":
                text = value.get("text", "")
                print(f"       Text: {text[:80]}...")
            elif comp_type == "Heading":
                print(f"       Text: {value.get('text')}")

print("\n" + "=" * 70)
print("✓ TEST COMPLETED")
print("=" * 70)
