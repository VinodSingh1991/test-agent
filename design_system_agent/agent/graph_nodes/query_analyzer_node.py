"""
Query Analyzer - Analyzes user intent and extracts key information
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
from design_system_agent.agent.core.llm_factory import LLMFactory


class QueryAnalysis(BaseModel):
    """Structured output for query analysis"""
    normalized_query: str = Field(description="Query normalized to standard English grammar")
    intent: str = Field(description="HTTP-like intent: GET, POST, UPDATE, DELETE")
    generated_queries: List[str] = Field(description="Multiple query variations with same intent for better RAG retrieval")
    object_type: str = Field(default="unknown", description="CRM object type extracted from query")
    layout_type: str = Field(default="list", description="Layout type inferred from intent and query")
    confidence: float = Field(description="Confidence score 0-1 for the analysis")


class QueryAnalyzer:
    """Analyzes user queries to understand intent and requirements"""
    
    @classmethod
    def get_analysis_prompt(cls) -> ChatPromptTemplate:
        system_prompt = """You are an intelligent query normalizer and intent classifier.

**Your Task:**
1. **Normalize** the query to standard English (fix grammar, spelling, typos, casual language)
2. **Extract Intent** - Classify as HTTP-like operation:
   - GET: show, display, view, list, get, retrieve, fetch
   - POST: create, add, new, insert, submit, send
   - UPDATE: update, modify, edit, change
   - DELETE: delete, remove, archive
3. **Extract CRM Information:**
   - object_type: lead, opportunity, account, contact, case, task, dashboard, or unknown
   - layout_type: list (GET multiple), detail (GET single), form (POST/UPDATE), dashboard (metrics)
4. **Generate Query Variations** - Create 3-5 variations with same intent:
   - Use synonyms (show → display, view, get)
   - Reorder words ("show my leads" → "my leads show")
   - Add context ("leads" → "leads in list view")
   - Use different phrasing

**Examples:**

Input: "show me my lead"
Output: {{
  "normalized_query": "Show me my leads",
  "intent": "GET",
  "generated_queries": [
    "show me my leads",
    "display my leads",
    "get all my leads",
    "view my leads list",
    "retrieve my leads"
  ],
  "object_type": "lead",
  "layout_type": "list",
  "confidence": 0.95
}}

Input: "show mww my lad"
Output: {{
  "normalized_query": "Show me my leads",
  "intent": "GET",
  "generated_queries": [
    "show me my leads",
    "display my leads",
    "get my leads",
    "view leads list",
    "show all leads"
  ],
  "object_type": "lead",
  "layout_type": "list",
  "confidence": 0.90
}}

Input: "create new opp"
Output: {{
  "normalized_query": "Create new opportunity",
  "intent": "POST",
  "generated_queries": [
    "create new opportunity",
    "add new opportunity",
    "new opportunity form",
    "insert opportunity",
    "create opportunity"
  ],
  "object_type": "opportunity",
  "layout_type": "form",
  "confidence": 0.92
}}

Input: "update account details"
Output: {{
  "normalized_query": "Update account details",
  "intent": "UPDATE",
  "generated_queries": [
    "update account details",
    "edit account information",
    "modify account",
    "change account details",
    "update account"
  ],
  "object_type": "account",
  "layout_type": "form",
  "confidence": 0.93
}}

Input: "view opportunities dashboard"
Output: {{
  "normalized_query": "View opportunities dashboard",
  "intent": "GET",
  "generated_queries": [
    "view opportunities dashboard",
    "show opportunities dashboard",
    "display opportunities metrics",
    "get opportunities overview",
    "opportunities dashboard"
  ],
  "object_type": "opportunity",
  "layout_type": "dashboard",
  "confidence": 0.88
}}

Now analyze this query:
{normalized_query}
"""
        
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt)
        ])
    
    @classmethod
    def invoke(cls, normalized_query: str) -> QueryAnalysis:
        """Analyze the normalized query and return structured analysis"""
        prompt = cls.get_analysis_prompt()
        parser = JsonOutputParser(pydantic_object=QueryAnalysis)
        
        chain = prompt | LLMFactory.open_ai() | parser
        
        print(f"[QueryAnalyzer] Analyzing query: {normalized_query}")
        
        try:
            result = chain.invoke({"normalized_query": normalized_query})
            analysis = QueryAnalysis(**result)
            print(f"[QueryAnalyzer] Normalized: {analysis.normalized_query}")
            print(f"[QueryAnalyzer] Intent: {analysis.intent}, Object: {analysis.object_type}, Layout: {analysis.layout_type}")
            print(f"[QueryAnalyzer] Generated {len(analysis.generated_queries)} query variations")
            return analysis
        except Exception as e:
            print(f"[QueryAnalyzer] Error: {e}, using fallback analysis")
            # Fallback to simple analysis
            return QueryAnalysis(
                normalized_query=normalized_query,
                intent="GET",
                generated_queries=[normalized_query],
                object_type="unknown",
                layout_type="list",
                confidence=0.5
            )
