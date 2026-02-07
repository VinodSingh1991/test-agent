"""
Graph Builder - Constructs the workflow graph
Single Responsibility: Graph structure definition
"""
from langgraph.graph import StateGraph, END

from design_system_agent.agent.models import AgentState
from design_system_agent.agent.graph_nodes.node_executor import WorkflowExecutor


class GraphBuilder:
    """
    Builds the LangGraph workflow structure.
    Separates graph construction from execution logic.
    """
    
    @staticmethod
    def build(executor: WorkflowExecutor) -> StateGraph:
        """
        Build the LLM-powered workflow graph.
        
        Flow: plan → normalize → analyze_and_reformulate → retrieve(10→3) 
              → fetch_data → llm_select_and_fill → score_output → END
        
        Args:
            executor: WorkflowExecutor instance with all node methods
            
        Returns:
            Compiled StateGraph ready for execution
        """
        workflow = StateGraph(AgentState)
        
        # Add all nodes
        workflow.add_node("plan_tasks", executor.plan_tasks)
        workflow.add_node("normalize_query", executor.normalize_query)
        workflow.add_node("analyze_and_reformulate", executor.analyze_and_reformulate)
        workflow.add_node("retrieve_layouts", executor.retrieve_layouts)
        workflow.add_node("fetch_data", executor.fetch_data)
        workflow.add_node("llm_select_and_fill", executor.llm_select_and_fill)
        workflow.add_node("score_output", executor.score_output)
        
        # Define edges (workflow flow)
        workflow.set_entry_point("plan_tasks")
        workflow.add_edge("plan_tasks", "normalize_query")
        workflow.add_edge("normalize_query", "analyze_and_reformulate")
        workflow.add_edge("analyze_and_reformulate", "retrieve_layouts")
        workflow.add_edge("retrieve_layouts", "fetch_data")
        workflow.add_edge("fetch_data", "llm_select_and_fill")
        workflow.add_edge("llm_select_and_fill", "score_output")
        workflow.add_edge("score_output", END)
        
        return workflow.compile()
