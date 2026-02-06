"""Display statistics for generated banking CRM queries"""

from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    COMPREHENSIVE_QUERIES_2000, 
    get_query_statistics,
    PATTERN_TO_VIEW_TYPE
)

def show_statistics():
    """Display comprehensive query statistics"""
    stats = get_query_statistics()
    
    print("=" * 80)
    print("BANKING CRM QUERY GENERATION STATISTICS")
    print("=" * 80)
    
    print(f"\n📊 Total Queries Generated: {stats['total_queries']}")
    
    print("\n📦 Queries by Object:")
    print("-" * 40)
    for obj, count in sorted(stats['by_object'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['total_queries']) * 100
        print(f"  {obj:12} : {count:4} ({percentage:5.1f}%)")
    
    print("\n🎯 Queries by Pattern:")
    print("-" * 40)
    for pattern, count in sorted(stats['by_pattern'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['pattern_queries']) * 100 if stats['pattern_queries'] > 0 else 0
        print(f"  {pattern:30} : {count:4} ({percentage:5.1f}%)")
    
    print("\n📋 Queries by View Type:")
    print("-" * 40)
    for view_type, count in sorted(stats['by_view_type'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['pattern_queries']) * 100 if stats['pattern_queries'] > 0 else 0
        print(f"  {view_type:12} : {count:4} ({percentage:5.1f}%)")
    
    print("\n" + "=" * 80)
    print("SAMPLE QUERIES (First 20)")
    print("=" * 80)
    
    for i, query in enumerate(COMPREHENSIVE_QUERIES_2000[:20], 1):
        print(f"{i:3}. {query}")
    
    print("\n" + "=" * 80)
    print("SAMPLE QUERIES BY PATTERN")
    print("=" * 80)
    
    # Show samples from different patterns
    pattern_samples = {
        "LIST_SIMPLE": [],
        "LIST_ADVANCED": [],
        "MULTI_OBJECT": [],
        "AGGREGATE": [],
        "FULL_COMPLEX": [],
        "BRANCH_MANAGER_QUERIES": []
    }
    
    for query in COMPREHENSIVE_QUERIES_2000:
        for pattern in pattern_samples.keys():
            if len(pattern_samples[pattern]) < 3:
                # Simple heuristic to match query to pattern
                if pattern == "LIST_SIMPLE" and "show all" in query:
                    pattern_samples[pattern].append(query)
                elif pattern == "LIST_ADVANCED" and ("top 10" in query or "sorted by" in query):
                    pattern_samples[pattern].append(query)
                elif pattern == "MULTI_OBJECT" and "with related" in query:
                    pattern_samples[pattern].append(query)
                elif pattern == "AGGREGATE" and any(word in query for word in ["sum", "count", "average", "total"]):
                    pattern_samples[pattern].append(query)
                elif pattern == "FULL_COMPLEX" and "portfolio" in query:
                    pattern_samples[pattern].append(query)
                elif pattern == "BRANCH_MANAGER_QUERIES" and "branch" in query:
                    pattern_samples[pattern].append(query)
    
    for pattern, samples in pattern_samples.items():
        if samples:
            print(f"\n{pattern}:")
            for query in samples[:3]:
                print(f"  • {query}")

if __name__ == "__main__":
    show_statistics()
