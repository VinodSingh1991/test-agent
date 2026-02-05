"""
Task Planner - Creates execution plan based on query analysis
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List
from design_system_agent.agent.core.llm_factory import LLMFactory


class Task(BaseModel):
    """Individual task in the execution plan"""
    task_id: str = Field(description="Unique task identifier")
    task_type: str = Field(description="Type of task (e.g., 'select_pattern', 'generate_layout', 'validate')")
    description: str = Field(description="Human-readable task description")
    parameters: dict = Field(default_factory=dict, description="Parameters needed for this task")
    priority: int = Field(description="Execution priority (1=highest)")


class ExecutionPlan(BaseModel):
    """Complete execution plan for resolving the query"""
    plan_summary: str = Field(description="Brief summary of the execution plan")
    tasks: List[Task] = Field(description="Ordered list of tasks to execute")
    estimated_complexity: str = Field(description="Overall complexity: 'low', 'medium', 'high'")


class TaskPlanner:
    """Creates execution plans based on query analysis"""
    
    @classmethod
    def get_planning_prompt(cls) -> ChatPromptTemplate:
        system_prompt = """
        You are a task planning expert for a design system agent.
        
        Based on the query analysis, create a detailed execution plan with specific tasks.
        
        Available task types:
        1. **select_pattern**: Choose the right UI pattern (title+desc, title+list+button, etc.)
        2. **extract_content**: Extract or generate content for components
        3. **generate_layout**: Build the layout structure using builders
        4. **validate_output**: Ensure the output meets requirements
        
        Examples:
        
        Analysis: intent="show_notifications", components=["title", "description"], complexity="simple"
        Plan:
        - Task 1: select_pattern (pattern: "title_description")
        - Task 2: extract_content (title: "Notifications", description: "notification text")
        - Task 3: generate_layout (using title_description pattern)
        - Task 4: validate_output (check completeness)
        
        Analysis: intent="show_approvals", components=["title", "list", "button"], complexity="moderate"
        Plan:
        - Task 1: select_pattern (pattern: "title_list_button")
        - Task 2: extract_content (title: "Pending Approvals", list_items: ["item1", "item2"], button: "Review All")
        - Task 3: generate_layout (using title_list_button pattern)
        - Task 4: validate_output (check all components present)
        
        Now create an execution plan for this analysis:
        
        Intent: {intent}
        Components Needed: {components_needed}
        Data Type: {data_type}
        Action Required: {action_required}
        Complexity: {complexity}
        """
        
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt)
        ])
    
    @classmethod
    def invoke(cls, analysis: dict) -> ExecutionPlan:
        """Create execution plan based on query analysis"""
        prompt = cls.get_planning_prompt()
        parser = JsonOutputParser(pydantic_object=ExecutionPlan)
        
        chain = prompt | LLMFactory.open_ai() | parser
        
        print(f"[TaskPlanner] Creating plan for intent: {analysis.get('intent')}")
        
        try:
            result = chain.invoke({
                "intent": analysis.get("intent", "unknown"),
                "components_needed": analysis.get("components_needed", []),
                "data_type": analysis.get("data_type", ""),
                "action_required": analysis.get("action_required", ""),
                "complexity": analysis.get("complexity", "simple")
            })
            
            plan = ExecutionPlan(**result)
            print(f"[TaskPlanner] Plan created with {len(plan.tasks)} tasks")
            for task in plan.tasks:
                print(f"  - {task.task_id}: {task.description}")
            
            return plan
        except Exception as e:
            print(f"[TaskPlanner] Error: {e}, using fallback plan")
            # Fallback to basic plan
            return ExecutionPlan(
                plan_summary="Basic layout generation",
                tasks=[
                    Task(
                        task_id="task_1",
                        task_type="select_pattern",
                        description="Select title_description pattern",
                        parameters={"pattern": "title_description"},
                        priority=1
                    ),
                    Task(
                        task_id="task_2",
                        task_type="generate_layout",
                        description="Generate basic layout",
                        parameters={},
                        priority=2
                    )
                ],
                estimated_complexity="low"
            )
