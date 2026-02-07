"""
Layout Selector Agent
Specialized agent for selecting the best layout from candidates using LLM
"""
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import json

from design_system_agent.agent.core.llm_factory import LLMFactory
from design_system_agent.core.component_types import ACTIVE_COMPONENTS, COMPONENT_CATEGORIES
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools


class LayoutSelectionResult(BaseModel):
    """Result from layout selection/adaptation"""
    selected_layout_id: str = Field(description="ID of the selected layout or 'custom_layout' if created from scratch")
    confidence: float = Field(description="Confidence score 0-1")
    reasoning: str = Field(description="Why this layout was selected/adapted/created")
    is_adapted: bool = Field(default=False, description="Whether layout was modified")
    created_from_scratch: bool = Field(default=False, description="Whether layout was created from scratch")
    adaptations: list = Field(default_factory=list, description="List of adaptations/creations made")
    custom_layout: dict = Field(default_factory=dict, description="Custom layout structure if created from scratch")


class LayoutSelectorAgent:
    """
    Agent responsible for selecting the best layout from candidates.
    Uses LLM to analyze query intent and match with available layouts.
    """
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
        self.design_tools = get_design_system_tools()
    
    def _validate_design_tokens(self, layout: dict) -> dict:
        """
        Validate and fix colors/icons in layout to ensure they exist in design system
        
        Args:
            layout: Layout structure with rows and components
            
        Returns:
            Validated layout with fixed/default colors and icons
        """
        valid_colors = set(self.design_tools.list_available_colors().get("primary", {}).keys())
        valid_colors.update(self.design_tools.get_semantic_colors().keys())
        valid_colors.update(["neutral-white", "neutral-primary", "neutral-secondary", "neutral-disabled"])
        
        valid_icons = set(self.design_tools.get_all_icons())
        
        fixes = []
        
        def validate_component(comp):
            """Recursively validate component colors and icons"""
            if not isinstance(comp, dict):
                return
            
            # Check props for colors
            props = comp.get("props", {})
            if "color" in props and props["color"] not in valid_colors:
                old_color = props["color"]
                props["color"] = "blue-60"  # Default fallback
                fixes.append(f"Fixed invalid color '{old_color}' → 'blue-60'")
            
            # Check value for icons
            value = comp.get("value", {})
            if "icon" in value and value["icon"] and value["icon"] not in valid_icons:
                old_icon = value["icon"]
                value["icon"] = ""  # Remove invalid icon
                fixes.append(f"Removed invalid icon '{old_icon}'")
        
        # Validate all components in layout
        for row in layout.get("rows", []):
            for comp in row.get("pattern_info", []):
                validate_component(comp)
        
        if fixes:
            print(f"[LayoutSelectorAgent] Fixed {len(fixes)} design token issues:")
            for fix in fixes[:5]:  # Show first 5
                print(f"  - {fix}")
        
        return layout
    
    def select_best_layout(
        self,
        query: str,
        normalized_query: str,
        candidate_layouts: List[Dict],
        data_summary: str,
        analysis: Optional[Dict] = None
    ) -> Dict:
        """
        Select the best layout from candidates or create a new one.
        
        Args:
            query: Original user query
            normalized_query: Normalized query
            candidate_layouts: List of candidate layouts (top 3 from reranking)
            data_summary: Summary of available data
            analysis: Query analysis
            
        Returns:
            dict with:
                - selected_layout: The selected/adapted/created layout object
                - confidence: Selection confidence
                - reasoning: Why this layout was selected/created
                - is_adapted: Whether layout was modified
                - created_from_scratch: Whether layout was created from scratch
                - adaptations: List of changes made
        """
        if not candidate_layouts:
            # No candidates, create from scratch
            print("[LayoutSelectorAgent] No candidate layouts provided, will create from scratch")
        
        # Build selection prompt
        prompt = self._build_prompt(
            query, normalized_query, candidate_layouts, data_summary, analysis
        )
        
        # LLM evaluates and selects/creates
        fallback_id = candidate_layouts[0].get("id", "custom_layout") if candidate_layouts else "custom_layout"
        selection = self._invoke_llm(prompt, fallback_id)
        
        # Handle custom layout creation
        if selection.created_from_scratch and selection.custom_layout:
            # Use the custom layout structure and validate design tokens
            selected = self._validate_design_tokens(selection.custom_layout)
            print(f"[LayoutSelectorAgent] Created custom layout from scratch")
        else:
            # Get the selected layout from candidates
            selected = next(
                (l for l in candidate_layouts if l.get("id") == selection.selected_layout_id),
                candidate_layouts[0] if candidate_layouts else {}
            )
            # Validate if adapted
            if selection.is_adapted and selected:
                selected = self._validate_design_tokens(selected)
        
        return {
            "selected_layout": selected,
            "confidence": selection.confidence,
            "reasoning": selection.reasoning,
            "is_adapted": selection.is_adapted,
            "created_from_scratch": selection.created_from_scratch,
            "adaptations": selection.adaptations
        }
    
    def _build_prompt(
        self,
        query: str,
        normalized_query: str,
        layouts: List[Dict],
        data_summary: str,
        analysis: Optional[Dict]
    ) -> str:
        """Build LLM prompt for dynamic layout selection and adaptation"""
        
        # Format layouts with ACTUAL structure (not just summary)
        layouts_info = []
        for i, layout in enumerate(layouts, 1):
            layout_obj = layout.get("layout", {})
            rows = layout_obj.get("rows", [])
            
            # Extract row structure with component details
            rows_structure = []
            for row_idx, row in enumerate(rows):
                pattern_info = row.get("pattern_info", [])
                components = []
                for comp in pattern_info:
                    if isinstance(comp, dict):
                        components.append({
                            "type": comp.get("type"),
                            "props": list(comp.get("props", {}).keys())  # Only prop names, not values
                        })
                rows_structure.append({
                    "row": row_idx + 1,
                    "pattern_type": row.get("pattern_type"),
                    "components": components
                })
            
            layouts_info.append({
                "rank": i,
                "id": layout.get("id"),
                "pattern": layout.get("patterns_used", ["unknown"])[0] if layout.get("patterns_used") else "unknown",
                "rows": rows_structure,
                "sample_query": layout.get("query", "")
            })
        
        # Get available components list
        components_by_category = {
            category: components for category, components in COMPONENT_CATEGORIES.items()
        }
        
        # Get design system tools for colors and icons (compressed format)
        design_tools = get_design_system_tools()
        
        # Compressed color reference (instead of full 110-color JSON)
        color_summary = {
            "primary_colors": ["red", "blue", "green", "orange", "yellow", "purple", "pink", "cyan", "teal", "indigo", "gray"],
            "shades": "10, 20, 30, 40, 50, 60, 70, 80, 90, 100",
            "format": "color-shade (e.g., blue-60, red-40)",
            "semantic": ["success", "success-light", "error", "error-light", "warning", "warning-light", "info", "info-light"],
            "neutral": ["neutral-white", "neutral-primary", "neutral-secondary", "neutral-disabled"]
        }
        
        # Compressed icon reference (instead of full 90-icon list)
        icon_summary = {
            "total": len(design_tools.get_all_icons()),
            "categories": ["user", "action", "navigation", "data", "finance", "status", "communication", "file", "time", "business", "settings", "media", "location", "other"],
            "common_examples": ["user", "trending-up", "trending-down", "check-circle", "alert-circle", "star", "calendar", "dollar-sign", "mail", "phone", "settings", "search", "edit", "trash", "download", "upload", "chart", "globe", "home", "menu"]
        }
        
        prompt = f"""CRM Layout Architect: SELECT, ADAPT, or CREATE layout matching user query.

QUERY: {query}
NORMALIZED: {normalized_query}
ANALYSIS: {json.dumps(analysis, indent=2) if analysis else "N/A"}
DATA: {data_summary}

CANDIDATES (Top 3):
{json.dumps(layouts_info, indent=2)}

COMPONENTS (19 types):
{json.dumps(components_by_category, indent=2)}

COLORS (Compact Reference):
Primary: {', '.join(color_summary['primary_colors'])}
Shades: {color_summary['shades']}
Format: {color_summary['format']}
Semantic: {', '.join(color_summary['semantic'])}
Neutral: {', '.join(color_summary['neutral'])}

ICONS ({icon_summary['total']} total):
Categories: {', '.join(icon_summary['categories'])}
Examples: {', '.join(icon_summary['common_examples'])}
Note: Use descriptive icon names matching the action/object (e.g., "calendar" for dates, "dollar-sign" for money, "trending-up" for growth)

COMPONENT STRUCTURE (REQUIRED):
{{"type": "ComponentType", "props": {{"size": "md", "color": "blue-60"}}, "value": {{"text": "content", "icon": "user"}}}}

CONSTRAINTS:
- Components MUST use type/props/value structure
- Props = config (size, variant, level, color from palette)
- Value = data (text, labels, items, icon from list)
- Colors: Use format "color-shade" (e.g., blue-60, red-40) or semantic (success, error, warning, info)
  Examples: ✓ "blue-60", "success", "error-light" | ✗ "dark-blue", "custom-red"
- Icons: Use descriptive names matching action/object (check examples above)
  Examples: ✓ "user", "trending-up", "calendar" | ✗ "custom-icon", "my-icon"
- Components: ONLY from 19 types above
- Invalid colors/icons will be auto-fixed or removed during validation

DECISION LOGIC:
1. Analyze: Check candidates' rows/components vs query
2. Match %: Does any candidate fit >60%?
3. Strategy:
   - >90% match → OPTION A: Use as-is (is_adapted=false, created_from_scratch=false, confidence>0.9)
   - >60% match → OPTION B: Adapt (is_adapted=true, created_from_scratch=false, list changes)
   - <60% OR no candidates → OPTION C: Create (selected_layout_id="custom_layout", created_from_scratch=true, provide custom_layout structure)

RULES:
✓ CAN: Add/remove components from 19 types, reorganize, combine layouts, create new when <60% match
✗ CANNOT: Use unlisted components, add without data, send empty components, break type/props/value structure
DATA: Complex query + limited data = simpler layout; Rich data = detailed layout; Skip components without data
CREATE: Build rows → pattern_info arrays → components with type/props/value → map data to value fields

COMPONENTS BY CATEGORY:
Typography: Heading (H1-H6), Text (paragraphs), Label (metadata)
Interactive: Button (actions), Link (navigation)
Display: Badge (status), Chip (tags), Avatar (profiles), Image, Divider
Container: Card (panels), Stack (layouts)
Data: List, Table (multiple records), Metric (KPIs), Dashlet (charts)
Complex: ListCard (avatar+title+meta), BirthdayCard, Insights (AI), Alert (notifications)

EXAMPLES:

EX1 (Use): Query="show open opportunities" | Layout has Table+Badge+Link → {{"selected_layout_id": "crm_123", "is_adapted": false, "confidence": 0.95, "reasoning": "Perfect match", "adaptations": []}}

EX2 (Adapt): Query="opportunity details with metrics" | Layout1=Card+Text, Layout2=Metric+Insights → {{"selected_layout_id": "crm_123", "is_adapted": true, "confidence": 0.88, "reasoning": "Added metrics", "adaptations": ["Added Metric to Row 2", "Added Insights to Row 3"]}}

EX3 (Simplify): Query="full analysis with metrics/charts" | Data=only name/email/phone → {{"selected_layout_id": "crm_456", "is_adapted": true, "confidence": 0.75, "reasoning": "Limited data—removed Metric/Insights", "adaptations": ["Removed Metric (no data)", "Kept Card+Text"]}}

EX4 (Create): Query="lead scorecard with ranking" | No match <50% | Data=leads[name,score,priority,status] → {{
  "selected_layout_id": "custom_layout",
  "created_from_scratch": true,
  "confidence": 0.85,
  "reasoning": "No suitable layout—created scorecard",
  "adaptations": ["Row 1: Heading", "Row 2: Metrics (avg/high/low)", "Row 3: Table sorted by priority"],
  "custom_layout": {{
    "rows": [
      {{"pattern_type": "header", "pattern_info": [{{"type": "Heading", "props": {{"level": 1}}, "value": {{"text": "Lead Qualification Scorecard", "icon": "target"}}}}]}},
      {{"pattern_type": "metrics", "pattern_info": [{{"type": "Metric", "props": {{"size": "md", "color": "brand"}}, "value": {{"label": "Average Score", "value": "7.5", "icon": "trending-up"}}}}, {{"type": "Metric", "props": {{"size": "md", "color": "success"}}, "value": {{"label": "High Priority", "value": "12", "icon": "star"}}}}]}},
      {{"pattern_type": "data_table", "pattern_info": [{{"type": "Table", "props": {{"striped": true}}, "value": {{"headers": ["Name", "Score", "Priority", "Status", "Assignee"], "rows": [["Data here"]]}}}}]}}
    ]
  }}
}}

OUTPUT JSON:
{{
  "selected_layout_id": "from candidates OR 'custom_layout'",
  "is_adapted": bool,
  "created_from_scratch": bool,
  "confidence": 0-1,
  "reasoning": "why this decision",
  "adaptations": ["list changes"],
  "custom_layout": {{"rows": [{{"pattern_type": "...", "pattern_info": [...]}}]}}  // REQUIRED if created_from_scratch=true
}}

Analyze and decide:
"""
        return prompt
    
    def _invoke_llm(
        self, prompt: str, fallback_layout_id: str
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
            # Default to first layout or create minimal fallback
            if fallback_layout_id == "custom_layout":
                # No candidates, create minimal fallback
                return LayoutSelectionResult(
                    selected_layout_id="custom_layout",
                    confidence=0.5,
                    reasoning="LLM invocation failed, created minimal fallback layout",
                    created_from_scratch=True,
                    custom_layout={
                        "rows": [
                            {
                                "pattern_type": "header",
                                "pattern_info": [
                                    {
                                        "type": "Heading",
                                        "props": {"level": 1},
                                        "value": {"text": "Results", "icon": ""}
                                    }
                                ]
                            },
                            {
                                "pattern_type": "content",
                                "pattern_info": [
                                    {
                                        "type": "Text",
                                        "props": {},
                                        "value": {"text": "No suitable layout found. Please refine your query."}
                                    }
                                ]
                            }
                        ]
                    }
                )
            else:
                # Use first layout from candidates
                return LayoutSelectionResult(
                    selected_layout_id=fallback_layout_id,
                    confidence=0.7,
                    reasoning="LLM invocation failed, selected first layout as default"
                )

