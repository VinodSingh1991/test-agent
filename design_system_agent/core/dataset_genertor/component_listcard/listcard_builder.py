"""
List Card Builder

Builder for creating card components with list items.
Single Responsibility: Build cards containing lists of items (contacts, tasks, etc).
Outputs TypeScript-compatible ComponentListCardProps.
"""

from typing import Dict, Any, Optional, List


class ListCardBuilder:
    """Builder for List Card components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize ListCardBuilder
        
        Args:
            title: Card title
        """
        self._type = "ListCard"
        self._title = title
        self._title_icon = ""
        self._items = []
        self._description = ""
        self._additional_info = ""
        self._props = {
            "variant": "elevated",
            "hoverable": False
        }
        self._events = {}
        self._classes = []
    
    def items(self, items: List[Dict[str, Any]]) -> 'ListCardBuilder':
        """
        Set list items
        Each item: {id, title, subtitle?, avatar?, badge?, icon?}
        """
        self._items = items
        return self
    
    def add_item(self, title: str, subtitle: Optional[str] = None, 
                 avatar: Optional[str] = None, badge: Optional[str] = None,
                 icon: Optional[str] = None) -> 'ListCardBuilder':
        """
        Add list item
        
        Args:
            title: Item title/primary text
            subtitle: Item subtitle/secondary text
            avatar: Avatar (initials or image URL)
            badge: Badge text
            icon: Icon name
        """
        item = {
            "id": f"item-{len(self._props['items'])}",
            "title": title
        }
        if subtitle:
            item["subtitle"] = subtitle
        if avatar:
            item["avatar"] = avatar
        if badge:
            item["badge"] = badge
        if icon:
            item["icon"] = icon
        
        self._items.append(item)
        return self
    
    def description(self, description: str) -> 'ListCardBuilder':
        """Set card description"""
        self._description = description
        return self
    
    def action(self, label: str, on_click: Optional[str] = None) -> 'ListCardBuilder':
        """
        Add action button
        
        Args:
            label: Action label
            on_click: onClick callback identifier
        """
        if on_click:
            self._events["onAction"] = on_click
        self._additional_info = label
        return self
    
    def with_action(self, label: str) -> 'ListCardBuilder':
        """Add action button (alias)"""
        return self.action(label)
    
    def icon(self, icon: str) -> 'ListCardBuilder':
        """Set title icon"""
        self._title_icon = icon
        return self
    
    def with_icon(self, icon: str) -> 'ListCardBuilder':
        """Set title icon (alias)"""
        return self.icon(icon)
    
    def variant(self, variant: str) -> 'ListCardBuilder':
        """Set variant: elevated, outlined, filled"""
        self._props["variant"] = variant
        return self
    
    def hoverable(self, hoverable: bool = True) -> 'ListCardBuilder':
        """Enable hover effect"""
        self._props["hoverable"] = hoverable
        return self
    
    def max_items(self, max: int) -> 'ListCardBuilder':
        """Set maximum items to display"""
        self._props["maxItems"] = max
        return self
    
    def with_id(self, id: str) -> 'ListCardBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'ListCardBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'ListCardBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_item_click(self, handler: str) -> 'ListCardBuilder':
        """Set item click event handler"""
        self._events["onItemClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """
        Build the list card component
        
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
                "title": self._title,
                "items": self._items,
                "description": self._description,
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
