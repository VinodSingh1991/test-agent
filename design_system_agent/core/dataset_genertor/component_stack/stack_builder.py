"""
Stack Builder

Builder for creating stack layout components (vertical/horizontal).
Single Responsibility: Build stacked layouts with spacing.
"""

from typing import Dict, Any, Optional, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class StackBuilder:
    """Builder for Stack layout components with fluent interface"""
    
    def __init__(self):
        """Initialize StackBuilder"""
        self._direction = "vertical"
        self._spacing = "md"
        self._align = "start"
        self._children: List[Union[Dict, Component]] = []
        self._id: Optional[str] = None
    
    def vertical(self) -> 'StackBuilder':
        """Set stack direction to vertical"""
        self._direction = "vertical"
        return self
    
    def horizontal(self) -> 'StackBuilder':
        """Set stack direction to horizontal"""
        self._direction = "horizontal"
        return self
    
    def small_spacing(self) -> 'StackBuilder':
        """Set small spacing"""
        self._spacing = "sm"
        return self
    
    def medium_spacing(self) -> 'StackBuilder':
        """Set medium spacing"""
        self._spacing = "md"
        return self
    
    def large_spacing(self) -> 'StackBuilder':
        """Set large spacing"""
        self._spacing = "lg"
        return self
    
    def align_start(self) -> 'StackBuilder':
        """Align items to start"""
        self._align = "start"
        return self
    
    def align_center(self) -> 'StackBuilder':
        """Align items to center"""
        self._align = "center"
        return self
    
    def align_end(self) -> 'StackBuilder':
        """Align items to end"""
        self._align = "end"
        return self
    
    def add_child(self, child: Union[Dict, Component]) -> 'StackBuilder':
        """Add child to stack"""
        self._children.append(child)
        return self
    
    def with_id(self, id: str) -> 'StackBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the stack component"""
        classes = [
            "bd-stack",
            f"bd-stack-{self._direction}",
            f"bd-gap-{self._spacing}",
        ]
        
        if self._direction == "vertical":
            classes.append("bd-flex")
            classes.append("bd-flex-col")
        else:
            classes.append("bd-flex")
            classes.append("bd-flex-row")
        
        if self._align == "center":
            classes.append("bd-items-center")
        elif self._align == "end":
            classes.append("bd-items-end")
        else:
            classes.append("bd-items-start")
        
        children = []
        for child in self._children:
            if isinstance(child, Component):
                children.append(child.to_dict())
            else:
                children.append(child)
        
        return Component(
            type="div",
            classes=classes,
            props={},
            children=children,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
