"""
Example Usage of Pattern Factory

Shows how to use patterns to generate layouts with rows
Demonstrates all 16 patterns and various combinations
"""

from design_system_agent.core.dataset_genertor.crm_dataset.pattern_factory import PatternFactory

# Sample data
sample_data = {
    "name": "John Doe",
    "status": "Active",
    "priority": "High",
    "owner": "Sarah Smith",
    "created_date": "2026-01-15",
    "email": "john.doe@example.com",
    "phone": "+1-555-0100"
}

print("="*80)
print("PATTERN FACTORY EXAMPLES")
print("="*80)

# Example 1: Simple customer details
print("\n1. SIMPLE CUSTOMER DETAILS (Pattern 1)")
layout1 = PatternFactory.generate_layout(
    query="Show customer details",
    object_type="lead",
    data=sample_data,
    pattern_mappings=["pattern1"]
)
print(f"Query: {layout1['query']}")
print(f"Rows: {len(layout1['rows'])} row(s)")
for row in layout1['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 2: Detailed view with breakdown
print("\n2. DETAILED VIEW (Pattern 2)")
layout2 = PatternFactory.generate_layout(
    query="Show complete lead information",
    object_type="lead",
    data=sample_data,
    pattern_mappings=["pattern2"]
)
print(f"Query: {layout2['query']}")
for row in layout2['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 3: Dashboard with metrics
print("\n3. DASHBOARD VIEW (Pattern 7 + Pattern 9)")
layout3 = PatternFactory.generate_layout(
    query="Show complete dashboard with metrics",
    object_type="case",
    data=sample_data,
    pattern_mappings=["pattern7", "pattern9"]
)
print(f"Query: {layout3['query']}")
for row in layout3['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 4: Status alert view
print("\n4. URGENT STATUS VIEW (Pattern 12)")
layout4 = PatternFactory.generate_layout(
    query="Show urgent high priority leads",
    object_type="lead",
    data=sample_data,
    pattern_mappings=["pattern12"]
)
print(f"Query: {layout4['query']}")
for row in layout4['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 5: Analytics report
print("\n5. ANALYTICS REPORT (Pattern 14)")
layout5 = PatternFactory.generate_layout(
    query="Show analytics with metrics and data",
    object_type="account",
    data=sample_data,
    pattern_mappings=["pattern14"]
)
print(f"Query: {layout5['query']}")
for row in layout5['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 6: Comparison view
print("\n6. COMPARISON VIEW (Pattern 10)")
layout6 = PatternFactory.generate_layout(
    query="Compare two accounts side by side",
    object_type="account",
    data=sample_data,
    pattern_mappings=["pattern10"]
)
print(f"Query: {layout6['query']}")
for row in layout6['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 7: Complete field inspection
print("\n7. COMPLETE FIELD VIEW (Pattern 15)")
layout7 = PatternFactory.generate_layout(
    query="Show all customer fields",
    object_type="customer",
    data=sample_data,
    pattern_mappings=["pattern15"]
)
print(f"Query: {layout7['query']}")
for row in layout7['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# Example 8: Complex multi-pattern layout
print("\n8. COMPREHENSIVE DASHBOARD (Pattern 7 + Pattern 11 + Pattern 8)")
layout8 = PatternFactory.generate_layout(
    query="Show complete overview with dashboard, table, and status",
    object_type="lead",
    data=sample_data,
    pattern_mappings=["pattern7", "pattern11", "pattern8"]
)
print(f"Query: {layout8['query']}")
for row in layout8['rows']:
    print(f"  - {row['pattern_type']}: {len(row['pattern_info'])} components")

# List all available patterns
print("\n" + "="*80)
print("AVAILABLE PATTERNS (16 total)")
print("="*80)
for pattern_type in PatternFactory.list_patterns():
    info = PatternFactory.get_pattern_info(pattern_type)
    doc_lines = info['description'].strip().split('\n')
    title = doc_lines[0] if doc_lines else "No description"
    print(f"{pattern_type}: {title}")
    print(f"  Components: {', '.join(info['components'])}")

print("\n" + "="*80)
print("See PATTERN_CATALOG.md for complete LLM decision guide")
print("="*80)

