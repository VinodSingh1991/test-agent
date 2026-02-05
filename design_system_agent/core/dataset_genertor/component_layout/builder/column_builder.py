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
    
    def add_component(self, component_type: str, content: Any, classes: List[str] = None, props: Dict[str, Any] = None) -> 'ColumnBuilder':
        """
        Add a component to this column using ComponentBuilder
        
        Args:
            component_type: Component type (e.g., 'h2', 'p', 'button')
            content: Component content/children
            classes: Optional CSS classes for the component
            props: Optional properties for the component
            
        Returns:
            Self for method chaining
        """
        # Create component using ComponentBuilder
        component_builder = ComponentBuilder(component_type)
        
        # Add classes if provided
        if classes:
            component_builder.with_classes(*classes)
        
        # Add props if provided
        if props:
            component_builder.with_props(**props)
        
        # Build with type and content
        self._children = component_builder.build(component_type=component_type, content=content)
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
