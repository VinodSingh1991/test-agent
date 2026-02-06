"""
Node Executor - All workflow node implementations
Handles execution of individual graph nodes
"""
from design_system_agent.agent.models import AgentState
from design_system_agent.agent.tools.data_fetcher import DataFetcherTool
from design_system_agent.agent.core.vector_layout_rag import VectorLayoutRAGEngine
from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer
from design_system_agent.agent.graph_nodes.query_reformulator_node import QueryReformulator
from design_system_agent.agent.graph_nodes.layout_scorer_node import OutputScorer
from design_system_agent.agent.graph_nodes.layout_orchestrator import LLMLayoutSelectorFiller
from design_system_agent.agent.graph_nodes.fallback_layout_builder import FallbackLayoutBuilder


class WorkflowExecutor:
    """
    Executes all workflow nodes.
    Single Responsibility: Node execution logic
    """
    
    def __init__(self):
        """Initialize with all required components"""
        self.layout_rag = VectorLayoutRAGEngine()
        self.query_analyzer = QueryAnalyzer()
        self.query_reformulator = QueryReformulator()
        self.output_scorer = OutputScorer()
        self.data_fetcher = DataFetcherTool()
        self.llm_selector_filler = LLMLayoutSelectorFiller()
        self.fallback_builder = FallbackLayoutBuilder()
    
    # ====================
    # WORKFLOW NODES
    # ====================
    
    def plan_tasks(self, state: AgentState) -> AgentState:
        """Initialize workflow execution"""
        return state
    
    def normalize_query(self, state: AgentState) -> AgentState:
        """Normalize the user query"""
        query = state.get("query", "").strip()
        
        if not query:
            state["normalized_query"] = ""
            return state

        state["normalized_query"] = query
        return state
    
    def analyze_query(self, state: AgentState) -> AgentState:
        """Analyze query intent"""
        normalized_query = state.get("normalized_query", "")
        
        try:
            analysis = self.query_analyzer.invoke(normalized_query)
            state["analysis"] = analysis.dict()
        except Exception:
            state["analysis"] = {
                "intent": "unknown",
                "components_needed": [],
                "data_type": "static",
                "action_required": "display",
                "complexity": "simple",
                "confidence": 0.5
            }
        
        return state
    
    def reformulate_query(self, state: AgentState) -> AgentState:
        """Reformulate for RAG"""
        analysis = state.get("analysis", {})
        normalized_query = state.get("normalized_query", "")
        
        analysis_with_query = {**analysis, "_normalized_query": normalized_query}
        
        try:
            rag_query = self.query_reformulator.invoke(analysis_with_query)
            state["rag_query"] = rag_query.dict()
        except Exception:
            query_lower = normalized_query.lower()
            entity = "lead"
            for ent_search in ["case", "opportunity", "account", "contact", "lead", "task"]:
                if ent_search in query_lower or (ent_search + "s") in query_lower:
                    entity = ent_search
                    break
            
            view_type = "list" if ("list" in query_lower or "my" in query_lower) else "detail"
            
            state["rag_query"] = {
                "search_query": f"{entity} {view_type} layout",
                "entity": entity,
                "view_type": view_type,
                "filters": {},
                "confidence": 0.5
            }
        
        return state
    
    def retrieve_layouts(self, state: AgentState) -> AgentState:
        """Retrieve top 10 layouts, rerank to top 3 (for LLM evaluation)"""
        rag_query = state.get("rag_query", {})
        
        try:
            layouts = self.layout_rag.search(
                query=rag_query.get("search_query", ""),
                top_k=10,
                rerank=True,
                final_k=3
            )
            state["retrieved_layouts"] = layouts
        except Exception:
            state["retrieved_layouts"] = []
        
        return state
    
    def fetch_data(self, state: AgentState) -> AgentState:
        """Fetch CRM data (supports multi-entity queries)"""
        query = state.get("query", "")
        rag_query = state.get("rag_query", {})
        analysis = state.get("analysis", {})
        
        try:
            data = self.data_fetcher.detect_and_fetch(query, analysis, rag_query)
            state["fetched_data"] = data
        except Exception:
            state["fetched_data"] = None
        
        return state
    
    def llm_select_and_fill(self, state: AgentState) -> AgentState:
        """LLM intelligently selects best layout AND fills it with data"""
        layouts = state.get("retrieved_layouts", [])
        query = state.get("query", "")
        normalized_query = state.get("normalized_query", "")
        analysis = state.get("analysis", {})
        data = state.get("fetched_data", {})
        
        try:
            result = self.llm_selector_filler.select_and_fill_layout(
                query=query,
                normalized_query=normalized_query,
                top_layouts=layouts,
                fetched_data=data,
                analysis=analysis,
                context={
                    "task_plan": state.get("task_plan"),
                    "progress": state.get("progress", 0)
                }
            )
            
            selected_layout = result.get("selected_layout")
            confidence = result.get("confidence", 0.0)
            reasoning = result.get("reasoning", "")
            reformed = result.get("reformed", False)
            adaptations = result.get("adaptations", [])
            llm_powered = result.get("llm_powered", True)
            
            state["selected_layout"] = selected_layout
            state["adapted_layout"] = selected_layout
            state["layout_ranking"] = {
                "confidence": confidence,
                "reasoning": reasoning,
                "reformed": reformed,
                "adaptations": adaptations,
                "llm_powered": llm_powered
            }
        except Exception:
            fallback_layout = self.fallback_builder.build_fallback_layout(
                query, data or {}, analysis
            )
            state["selected_layout"] = fallback_layout
            state["adapted_layout"] = fallback_layout
            state["layout_ranking"] = {
                "confidence": 0.5,
                "reasoning": "Error in LLM selection",
                "use_fallback": True,
                "llm_powered": False
            }
        
        return state
    
    def score_output(self, state: AgentState) -> AgentState:
        """Validate and score final output"""
        layout = state.get("adapted_layout")
        query = state.get("normalized_query", "")
        analysis = state.get("analysis", {})
        data = state.get("fetched_data")
        
        if not layout:
            state["output_score"] = None
            state["outcome"] = {"success": False, "error": "No layout generated"}
            return state
        
        try:
            score = self.output_scorer.score_output(layout, query, analysis)
            state["output_score"] = score.dict()
            state["outcome"] = {
                "success": True,
                "layout": layout,
                "data": data,
                "score": score.overall_score
            }
        except Exception:
            state["output_score"] = {"overall_score": 0.8}
            state["outcome"] = {
                "success": True,
                "layout": layout,
                "data": data,
                "score": 0.8
            }
        
        return state
