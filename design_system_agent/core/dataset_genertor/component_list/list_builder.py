"""
List Builder

Builder for creating list components with fluent API.
Single Responsibility: Build ordered/unordered list components.
"""

from typing import Dict, Any, List, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ListBuilder:
    """Builder for List components with fluent interface"""
    
    def __init__(self, *items: str):
        """
        Initialize ListBuilder
        
        Args:
            *items: List items as strings
        """
        self._items = list(items)
        self._ordered = False
        self._classes = []
        self._id: Optional[str] = None
    
    def ordered(self) -> 'ListBuilder':
        """Make this an ordered list (ol)"""
        self._ordered = True
        return self
    
    def unordered(self) -> 'ListBuilder':
        """Make this an unordered list (ul)"""
        self._ordered = False
        return self
    
    def add_item(self, item: str) -> 'ListBuilder':
        """
        Add an item to the list
        
        Args:
            item: List item text
        """
        self._items.append(item)
        return self
    
    def add_items(self, *items: str) -> 'ListBuilder':
        """
        Add multiple items to the list
        
        Args:
            *items: List item texts
        """
        self._items.extend(items)
        return self
    
    def with_disc(self) -> 'ListBuilder':
        """Use disc bullets (for unordered lists)"""
        if "bd-list-disc" not in self._classes:
            self._classes.append("bd-list-disc")
        return self
    
    def with_circle(self) -> 'ListBuilder':
        """Use circle bullets (for unordered lists)"""
        if "bd-list-circle" not in self._classes:
            self._classes.append("bd-list-circle")
        return self
    
    def with_decimal(self) -> 'ListBuilder':
        """Use decimal numbers (for ordered lists)"""
        if "bd-list-decimal" not in self._classes:
            self._classes.append("bd-list-decimal")
        return self
    
    def with_padding(self) -> 'ListBuilder':
        """Add left padding"""
        if "bd-pl-24" not in self._classes:
            self._classes.append("bd-pl-24")
        return self
    
    def with_classes(self, *classes: str) -> 'ListBuilder':
        """
        Add custom CSS classes
        
        Args:
            *classes: CSS class names
        """
        self._classes.extend(classes)
        return self
    
    def with_id(self, list_id: str) -> 'ListBuilder':
        """
        Set list ID
        
        Args:
            list_id: List identifier
        """
        self._id = list_id
        return self
    
    def build(self) -> Component:
        """
        Build and return the List component
        
        Returns:
            Component instance
        """
        list_type = "ol" if self._ordered else "ul"
        
        # Default classes
        default_classes = ["bd-list-disc", "bd-pl-24"] if not self._ordered else ["bd-list-decimal", "bd-pl-24"]
        
        # Use custom classes if provided, otherwise use defaults
        classes = self._classes.copy() if self._classes else default_classes
        
        # Create list items
        list_items = [
            {"type": "li", "children": item}
            for item in self._items
        ]
        
        return Component(
            type=list_type,
            classes=classes,
            props={},
            children=list_items,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
