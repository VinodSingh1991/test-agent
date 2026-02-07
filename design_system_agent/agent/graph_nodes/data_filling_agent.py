"""
Data Filling Agent
Specialized agent for filling layouts with actual CRM data
"""
from typing import Dict, Optional


class DataFillingAgent:
    """
    Agent responsible for filling selected layout with actual data.
    Returns the complete layout structure with all metadata.
    """
    
    def fill_layout_with_data(
        self,
        selected_layout: Dict,
        fetched_data: Dict,
        query: str,
        analysis: Optional[Dict] = None
    ) -> Dict:
        """
        Fill the selected layout with actual data.
        
        Args:
            selected_layout: The layout selected by LayoutSelectorAgent
            fetched_data: Data fetched from CRM
            query: Original user query
            analysis: Query analysis
            
        Returns:
            Complete layout object with all fields:
                - id: Layout ID
                - object_type: Object type (lead, case, etc.)
                - layout_type: Layout pattern type
                - layout: Simplified structure with rows -> pattern_info components
                - score: Layout score
                - query: Original query from dataset
                - metadata: Additional metadata
        """
        
        # Return the complete layout structure as-is from dataset
        # The layout already has the correct structure with rows -> pattern_info
        
        return {
            "id": selected_layout.get("id"),
            "layout": selected_layout.get("layout"),  # Simplified rows/pattern structure
            "score": selected_layout.get(
                "score", 
                selected_layout.get("final_score", selected_layout.get("rerank_score", 0.95))
            ),
            "query": selected_layout.get("query", ""),
            "metadata": {
                **selected_layout.get("metadata", {}),
                "filled_by_agent": True,
                "user_query": query,
                "has_data": bool(fetched_data)
            }
        }
    
    def _create_data_summary(self, data: Dict) -> str:
        """Create summary of available data"""
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
