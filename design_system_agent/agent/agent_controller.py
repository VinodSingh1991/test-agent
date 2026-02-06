"""
Main agent controller using Streaming Agent.
"""
from .layout_graph_agent import GraphAgent


class AgentController:
    """Controller using streaming agent with real-time updates."""
    
    def __init__(self):
        self.agent = GraphAgent(verbose=False)
        print("AgentController initialized with Streaming Agent")
    
    def process_query(self, query: str):
        """Process query through streaming agent.
        
        Args:
            query: User's natural language query
        
        Returns:
            Dict with generated layout and metadata
        """
        return self.agent.invoke(query)
