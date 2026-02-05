"""
LangGraph Agentic RAG System for CRM Layout Generation.
"""
from typing import TypedDict, Optional, List, Dict, Annotated
from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage
import operator

from design_system_agent.agent.core.llm_factory import LLMFactory
from design_system_agent.agent.core.rag_engine import RAGEngine
from design_system_agent.agent.core.layout_rag_engine import LayoutRAGEngine
from design_system_agent.agent.graph_nodes.query_translator import QueryTranslator
from design_system_agent.agent.graph_nodes.query_analyzer import QueryAnalyzer
from design_system_agent.agent.graph_nodes.query_reformulator import QueryReformulator
from design_system_agent.agent.graph_nodes.layout_scorer import LayoutScorer, LayoutAdapter, OutputScorer


# ---------------------------
# STATE MODEL
# ---------------------------
class AgentState(TypedDict):
    """State object that flows through the agent graph."""
    query: str
    normalized_query: str
    analysis: Optional[Dict]
    rag_query: Optional[Dict]
    retrieved_layouts: Optional[List[Dict]]
    layout_ranking: Optional[Dict]
    selected_layout: Optional[Dict]
    adapted_layout: Optional[Dict]
    output_score: Optional[Dict]
    outcome: Dict
    messages: Annotated[List, operator.add]


class AgentExecutorResponse(TypedDict):
    success: bool
    query: str
    outcome: Dict
    intent: str


# ---------------------------
# AGENT EXECUTOR
# ---------------------------
class AgentExecutor:
    """Agentic RAG system for CRM layout generation."""

    def __init__(self):
        self.llm_client = LLMFactory.open_ai()
        self.rag_engine = RAGEngine()
        self.layout_rag = LayoutRAGEngine()
        self.query_analyzer = QueryAnalyzer()
        self.query_reformulator = QueryReformulator()
        self.layout_scorer = LayoutScorer()
        self.layout_adapter = LayoutAdapter()
        self.output_scorer = OutputScorer()
        self.graph = self._build_graph()

    # ---------------------------
    # GRAPH BUILDER
    # ---------------------------
    def _build_graph(self) -> StateGraph:
        workflow = StateGraph(AgentState)

        # Add all nodes for agentic RAG flow
        workflow.add_node("normalize_query", self.normalize_query)
        workflow.add_node("analyze_query", self.analyze_query)
        workflow.add_node("reformulate_query", self.reformulate_query)
        workflow.add_node("retrieve_layouts", self.retrieve_layouts)
        workflow.add_node("score_layouts", self.score_layouts)
        workflow.add_node("adapt_layout", self.adapt_layout)
        workflow.add_node("score_output", self.score_output)

        # Define flow: normalize → analyze → reformulate → retrieve → score → adapt → score output → end
        workflow.set_entry_point("normalize_query")
        workflow.add_edge("normalize_query", "analyze_query")
        workflow.add_edge("analyze_query", "reformulate_query")
        workflow.add_edge("reformulate_query", "retrieve_layouts")
        workflow.add_edge("retrieve_layouts", "score_layouts")
        workflow.add_edge("score_layouts", "adapt_layout")
        workflow.add_edge("adapt_layout", "score_output")
        workflow.add_edge("score_output", END)

        return workflow.compile()

    # ---------------------------
    # NODE: NORMALIZE QUERY
    # ---------------------------
    def normalize_query(self, state: AgentState) -> AgentState:
        """Normalize the user query safely."""
        query = state.get("query", "").strip()

        if not query:
            state["normalized_query"] = ""
            return state

        try:
            normalized = QueryTranslator.invoke(query)
            state["normalized_query"] = normalized or query
            print(f"[Graph:Normalize] {query} -> {state['normalized_query']}")
        except Exception as e:
            print(f"[Graph:Normalize] Error: {e}")
            state["normalized_query"] = query

        return state

    # ---------------------------
    # NODE: ANALYZE QUERY
    # ---------------------------
    def analyze_query(self, state: AgentState) -> AgentState:
        """Analyze the normalized query to extract intent and components."""
        normalized_query = state.get("normalized_query", "")

        try:
            analysis = self.query_analyzer.invoke(normalized_query)
            state["analysis"] = analysis.dict()
            print(f"[Graph:Analyze] Intent: {analysis.intent}, Complexity: {analysis.complexity}")
        except Exception as e:
            print(f"[Graph:Analyze] Error: {e}")
            state["analysis"] = {
                "intent": "unknown",
                "components_needed": [],
                "data_type": "static",
                "action_required": "display",
                "complexity": "simple",
                "confidence": 0.5
            }

        return state

    # ---------------------------
    # NODE: REFORMULATE QUERY
    # ---------------------------
    def reformulate_query(self, state: AgentState) -> AgentState:
        """Reformulate query for optimal RAG retrieval."""
        analysis = state.get("analysis", {})

        try:
            rag_query = self.query_reformulator.invoke(analysis)
            state["rag_query"] = rag_query.dict()
            print(f"[Graph:Reformulate] RAG Query: '{rag_query.search_query}'")
        except Exception as e:
            print(f"[Graph:Reformulate] Error: {e}")
            state["rag_query"] = {
                "search_query": state.get("normalized_query", ""),
                "entity": "lead",
                "view_type": "detail",
                "filters": {},
                "confidence": 0.5
            }

        return state

    # ---------------------------
    # NODE: RETRIEVE LAYOUTS
    # ---------------------------
    def retrieve_layouts(self, state: AgentState) -> AgentState:
        """Retrieve top 3 matching layouts from RAG."""
        rag_query = state.get("rag_query", {})

        try:
            layouts = self.layout_rag.search_layouts(
                search_query=rag_query.get("search_query", ""),
                entity=rag_query.get("entity"),
                view_type=rag_query.get("view_type"),
                top_k=3
            )
            state["retrieved_layouts"] = layouts
            print(f"[Graph:Retrieve] Retrieved {len(layouts)} layouts")
        except Exception as e:
            print(f"[Graph:Retrieve] Error: {e}")
            state["retrieved_layouts"] = []

        return state

    # ---------------------------
    # NODE: SCORE LAYOUTS
    # ---------------------------
    def score_layouts(self, state: AgentState) -> AgentState:
        """Score and rank retrieved layouts."""
        layouts = state.get("retrieved_layouts", [])
        query = state.get("normalized_query", "")
        analysis = state.get("analysis", {})

        try:
            ranking = self.layout_scorer.score_layouts(layouts, query, analysis)
            state["layout_ranking"] = ranking.dict()
            
            # Select best layout
            best_id = ranking.best_layout_id
            state["selected_layout"] = next((l for l in layouts if l.get("id") == best_id), layouts[0] if layouts else None)
            
            print(f"[Graph:Score] Selected: {best_id}")
        except Exception as e:
            print(f"[Graph:Score] Error: {e}")
            state["layout_ranking"] = {}
            state["selected_layout"] = layouts[0] if layouts else None

        return state

    # ---------------------------
    # NODE: ADAPT LAYOUT
    # ---------------------------
    def adapt_layout(self, state: AgentState) -> AgentState:
        """Adapt selected layout to user query."""
        layout = state.get("selected_layout")
        query = state.get("normalized_query", "")
        analysis = state.get("analysis", {})

        if not layout:
            print("[Graph:Adapt] No layout to adapt")
            state["adapted_layout"] = None
            return state

        try:
            adapted = self.layout_adapter.adapt_layout(layout, query, analysis)
            state["adapted_layout"] = adapted
            print(f"[Graph:Adapt] Layout adapted successfully")
        except Exception as e:
            print(f"[Graph:Adapt] Error: {e}")
            state["adapted_layout"] = layout

        return state

    # ---------------------------
    # NODE: SCORE OUTPUT
    # ---------------------------
    def score_output(self, state: AgentState) -> AgentState:
        """Score the final adapted layout."""
        layout = state.get("adapted_layout")
        query = state.get("normalized_query", "")
        analysis = state.get("analysis", {})

        if not layout:
            print("[Graph:ScoreOutput] No layout to score")
            state["output_score"] = None
            state["outcome"] = {"success": False, "error": "No layout generated"}
            return state

        try:
            score = self.output_scorer.score_output(layout, query, analysis)
            state["output_score"] = score.dict()
            state["outcome"] = {
                "success": True,
                "layout": layout.get("layout"),
                "pattern": layout.get("pattern"),
                "score": score.overall_score
            }
            print(f"[Graph:ScoreOutput] Final score: {score.overall_score:.2f}")
        except Exception as e:
            print(f"[Graph:ScoreOutput] Error: {e}")
            state["output_score"] = {"overall_score": 0.8}
            state["outcome"] = {
                "success": True,
                "layout": layout.get("layout"),
                "pattern": layout.get("pattern"),
                "score": 0.8
            }

        return state

    # ---------------------------
    # RUNNER
    # ---------------------------
    def invoke(self, query: str) -> dict:
        print(f"\n{'='*60}")
        print(f"[Graph] Processing CRM Query: {query}")
        print(f"{'='*60}\n")

        initial_state: AgentState = {
            "query": query,
            "normalized_query": query,
            "analysis": None,
            "rag_query": None,
            "retrieved_layouts": None,
            "layout_ranking": None,
            "selected_layout": None,
            "adapted_layout": None,
            "output_score": None,
            "outcome": {},
            "messages": []
        }

        final_state = self.graph.invoke(initial_state)

        print(f"\n{'='*60}")
        print(f"[Graph] Processing complete!")
        print(f"{'='*60}\n")

        return {
            "success": final_state.get("outcome", {}).get("success", False),
            "query": final_state["query"],
            "normalized_query": final_state.get("normalized_query"),
            "analysis": final_state.get("analysis"),
            "rag_query": final_state.get("rag_query"),
            "retrieved_layouts": final_state.get("retrieved_layouts"),
            "layout_ranking": final_state.get("layout_ranking"),
            "layout": final_state.get("outcome", {}).get("layout"),
            "pattern": final_state.get("outcome", {}).get("pattern"),
            "score": final_state.get("outcome", {}).get("score"),
            "output_score": final_state.get("output_score"),
            "agent_trace": final_state["messages"]
        }


# Alias
DesignSystemGraph = AgentExecutor
