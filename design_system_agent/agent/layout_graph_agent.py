"""
Graph Agent - Main Orchestrator
Single Responsibility: Coordinate the layout generation workflow
"""
from design_system_agent.agent.models import AgentState
from design_system_agent.agent.graph_nodes.node_executor import WorkflowExecutor
from design_system_agent.agent.layout_graph_builder import GraphBuilder


class GraphAgent:
    """
    Main orchestrator for CRM layout generation workflow.
    
    Responsibility:
    - Coordinate execution flow between nodes
    - Manage state transitions
    - Emit events for streaming UI updates
    
    Features:
    - Real-time streaming updates
    - Task planning with progress tracking
    - LLM-powered intelligent layout selection
    - Comprehensive error handling
    """
    
    def __init__(self, verbose: bool = True):
        """Initialize agent with workflow executor and graph"""
        self.executor = WorkflowExecutor()
        self.graph = GraphBuilder.build(self.executor)
        self.verbose = verbose
    
    def _create_initial_state(self, query: str) -> AgentState:
        """Create initial state for graph execution"""
        return {
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
            "messages": [],
            "task_plan": None,
            "current_task_index": 0,
            "fetched_data": None,
            "events": [],
            "progress": 0.0,
            "error": None
        }
    
    def _extract_result(self, final_state: AgentState) -> dict:
        """Extract result from final state - returns complete layout with all metadata"""
        outcome = final_state.get("outcome", {})
        layout_obj = outcome.get("layout", {})
        rag_query = final_state.get("rag_query", {})
        
        # Extract only essential fields: id, query, layout, score, object_type, layout_type
        return {
            "id": layout_obj.get("id"),
            "query": final_state["query"],
            "layout": layout_obj.get("layout", {}),  # The rows/pattern_info structure
            "score": outcome.get("score", layout_obj.get("score", 0.0)),
            "object_type": rag_query.get("object_type", "unknown"),
            "layout_type": rag_query.get("layout_type", "list")
        }
    
    def invoke(self, query: str, json_output: bool = False) -> dict:
        """
        Synchronous execution of the workflow.
        
        Args:
            query: User's natural language query
            json_output: If True, prints clean JSON output only
            
        Returns:
            Result dictionary with layout, data, and metadata
        """
        if self.verbose and not json_output:
            print(f"\n{'='*60}")
            print(f"[GraphAgent] Processing Query: {query}")
            print(f"{'='*60}\n")
        
        initial_state = self._create_initial_state(query)
        final_state = self.graph.invoke(initial_state)
        
        result = self._extract_result(final_state)
        
        if json_output:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        elif self.verbose:
            print(f"\n{'='*60}")
            print(f"[GraphAgent] Execution Complete!")
            print(f"{'='*60}\n")
        
        return result
    
    async def astream(self, query: str) -> AsyncGenerator[AgentEvent, None]:
        """
        Async streaming execution - yields events in real-time.
        
        Args:
            query: User's natural language query
            
        Yields:
            AgentEvent objects as they occur during execution
        """
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"[GraphAgent] Streaming Query: {query}")
            print(f"{'='*60}\n")
        
        event_queue = asyncio.Queue()
        loop = asyncio.get_event_loop()
        
        def event_handler(event: AgentEvent):
            loop.call_soon_threadsafe(event_queue.put_nowait, event)
        
        self.set_event_callback(event_handler)
        
        async def run_graph():
            try:
                initial_state = self._create_initial_state(query)
                await asyncio.to_thread(self.graph.invoke, initial_state)
                await event_queue.put(None)  # Sentinel
            except Exception as e:
                error_event: AgentEvent = {
                    "event_type": EventType.ERROR,
                    "timestamp": datetime.now().isoformat(),
                    "node_name": "executor",
                    "status": "failed",
                    "data": {"error": str(e)},
                    "message": f"Execution failed: {e}",
                    "progress": 0.0
                }
                await event_queue.put(error_event)
                await event_queue.put(None)
        
        asyncio.create_task(run_graph())
        
        while True:
            event = await event_queue.get()
            if event is None:
                break
            yield event


# Alias for backwards compatibility
DesignSystemGraph = GraphAgent
