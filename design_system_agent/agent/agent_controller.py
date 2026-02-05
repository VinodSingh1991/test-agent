"""
Main agent controller using LangGraph multi-agent system.
"""
from .graph_agent import DesignSystemGraph


class AgentController:
    """Simplified controller using LangGraph multi-agent system."""
    
    def __init__(self):
        self.graph = DesignSystemGraph()
        print("AgentController initialized with LangGraph multi-agent system")
    
    def process_query(self, query: str):
        """Process query through multi-agent graph.
        
        Args:
            query: User's natural language query
        
        Returns:
            Dict with generated code and metadata
        """
        return self.graph.invoke(query)
