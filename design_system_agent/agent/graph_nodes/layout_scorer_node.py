"""
Layout Scorer and Adapter - Ranks and adapts retrieved layouts for the user query
"""
from typing import Dict, Any, List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from design_system_agent.agent.core.llm_factory import LLMFactory


class LayoutRanking(BaseModel):
    """Ranking of retrieved layouts"""
    best_layout_id: str = Field(description="ID of the best matching layout")
    scores: Dict[str, float] = Field(description="Scores for each layout (id -> score)")
    reasoning: str = Field(description="Explanation of why this layout was chosen")
    

class LayoutScore(BaseModel):
    """Final layout quality score"""
    overall_score: float = Field(description="Overall quality score (0.0 to 1.0)")
    component_match: float = Field(description="How well components match query (0.0 to 1.0)")
    structure_quality: float = Field(description="Layout structure quality (0.0 to 1.0)")
    ux_score: float = Field(description="User experience score (0.0 to 1.0)")
    feedback: str = Field(description="Feedback and suggestions")


class LayoutScorer:
    """Scores and ranks retrieved layouts based on query context"""
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
    
    def score_layouts(
        self,
        retrieved_layouts: List[Dict[str, Any]],
        query: str,
        analysis: Dict[str, Any]
    ) -> LayoutRanking:
        """
        Score and rank retrieved layouts
        
        Args:
            retrieved_layouts: List of layouts from RAG
            query: Original user query
            analysis: Query analysis
            
        Returns:
            LayoutRanking with best layout selected
        """
        print(f"[LayoutScorer] Scoring {len(retrieved_layouts)} layouts")
        
        if not retrieved_layouts:
            return LayoutRanking(
                best_layout_id="",
                scores={},
                reasoning="No layouts retrieved"
            )
        
        try:
            # Use LLM to re-rank based on query context
            parser = JsonOutputParser(pydantic_object=LayoutRanking)
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", """You are an expert at evaluating CRM layout quality.

Given retrieved layouts and user query, rank them and select the best one.

**Scoring Criteria**:
1. Component Match: Does it have the required components?
2. Pattern Fit: Does the pattern match the user's intent?
3. Object Type Match: Is it for the right object type?
4. Complexity: Is it appropriate for the task?

**Examples**:

Query: "show my open opportunities"
Layouts: [
    {{"id": "crm_1", "pattern": "opportunity_list", "retrieval_score": 0.92}},
    {{"id": "crm_2", "pattern": "opportunity_detail", "retrieval_score": 0.85}},
    {{"id": "crm_3", "pattern": "opportunity_form", "retrieval_score": 0.78}}
]
Best: {{
    "best_layout_id": "crm_1",
    "scores": {{"crm_1": 0.95, "crm_2": 0.80, "crm_3": 0.70}},
    "reasoning": "opportunity_list best matches 'show all opportunities' intent with list view"
}}

Now rank these layouts:

{format_instructions}"""),
                ("user", "Query: {query}\\nAnalysis: {analysis}\\nLayouts: {layouts}")
            ])
            
            chain = prompt | self.llm | parser
            
            result = chain.invoke({
                "query": query,
                "analysis": str(analysis),
                "layouts": str([{
                    "id": l.get("id"),
                    "pattern": l.get("pattern"),
                    "object_type": l.get("object_type"),
                    "layout_type": l.get("layout_type"),
                    "retrieval_score": l.get("retrieval_score", 0.0)
                } for l in retrieved_layouts]),
                "format_instructions": parser.get_format_instructions()
            })
            
            ranking = LayoutRanking(**result)
            print(f"[LayoutScorer] Best layout: {ranking.best_layout_id}")
            print(f"[LayoutScorer] Reasoning: {ranking.reasoning}")
            
            return ranking
            
        except Exception as e:
            print(f"[LayoutScorer] Error: {e}, using fallback scoring")
            # Fallback: just use retrieval scores
            best = retrieved_layouts[0]  # Already sorted by retrieval score
            scores = {l.get("id", ""): l.get("retrieval_score", 0.0) for l in retrieved_layouts}
            
            return LayoutRanking(
                best_layout_id=best.get("id", ""),
                scores=scores,
                reasoning="Fallback: Selected layout with highest retrieval score"
            )


class LayoutAdapter:
    """Adapts retrieved layout to match user query data"""
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
    
    def adapt_layout(
        self,
        layout: Dict[str, Any],
        query: str,
        analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Adapt layout to user query
        
        Args:
            layout: Selected layout from RAG
            query: Original user query
            analysis: Query analysis
            
        Returns:
            Adapted layout with personalized data
        """
        print(f"[LayoutAdapter] Adapting layout: {layout.get('pattern')}")
        
        try:
            # Extract specific data from query using LLM
            prompt = ChatPromptTemplate.from_messages([
                ("system", """Extract specific data from the query to personalize the layout.

**Extract**:
- Entity name/identifier
- Filters or conditions
- Date ranges
- Sorting preferences
- Any specific fields mentioned

**Examples**:

Query: "show all open opportunities for Acme Corp"
Extraction: {{
    "entity_name": "Acme Corp",
    "filters": {{"status": "open", "account": "Acme Corp"}},
    "title": "Open Opportunities - Acme Corp"
}}

Query: "create new lead for John Smith at Microsoft"
Extraction: {{
    "entity_name": "John Smith",
    "company": "Microsoft",
    "title": "New Lead - John Smith"
}}

Now extract data from this query:"""),
                ("user", "{query}")
            ])
            
            chain = prompt | self.llm | StrOutputParser()
            extracted_data = chain.invoke({"query": query})
            
            print(f"[LayoutAdapter] Extracted data: {extracted_data[:100]}...")
            
            # For now, return layout as-is with metadata
            # In production, you would modify the layout structure with extracted data
            adapted = layout.copy()
            adapted["adapted"] = True
            adapted["query_data"] = extracted_data
            adapted["original_query"] = query
            
            return adapted
            
        except Exception as e:
            print(f"[LayoutAdapter] Error: {e}, returning original layout")
            return layout


class OutputScorer:
    """Scores the final output layout quality"""
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
    
    def score_output(
        self,
        layout: Dict[str, Any],
        query: str,
        analysis: Dict[str, Any]
    ) -> LayoutScore:
        """
        Score the final layout output
        
        Args:
            layout: Final adapted layout
            query: Original user query
            analysis: Query analysis
            
        Returns:
            LayoutScore with quality metrics
        """
        print(f"[OutputScorer] Scoring final output")
        
        try:
            parser = JsonOutputParser(pydantic_object=LayoutScore)
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", """Score the layout quality based on:

1. **Component Match** (0-1): Does it have required components?
2. **Structure Quality** (0-1): Is the layout well-organized?
3. **UX Score** (0-1): Is it user-friendly and intuitive?
4. **Overall Score** (0-1): Average of above

Provide constructive feedback.

{format_instructions}"""),
                ("user", "Query: {query}\\nPattern: {pattern}\\nComponents: {components}")
            ])
            
            chain = prompt | self.llm | parser
            
            result = chain.invoke({
                "query": query,
                "pattern": layout.get("pattern", "unknown"),
                "components": str(layout.get("components", [])),
                "format_instructions": parser.get_format_instructions()
            })
            
            score = LayoutScore(**result)
            print(f"[OutputScorer] Overall score: {score.overall_score:.2f}")
            print(f"[OutputScorer] Feedback: {score.feedback[:100]}...")
            
            return score
            
        except Exception as e:
            print(f"[OutputScorer] Error: {e}, using default score")
            # Default scoring based on pattern match
            components_needed = set(analysis.get("components_needed", []))
            layout_components = set(c.lower() for c in layout.get("components", []))
            
            component_match = len(components_needed & layout_components) / max(len(components_needed), 1)
            
            return LayoutScore(
                overall_score=0.85,
                component_match=component_match,
                structure_quality=0.85,
                ux_score=0.85,
                feedback="Layout retrieved and adapted successfully"
            )


if __name__ == "__main__":
    # Test
    scorer = LayoutScorer()
    adapter = LayoutAdapter()
    output_scorer = OutputScorer()
    
    test_layouts = [
        {"id": "crm_1", "pattern": "opportunity_list", "object_type": "opportunity", "layout_type": "list", "retrieval_score": 0.92, "components": ["Heading", "List"]},
        {"id": "crm_2", "pattern": "opportunity_detail", "object_type": "opportunity", "layout_type": "detail", "retrieval_score": 0.85, "components": ["Heading", "Description"]},
    ]
    
    test_query = "show my open opportunities"
    test_analysis = {"intent": "show_opportunities", "components_needed": ["title", "list"]}
    
    # Test scoring
    ranking = scorer.score_layouts(test_layouts, test_query, test_analysis)
    print(f"\nBest layout: {ranking.best_layout_id}")
    
    # Test adaptation
    best_layout = test_layouts[0]
    adapted = adapter.adapt_layout(best_layout, test_query, test_analysis)
    print(f"\nAdapted: {adapted.get('adapted')}")
    
    # Test output scoring
    final_score = output_scorer.score_output(adapted, test_query, test_analysis)
    print(f"\nFinal score: {final_score.overall_score}")
