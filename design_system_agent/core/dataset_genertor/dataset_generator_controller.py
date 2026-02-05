from design_system_agent.core.dataset_genertor.crm_dataset.crm_layout_generator import CRMLayoutGenerator
class DataSetGeneratorController:
    def __init__(self):
        self.crm_layout_generator = CRMLayoutGenerator()

    def generate_summary_dataset(self):
        """Generate summary dataset and save to JSONL file"""
        self.crm_layout_generator.save_dataset()
        return {"status": "success", "message": "Summary dataset generated successfully"}