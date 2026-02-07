"""
Query Reformulator - Generates optimal RAG search queries
"""
from typing import Dict, Any, List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from design_system_agent.agent.core.llm_factory import LLMFactory


class RAGQuery(BaseModel):
    """RAG search query model with multiple variations"""
    search_query: str = Field(description="Primary optimized query for RAG retrieval")
    search_queries: List[str] = Field(description="Multiple query variations with same intent for better recall")
    object_type: str = Field(default="unknown", description="CRM object type (lead, account, contact, case, opportunity, etc.)")
    layout_type: str = Field(default="list", description="Layout type (list, detail, form, dashboard, etc.)")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Additional filters for retrieval")
    confidence: float = Field(description="Confidence in query reformulation (0.0 to 1.0)")


class QueryReformulator:
    """Reformulates user queries into optimal RAG search queries"""
    
    def __init__(self):
        self.llm = LLMFactory.open_ai()
        self.parser = JsonOutputParser(pydantic_object=RAGQuery)
    
    def get_reformulation_prompt(self) -> ChatPromptTemplate:
        """Get the prompt for extracting CRM object and layout type"""
        return ChatPromptTemplate.from_messages([
            ("system", """You are an expert at extracting CRM information from queries.

**Your Task:**
Use the query variations to extract:
1. object_type: lead, opportunity, account, contact, case, task, or dashboard
2. layout_type: list, detail, form, or dashboard (infer from intent: GET→list/detail, POST→form, dashboard words→dashboard)
3. Add 1-2 more query variations for better RAG retrieval

**Layout Type Rules:**
- GET intent + plural/multiple → list
- GET intent + single/specific → detail  
- POST intent → form
- Contains "dashboard"/"metrics" → dashboard

**Examples:**

Input: {{
  "normalized_query": "Show me my leads",
  "intent": "GET",
  "generated_queries": ["show me my leads", "display my leads", "get all my leads"]
}}
Output: {{
  "search_query": "show me my leads",
  "search_queries": ["show me my leads", "display my leads", "get all my leads", "leads list view", "view my leads"],
  "object_type": "lead",
  "layout_type": "list",
  "filters": {{"pattern": "list"}},
  "confidence": 0.95
}}

Input: {{
  "normalized_query": "Create new opportunity",
  "intent": "POST",
  "generated_queries": ["create new opportunity", "add new opportunity", "new opportunity form"]
}}
Output: {{
  "search_query": "create new opportunity",
  "search_queries": ["create new opportunity", "add new opportunity", "new opportunity form", "opportunity creation form"],
  "object_type": "opportunity",
  "layout_type": "form",
  "filters": {{"pattern": "form"}},
  "confidence": 0.92
}}

Input: {{
  "normalized_query": "View account details",
  "intent": "GET",
  "generated_queries": ["view account details", "show account information"]
}}
Output: {{
  "search_query": "view account details",
  "search_queries": ["view account details", "show account information", "account detail view", "single account"],
  "object_type": "account",
  "layout_type": "detail",
  "filters": {{"pattern": "detail"}},
  "confidence": 0.93
}}

Now extract CRM information:

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
            print(f"[QueryReformulator] Generated search queries: {rag_query.search_queries}")
            print(f"[QueryReformulator] Object: {rag_query.object_type}, Layout: {rag_query.layout_type}")
            
            return rag_query
            
        except Exception as e:
            print(f"[QueryReformulator] Error: {e}, using fallback")
            # Fallback query reformulation
            intent = analysis.get("intent", "unknown")
            components = analysis.get("components_needed", [])
            
            # Simple pattern detection from intent and query
            analysis_str = str(analysis).lower()
            normalized_query = analysis.get("_normalized_query", "").lower()
            search_text = f"{analysis_str} {normalized_query}"
            
            # Detect object type from query
            object_type = "unknown"
            for obj_search in ["lead", "opportunity", "account", "contact", "case", "task", "dashboard"]:
                if obj_search in search_text or (obj_search + "s") in search_text:
                    object_type = obj_search
                    break
            
            # Detect layout type from query intent
            layout_type = "list"  # default
            if "detail" in intent or "view" in intent:
                layout_type = "detail"
            elif "list" in intent or "show_all" in intent or "my" in search_text:
                layout_type = "list"
            elif "create" in intent or "new" in intent or "form" in intent:
                layout_type = "form"
            elif "dashboard" in intent or "metrics" in intent:
                layout_type = "dashboard"
            
            # Build search query and variations
            search_query = f"{object_type} {layout_type} layout with {' and '.join(components) if components else 'standard components'}"
            search_queries = [
                search_query,
                f"show {object_type} {layout_type} view",
                f"display {object_type} in {layout_type}"
            ]
            
            return RAGQuery(
                search_query=search_query,
                search_queries=search_queries,
                object_type=object_type,
                layout_type=layout_type,
                filters={"pattern": layout_type},
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
