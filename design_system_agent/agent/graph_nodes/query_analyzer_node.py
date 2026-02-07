"""
Query Analyzer - Analyzes user intent and extracts key information
"""
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
from design_system_agent.agent.core.llm_factory import LLMFactory


class QueryAnalysis(BaseModel):
    """Structured output for query analysis"""
    normalized_query: str = Field(description="Query normalized to standard English grammar")
    intent: str = Field(description="HTTP-like intent: GET, POST, UPDATE, DELETE")
    generated_queries: List[str] = Field(description="Multiple query variations with same intent for better RAG retrieval")
    object_type: str = Field(default="unknown", description="Primary CRM object type")
    objects: List[str] = Field(default_factory=list, description="All objects mentioned (for multi-object queries)")
    layout_type: str = Field(default="list", description="Layout type: list, detail, form, dashboard")
    view_type: str = Field(default="table", description="View type: table, list, card")
    pattern_type: str = Field(default="LIST_SIMPLE", description="Query pattern: LIST_SIMPLE, AGGREGATE, FULL_COMPLEX, etc.")
    complexity_level: str = Field(default="basic", description="Complexity: basic, medium, advanced")
    aggregation_type: Optional[str] = Field(default=None, description="Aggregation: sum, count, average, min, max, grouped")
    group_by_field: Optional[str] = Field(default=None, description="Field to group by: branch, manager, status, etc.")
    has_conditions: bool = Field(default=False, description="Whether query has WHERE/filter conditions")
    has_sorting: bool = Field(default=False, description="Whether query has sorting (top 10, sorted by)")
    confidence: float = Field(description="Confidence score 0-1 for the analysis")


class QueryAnalyzer:
    """Analyzes user queries to understand intent and requirements"""
    
    @classmethod
    def get_analysis_prompt(cls) -> ChatPromptTemplate:
        system_prompt = """You are an advanced CRM query analyzer specialized in Banking/CRM patterns.

**Your Task:**
1. **Normalize** the query to standard English (fix grammar, spelling, typos)
2. **Extract Intent** - HTTP-like operation:
   - GET: show, display, view, list, get, retrieve, fetch
   - POST: create, add, new, insert
   - UPDATE: update, modify, edit, change
   - DELETE: delete, remove, archive

3. **Extract ALL CRM Objects** (for multi-object queries):
   - Primary object_type: lead, case, account, customer, loan, task, appointment, branch
   - All objects: ['customer', 'loan', 'account'] for complex queries

4. **Detect Pattern Type:**
   - LIST_SIMPLE: "show all leads", "get my cases"
   - LIST_ADVANCED: "top 10 leads", "sorted by created_date", "where status is open"
   - MULTI_OBJECT: "leads with related customer", "customer + account filtered by status"
   - AGGREGATE: "sum of loan_amount", "count of leads", "average balance"
   - FULL_COMPLEX: "customers with balance > 100000 and loan > 50000", "branch wise count of leads where status is approved"
   - ADVANCED_AGGREGATE_RELATED: "sum of loan amount for customers grouped by branch"
   - TASK_RELATED: "overdue tasks related to leads"
   - BRANCH_MANAGER_QUERIES: "branch wise leads", "my branch accounts"

5. **Detect Complexity:**
   - basic: Simple list queries
   - medium: Filtered/sorted queries, multi-object
   - advanced: Aggregations, grouping, multiple conditions

6. **Extract Aggregation & Grouping:**
   - aggregation_type: sum, count, average, min, max, grouped (if present)
   - group_by_field: branch, manager, product, status (if "grouped by" or "wise" present)

7. **Determine View Type:**
   - table: Simple/advanced lists, sorted data
   - list: Multi-object queries, related entities
   - card: Aggregations, metrics, dashboards, "grouped by" queries

8. **Detect Conditions & Sorting:**
   - has_conditions: true if WHERE/filter conditions present
   - has_sorting: true if "top 10", "sorted by", order present

9. **Generate Query Variations** (3-5 variations with same intent):
   - Use synonyms (show → display, fetch, get)
   - Reorder words
   - Add/remove context

**Examples:**

Input: "show me my lead"
Output: {{
  "normalized_query": "Show me my leads",
  "intent": "GET",
  "generated_queries": ["show me my leads", "display my leads", "get my leads", "view leads list"],
  "object_type": "lead",
  "objects": ["lead"],
  "layout_type": "list",
  "view_type": "table",
  "pattern_type": "LIST_SIMPLE",
  "complexity_level": "basic",
  "aggregation_type": null,
  "group_by_field": null,
  "has_conditions": false,
  "has_sorting": false,
  "confidence": 0.95
}}

Input: "top 10 leads sorted by created_date"
Output: {{
  "normalized_query": "Top 10 leads sorted by created_date",
  "intent": "GET",
  "generated_queries": ["top 10 leads sorted by created date", "show top 10 leads ordered by created date", "display 10 leads sorted by date"],
  "object_type": "lead",
  "objects": ["lead"],
  "layout_type": "list",
  "view_type": "table",
  "pattern_type": "LIST_ADVANCED",
  "complexity_level": "medium",
  "aggregation_type": null,
  "group_by_field": null,
  "has_conditions": false,
  "has_sorting": true,
  "confidence": 0.92
}}

Input: "sum of loan amount for customers grouped by branch"
Output: {{
  "normalized_query": "Sum of loan amount for customers grouped by branch",
  "intent": "GET",
  "generated_queries": ["total loan amount grouped by branch", "branch wise sum of loan amount for customers", "aggregate loan amount by branch"],
  "object_type": "loan",
  "objects": ["customer", "loan", "branch"],
  "layout_type": "dashboard",
  "view_type": "card",
  "pattern_type": "ADVANCED_AGGREGATE_RELATED",
  "complexity_level": "advanced",
  "aggregation_type": "sum",
  "group_by_field": "branch",
  "has_conditions": false,
  "has_sorting": false,
  "confidence": 0.90
}}

Input: "customers with total balance greater than 100000 and loan amount greater than 50000"
Output: {{
  "normalized_query": "Customers with total balance greater than 100000 and loan amount greater than 50000",
  "intent": "GET",
  "generated_queries": ["customers where balance > 100000 and loan > 50000", "high value customers with balance > 100k and loan > 50k"],
  "object_type": "customer",
  "objects": ["customer", "account", "loan"],
  "layout_type": "list",
  "view_type": "card",
  "pattern_type": "FULL_COMPLEX",
  "complexity_level": "advanced",
  "aggregation_type": null,
  "group_by_field": null,
  "has_conditions": true,
  "has_sorting": false,
  "confidence": 0.88
}}

Input: "branch wise count of leads where loan status is approved"
Output: {{
  "normalized_query": "Branch wise count of leads where loan status is approved",
  "intent": "GET",
  "generated_queries": ["count of leads by branch where loan is approved", "branch wise lead count with approved loans", "leads grouped by branch filtered by loan status approved"],
  "object_type": "lead",
  "objects": ["lead", "loan", "branch"],
  "layout_type": "dashboard",
  "view_type": "card",
  "pattern_type": "FULL_COMPLEX",
  "complexity_level": "advanced",
  "aggregation_type": "count",
  "group_by_field": "branch",
  "has_conditions": true,
  "has_sorting": false,
  "confidence": 0.85
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
        
        # Use structured output with Pydantic model
        llm = LLMFactory.open_ai_structured_llm(structured_output=QueryAnalysis)
        chain = prompt | llm
        
        print(f"[QueryAnalyzer] Analyzing query: {normalized_query}")
        
        # LLM-only approach - no keyword fallback
        analysis = chain.invoke({"normalized_query": normalized_query})
        print(f"[QueryAnalyzer] Normalized: {analysis.normalized_query}")
        print(f"[QueryAnalyzer] Pattern: {analysis.pattern_type}, Objects: {analysis.objects}, Complexity: {analysis.complexity_level}")
        print(f"[QueryAnalyzer] View Type: {analysis.view_type}, Aggregation: {analysis.aggregation_type}, Group By: {analysis.group_by_field}")
        print(f"[QueryAnalyzer] Generated {len(analysis.generated_queries)} query variations")
        return analysis
    
    @classmethod
    def _fallback_analysis_deprecated(cls, query: str) -> QueryAnalysis:
        """Keyword-based analysis when LLM is unavailable"""
        query_lower = query.lower()
        
        # Detect object type from keywords
        object_keywords = {
            "lead": ["lead", "leads", "prospect", "prospects"],
            "case": ["case", "cases", "ticket", "tickets", "issue", "issues"],
            "account": ["account", "accounts", "company", "companies", "organization"],
            "contact": ["contact", "contacts", "person", "people"],
            "opportunity": ["opportunity", "opportunities", "deal", "deals"],
            "task": ["task", "tasks", "todo", "activity", "activities"],
            "loan": ["loan", "loans"],
            "policy": ["policy", "policies", "insurance"]
        }
        
        detected_objects = []
        primary_object = "data"
        
        for obj_type, keywords in object_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                detected_objects.append(obj_type)
                if not primary_object or primary_object == "data":
                    primary_object = obj_type
        
        # Detect intent
        intent = "GET"
        if any(word in query_lower for word in ["create", "add", "new", "insert"]):
            intent = "POST"
        elif any(word in query_lower for word in ["update", "modify", "edit", "change"]):
            intent = "UPDATE"
        elif any(word in query_lower for word in ["delete", "remove", "archive"]):
            intent = "DELETE"
        
        # Detect aggregation
        aggregation = None
        if "sum" in query_lower or "total" in query_lower:
            aggregation = "sum"
        elif "count" in query_lower or "number of" in query_lower:
            aggregation = "count"
        elif "average" in query_lower or "avg" in query_lower:
            aggregation = "average"
        
        # Detect grouping
        group_by = None
        if "group by" in query_lower or "grouped by" in query_lower:
            for field in ["branch", "status", "manager", "type", "priority"]:
                if field in query_lower:
                    group_by = field
                    break
        elif "wise" in query_lower:
            for field in ["branch", "status", "manager", "type", "priority"]:
                if field in query_lower:
                    group_by = field
                    break
        
        # View type based on query pattern
        view_type = "table"
        if aggregation or group_by:
            view_type = "card"
        elif len(detected_objects) > 1:
            view_type = "list"
        
        # Pattern type
        pattern_type = "LIST_SIMPLE"
        complexity = "basic"
        if aggregation and group_by:
            pattern_type = "GROUPED_AGGREGATE"
            complexity = "advanced"
        elif aggregation:
            pattern_type = "AGGREGATE"
            complexity = "medium"
        elif len(detected_objects) > 1:
            pattern_type = "MULTI_OBJECT"
            complexity = "medium"
        
        print(f"[QueryAnalyzer] Fallback detected: object={primary_object}, objects={detected_objects}, pattern={pattern_type}")
        
        return QueryAnalysis(
            normalized_query=query,
            intent=intent,
            generated_queries=[query],
            object_type=primary_object,
            objects=detected_objects if detected_objects else [primary_object],
            layout_type="list",
            view_type=view_type,
            pattern_type=pattern_type,
            complexity_level=complexity,
            aggregation_type=aggregation,
            group_by_field=group_by,
            has_conditions="where" in query_lower or "filter" in query_lower,
            has_sorting="sort" in query_lower or "top" in query_lower,
            confidence=0.6  # Lower confidence for fallback
        )

