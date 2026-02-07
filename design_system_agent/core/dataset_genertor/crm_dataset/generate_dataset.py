"""
Generate CRM Query Dataset

Simple script to generate training dataset from query templates.
Run this to create dataset files for LLM training.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from design_system_agent.core.dataset_genertor.crm_dataset.query_dataset_generator import (
    QueryDatasetGenerator
)
from design_system_agent.core.dataset_genertor.crm_dataset.queries import PATTERNS


def main():
    print("\n" + "="*60)
    print("CRM QUERY DATASET GENERATOR")
    print("="*60)
    
    # Calculate query statistics
    print("\nQuery Template Statistics:")
    object_type_counts = {}
    layout_pattern_counts = {}
    
    for query, data in PATTERNS.items():
        obj_type = data["object_type"]
        layout = data["layout_pattern"]
        object_type_counts[obj_type] = object_type_counts.get(obj_type, 0) + 1
        layout_pattern_counts[layout] = layout_pattern_counts.get(layout, 0) + 1
    
    print(f"Total queries: {len(PATTERNS)}")
    print(f"\nBy object type:")
    for obj_type, count in sorted(object_type_counts.items()):
        print(f"  {obj_type}: {count}")
    print(f"\nBy layout pattern:")
    for layout, count in sorted(layout_pattern_counts.items()):
        print(f"  {layout}: {count}")
    
    # Initialize generator
    print("\nInitializing dataset generator...")
    generator = QueryDatasetGenerator(output_dir="dataset")
    
    # Generate dataset
    print(f"\nGenerating dataset from {len(PATTERNS)} queries...")
    dataset = generator.generate_from_queries(PATTERNS)
    
    # Print statistics
    generator.print_statistics(dataset)
    
    # Save datasets
    print("Saving datasets...")
    json_path = generator.save_dataset(dataset, "crm_query_dataset.json")
    jsonl_path = generator.save_dataset_jsonl(dataset, "crm_query_dataset.jsonl")
    
    # Print sample
    print("\n" + "="*60)
    print("SAMPLE DATASET ENTRY")
    print("="*60)
    sample = dataset[0]
    print(f"Query: {sample['query']}")
    print(f"Object Type: {sample['object_type']}")
    print(f"Layout Type: {sample['layout_type']}")
    print(f"Patterns Used: {sample['patterns_used']}")
    print(f"Number of Rows: {sample['metadata']['num_rows']}")
    print(f"Number of Components: {sample['metadata']['num_components']}")
    
    print("\n" + "="*60)
    print("GENERATION COMPLETE")
    print("="*60)
    print(f"\nGenerated {len(dataset)} dataset entries")
    print(f"JSON file: {json_path}")
    print(f"JSONL file: {jsonl_path}")
    print("\nDataset ready for LLM training!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
