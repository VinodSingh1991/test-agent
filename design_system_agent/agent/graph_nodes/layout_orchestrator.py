"""
LLM Layout Selector and Filler
Orchestrates three specialized agents for layout selection, data filling, and validation
"""
from typing import Dict, List, Any, Optional

from design_system_agent.agent.graph_nodes.layout_selector_agent import LayoutSelectorAgent
from design_system_agent.agent.graph_nodes.data_filling_agent import DataFillingAgent
from design_system_agent.agent.graph_nodes.output_validator_agent import OutputValidatorAgent


class LLMLayoutSelectorFiller:
    """
    Orchestrator for layout generation using three specialized agents:
    1. LayoutSelectorAgent - Selects best layout from candidates using LLM
    2. DataFillingAgent - Fills layout with actual CRM data
    3. OutputValidatorAgent - Validates final output structure
    """
    
    def __init__(self):
        self.selector_agent = LayoutSelectorAgent()
        self.filling_agent = DataFillingAgent()
        self.validator_agent = OutputValidatorAgent()
    
    def select_and_fill_layout(
        self,
        query: str,
        normalized_query: str,
        top_layouts: List[Dict],
        fetched_data: Dict[str, Any],
        analysis: Optional[Dict] = None,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Orchestrate layout selection, filling, and validation using specialized agents.
        
        Args:
            query: Original user query
            normalized_query: Normalized query
            top_layouts: Top 3 layouts from reranking
            fetched_data: Fetched CRM data
            analysis: Query analysis
            context: Additional context
            
        Returns:
            dict with:
                - selected_layout: Complete layout with all structure
                - confidence: Selection confidence
                - reasoning: Selection reasoning
                - validation: Validation results
        """
        if not top_layouts:
            raise ValueError("No layouts available for selection")
        
        # Create data summary for agents
        data_summary = self._create_data_summary(fetched_data)
        
        # AGENT 1: Layout Selector - Selects best layout from candidates
        selection_result = self.selector_agent.select_best_layout(
            query=query,
            normalized_query=normalized_query,
            candidate_layouts=top_layouts,
            data_summary=data_summary,
            analysis=analysis
        )
        
        selected_layout = selection_result["selected_layout"]
        confidence = selection_result["confidence"]
        reasoning = selection_result["reasoning"]
        is_adapted = selection_result.get("is_adapted", False)
        adaptations = selection_result.get("adaptations", [])
        
        # AGENT 2: Data Filling - Returns complete layout structure
        filled_layout = self.filling_agent.fill_layout_with_data(
            selected_layout=selected_layout,
            fetched_data=fetched_data,
            query=query,
            analysis=analysis
        )
        
        # AGENT 3: Output Validator - Validates final output
        validation = self.validator_agent.validate_output(
            layout=filled_layout,
            query=query,
            analysis=analysis
        )
        
        return {
            "selected_layout": filled_layout,
            "confidence": confidence,
            "reasoning": reasoning,
            "is_adapted": is_adapted,
            "adaptations": adaptations,
            "llm_powered": True,
            "validation": {
                "is_valid": validation.is_valid,
                "score": validation.validation_score,
                "issues": validation.issues,
                "warnings": validation.warnings
            }
        }
    
    def _create_data_summary(self, data: Dict) -> str:
        """Create concise data summary for agents"""
        if not data:
            return "No data available"
        
        summary_parts = []
        
        # Data summary
        fields = data.get("fields", {})
        
        if fields:
            summary_parts.append(f"Available fields: {len(fields)}")
            sample_fields = list(fields.keys())[:5]
            summary_parts.append(f"Sample fields: {', '.join(sample_fields)}")
        else:
            summary_parts.append("No fields available")
        
        return "\n".join(summary_parts)
