"""
Layout Selector Agent
Specialized agent for selecting the best layout from candidates using LLM
"""
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import json

from design_system_agent.agent.core.llm_factory import LLMFactory
from design_system_agent.core.component_types import ACTIVE_COMPONENTS, COMPONENT_CATEGORIES
from design_system_agent.agent.tools.design_system_tools import get_design_system_tools
from design_system_agent.agent.tools.langchain_design_tools import get_langchain_design_tools


class LayoutSelectionResult(BaseModel):
    """Result from layout selection/adaptation"""
    selected_layout_id: str = Field(description="ID of the selected layout or 'custom_layout' if created from scratch")
    confidence: float = Field(description="Confidence score 0-1")
    reasoning: str = Field(description="Why this layout was selected/adapted/created")
    is_adapted: bool = Field(default=False, description="Whether layout was modified")
    created_from_scratch: bool = Field(default=False, description="Whether layout was created from scratch")
    adaptations: List[str] = Field(default_factory=list, description="List of adaptations/creations made")
    custom_layout: Dict[str, Any] = Field(default_factory=dict, description="Custom layout structure if created from scratch")


class LayoutSelectorAgent:
    """
    Agent responsible for selecting the best layout from candidates.
    Uses LLM to analyze query intent and match with available layouts.
    """
    
    def __init__(self, use_tools: bool = True):
        """
        Initialize Layout Selector Agent with structured output LLM.
        Uses Pydantic LayoutSelectionResult model for guaranteed structured responses.
        
        Args:
            use_tools: If True, bind design system tools for dynamic queries (recommended)
                      Automatically falls back to False if OpenAI API key not available
        """
        self.use_tools = use_tools
        
        if use_tools:
            try:
                # Create LLM with design system tools bound (for information gathering)
                base_llm = LLMFactory.open_ai(max_tokens=3000)
                
                # Check if bind_tools is supported (not supported by mock LLM)
                if hasattr(base_llm, 'bind_tools'):
                    self.llm_with_tools = base_llm.bind_tools(get_langchain_design_tools())
                    
                    # Create structured output LLM for final selection decision
                    self.llm_structured = LLMFactory.open_ai_structured_llm(
                        structured_output=LayoutSelectionResult,
                        max_tokens=3000
                    )
                    print(f"[LayoutSelectorAgent] ✓ Initialized with bind_tools (12 design tools available)")
                else:
                    # Mock LLM doesn't support bind_tools, fall back to legacy
                    print(f"[LayoutSelectorAgent] WARNING: bind_tools not supported by LLM, falling back to legacy mode")
                    self.use_tools = False
                    self.llm_with_tools = None
                    self.llm_structured = LLMFactory.open_ai_structured_llm(
                        structured_output=LayoutSelectionResult,
                        max_tokens=3000
                    )
                    print(f"[LayoutSelectorAgent] ✓ Initialized with structured output (legacy mode)")
            except (NotImplementedError, AttributeError) as e:
                # bind_tools not implemented, fall back to legacy
                print(f"[LayoutSelectorAgent] WARNING: bind_tools failed ({type(e).__name__}), falling back to legacy mode")
                self.use_tools = False
                self.llm_with_tools = None
                self.llm_structured = LLMFactory.open_ai_structured_llm(
                    structured_output=LayoutSelectionResult,
                    max_tokens=3000
                )
                print(f"[LayoutSelectorAgent] ✓ Initialized with structured output (legacy mode)")
        else:
            # Legacy mode: single LLM with structured output, info in prompt
            self.llm_with_tools = None
            self.llm_structured = LLMFactory.open_ai_structured_llm(
                structured_output=LayoutSelectionResult,
                max_tokens=3000
            )
            print(f"[LayoutSelectorAgent] ✓ Initialized with structured output (legacy mode)")
        
        print(f"[LayoutSelectorAgent] Structured output model: {LayoutSelectionResult.__name__}")
    
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
            print("[LayoutSelectorAgent] ERROR: No candidate layouts provided!")
            raise ValueError("LayoutSelectorAgent requires at least one candidate layout")
        
        # Build selection prompt
        prompt = self._build_prompt(
            query, normalized_query, candidate_layouts, data_summary, analysis
        )
        
        # LLM evaluates and selects best match
        fallback_id = candidate_layouts[0].get("id")
        selection = self._invoke_llm(prompt, fallback_id)
        
        # Get the selected layout from candidates (MUST select one)
        selected = next(
            (l for l in candidate_layouts if l.get("id") == selection.selected_layout_id),
            candidate_layouts[0]  # Always fall back to first candidate
        )
        
        # Debug: Check what we got
        if not isinstance(selected, dict):
            print(f"[LayoutSelectorAgent] ERROR: selected is not a dict, type: {type(selected).__name__}")
            selected = {}
        elif not selected:
            print(f"[LayoutSelectorAgent] WARNING: selected layout is empty dict")
        else:
            print(f"[LayoutSelectorAgent] Selected layout keys: {list(selected.keys())}")
        
        # Final safety check: ensure selected is a valid dict with rows
        if not isinstance(selected, dict):
            print(f"[LayoutSelectorAgent] ERROR: Final selected is {type(selected).__name__}, using empty structure")
            selected = {"rows": []}
        elif "rows" not in selected and "layout" not in selected:
            print(f"[LayoutSelectorAgent] WARNING: Selected layout missing 'rows' key, wrapping it")
            selected = {"rows": [selected] if selected else []}
        
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
        
        # Choose prompt based on whether tools are available
        if self.use_tools:
            # SHORTER PROMPT: Tools available for querying colors/icons/patterns dynamically
            prompt = f"""CRM Layout Architect: SELECT, ADAPT, or CREATE layout matching user query.

QUERY: {query}
NORMALIZED: {normalized_query}
ANALYSIS: {json.dumps(analysis, indent=2) if analysis else "N/A"}
DATA: {data_summary}

CANDIDATES (Top 3):
{json.dumps(layouts_info, indent=2)}

COMPONENTS (19 types):
{json.dumps(components_by_category, indent=2)}

DESIGN SYSTEM TOOLS:
You have access to tools for querying design resources (use them as needed):
- search_icons(query) - Find icons by keyword (e.g search_icons("trending") → ["trending-up", "trending-down"])
- get_icons_by_category(category) - Get icons in category (finance, user, action, status, etc.)
- get_color_shades(color) - Get shades for a color name (e.g get_color_shades("blue") → ["blue-10", ..., "blue-100"])
- get_semantic_colors() - Get status colors (returns: success, error, warning, info with variants)
- get_all_colors() - Get all color families and shades (use sparingly, returns 110+ colors)
- get_component_schema(type) - Get component prop/value structure details

Use these tools when you need specific colors or icons. For common needs, you can use standard colors (blue-60, red-40, success, error) and common icons (user, trending-up, calendar, dollar-sign) directly.

COMPONENT STRUCTURE:
{{"type": "ComponentType", "props": {{"size": "md", "color": "blue-60"}}, "value": {{"text": "content", "icon": "user"}}}}

DECISION LOGIC:"""
        else:
            # LEGACY: Full info in prompt (no tools)
            design_tools = get_design_system_tools()
            
            color_summary = {
                "primary_colors": ["red", "blue", "green", "orange", "yellow", "purple", "pink", "cyan", "teal", "indigo", "gray"],
                "shades": "10, 20, 30, 40, 50, 60, 70, 80, 90, 100",
                "format": "color-shade (e.g., blue-60, red-40)",
                "semantic": ["success", "success-light", "error", "error-light", "warning", "warning-light", "info", "info-light"],
                "neutral": ["neutral-white", "neutral-primary", "neutral-secondary", "neutral-disabled"]
            }
            
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
Note: Use descriptive icon names matching the action/object

COMPONENT STRUCTURE (REQUIRED):
{{"type": "ComponentType", "props": {{"size": "md", "color": "blue-60"}}, "value": {{"text": "content", "icon": "user"}}}}

CONSTRAINTS:
- Components MUST use type/props/value structure
- Props = config (size, variant, level, color from palette)
- Value = data (text, labels, items, icon from list)
- Colors: Use format "color-shade" (e.g., blue-60, red-40) or semantic (success, error, warning, info)
- Icons: Use descriptive names matching action/object
- Components: ONLY from 19 types above

DECISION LOGIC:"""
        
        # Common decision rules for both modes
        prompt += """
1. **Analyze Query Pattern** (from ANALYSIS):
   - pattern_type: LIST_SIMPLE, LIST_ADVANCED, AGGREGATE, FULL_COMPLEX, ADVANCED_AGGREGATE_RELATED, etc.
   - complexity_level: basic, medium, advanced
   - view_type: table (lists), list (multi-object), card (aggregations/metrics)
   - aggregation_type: sum, count, average, min, max, grouped
   - group_by_field: branch, manager, status, etc.

2. **Match Required Components:**
   - LIST_SIMPLE/LIST_ADVANCED → Table + Heading + Badge
   - MULTI_OBJECT → ListCard + Avatar + Badge
   - AGGREGATE/ADVANCED_AGGREGATE_RELATED → Card + Metric + Heading (+ optional Dashlet for visualization)
   - FULL_COMPLEX (multi-condition) → Card + Metric + Table + Badge

3. **Match % Evaluation:**
   - >90% match → Use as-is
   - 70-90% match → Adapt by ADDING components
   - <70% match → Select closest match and ADD missing components

4. **Strategy (ALWAYS SELECT A CANDIDATE):**
   - CRITICAL: You MUST select one of the provided candidate layouts
   - created_from_scratch = false (ALWAYS)
   - custom_layout = {} (ALWAYS EMPTY)
   
   - >90% match → OPTION A: Use as-is (is_adapted=false, confidence>0.9, selected_layout_id from candidates)
   - 70-90% match → OPTION B: Adapt by ADDING (is_adapted=true, list added components in adaptations)
   - <70% match → OPTION C: Select best + ADD heavily (is_adapted=true, extensive additions in adaptations)

RULES:
✓ CAN: ADD components to selected layout, reorganize rows, extend with additional patterns
✗ CANNOT: Remove components from selected layout, create from scratch, use unlisted components, send empty adaptations list
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

EX1 (Simple List): Query="show all leads" | pattern_type=LIST_SIMPLE → {{"selected_layout_id": "crm_123", "is_adapted": false, "confidence": 0.95, "reasoning": "Perfect match - Table layout", "adaptations": []}}

EX2 (Adapt for Advanced List): Query="top 10 leads sorted by created_date" | pattern_type=LIST_ADVANCED | Layout=Table+Badge → {{"selected_layout_id": "crm_234", "is_adapted": true, "confidence": 0.90, "reasoning": "Added sorting indicator", "adaptations": ["Added Chip for sorting indicator"]}}

EX3 (Adapt for Aggregation): Query="sum of loan amount for customers grouped by branch" | pattern_type=ADVANCED_AGGREGATE_RELATED | aggregation_type=sum | group_by_field=branch | Best=crm_789 (has Table) → {{
  "selected_layout_id": "crm_789",
  "created_from_scratch": false,
  "is_adapted": true,
  "confidence": 0.85,
  "reasoning": "Selected table layout, adding Metric cards for branch aggregation and Dashlet for visualization",
  "adaptations": ["Added Row 1: Heading with aggregation title", "Added Row 2: Metric cards for branch totals", "Added Row 3: Dashlet bar chart", "Kept existing table for detail view"]
}}

EX4 (Adapt for Complex Multi-Object): Query="customers with balance > 100000 and loan > 50000" | pattern_type=FULL_COMPLEX | objects=[customer,account,loan] | has_conditions=true | Best=crm_456 (customer table) → {{
  "selected_layout_id": "crm_456",
  "created_from_scratch": false,
  "is_adapted": true,
  "confidence": 0.82,
  "reasoning": "Selected customer table layout, adding summary metrics and condition badges",
  "adaptations": ["Added Row 1: Heading + Badge showing filter conditions", "Added Row 2: Summary metrics (count, avg balance, total loan)", "Kept Row 3: Existing customer table with balance/loan columns"]
}}

EX5 (Adapt for Branch-wise Count): Query="branch wise count of leads where loan status is approved" | pattern_type=FULL_COMPLEX | aggregation_type=count | group_by_field=branch | Best=crm_234 (lead list) → {{
  "selected_layout_id": "crm_234",
  "created_from_scratch": false,
  "is_adapted": true,
  "confidence": 0.80,
  "reasoning": "Selected lead list layout, adding grouped metrics and chart for branch-wise count",
  "adaptations": ["Added Row 1: Heading + Chip filter (Loan: Approved)", "Added Row 2: Metric cards per branch (North: 45, South: 38, East: 52)", "Added Row 3: Pie chart for distribution", "Kept original lead table for drill-down"]
}}

OUTPUT JSON (MUST SELECT FROM CANDIDATES):
{{
  "selected_layout_id": "MUST be ID from provided candidates (e.g., crm_123, crm_234)",
  "is_adapted": bool,
  "created_from_scratch": false,  // ALWAYS false
  "confidence": 0-1,
  "reasoning": "why you selected this candidate + what you're adding",
  "adaptations": ["list of components/rows ADDED to selected layout"],
  "custom_layout": {{}}  // ALWAYS empty
}}

Analyze and decide:
"""
        return prompt
    
    def _invoke_llm(
        self, prompt: str, fallback_layout_id: str
    ) -> LayoutSelectionResult:
        """
        Invoke LLM to select layout using structured output with Pydantic model.
        
        Args:
            prompt: The prompt string for layout selection
            fallback_layout_id: Fallback layout ID if LLM fails
            
        Returns:
            LayoutSelectionResult: Structured Pydantic model with selection result
        """
        
        try:
            print(f"[LayoutSelectorAgent] Invoking LLM with prompt length: {len(prompt)} chars")
            print(f"[LayoutSelectorAgent] Using structured output with model: {LayoutSelectionResult.__name__}")
            
            # Invoke LLM with structured output (returns LayoutSelectionResult directly)
            result = self.llm_structured.invoke(prompt)
            
            # Verify result is correct type (real API returns LayoutSelectionResult, mock may differ)
            if isinstance(result, LayoutSelectionResult):
                print(f"[LayoutSelectorAgent] ✓ Successfully received structured output")
                print(f"[LayoutSelectorAgent] ✓ Selected: {result.selected_layout_id}, Confidence: {result.confidence}")
                print(f"[LayoutSelectorAgent] ✓ Created from scratch: {result.created_from_scratch}, Adapted: {result.is_adapted}")
                return result
            else:
                # Mock LLM or unexpected response - use fallback
                print(f"[LayoutSelectorAgent] WARNING: Expected LayoutSelectionResult, got {type(result).__name__}")
                print(f"[LayoutSelectorAgent] Using fallback layout due to unexpected response type")
                raise TypeError(f"LLM returned {type(result).__name__} instead of LayoutSelectionResult")
            
            
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            print(f"[LayoutSelectorAgent] LLM invocation failed ({error_type}): {error_msg}")
            
            # Check for common issues
            if "rate_limit" in error_msg.lower():
                print("[LayoutSelectorAgent] ⚠️  Rate limit exceeded - wait and retry")
            elif "quota" in error_msg.lower():
                print("[LayoutSelectorAgent] ⚠️  API quota exceeded - check billing")
            elif "token" in error_msg.lower() or "length" in error_msg.lower():
                print(f"[LayoutSelectorAgent] ⚠️  Token limit issue - prompt: {len(prompt)} chars")
            elif "api_key" in error_msg.lower() or "auth" in error_msg.lower():
                print("[LayoutSelectorAgent] ⚠️  API key authentication failed")
            
            # Default to first candidate layout
            return LayoutSelectionResult(
                selected_layout_id=fallback_layout_id,
                confidence=0.5,
                reasoning="LLM invocation failed, selected first candidate layout as fallback",
                created_from_scratch=False,
                is_adapted=False
            )

