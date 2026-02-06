"""
Layout Selector Agent
Specialized agent for selecting the best layout from candidates using LLM
"""
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import json

from design_system_agent.agent.core.llm_factory import LLMFactory


class LayoutSelectionResult(BaseModel):
    """Result from layout selection"""
    selected_layout_id: str = Field(description="ID of the selected layout")
    confidence: float = Field(description="Confidence score 0-1")
    reasoning: str = Field(description="Why this layout was selected")


class LayoutSelectorAgent:
    """
    Agent responsible for selecting the best layout from candidates.
    Uses LLM to analyze query intent and match with available layouts.
    """
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
    
    def select_best_layout(
        self,
        query: str,
        normalized_query: str,
        candidate_layouts: List[Dict],
        data_summary: str,
        analysis: Optional[Dict] = None
    ) -> Dict:
        """
        Select the best layout from candidates.
        
        Args:
            query: Original user query
            normalized_query: Normalized query
            candidate_layouts: List of candidate layouts (top 3 from reranking)
            data_summary: Summary of available data
            analysis: Query analysis
            
        Returns:
            dict with:
                - selected_layout: The selected layout object
                - confidence: Selection confidence
                - reasoning: Why this layout was selected
        """
        if not candidate_layouts:
            raise ValueError("No candidate layouts provided")
        
        # Build selection prompt
        prompt = self._build_prompt(
            query, normalized_query, candidate_layouts, data_summary, analysis
        )
        
        # LLM evaluates and selects
        selection = self._invoke_llm(prompt, candidate_layouts)
        
        # Get the selected layout
        selected = next(
            (l for l in candidate_layouts if l.get("id") == selection.selected_layout_id),
            candidate_layouts[0]  # Fallback to first
        )
        
        return {
            "selected_layout": selected,
            "confidence": selection.confidence,
            "reasoning": selection.reasoning
        }
    
    def _build_prompt(
        self,
        query: str,
        normalized_query: str,
        layouts: List[Dict],
        data_summary: str,
        analysis: Optional[Dict]
    ) -> str:
        """Build LLM prompt for layout selection"""
        
        # Format layouts with structure overview
        layouts_info = []
        for i, layout in enumerate(layouts, 1):
            layout_structure = self._summarize_structure(layout.get("layout", {}))
            
            layouts_info.append({
                "rank": i,
                "id": layout.get("id"),
                "pattern": layout.get("pattern"),
                "components": layout.get("components", []),
                "layout_structure": layout_structure,
                "sample_query": layout.get("query", "")
            })
        
        prompt = f"""You are a Layout Selection Agent for a CRM system.

**Task:** SELECT the best pre-built layout from 3 candidates that matches the user's query intent.

**User Query:** {query}
**Normalized Query:** {normalized_query}

**Query Analysis:**
{json.dumps(analysis, indent=2) if analysis else "Not available"}

**Available Data:**
{data_summary}

**Layout Candidates:**
{json.dumps(layouts_info, indent=2)}

**Selection Criteria:**
1. Pattern matches query intent (list/detail/card/dashboard/etc)
2. Components can display the required data
3. Structure fits the use case

**Important:**
- You are SELECTING one existing layout, not creating new ones
- Selected layout will be returned with complete Tabs→Sections→Rows→Cols structure
- MUST select from the 3 provided candidates

**Response Format (JSON):**
{{
    "selected_layout_id": "layout_id from candidates",
    "confidence": 0.0-1.0,
    "reasoning": "Why this layout best matches the query"
}}
"""
        return prompt
    
    def _summarize_structure(self, layout: Dict) -> Dict:
        """Summarize layout structure without detailed component definitions"""
        if not layout:
            return {}
        
        if "Tabs" not in layout:
            return {"type": "simple", "structure": "non-tabbed layout"}
        
        # Summarize hierarchy
        tabs_summary = []
        for tab in layout.get("Tabs", []):
            sections_summary = []
            for section in tab.get("Sections", []):
                rows_summary = []
                for row in section.get("Rows", []):
                    cols_count = len(row.get("Cols", []))
                    col_components = []
                    
                    for col in row.get("Cols", []):
                        child = col.get("Children", {})
                        if isinstance(child, dict):
                            col_components.append(child.get("type", "unknown"))
                        elif isinstance(child, list):
                            col_components.extend([
                                c.get("type", "unknown") for c in child if isinstance(c, dict)
                            ])
                    
                    rows_summary.append({
                        "RowName": row.get("RowName"),
                        "cols_count": cols_count,
                        "components": col_components
                    })
                
                sections_summary.append({
                    "SectionName": section.get("SectionName"),
                    "rows_count": len(section.get("Rows", [])),
                    "rows": rows_summary
                })
            
            tabs_summary.append({
                "TabName": tab.get("TabName"),
                "sections_count": len(tab.get("Sections", [])),
                "sections": sections_summary
            })
        
        return {
            "type": "tabbed",
            "tabs_count": len(layout.get("Tabs", [])),
            "tabs": tabs_summary
        }
    
    def _invoke_llm(
        self, prompt: str, layouts: List[Dict]
    ) -> LayoutSelectionResult:
        """Invoke LLM to select layout"""
        
        try:
            response = self.llm.invoke(prompt)
            response_text = response.content if hasattr(response, 'content') else str(response)
            
            # Parse JSON response
            result_dict = json.loads(response_text)
            
            return LayoutSelectionResult(**result_dict)
            
        except Exception as e:
            print(f"[LayoutSelectorAgent] LLM invocation failed: {e}")
            # Default to first layout
            return LayoutSelectionResult(
                selected_layout_id=layouts[0].get("id") if layouts else "",
                confidence=0.7,
                reasoning="LLM invocation failed, selected first layout as default"
            )
