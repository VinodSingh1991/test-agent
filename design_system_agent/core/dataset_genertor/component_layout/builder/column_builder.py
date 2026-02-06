"""
Column Builder

Builder for creating columns with fluent API.
Single Responsibility: Build Column objects only.
"""

from typing import Dict, Any, Union, List
from design_system_agent.core.component_types import ComponentType
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Column, Component
from design_system_agent.core.dataset_genertor.component_layout.builder.component_builder import ComponentBuilder


class ColumnBuilder:
    """Builder for Column with fluent interface"""
    
    def __init__(self, name: str, col_id: str):
        """
        Initialize ColumnBuilder
        
        Args:
            name: Column name
            col_id: Column ID
        """
        self._name = name
        self._id = col_id
        self._children: Union[Component, Dict[str, Any], None] = None
        self._component_type: str = None
    
    def add_component(self, component_or_type: Union[Component, str], content: Any = None, classes: List[str] = None, props: Dict[str, Any] = None, value: Dict[str, str] = None, events: Dict[str, str] = None) -> 'ColumnBuilder':
        """
        Add a component to this column
        
        Args:
            component_or_type: Either a Component object or component type string
            content: Component content/children (for complex components, when type is string)
            classes: Optional CSS classes (when type is string)
            props: Optional properties (when type is string)
            value: Optional value dict with icon and text (when type is string)
            events: Optional event handlers (when type is string)
            
        Returns:
            Self for method chaining
        """
        # If this is a Component object being passed directly, use it
        if isinstance(component_or_type, Component):
            self._children = component_or_type
            self._component_type = component_or_type.type
            return self
        
        # Otherwise build component from parameters
        component_type = component_or_type
        component_dict = {
            "type": component_type,
            "classes": classes if classes else [],
            "props": props if props else {},
        }
        
        if value is not None:
            component_dict["value"] = value
        elif content is not None:
            component_dict["children"] = content
        
        if events:
            component_dict["events"] = events
        
        self._children = component_dict
        self._component_type = component_type
        return self
    
    def build(self) -> Column:
        """
        Build and return the Column
        
        Returns:
            Column instance
        """
        if self._children is None:
            raise ValueError("Column must have children. Use add_component() to set it.")
        
        # Convert Component objects to dict before passing to Column
        # Column.to_dict() will handle Component objects, but we should pass them directly
        # so Column can use its to_dict() method properly
        return Column(
            name=self._name,
            id=self._id,
            children=self._children  # Column.to_dict() will convert Component to dict
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation with PascalCase keys
        """
        return self.build().to_dict()
