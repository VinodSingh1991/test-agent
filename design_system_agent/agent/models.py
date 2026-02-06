"""
Agent Models and Types
Single Responsibility: Define type structures for agent execution
"""
from typing import TypedDict, Optional, List, Dict, Annotated
from enum import Enum
import operator


# ---------------------------
# EVENT TYPES
# ---------------------------
class EventType(str, Enum):
    """Event types for streaming updates"""
    NODE_STARTED = "node_started"
    NODE_COMPLETED = "node_completed"
    TASK_PLANNED = "task_planned"
    DATA_FETCHED = "data_fetched"
    LAYOUT_RETRIEVED = "layout_retrieved"
    FINAL_RESULT = "final_result"
    ERROR = "error"


class AgentEvent(TypedDict):
    """Event emitted during agent execution"""
    event_type: EventType
    timestamp: str
    node_name: str
    status: str
    data: Optional[Dict]
    message: str
    progress: float  # 0.0 to 1.0


# ---------------------------
# STATE MODEL
# ---------------------------
class AgentState(TypedDict):
    """State model for agent execution with streaming and task planning"""
    # Query processing
    query: str
    normalized_query: str
    analysis: Optional[Dict]
    rag_query: Optional[Dict]
    
    # Layout processing
    retrieved_layouts: Optional[List[Dict]]
    layout_ranking: Optional[Dict]
    selected_layout: Optional[Dict]
    adapted_layout: Optional[Dict]
    output_score: Optional[Dict]
    
    # Result
    outcome: Dict
    messages: Annotated[List, operator.add]
    
    # Task planning
    task_plan: Optional[List[Dict]]  # Task execution plan
    current_task_index: int          # Current task index
    
    # Data fetching
    fetched_data: Optional[Dict]     # Data for populating layout
    
    # Streaming
    events: Annotated[List[AgentEvent], operator.add]  # Event stream
    progress: float                  # Overall progress (0.0 to 1.0)
    error: Optional[str]             # Error message if any
