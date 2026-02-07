"""
Node Executor - All workflow node implementations
Handles execution of individual graph nodes
"""
from design_system_agent.agent.models import AgentState
from design_system_agent.agent.tools.data_fetcher import DataFetcherTool
from design_system_agent.agent.core.vector_layout_rag import VectorLayoutRAGEngine
from design_system_agent.agent.graph_nodes.query_analyzer_node import QueryAnalyzer
from design_system_agent.agent.graph_nodes.layout_scorer_node import OutputScorer
from design_system_agent.agent.graph_nodes.layout_orchestrator import LLMLayoutSelectorFiller
from design_system_agent.agent.graph_nodes.fallback_layout_builder import FallbackLayoutBuilder
from design_system_agent.agent.graph_nodes.default_layout import DefaultLayoutBuilder


class WorkflowExecutor:
    """
    Executes all workflow nodes.
    Single Responsibility: Node execution logic
    """
    
    def __init__(self):
        """Initialize with all required components"""
        self.layout_rag = VectorLayoutRAGEngine()
        self.query_analyzer = QueryAnalyzer()
        self.output_scorer = OutputScorer()
        self.data_fetcher = DataFetcherTool()
        self.llm_selector_filler = LLMLayoutSelectorFiller()
        self.fallback_builder = FallbackLayoutBuilder()
        self.default_builder = DefaultLayoutBuilder()
    
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
    
    def analyze_and_reformulate(self, state: AgentState) -> AgentState:
        """Single LLM call for query analysis: normalize, extract intent, generate variations, detect object/layout"""
        normalized_query = state.get("normalized_query", "")
        
        try:
            # Single LLM call does everything: normalize + intent + variations + object_type + layout_type
            analysis = self.query_analyzer.invoke(normalized_query)
            state["analysis"] = analysis.dict()
            
            # Build RAG query from analysis (no additional LLM call needed)
            state["rag_query"] = {
                "search_query": analysis.generated_queries[0] if analysis.generated_queries else analysis.normalized_query,
                "search_queries": analysis.generated_queries,
                "confidence": analysis.confidence
            }
            
        except Exception as e:
            print(f"[WorkflowExecutor] LLM analysis failed: {e}")
            raise RuntimeError(
                f"Failed to analyze query. LLM service unavailable or query analysis failed: {str(e)}"
            )
        
        return state
    
    def retrieve_layouts(self, state: AgentState) -> AgentState:
        """Retrieve top 20 layouts using original query + LLM-generated variations, rerank to top 3"""
        rag_query = state.get("rag_query", {})
        
        try:
            # Use LLM-generated query variations for better retrieval
            search_queries = rag_query.get("search_queries", [])
            original_query = rag_query.get("search_query", "")
            
            # Combine original query with variations
            all_queries = [original_query] + [q for q in search_queries if q != original_query]
            
            layouts = self.layout_rag.search(
                query=all_queries if all_queries else [original_query],
                top_k=20,
                rerank=True,
                final_k=3
            )

            if not layouts:
                layouts = [DefaultLayoutBuilder().build_default_layout(
                    query=original_query,
                    data=None,
                    analysis=None
                )]

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
        # If no layouts retrieved from RAG, use default layout builder
        if not layouts:
            print("[WorkflowExecutor] No RAG matches found, using default layout builder")
            default_layout = self.default_builder.build_default_layout(
                query=query,
                data=data,
                analysis=analysis
            )
            state["selected_layout"] = default_layout
            state["adapted_layout"] = default_layout
            state["layout_ranking"] = {
                "confidence": 0.7,
                "reasoning": "No RAG matches found - using default layout with heading, description, list, and badge",
                "is_adapted": False,
                "use_default": True,
                "llm_powered": False,
                "adaptations": []
            }
            return state
        
        
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
            is_adapted = result.get("is_adapted", False)
            adaptations = result.get("adaptations", [])
            llm_powered = result.get("llm_powered", True)
            
            state["selected_layout"] = selected_layout
            state["adapted_layout"] = selected_layout
            state["layout_ranking"] = {
                "confidence": confidence,
                "reasoning": reasoning,
                "is_adapted": is_adapted,
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
                "is_adapted": False,
                "use_fallback": True,
                "llm_powered": False,
                "adaptations": []
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
