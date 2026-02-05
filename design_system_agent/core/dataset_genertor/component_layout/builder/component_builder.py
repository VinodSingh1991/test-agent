"""
Component Builder

Builder for creating UI components with fluent API.
Single Responsibility: Build Component objects only.
"""

from typing import Dict, List, Any, Optional, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ComponentBuilder:
    """Builder for Component with fluent interface"""
    
    def __init__(self, component_type: str):
        """
        Initialize ComponentBuilder
        
        Args:
            component_type: The HTML/component type (e.g., 'div', 'button', 'input')
        """
        self._type = component_type
        self._classes: List[str] = []
        self._props: Dict[str, Any] = {}
        self._children: Optional[Union[str, List[Any], Dict[str, Any]]] = None
        self._events: Optional[Dict[str, str]] = None
        self._id: Optional[str] = None
    
    def with_classes(self, *classes: str) -> 'ComponentBuilder':
        """
        Add CSS classes to the component
        
        Args:
            *classes: CSS class names
            
        Returns:
            Self for method chaining
        """
        self._classes.extend(classes)
        return self
    
    def with_props(self, **props: Any) -> 'ComponentBuilder':
        """
        Add properties to the component
        
        Args:
            **props: Component properties as key-value pairs
            
        Returns:
            Self for method chaining
        """
        self._props.update(props)
        return self
    
    def with_children(self, children: Union[str, List[Any], Dict[str, Any]]) -> 'ComponentBuilder':
        """
        Set children for the component
        
        Args:
            children: Component children (string, list, or dict)
            
        Returns:
            Self for method chaining
        """
        self._children = children
        return self
    
    def with_events(self, **events: str) -> 'ComponentBuilder':
        """
        Add event handlers to the component
        
        Args:
            **events: Event handlers as key-value pairs (e.g., onClick="handleClick")
            
        Returns:
            Self for method chaining
        """
        if self._events is None:
            self._events = {}
        self._events.update(events)
        return self
    
    def with_id(self, component_id: str) -> 'ComponentBuilder':
        """
        Set component ID
        
        Args:
            component_id: Unique component identifier
            
        Returns:
            Self for method chaining
        """
        self._id = component_id
        return self
    
    def build(self, component_type: str = None, content: Any = None) -> Component:
        """
        Build and return the Component
        
        Args:
            component_type: Optional override for component type
            content: Optional override for component content/children
        
        Returns:
            Component instance
        """
        return Component(
            type=component_type if component_type else self._type,
            classes=self._classes.copy(),
            props=self._props.copy(),
            children=content if content is not None else self._children,
            events=self._events.copy() if self._events else None,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
