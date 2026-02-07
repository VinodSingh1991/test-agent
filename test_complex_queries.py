"""
Test script for complex CRM queries
Tests the enhanced QueryAnalyzer with complex patterns
"""
import os
os.environ["OPENAI_API_KEY"] = "test"  # Set a test key

from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer

# Test queries from crm_queries.py patterns
test_queries = [
    # LIST_SIMPLE
    "show all leads",
    
    # LIST_ADVANCED  
    "top 10 leads sorted by created_date desc",
    
    # MULTI_OBJECT
    "show leads with related customer",
    
    # AGGREGATE
    "sum of loan amount in customer",
    
    # ADVANCED_AGGREGATE_RELATED
    "sum of loan amount for customers grouped by branch",
    "branch wise count of emi amount",
    
    # FULL_COMPLEX
    "show customers with total balance greater than 100000 and loan amount greater than 50000",
    "branch wise count of leads where loan status is approved",
    "show customers who have loans and also leads in pending status",
    
    # PATTERN_COMBINATIONS
    "show customers whose account balance is greater than 100000",
    "show leads where customer has loan status approved",
]

def test_query_analysis():
    """Test query analyzer with complex queries"""
    analyzer = QueryAnalyzer()
    
    print("=" * 80)
    print("TESTING COMPLEX QUERY ANALYSIS")
    print("=" * 80)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'─' * 80}")
        print(f"TEST {i}: {query}")
        print(f"{'─' * 80}")
        
        try:
            analysis = analyzer.invoke(query)
            
            print(f"\n✓ Normalized: {analysis.normalized_query}")
            print(f"✓ Pattern Type: {analysis.pattern_type}")
            print(f"✓ Complexity: {analysis.complexity_level}")
            print(f"✓ Objects: {analysis.objects}")
            print(f"✓ View Type: {analysis.view_type}")
            
            if analysis.aggregation_type:
                print(f"✓ Aggregation: {analysis.aggregation_type}")
            if analysis.group_by_field:
                print(f"✓ Group By: {analysis.group_by_field}")
            if analysis.has_conditions:
                print(f"✓ Has Conditions: True")
            if analysis.has_sorting:
                print(f"✓ Has Sorting: True")
                
            print(f"\n  Generated Queries:")
            for j, gq in enumerate(analysis.generated_queries[:3], 1):
                print(f"  {j}. {gq}")
            
            print(f"\n  Confidence: {analysis.confidence}")
            
        except Exception as e:
            print(f"\n✗ ERROR: {e}")

if __name__ == "__main__":
    test_query_analysis()
