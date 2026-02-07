"""
Stack Builder

Builder for creating stack layout components (vertical/horizontal).
Single Responsibility: Build stacked layouts with spacing.
Outputs TypeScript-compatible ComponentStackProps.
"""

from typing import Dict, Any, Optional, List, Union


class StackBuilder:
    """Builder for Stack layout components with fluent interface"""
    
    def __init__(self):
        """Initialize StackBuilder"""
        self._props = {
            "type": "Stack",
            "direction": "vertical",
            "spacing": "md",
            "align": "start",
            "wrap": False,
            "children": []
        }
        self._classes = []
    
    def vertical(self) -> 'StackBuilder':
        """Set stack direction to vertical"""
        self._props["direction"] = "vertical"
        return self
    
    def horizontal(self) -> 'StackBuilder':
        """Set stack direction to horizontal"""
        self._props["direction"] = "horizontal"
        return self
    
    def spacing(self, spacing: str) -> 'StackBuilder':
        """Set spacing: none, xs, sm, md, lg, xl, 2xl"""
        self._props["spacing"] = spacing
        return self
    
    def small_spacing(self) -> 'StackBuilder':
        """Set small spacing"""
        self._props["spacing"] = "sm"
        return self
    
    def medium_spacing(self) -> 'StackBuilder':
        """Set medium spacing"""
        self._props["spacing"] = "md"
        return self
    
    def large_spacing(self) -> 'StackBuilder':
        """Set large spacing"""
        self._props["spacing"] = "lg"
        return self
    
    def align(self, align: str) -> 'StackBuilder':
        """Set align: start, center, end, stretch"""
        self._props["align"] = align
        return self
    
    def align_start(self) -> 'StackBuilder':
        """Align items to start"""
        self._props["align"] = "start"
        return self
    
    def align_center(self) -> 'StackBuilder':
        """Align items to center"""
        self._props["align"] = "center"
        return self
    
    def align_end(self) -> 'StackBuilder':
        """Align items to end"""
        self._props["align"] = "end"
        return self
    
    def justify(self, justify: str) -> 'StackBuilder':
        """Set justify: start, center, end, between, around"""
        self._props["justify"] = justify
        return self
    
    def wrap(self, wrap: bool = True) -> 'StackBuilder':
        """Enable wrapping"""
        self._props["wrap"] = wrap
        return self
    
    def full_width(self, full: bool = True) -> 'StackBuilder':
        """Make stack full width"""
        self._props["fullWidth"] = full
        return self
    
    def add_child(self, child: Union[Dict, Any]) -> 'StackBuilder':
        """Add child to stack"""
        self._props["children"].append(child)
        return self
    
    def children(self, children: List[Union[Dict, Any]]) -> 'StackBuilder':
        """Set all children at once"""
        self._props["children"] = children
        return self
    
    def with_id(self, id: str) -> 'StackBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'StackBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the stack component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
