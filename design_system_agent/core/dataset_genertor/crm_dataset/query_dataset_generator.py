"""
Query Dataset Generator

Generates training datasets by mapping queries to layouts and components.
Creates query-layout-pattern-component triplets for LLM training.
"""

import json
import random
from typing import List, Dict, Any, Optional
from pathlib import Path

from design_system_agent.core.dataset_genertor.crm_dataset.layout_patterns import (
    LayoutPatternFactory
)
from design_system_agent.core.dataset_genertor.crm_dataset.pattern_factory import (
    PatternFactory
)


class QueryDatasetGenerator:
    """
    Generates datasets from queries by:
    1. Matching queries to layout patterns
    2. Generating component patterns
    3. Creating sample data
    4. Outputting training examples
    """
    
    def __init__(self, output_dir: str = "dataset"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def match_query_to_layout(self, query_data: Dict[str, str]) -> str:
        """
        Get layout pattern from query data.
        Query data has explicit layout_pattern field.
        """
        return query_data.get("layout_pattern", "layout_pattern1")
    
    def generate_sample_data(self, object_type: str, layout_type: str) -> Dict[str, Any]:
        """Generate sample data based on object type and layout"""
        
        # Sample data templates
        lead_data = {
            "name": random.choice(["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams"]),
            "email": random.choice(["john@example.com", "jane@company.com", "bob@firm.com"]),
            "phone": "+1-555-0100",
            "status": random.choice(["New", "Active", "Qualified", "Converted"]),
            "priority": random.choice(["High", "Medium", "Low"]),
            "source": random.choice(["Website", "Referral", "Campaign"]),
            "owner": random.choice(["Sarah Admin", "Mike Sales", "Lisa Manager"]),
            "created_date": "2026-01-15",
            "score": random.randint(50, 100),
            "company": random.choice(["Acme Corp", "TechStart Inc", "Global Solutions"]),
            "total_leads": random.randint(100, 500),
            "active_leads": random.randint(50, 200),
            "converted_leads": random.randint(20, 100),
            "conversion_rate": round(random.uniform(15.0, 45.0), 1),
            "avg_response_time": round(random.uniform(1.0, 5.0), 1)
        }
        
        case_data = {
            "id": f"C{random.randint(1000, 9999)}",
            "subject": random.choice(["Login Issue", "Payment Failed", "Bug Report", "Feature Request"]),
            "status": random.choice(["Open", "Pending", "In Progress", "Resolved", "Closed"]),
            "priority": random.choice(["Critical", "High", "Medium", "Low"]),
            "type": random.choice(["Technical", "Billing", "General"]),
            "owner": random.choice(["Support Team", "Tech Team", "Admin"]),
            "created_date": "2026-02-01",
            "description": "Customer reported an issue that needs investigation",
            "total_cases": random.randint(50, 300),
            "open_cases": random.randint(10, 50),
            "resolved_cases": random.randint(30, 200),
            "resolution_rate": round(random.uniform(60.0, 95.0), 1),
            "avg_resolution_time": round(random.uniform(2.0, 8.0), 1)
        }
        
        account_data = {
            "name": random.choice(["Acme Corporation", "Tech Innovations", "Global Enterprises"]),
            "industry": random.choice(["Technology", "Finance", "Healthcare", "Retail"]),
            "type": random.choice(["Customer", "Partner", "Prospect"]),
            "status": random.choice(["Active", "Inactive", "Pending"]),
            "revenue": f"${random.randint(100, 999)}K",
            "employees": random.randint(10, 1000),
            "owner": random.choice(["Account Manager 1", "Account Manager 2"]),
            "created_date": "2025-12-01",
            "total_accounts": random.randint(50, 200),
            "active_accounts": random.randint(30, 150)
        }
        
        contact_data = {
            "name": random.choice(["Michael Brown", "Emily Davis", "David Wilson"]),
            "email": random.choice(["michael@company.com", "emily@firm.com"]),
            "phone": "+1-555-0200",
            "title": random.choice(["Manager", "Director", "VP Sales"]),
            "account": random.choice(["Acme Corp", "TechStart Inc"]),
            "status": random.choice(["Active", "Inactive"]),
            "owner": random.choice(["Sales Rep 1", "Sales Rep 2"]),
            "total_contacts": random.randint(100, 500)
        }
        
        data_map = {
            "lead": lead_data,
            "case": case_data,
            "account": account_data,
            "contact": contact_data
        }
        
        return data_map.get(object_type, lead_data)
    
    def generate_dataset_entry(self, query: str, query_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Generate a complete dataset entry for a query.
        Args:
            query: The query string
            query_data: Dict with object_type and layout_pattern
        Returns: {query, object_type, layout_type, patterns, components}
        """
        object_type = query_data["object_type"]
        
        # Step 1: Get layout from query data
        layout_type = self.match_query_to_layout(query_data)
        
        # Step 2: Get patterns for layout
        patterns = LayoutPatternFactory.get_patterns_for_layout(layout_type)
        
        # Step 3: Generate sample data
        data = self.generate_sample_data(object_type, layout_type)
        
        # Step 4: Generate complete layout with components
        layout = PatternFactory.generate_layout(
            query=query,
            object_type=object_type,
            data=data,
            pattern_mappings=patterns
        )
        
        # Step 5: Create dataset entry
        entry = {
            "query": query,
            "object_type": object_type,
            "layout_type": layout_type,
            "patterns_used": patterns,
            "layout": layout,
            "metadata": {
                "num_rows": len(layout["rows"]),
                "num_components": sum(len(row["pattern_info"]) for row in layout["rows"])
            }
        }
        
        return entry
    
    def generate_from_queries(self, patterns_dict: Dict[str, Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Generate dataset from PATTERNS dictionary.
        Args:
            patterns_dict: Dict mapping query strings to {object_type, layout_pattern}
        Returns:
            List of dataset entries
        """
        dataset = []
        
        for query, query_data in patterns_dict.items():
            entry = self.generate_dataset_entry(query, query_data)
            dataset.append(entry)
        
        return dataset
    
    def save_dataset(self, dataset: List[Dict[str, Any]], filename: str = "crm_query_dataset.json"):
        """Save dataset to JSON file"""
        output_path = self.output_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        
        print(f"Dataset saved to: {output_path}")
        return output_path
    
    def save_dataset_jsonl(self, dataset: List[Dict[str, Any]], filename: str = "crm_query_dataset.jsonl"):
        """Save dataset to JSONL file (one JSON per line)"""
        output_path = self.output_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for entry in dataset:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        
        print(f"Dataset saved to: {output_path}")
        return output_path
    
    def generate_statistics(self, dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate statistics about the dataset"""
        
        layout_counts = {}
        object_counts = {}
        pattern_counts = {}
        
        for entry in dataset:
            # Count layouts
            layout_type = entry["layout_type"]
            layout_counts[layout_type] = layout_counts.get(layout_type, 0) + 1
            
            # Count object types
            obj_type = entry["object_type"]
            object_counts[obj_type] = object_counts.get(obj_type, 0) + 1
            
            # Count patterns
            for pattern in entry["patterns_used"]:
                pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        stats = {
            "total_entries": len(dataset),
            "layout_distribution": layout_counts,
            "object_distribution": object_counts,
            "pattern_distribution": pattern_counts,
            "avg_rows_per_layout": sum(entry["metadata"]["num_rows"] for entry in dataset) / len(dataset),
            "avg_components_per_layout": sum(entry["metadata"]["num_components"] for entry in dataset) / len(dataset)
        }
        
        return stats
    
    def print_statistics(self, dataset: List[Dict[str, Any]]):
        """Print dataset statistics"""
        stats = self.generate_statistics(dataset)
        
        print("\n" + "="*60)
        print("DATASET STATISTICS")
        print("="*60)
        print(f"Total entries: {stats['total_entries']}")
        print(f"\nLayout Distribution:")
        for layout, count in sorted(stats['layout_distribution'].items()):
            print(f"  {layout}: {count}")
        print(f"\nObject Type Distribution:")
        for obj, count in sorted(stats['object_distribution'].items()):
            print(f"  {obj}: {count}")
        print(f"\nPattern Distribution:")
        for pattern, count in sorted(stats['pattern_distribution'].items()):
            print(f"  {pattern}: {count}")
        print(f"\nAverages:")
        print(f"  Rows per layout: {stats['avg_rows_per_layout']:.2f}")
        print(f"  Components per layout: {stats['avg_components_per_layout']:.2f}")
        print("="*60 + "\n")


def main():
    """Example usage"""
    from design_system_agent.core.dataset_genertor.crm_dataset.queries import PATTERNS
    
    # Initialize generator
    generator = QueryDatasetGenerator(output_dir="e:/design-system-agent/dataset")
    
    # Generate dataset from predefined queries
    dataset = generator.generate_from_queries(PATTERNS)
    
    # Print statistics
    generator.print_statistics(dataset)
    
    # Save in both formats
    generator.save_dataset(dataset, "crm_query_dataset.json")
    generator.save_dataset_jsonl(dataset, "crm_query_dataset.jsonl")
    
    print(f"\nGenerated {len(dataset)} dataset entries")
    print(f"Sample entry query: {dataset[0]['query']}")
    print(f"Sample entry layout: {dataset[0]['layout_type']}")


if __name__ == "__main__":
    main()
