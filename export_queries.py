"""Export all 2000 generated banking CRM queries to various formats"""

import json
from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import (
    COMPREHENSIVE_QUERIES_2000,
    PATTERN_TO_VIEW_TYPE,
    PATTERN_BASED_QUERIES,
    get_query_statistics
)

def export_to_text(filename="banking_crm_queries_2000.txt"):
    """Export queries to a text file"""
    stats = get_query_statistics()
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BANKING CRM QUERIES - 2000 COMPREHENSIVE QUERIES\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Total Queries: {len(COMPREHENSIVE_QUERIES_2000)}\n")
        f.write(f"Generated: February 6, 2026\n\n")
        
        f.write("Query Distribution:\n")
        f.write("-" * 40 + "\n")
        for obj, count in sorted(stats['by_object'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / stats['total_queries']) * 100
            f.write(f"  {obj:12} : {count:4} ({percentage:5.1f}%)\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("ALL QUERIES\n")
        f.write("=" * 80 + "\n\n")
        
        for i, query in enumerate(COMPREHENSIVE_QUERIES_2000, 1):
            f.write(f"{i:4}. {query}\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("QUERY STATISTICS\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("Queries by Pattern:\n")
        for pattern, count in sorted(stats['by_pattern'].items(), key=lambda x: x[1], reverse=True):
            f.write(f"  {pattern:30} : {count:4}\n")
        
        f.write("\nQueries by View Type:\n")
        for view_type, count in sorted(stats['by_view_type'].items(), key=lambda x: x[1], reverse=True):
            f.write(f"  {view_type:12} : {count:4}\n")
    
    print(f"✅ Exported {len(COMPREHENSIVE_QUERIES_2000)} queries to {filename}")
    return filename


def export_to_json(filename="banking_crm_queries_2000.json"):
    """Export queries to a JSON file with metadata"""
    stats = get_query_statistics()
    
    # Create structured JSON
    data = {
        "metadata": {
            "total_queries": len(COMPREHENSIVE_QUERIES_2000),
            "generated_date": "2026-02-06",
            "domain": "Banking CRM",
            "objects": list(stats['by_object'].keys()),
            "statistics": stats
        },
        "queries": []
    }
    
    # Add queries with metadata
    for i, query in enumerate(COMPREHENSIVE_QUERIES_2000, 1):
        # Determine object type
        obj_type = None
        for obj in stats['by_object'].keys():
            if obj in query:
                obj_type = obj
                break
        
        # Determine view type based on query keywords
        view_type = "table"  # default
        if any(word in query for word in ["sum", "count", "average", "total", "metrics", "grouped"]):
            view_type = "chart"
        elif "branch" in query and any(word in query for word in ["summary", "performance", "wise"]):
            view_type = "summary"
        
        data["queries"].append({
            "id": i,
            "query": query,
            "object_type": obj_type,
            "view_type": view_type
        })
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Exported {len(COMPREHENSIVE_QUERIES_2000)} queries to {filename}")
    return filename


def export_to_csv(filename="banking_crm_queries_2000.csv"):
    """Export queries to a CSV file"""
    import csv
    
    stats = get_query_statistics()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Query', 'Object Type', 'View Type', 'Length'])
        
        for i, query in enumerate(COMPREHENSIVE_QUERIES_2000, 1):
            # Determine object type
            obj_type = ""
            for obj in stats['by_object'].keys():
                if obj in query:
                    obj_type = obj
                    break
            
            # Determine view type
            view_type = "table"
            if any(word in query for word in ["sum", "count", "average", "total", "metrics", "grouped"]):
                view_type = "chart"
            elif "branch" in query and any(word in query for word in ["summary", "performance", "wise"]):
                view_type = "summary"
            
            writer.writerow([i, query, obj_type, view_type, len(query)])
    
    print(f"✅ Exported {len(COMPREHENSIVE_QUERIES_2000)} queries to {filename}")
    return filename


def export_by_pattern(output_dir="query_patterns"):
    """Export queries organized by pattern into separate files"""
    import os
    
    os.makedirs(output_dir, exist_ok=True)
    
    for obj, patterns in PATTERN_BASED_QUERIES.items():
        obj_dir = os.path.join(output_dir, obj)
        os.makedirs(obj_dir, exist_ok=True)
        
        for pattern, queries in patterns.items():
            filename = os.path.join(obj_dir, f"{pattern}.txt")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Pattern: {pattern}\n")
                f.write(f"Object: {obj}\n")
                f.write(f"Total Queries: {len(queries)}\n")
                f.write("=" * 60 + "\n\n")
                
                for i, query in enumerate(queries, 1):
                    f.write(f"{i}. {query}\n")
    
    print(f"✅ Exported queries by pattern to {output_dir}/")
    return output_dir


if __name__ == "__main__":
    print("=" * 80)
    print("EXPORTING BANKING CRM QUERIES")
    print("=" * 80)
    print()
    
    export_to_text()
    export_to_json()
    export_to_csv()
    export_by_pattern()
    
    print()
    print("=" * 80)
    print("EXPORT COMPLETE")
    print("=" * 80)
    print("\nGenerated files:")
    print("  📄 banking_crm_queries_2000.txt  - Plain text format")
    print("  📄 banking_crm_queries_2000.json - JSON format with metadata")
    print("  📄 banking_crm_queries_2000.csv  - CSV format for Excel")
    print("  📁 query_patterns/               - Organized by object and pattern")
