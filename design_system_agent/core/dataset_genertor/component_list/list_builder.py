"""
List Builder

Builder for creating list components with fluent API.
Single Responsibility: Build ordered/unordered list components.
Outputs TypeScript-compatible ComponentListProps.
"""

from typing import Dict, Any, List, Optional


class ListBuilder:
    """Builder for List components with fluent interface"""
    
    def __init__(self, *items: str):
        """
        Initialize ListBuilder
        
        Args:
            *items: List items as strings or dicts
        """
        self._type = "List"
        self._items = [{"id": f"item-{i}", "content": item} for i, item in enumerate(items)]
        self._additional_info = ""
        self._props = {
            "ordered": False,
            "variant": "plain",
            "spacing": "normal",
            "marker": "disc"
        }
        self._events = {}
        self._classes = []
    
    def items(self, items: List[Dict[str, Any]]) -> 'ListBuilder':
        """
        Set list items
        Each item: {id, content, icon?, avatar?}
        """
        self._items = items
        return self
    
    def ordered(self, ordered: bool = True) -> 'ListBuilder':
        """Make this an ordered list"""
        self._props["ordered"] = ordered
        if ordered:
            self._props["marker"] = "decimal"
        return self
    
    def unordered(self) -> 'ListBuilder':
        """Make this an unordered list"""
        self._props["ordered"] = False
        self._props["marker"] = "disc"
        return self
    
    def variant(self, variant: str) -> 'ListBuilder':
        """Set variant: plain, bordered, divided"""
        self._props["variant"] = variant
        return self
    
    def spacing(self, spacing: str) -> 'ListBuilder':
        """Set spacing: compact, normal, relaxed"""
        self._props["spacing"] = spacing
        return self
    
    def marker(self, marker: str) -> 'ListBuilder':
        """Set marker: disc, circle, square, decimal, none"""
        self._props["marker"] = marker
        return self
    
    def add_item(self, content: str, icon: Optional[str] = None, avatar: Optional[str] = None) -> 'ListBuilder':
        """
        Add an item to the list
        
        Args:
            content: List item text
            icon: Optional icon
            avatar: Optional avatar
        """
        item = {"id": f"item-{len(self._items)}", "content": content}
        if icon:
            item["icon"] = icon
        if avatar:
            item["avatar"] = avatar
        self._items.append(item)
        return self
    
    def add_items(self, *items: str) -> 'ListBuilder':
        """
        Add multiple items to the list
        
        Args:
            *items: List item texts
        """
        for item in items:
            self.add_item(item)
        return self
    
    def with_disc(self) -> 'ListBuilder':
        """Use disc bullets"""
        self._props["marker"] = "disc"
        return self
    
    def with_circle(self) -> 'ListBuilder':
        """Use circle bullets"""
        self._props["marker"] = "circle"
        return self
    
    def with_decimal(self) -> 'ListBuilder':
        """Use decimal numbers"""
        self._props["marker"] = "decimal"
        self._props["ordered"] = True
        return self
    
    def with_id(self, list_id: str) -> 'ListBuilder':
        """
        Set list ID
        
        Args:
            list_id: List identifier
        """
        self._props["id"] = list_id
        return self
    
    def with_classes(self, *classes: str) -> 'ListBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'ListBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_item_click(self, handler: str) -> 'ListBuilder':
        """Set item click event handler"""
        self._events["onItemClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """
        Build and return the List component
        
        Returns:
            Dictionary representation
        """
        props = self._props.copy()
        if self._classes:
            props["className"] = " ".join(self._classes)
        
        result = {
            "type": self._type,
            "props": props,
            "value": {
                "items": self._items,
                "additionalInfo": self._additional_info
            }
        }
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build()
