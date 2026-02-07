"""
Dataset Generator Controller
Provides interface for generating datasets from various sources
"""

from design_system_agent.core.dataset_genertor.crm_dataset.crm_layout_generator import CRMLayoutGenerator


class DataSetGeneratorController:
    """Controller for managing dataset generation"""
    
    def __init__(self):
        self.crm_layout_generator = CRMLayoutGenerator()

    def generate_summary_dataset(self):
        """Generate summary dataset and save to JSONL file"""
        result = self.crm_layout_generator.save_dataset()
        return {
            "status": "success",
            "message": "Summary dataset generated successfully",
            "total_records": result["total_records"],
            "jsonl_path": result["jsonl_path"],
            "json_path": result["json_path"],
            "patterns": result.get("patterns", []),
            "entities": result.get("entities", [])
        }
