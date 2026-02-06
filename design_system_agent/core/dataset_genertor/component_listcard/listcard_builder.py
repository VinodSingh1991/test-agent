"""
List Card Builder

Builder for creating card components with list items.
Single Responsibility: Build cards containing lists of items (contacts, tasks, etc).
"""

from typing import Dict, Any, Optional, List
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ListCardBuilder:
    """Builder for List Card components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize ListCardBuilder
        
        Args:
            title: Card title
        """
        self._title = title
        self._items: List[Dict[str, Any]] = []
        self._avatar_items = False
        self._action_label: Optional[str] = None
        self._icon: Optional[str] = None
        self._id: Optional[str] = None
    
    def add_item(self, primary: str, secondary: Optional[str] = None, 
                 avatar: Optional[str] = None, badge: Optional[str] = None) -> 'ListCardBuilder':
        """
        Add list item
        
        Args:
            primary: Primary text
            secondary: Secondary text (subtitle)
            avatar: Avatar (initials or image URL)
            badge: Badge text
        """
        self._items.append({
            "primary": primary,
            "secondary": secondary,
            "avatar": avatar,
            "badge": badge
        })
        if avatar:
            self._avatar_items = True
        return self
    
    def with_action(self, label: str) -> 'ListCardBuilder':
        """
        Add action button
        
        Args:
            label: Action label
        """
        self._action_label = label
        return self
    
    def with_icon(self, icon: str) -> 'ListCardBuilder':
        """
        Add icon to title
        
        Args:
            icon: Icon class name
        """
        self._icon = icon
        return self
    
    def with_id(self, id: str) -> 'ListCardBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the list card component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-list-card",
            "bd-card"
        ]
        
        children = []
        
        # Header
        header_children = []
        
        # Title
        title_children = []
        if self._icon:
            title_children.append({
                "type": "i",
                "classes": [self._icon, "bd-mr-8"]
            })
        title_children.append(self._title)
        
        header_children.append({
            "type": "h3",
            "classes": ["bd-card-title", "bd-fs-lg", "bd-fw-semibold"],
            "children": title_children
        })
        
        if self._action_label:
            header_children.append({
                "type": "button",
                "classes": ["bd-btn", "bd-btn-sm", "bd-btn-primary"],
                "children": self._action_label
            })
        
        children.append({
            "type": "div",
            "classes": ["bd-card-header", "bd-p-16", "bd-flex", "bd-justify-between", "bd-items-center"],
            "children": header_children
        })
        
        # List items
        list_items = []
        for item in self._items:
            item_children = []
            
            # Avatar (if present)
            if item.get("avatar"):
                avatar_content = item["avatar"]
                is_image = avatar_content.startswith("http") or avatar_content.endswith((".jpg", ".png", ".svg"))
                
                if is_image:
                    item_children.append({
                        "type": "img",
                        "classes": ["bd-avatar", "bd-avatar-sm", "bd-avatar-circle"],
                        "props": {"src": avatar_content, "alt": item["primary"]}
                    })
                else:
                    item_children.append({
                        "type": "div",
                        "classes": ["bd-avatar", "bd-avatar-sm", "bd-avatar-circle", "bd-avatar-primary"],
                        "children": {
                            "type": "span",
                            "classes": ["bd-avatar-initials"],
                            "children": avatar_content[:2].upper()
                        }
                    })
            
            # Text content
            text_children = [
                {
                    "type": "div",
                    "classes": ["bd-list-item-primary", "bd-fw-medium"],
                    "children": item["primary"]
                }
            ]
            
            if item.get("secondary"):
                text_children.append({
                    "type": "div",
                    "classes": ["bd-list-item-secondary", "bd-text-sm", "bd-text-muted"],
                    "children": item["secondary"]
                })
            
            item_children.append({
                "type": "div",
                "classes": ["bd-list-item-text", "bd-flex-1"],
                "children": text_children
            })
            
            # Badge (if present)
            if item.get("badge"):
                item_children.append({
                    "type": "span",
                    "classes": ["bd-badge", "bd-badge-primary", "bd-badge-sm"],
                    "children": item["badge"]
                })
            
            list_items.append({
                "type": "div",
                "classes": ["bd-list-item", "bd-p-12", "bd-flex", "bd-items-center", "bd-gap-12", "bd-border-b"],
                "children": item_children
            })
        
        children.append({
            "type": "div",
            "classes": ["bd-card-body", "bd-p-0"],
            "children": list_items
        })
        
        return Component(
            type="ListCard",
            classes=classes,
            props={},
            children=children,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
