"""
Query Reformulator - Generates optimal RAG search queries
"""
from typing import Dict, Any
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from design_system_agent.agent.core.llm_factory import LLMFactory


class RAGQuery(BaseModel):
    """RAG search query model"""
    search_query: str = Field(description="Optimized query for RAG retrieval")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Additional filters for retrieval")
    confidence: float = Field(description="Confidence in query reformulation (0.0 to 1.0)")


class QueryReformulator:
    """Reformulates user queries into optimal RAG search queries"""
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
        self.parser = JsonOutputParser(pydantic_object=RAGQuery)
    
    def get_reformulation_prompt(self) -> ChatPromptTemplate:
        """Get the prompt for query reformulation"""
        return ChatPromptTemplate.from_messages([
            ("system", """You are an expert at reformulating CRM queries into optimal search queries for RAG retrieval.

Your task: Convert the analyzed query intention into an optimized search query that will find the best matching layout from a vector database.

**CRM Entities**: Lead, Opportunity, Account, Contact, Case, Task, Dashboard
**View Types**: detail, list, form, dashboard, search

**Guidelines**:
1. Focus on the layout pattern, not specific data
2. Include entity type and view type
3. Add relevant components (filter, table, metrics, etc.)
4. Be concise but descriptive

**Examples**:

Input Analysis: {{
    "intent": "show_opportunities",
    "entity": "Opportunity",
    "data_type": "dynamic",
    "action_required": "display_list"
}}
Output: {{
    "search_query": "opportunity list view with filters and table layout",
    "entity": "opportunity",
    "view_type": "list",
    "filters": {{"pattern": "list"}},
    "confidence": 0.95
}}

Input Analysis: {{
    "intent": "create_lead",
    "entity": "Lead",
    "data_type": "form",
    "action_required": "create"
}}
Output: {{
    "search_query": "lead creation form with input fields and validation",
    "entity": "lead",
    "view_type": "form",
    "filters": {{"pattern": "form"}},
    "confidence": 0.92
}}

Input Analysis: {{
    "intent": "show_lead_details",
    "entity": "Lead",
    "data_type": "dynamic",
    "action_required": "display_detail"
}}
Output: {{
    "search_query": "lead detail view with fields and related activities",
    "entity": "lead",
    "view_type": "detail",
    "filters": {{"pattern": "detail"}},
    "confidence": 0.98
}}

Input Analysis: {{
    "intent": "sales_dashboard",
    "entity": "Dashboard",
    "data_type": "aggregate",
    "action_required": "display_metrics"
}}
Output: {{
    "search_query": "sales dashboard with metrics charts and performance data",
    "entity": "dashboard",
    "view_type": "dashboard",
    "filters": {{"pattern": "dashboard"}},
    "confidence": 0.90
}}

Now reformulate this analysis into an optimal RAG search query:

{format_instructions}"""),
            ("user", "{analysis}")
        ])
    
    def invoke(self, analysis: Dict[str, Any]) -> RAGQuery:
        """
        Reformulate query based on analysis
        
        Args:
            analysis: Query analysis from QueryAnalyzer
            
        Returns:
            RAGQuery with optimized search query
        """
        print(f"[QueryReformulator] Reformulating query for intent: {analysis.get('intent', 'unknown')}")
        
        try:
            prompt = self.get_reformulation_prompt()
            chain = prompt | self.llm | self.parser
            
            result = chain.invoke({
                "analysis": str(analysis),
                "format_instructions": self.parser.get_format_instructions()
            })
            
            rag_query = RAGQuery(**result)
            print(f"[QueryReformulator] Generated search query: '{rag_query.search_query}'")
            
            return rag_query
            
        except Exception as e:
            print(f"[QueryReformulator] Error: {e}, using fallback")
            # Fallback query reformulation
            intent = analysis.get("intent", "unknown")
            components = analysis.get("components_needed", [])
            
            # Simple pattern detection from intent
            analysis_str = str(analysis).lower()
            normalized_query = analysis.get("_normalized_query", "").lower()
            search_text = f"{analysis_str} {normalized_query}"
            
            # Detect pattern from query intent
            pattern = "list"  # default
            if "detail" in intent or "view" in intent or "show" in intent:
                pattern = "detail"
            elif "list" in intent or "show_all" in intent or "my" in query_lower:
                pattern = "list"
            elif "create" in intent or "new" in intent or "form" in intent:
                pattern = "form"
            elif "dashboard" in intent or "metrics" in intent:
                pattern = "dashboard"
            
            # Build search query focused on pattern and components
            search_query = f"{pattern} layout with {' and '.join(components)}"
            
            return RAGQuery(
                search_query=search_query,
                filters={"pattern": pattern},
                confidence=0.7
            )


if __name__ == "__main__":
    # Test
    reformulator = QueryReformulator()
    
    test_analysis = {
        "intent": "show_opportunities",
        "components_needed": ["title", "description", "list"],
        "data_type": "dynamic",
        "action_required": "display_list",
        "complexity": "simple"
    }
    
    result = reformulator.invoke(test_analysis)
    print(f"\nResult: {result}")
