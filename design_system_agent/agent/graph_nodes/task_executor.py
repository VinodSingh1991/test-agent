"""
Task Executor - Executes tasks from the execution plan
"""
from typing import Dict, Any, List
from design_system_agent.core.dataset_genertor.component_layout.summary_dataset.summary_data_generator import SummaryDataGenerator


class TaskExecutor:
    """Executes tasks from the execution plan"""
    
    def __init__(self):
        self.generator = SummaryDataGenerator()
        self.pattern_map = {
            "title_description": "generate_title_description",
            "title_list": "generate_title_list",
            "title_list_description": "generate_title_list_description",
            "title_button": "generate_title_button",
            "title_description_button": "generate_title_description_button",
            "title_list_button": "generate_title_list_button"
        }
    
    def execute_plan(self, plan: Dict[str, Any], query: str) -> Dict[str, Any]:
        """Execute all tasks in the plan and return the result"""
        print(f"[TaskExecutor] Executing plan with {len(plan.get('tasks', []))} tasks")
        
        tasks = plan.get("tasks", [])
        context = {
            "selected_pattern": None,
            "content": {},
            "layout": None
        }
        
        for task in tasks:
            task_type = task.get("task_type")
            print(f"[TaskExecutor] Executing task: {task.get('task_id')} ({task_type})")
            
            if task_type == "select_pattern":
                context = self._select_pattern(task, context)
            elif task_type == "extract_content":
                context = self._extract_content(task, context, query)
            elif task_type == "generate_layout":
                context = self._generate_layout(task, context)
            elif task_type == "validate_output":
                context = self._validate_output(task, context)
        
        return {
            "success": True,
            "layout": context.get("layout"),
            "pattern_used": context.get("selected_pattern"),
            "query": query
        }
    
    def _select_pattern(self, task: Dict, context: Dict) -> Dict:
        """Select the appropriate pattern"""
        pattern = task.get("parameters", {}).get("pattern", "title_description")
        context["selected_pattern"] = pattern
        print(f"[TaskExecutor] Selected pattern: {pattern}")
        return context
    
    def _extract_content(self, task: Dict, context: Dict, query: str) -> Dict:
        """Extract or generate content for components"""
        params = task.get("parameters", {})
        
        # Use parameters or generate simple defaults based on query
        context["content"] = {
            "title": params.get("title", self._generate_title(query)),
            "description": params.get("description", self._generate_description(query)),
            "list_items": params.get("list_items", self._generate_list_items(query)),
            "button_text": params.get("button_text", self._generate_button_text(query))
        }
        
        print(f"[TaskExecutor] Extracted content: title='{context['content']['title']}'")
        return context
    
    def _generate_layout(self, task: Dict, context: Dict) -> Dict:
        """Generate the layout using the selected pattern"""
        pattern = context.get("selected_pattern", "title_description")
        content = context.get("content", {})
        
        method_name = self.pattern_map.get(pattern, "generate_title_description")
        method = getattr(self.generator, method_name, None)
        
        if not method:
            print(f"[TaskExecutor] Pattern method not found: {method_name}")
            return context
        
        try:
            # Build parameters based on pattern
            if pattern == "title_description":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    description=content.get("description", "Description")
                )
            elif pattern == "title_list":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    list_items=content.get("list_items", ["Item 1", "Item 2"])
                )
            elif pattern == "title_list_description":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    list_items=content.get("list_items", ["Item 1", "Item 2"]),
                    description=content.get("description", "Description")
                )
            elif pattern == "title_button":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    button_text=content.get("button_text", "Action")
                )
            elif pattern == "title_description_button":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    description=content.get("description", "Description"),
                    button_text=content.get("button_text", "Action")
                )
            elif pattern == "title_list_button":
                layout = method(
                    idx=1,
                    title=content.get("title", "Summary"),
                    list_items=content.get("list_items", ["Item 1", "Item 2"]),
                    button_text=content.get("button_text", "Action")
                )
            
            context["layout"] = layout.to_dict()
            print(f"[TaskExecutor] Layout generated successfully")
        except Exception as e:
            print(f"[TaskExecutor] Error generating layout: {e}")
        
        return context
    
    def _validate_output(self, task: Dict, context: Dict) -> Dict:
        """Validate the generated output"""
        layout = context.get("layout")
        if layout and "Tabs" in layout:
            print(f"[TaskExecutor] Validation passed: Layout has required structure")
        else:
            print(f"[TaskExecutor] Validation warning: Layout may be incomplete")
        return context
    
    # Simple content generators (can be replaced with LLM-based generation)
    def _generate_title(self, query: str) -> str:
        """Generate title from query"""
        if "notification" in query.lower():
            return "Notifications"
        elif "task" in query.lower():
            return "Tasks"
        elif "event" in query.lower():
            return "Events"
        elif "approval" in query.lower():
            return "Approvals"
        else:
            return "Summary"
    
    def _generate_description(self, query: str) -> str:
        """Generate description from query"""
        return f"Here is the information you requested: {query}"
    
    def _generate_list_items(self, query: str) -> List[str]:
        """Generate list items from query"""
        return ["Item 1", "Item 2", "Item 3"]
    
    def _generate_button_text(self, query: str) -> str:
        """Generate button text from query"""
        if "update" in query.lower():
            return "Update Now"
        elif "approve" in query.lower() or "approval" in query.lower():
            return "Review All"
        elif "submit" in query.lower():
            return "Submit"
        else:
            return "View Details"
