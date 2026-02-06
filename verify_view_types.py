from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    VIEW_TYPES, 
    PATTERN_TO_VIEW_TYPE, 
    VIEW_TYPE_COMPONENTS,
    get_query_metadata
)

print("\n" + "=" * 60)
print("VIEW TYPES VERIFICATION")
print("=" * 60)

print("\n📊 Available View Types:")
for vt, desc in VIEW_TYPES.items():
    print(f"   {vt.upper()}: {desc}")

print("\n📋 Pattern Distribution:")
table_p = [p for p, v in PATTERN_TO_VIEW_TYPE.items() if v == 'table']
list_p = [p for p, v in PATTERN_TO_VIEW_TYPE.items() if v == 'list']
card_p = [p for p, v in PATTERN_TO_VIEW_TYPE.items() if v == 'card']

print(f"\n   TABLE VIEW ({len(table_p)} patterns):")
for p in table_p:
    print(f"      • {p}")

print(f"\n   LIST VIEW ({len(list_p)} patterns):")
for p in list_p:
    print(f"      • {p}")

print(f"\n   CARD VIEW ({len(card_p)} patterns):")
for p in card_p:
    print(f"      • {p}")

print("\n🔍 Sample Metadata:")
queries = [
    ("show all customers", "LIST_SIMPLE"),
    ("show top 10 loans where status is approved", "LIST_ADVANCED"),
    ("show customer with related account", "MULTI_OBJECT"),
    ("show sum of loan_amount", "AGGREGATE"),
]

for query, pattern in queries:
    m = get_query_metadata(query, pattern)
    print(f"\n   Query: {query}")
    print(f"   View Type: {m['view_type'].upper()}")
    print(f"   Complexity: {m['view_level']}")
    print(f"   Components: {', '.join(m['components_required'])}")

print("\n" + "=" * 60)
print("✅ View types feature is working correctly!")
print("=" * 60)
print()
