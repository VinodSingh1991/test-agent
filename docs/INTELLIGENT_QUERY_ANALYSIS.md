# How Copilot Analyzes Queries - Intelligent Agent Architecture

## Overview

This document explains how an AI agent (like GitHub Copilot) analyzes user queries, extracts intent, creates execution plans, and resolves tasks. The implementation demonstrates a **multi-node LangGraph agent** that processes natural language queries into structured UI layouts.

---

## The Complete Flow

```
User Query 
    ↓
1. Query Translation (Normalize)
    ↓
2. Query Analysis (Extract Intent & Components)
    ↓
3. Task Planning (Create Execution Plan)
    ↓
4. Task Execution (Generate Layout)
    ↓
Result (Structured Layout)
```

---

## Phase-by-Phase Breakdown

### Phase 1: Query Translation (Normalization)

**Component**: [`QueryTranslator`](design_system_agent/agent/graph_nodes/query_translator.py)

**Purpose**: Clean and standardize the user's input

**What it does**:
- Converts Hinglish to English ("mujhe notifications dikhao" → "show my notifications")
- Fixes spelling errors
- Converts number words to digits ("five" → "5")
- Removes noise and standardizes format

**Example**:
```python
Input:  "mujhe 5 notifications dikhao pls"
Output: "show 5 notifications"
```

**How it works**:
```python
class QueryTranslator:
    @classmethod
    def invoke(cls, user_query: str) -> str:
        llm = LLMFactory.open_ai()
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Normalize this query to English"),
            ("user", "{query}")
        ])
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"query": user_query})
```

---

### Phase 2: Query Analysis (Intent Extraction)

**Component**: [`QueryAnalyzer`](design_system_agent/agent/graph_nodes/query_analyzer.py)

**Purpose**: Understand **what** the user wants and **which components** are needed

**What it extracts**:
- **Intent**: The user's goal (e.g., "show_notifications", "display_approvals")
- **Components Needed**: UI elements required (e.g., ["title", "description", "button"])
- **Data Type**: Static vs. dynamic data
- **Action Required**: What needs to happen (display, update, filter)
- **Complexity**: Simple, moderate, or complex
- **Confidence**: How certain the analysis is (0.0 - 1.0)

**Example**:
```python
Input Query: "show pending approvals with action button"

Analysis Output:
{
    "intent": "display_approvals",
    "components_needed": ["title", "description", "button"],
    "data_type": "dynamic",
    "action_required": "display_with_action",
    "complexity": "moderate",
    "confidence": 0.9
}
```

**How it works**:
```python
class QueryAnalysis(BaseModel):
    intent: str
    components_needed: List[str]
    data_type: str
    action_required: str
    complexity: str
    confidence: float

class QueryAnalyzer:
    def invoke(self, normalized_query: str) -> QueryAnalysis:
        llm = LLMFactory.open_ai()
        parser = JsonOutputParser(pydantic_object=QueryAnalysis)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Analyze the query and extract:
                - intent: What the user wants
                - components_needed: Which UI components
                - data_type: static or dynamic
                - action_required: display, update, delete, etc.
                - complexity: simple, moderate, complex
                - confidence: 0.0 to 1.0
            
            Examples:
            Query: "show my notifications"
            {{
                "intent": "show_notifications",
                "components_needed": ["title", "description"],
                "data_type": "dynamic",
                "action_required": "display",
                "complexity": "simple",
                "confidence": 0.95
            }}
            """),
            ("user", "{query}")
        ])
        
        chain = prompt | llm | parser
        return chain.invoke({"query": normalized_query})
```

**Key Insight**: The LLM acts as an **intelligent classifier** that extracts structured information from natural language.

---

### Phase 3: Task Planning (Execution Strategy)

**Component**: [`TaskPlanner`](design_system_agent/agent/graph_nodes/task_planner.py)

**Purpose**: Convert analysis into **actionable tasks**

**What it creates**:
- **Plan Summary**: High-level description
- **Tasks**: Ordered list of specific actions
- **Estimated Complexity**: Overall difficulty

**Task Types**:
1. `select_pattern`: Choose the right UI pattern (title+desc, title+list+button, etc.)
2. `extract_content`: Generate or fetch the actual content
3. `generate_layout`: Build the layout using builder pattern
4. `validate_output`: Verify the result

**Example**:
```python
Input Analysis: {
    "intent": "display_approvals",
    "components_needed": ["title", "description", "button"],
    "complexity": "moderate"
}

Execution Plan Output:
{
    "plan_summary": "Display approvals with title, description, and action button",
    "tasks": [
        {
            "task_id": "task_1",
            "task_type": "select_pattern",
            "description": "Select title_description_button pattern",
            "parameters": {"pattern": "title_description_button"},
            "priority": 1
        },
        {
            "task_id": "task_2",
            "task_type": "extract_content",
            "description": "Extract approval data",
            "parameters": {
                "title": "Pending Approvals",
                "description": "You have approvals waiting",
                "button_text": "Review All"
            },
            "priority": 2
        },
        {
            "task_id": "task_3",
            "task_type": "generate_layout",
            "description": "Generate layout using builder pattern",
            "parameters": {},
            "priority": 3
        },
        {
            "task_id": "task_4",
            "task_type": "validate_output",
            "description": "Validate generated layout structure",
            "parameters": {},
            "priority": 4
        }
    ],
    "estimated_complexity": "moderate"
}
```

**How it works**:
```python
class Task(BaseModel):
    task_id: str
    task_type: str
    description: str
    parameters: Dict[str, Any]
    priority: int

class ExecutionPlan(BaseModel):
    plan_summary: str
    tasks: List[Task]
    estimated_complexity: str

class TaskPlanner:
    def invoke(self, analysis: Dict) -> ExecutionPlan:
        llm = LLMFactory.open_ai()
        parser = JsonOutputParser(pydantic_object=ExecutionPlan)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Create an execution plan with tasks:
                Task Types:
                - select_pattern: Choose UI pattern
                - extract_content: Get/generate content
                - generate_layout: Build the layout
                - validate_output: Verify result
            
            Map analysis to tasks based on complexity and components.
            """),
            ("user", "{analysis}")
        ])
        
        chain = prompt | llm | parser
        return chain.invoke({"analysis": json.dumps(analysis)})
```

**Key Insight**: The LLM acts as a **strategic planner** that breaks down complex goals into sequential steps.

---

### Phase 4: Task Execution (Implementation)

**Component**: [`TaskExecutor`](design_system_agent/agent/graph_nodes/task_executor.py)

**Purpose**: Execute each task and generate the final layout

**What it does**:
1. **Select Pattern**: Maps analysis to one of 6 UI patterns
   - `title_description`
   - `title_list`
   - `title_list_description`
   - `title_button`
   - `title_description_button`
   - `title_list_button`

2. **Extract Content**: Generates or retrieves actual content (can use LLM)

3. **Generate Layout**: Uses builder pattern to create hierarchy
   ```
   Layout
   └── Tab
       └── Section
           └── Row
               └── Column
                   └── Component (Heading, Description, List, Button)
   ```

4. **Validate Output**: Ensures layout has required structure

**Example Execution**:
```python
class TaskExecutor:
    def __init__(self):
        self.generator = SummaryDataGenerator()
        self.pattern_map = {
            "title_description": "generate_title_description",
            "title_button": "generate_title_button",
            # ... more patterns
        }
    
    def execute_plan(self, plan: Dict, query: str) -> Dict:
        context = {"selected_pattern": None, "content": {}, "layout": None}
        
        for task in plan["tasks"]:
            if task["task_type"] == "select_pattern":
                context["selected_pattern"] = task["parameters"]["pattern"]
            
            elif task["task_type"] == "extract_content":
                context["content"] = {
                    "title": self._generate_title(query),
                    "description": self._generate_description(query),
                    "button_text": self._generate_button_text(query)
                }
            
            elif task["task_type"] == "generate_layout":
                pattern = context["selected_pattern"]
                method = getattr(self.generator, self.pattern_map[pattern])
                layout = method(**context["content"])
                context["layout"] = layout.to_dict()
            
            elif task["task_type"] == "validate_output":
                # Validate structure
                pass
        
        return {"success": True, "layout": context["layout"]}
```

**Output**:
```json
{
  "success": true,
  "layout": {
    "Tabs": [{
      "TabName": "Summary",
      "Sections": [{
        "SectionName": "Main Content",
        "Rows": [
          {
            "Cols": [{
              "Children": {
                "type": "Heading",
                "classes": "...",
                "props": {"text": "Pending Approvals"}
              }
            }]
          },
          {
            "Cols": [{
              "Children": {
                "type": "Description",
                "props": {"text": "You have approvals waiting"}
              }
            }]
          },
          {
            "Cols": [{
              "Children": {
                "type": "Button",
                "props": {"text": "Review All"}
              }
            }]
          }
        ]
      }]
    }]
  }
}
```

---

## LangGraph Integration

All components are orchestrated using **LangGraph**, a state machine for AI agents:

```python
class AgentState(TypedDict):
    query: str
    normalized_query: str
    analysis: Optional[Dict]
    execution_plan: Optional[Dict]
    result: Optional[Dict]
    outcome: Dict
    messages: List

class AgentExecutor:
    def __init__(self):
        self.query_analyzer = QueryAnalyzer()
        self.task_planner = TaskPlanner()
        self.task_executor = TaskExecutor()
        self.graph = self._build_graph()
    
    def _build_graph(self):
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("normalize_query", self.normalize_query)
        workflow.add_node("analyze_query", self.analyze_query)
        workflow.add_node("plan_tasks", self.plan_tasks)
        workflow.add_node("execute_tasks", self.execute_tasks)
        
        # Define flow
        workflow.set_entry_point("normalize_query")
        workflow.add_edge("normalize_query", "analyze_query")
        workflow.add_edge("analyze_query", "plan_tasks")
        workflow.add_edge("plan_tasks", "execute_tasks")
        workflow.add_edge("execute_tasks", END)
        
        return workflow.compile()
```

**State flows through each node**, accumulating information:
1. `query` → `normalized_query`
2. `normalized_query` → `analysis`
3. `analysis` → `execution_plan`
4. `execution_plan` → `result`

---

## Key Techniques

### 1. **Structured LLM Outputs with Pydantic**

Instead of parsing free-form text, use Pydantic models + JsonOutputParser:

```python
class QueryAnalysis(BaseModel):
    intent: str = Field(description="User's goal")
    components_needed: List[str] = Field(description="Required UI components")
    confidence: float = Field(description="Confidence score")

parser = JsonOutputParser(pydantic_object=QueryAnalysis)
chain = prompt | llm | parser
result: QueryAnalysis = chain.invoke(query)  # Structured output!
```

### 2. **Chain-of-Thought Prompting**

Provide examples in prompts to train the LLM:

```python
prompt = """
Analyze this query and extract components.

Examples:
Query: "show my tasks"
Analysis: {
    "intent": "show_tasks",
    "components_needed": ["title", "list"],
    "complexity": "simple"
}

Query: "display approvals with action button"
Analysis: {
    "intent": "display_approvals",
    "components_needed": ["title", "description", "button"],
    "complexity": "moderate"
}

Now analyze: {user_query}
"""
```

### 3. **Fallback Mechanisms**

Always have backup logic when LLM fails:

```python
try:
    analysis = self.query_analyzer.invoke(query)
except Exception as e:
    # Fallback analysis
    analysis = {
        "intent": "unknown",
        "components_needed": [],
        "complexity": "simple",
        "confidence": 0.5
    }
```

### 4. **Builder Pattern for Complex Structures**

Use fluent APIs to construct layouts:

```python
layout = (LayoutBuilder()
    .add_tab("Summary")
    .add_section("Main")
    .add_row()
    .add_column()
    .add_component(HeadingBuilder("Title").to_dict())
    .add_row()
    .add_column()
    .add_component(DescriptionBuilder("Desc").to_dict())
    .to_dict())
```

---

## How GitHub Copilot Works Similarly

GitHub Copilot uses a similar multi-stage process:

1. **Context Gathering**: Reads current file, open tabs, related files
2. **Intent Analysis**: Analyzes cursor position, surrounding code, comments
3. **Plan Generation**: Decides what code to generate (function, class, tests)
4. **Code Synthesis**: Generates code using GPT-4 with context
5. **Ranking**: Scores multiple completions, picks the best
6. **Streaming**: Shows suggestions in real-time

**Key Differences**:
- Copilot uses **code embeddings** for semantic search
- Copilot has **multi-model architecture** (fast model for quick suggestions, slow model for complex tasks)
- Copilot uses **reinforcement learning** from user acceptances/rejections

---

## Running the Demo

```bash
# Test the intelligent agent
python test_intelligent_agent.py

# Output shows:
# - Normalized query
# - Analysis (intent, components, complexity)
# - Execution plan (tasks with priorities)
# - Generated layout (complete JSON structure)
```

**Test Queries**:
- `"show my notifications"` → title + description layout
- `"list all my tasks"` → title + list layout
- `"display approvals with button"` → title + description + button layout

---

## Architecture Benefits

✅ **Modular**: Each phase is independent and testable  
✅ **Extensible**: Easy to add new patterns or analysis types  
✅ **Intelligent**: LLM makes decisions, not hardcoded rules  
✅ **Structured**: Pydantic ensures type safety  
✅ **Observable**: Each phase logs its decisions  
✅ **Resilient**: Fallback logic prevents complete failures  

---

## Files Reference

| Component | File | Purpose |
|-----------|------|---------|
| QueryTranslator | [query_translator.py](design_system_agent/agent/graph_nodes/query_translator.py) | Normalize queries |
| QueryAnalyzer | [query_analyzer.py](design_system_agent/agent/graph_nodes/query_analyzer.py) | Extract intent & components |
| TaskPlanner | [task_planner.py](design_system_agent/agent/graph_nodes/task_planner.py) | Create execution plan |
| TaskExecutor | [task_executor.py](design_system_agent/agent/graph_nodes/task_executor.py) | Execute tasks |
| AgentExecutor | [graph_agent.py](design_system_agent/agent/graph_agent.py) | LangGraph orchestration |
| SummaryDataGenerator | [summary_data_generator.py](design_system_agent/core/dataset_genertor/component_layout/summary_dataset/summary_data_generator.py) | Layout builder patterns |

---

## Next Steps

1. **Add Real LLM**: Set `OPENAI_API_KEY` to use GPT-4 instead of mock
2. **Expand Patterns**: Add more UI patterns (cards, tables, forms)
3. **Dynamic Content**: Use LLM to generate actual content from data sources
4. **Conditional Routing**: Add decision nodes in LangGraph for complex flows
5. **Feedback Loop**: Learn from user corrections to improve analysis

---

**This architecture demonstrates how modern AI agents think, plan, and execute - moving from natural language to structured outputs through intelligent reasoning.**
