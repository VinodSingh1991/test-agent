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
    intent: str = Field(description="Primary intent of the query (e.g., 'create_summary', 'show_notifications', 'display_data')")
    components_needed: List[str] = Field(description="List of UI components needed (e.g., ['title', 'description', 'button'])")
    data_type: Optional[str] = Field(default=None, description="Type of data to display (e.g., 'notifications', 'tasks', 'summary')")
    action_required: Optional[str] = Field(default=None, description="Action button needed (e.g., 'update', 'approve', 'submit')")
    complexity: str = Field(description="Complexity level: 'simple', 'moderate', or 'complex'")
    confidence: float = Field(description="Confidence score 0-1 for the analysis")


class QueryAnalyzer:
    """Analyzes user queries to understand intent and requirements"""
    
    @classmethod
    def get_analysis_prompt(cls) -> ChatPromptTemplate:
        system_prompt = """
        You are an intelligent query analyzer for a design system agent.
        
        Your task is to analyze the user query and extract:
        1. **Intent**: What does the user want to do?
        2. **Components Needed**: What UI components are required?
        3. **Data Type**: What kind of data will be displayed?
        4. **Action Required**: Does the user need an action button?
        5. **Complexity**: How complex is this query?
        
        Examples:
        
        Query: "show my notifications"
        Analysis:
        - intent: "show_notifications"
        - components_needed: ["title", "description"]
        - data_type: "notifications"
        - action_required: null
        - complexity: "simple"
        - confidence: 0.95
        
        Query: "display pending approvals with review button"
        Analysis:
        - intent: "show_approvals"
        - components_needed: ["title", "list", "button"]
        - data_type: "approvals"
        - action_required: "review"
        - complexity: "moderate"
        - confidence: 0.9
        
        Query: "create a dashboard showing tasks, events and allow me to add new ones"
        Analysis:
        - intent: "create_dashboard"
        - components_needed: ["title", "list", "description", "button"]
        - data_type: "mixed"
        - action_required: "add"
        - complexity: "complex"
        - confidence: 0.85
        
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
            print(f"[QueryAnalyzer] Intent detected: {analysis.intent}")
            print(f"[QueryAnalyzer] Components needed: {analysis.components_needed}")
            print(f"[QueryAnalyzer] Complexity: {analysis.complexity}")
            return analysis
        except Exception as e:
            print(f"[QueryAnalyzer] Error: {e}, using fallback analysis")
            # Fallback to simple analysis
            return QueryAnalysis(
                intent="show_data",
                components_needed=["title", "description"],
                data_type="generic",
                action_required=None,
                complexity="simple",
                confidence=0.5
            )
