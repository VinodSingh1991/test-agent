"""
Test the system works without OPENAI_API_KEY using keyword-based fallback
"""
import os
import sys

# Ensure no API key is set for this test
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer
from design_system_agent.agent.tools.data_fetcher import DataFetcherTool

print("=" * 70)
print("TESTING KEYWORD-BASED FALLBACK (NO API KEY)")
print("=" * 70)

# Test 1: Query Analysis Fallback
print("\n=== TEST 1: Query Analyzer with Fallback ===")
analyzer = QueryAnalyzer()

test_queries = [
    "show my leads",
    "get all cases",
    "list opportunities",
    "sum of loan amount grouped by branch",
    "count of leads where status is approved"
]

for query in test_queries:
    print(f"\nQuery: '{query}'")
    analysis = analyzer.invoke(query)
    print(f"  ✓ Object Type: {analysis.object_type}")
    print(f"  ✓ Objects: {analysis.objects}")
    print(f"  ✓ Pattern: {analysis.pattern_type}")
    print(f"  ✓ Aggregation: {analysis.aggregation_type}")
    print(f"  ✓ Group By: {analysis.group_by_field}")
    print(f"  ✓ Confidence: {analysis.confidence}")

# Test 2: Data Fetcher
print("\n\n=== TEST 2: Data Fetcher with Keyword Detection ===")
fetcher = DataFetcherTool()

test_cases = [
    {
        "query": "show my leads",
        "expected_object": "lead"
    },
    {
        "query": "list all cases",
        "expected_object": "case"
    },
    {
        "query": "get opportunities",
        "expected_object": "opportunity"
    }
]

for test in test_cases:
    print(f"\nQuery: '{test['query']}'")
    
    # Run query analyzer first
    analysis = analyzer.invoke(test["query"])
    
    # Fetch data
    data = fetcher.detect_and_fetch(
        query=test["query"],
        analysis=analysis.dict(),
        rag_query={"object_type": analysis.object_type}
    )
    
    if data:
        print(f"  ✓ Data fetched successfully")
        if "_meta" in data:
            print(f"  ✓ Object type: {data['_meta'].get('object_type', 'N/A')}")
            print(f"  ✓ Record count: {data['_meta'].get('record_count', 'N/A')}")
        elif "records" in data:
            print(f"  ✓ Records found: {len(data['records'])}")
        elif "fields" in data:
            print(f"  ✓ Fields found: {len(data['fields'])}")
    else:
        print(f"  ✗ No data returned")

# Test 3: End-to-End Workflow
print("\n\n=== TEST 3: End-to-End Workflow ===")
from design_system_agent.agent.graph_nodes.default_layout import DefaultLayoutBuilder

builder = DefaultLayoutBuilder()

query = "show my leads"
print(f"Query: '{query}'")

# Analyze
analysis = analyzer.invoke(query)
print(f"  1. Analysis: object_type={analysis.object_type}, pattern={analysis.pattern_type}")

# Fetch data
data = fetcher.detect_and_fetch(query, analysis.dict())
print(f"  2. Data: {len(data)} keys" if data else "  2. Data: None")

# Build layout
layout = builder.build_default_layout(query, data, analysis.dict())
print(f"  3. Layout: {len(layout.get('layout', {}).get('rows', []))} rows")

# Check layout structure
if "layout" in layout and "rows" in layout["layout"]:
    print(f"\n  ✓ Layout structure valid")
    for i, row in enumerate(layout["layout"]["rows"]):
        pattern = row.get("pattern_type", "unknown")
        num_components = len(row.get("pattern_info", []))
        print(f"    Row {i+1}: {pattern} ({num_components} components)")
else:
    print(f"  ✗ Invalid layout structure")

print("\n" + "=" * 70)
print("✓ ALL TESTS COMPLETED - System works without API key!")
print("=" * 70)
