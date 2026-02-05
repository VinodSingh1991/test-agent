"""
Dashlet Builder

Builder for creating dashboard widget components.
Single Responsibility: Build small dashboard widgets with title, content, actions.
"""

from typing import Dict, Any, Optional, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class DashletBuilder:
    """Builder for Dashlet components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize DashletBuilder
        
        Args:
            title: Dashlet title
        """
        self._title = title
        self._content: List[Union[str, Dict, Component]] = []
        self._action_label: Optional[str] = None
        self._icon: Optional[str] = None
        self._variant = "default"
        self._loading = False
        self._id: Optional[str] = None
    
    def add_content(self, *content: Union[str, Dict, Component]) -> 'DashletBuilder':
        """
        Add content to dashlet
        
        Args:
            content: Content items
        """
        self._content.extend(content)
        return self
    
    def with_action(self, label: str) -> 'DashletBuilder':
        """
        Add action button/link
        
        Args:
            label: Action label
        """
        self._action_label = label
        return self
    
    def with_icon(self, icon: str) -> 'DashletBuilder':
        """
        Add icon to title
        
        Args:
            icon: Icon class name
        """
        self._icon = icon
        return self
    
    def primary(self) -> 'DashletBuilder':
        """Set dashlet variant to primary"""
        self._variant = "primary"
        return self
    
    def success(self) -> 'DashletBuilder':
        """Set dashlet variant to success"""
        self._variant = "success"
        return self
    
    def warning(self) -> 'DashletBuilder':
        """Set dashlet variant to warning"""
        self._variant = "warning"
        return self
    
    def loading(self) -> 'DashletBuilder':
        """Show loading state"""
        self._loading = True
        return self
    
    def with_id(self, id: str) -> 'DashletBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the dashlet component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-dashlet",
            "bd-card",
            "bd-p-16",
            f"bd-dashlet-{self._variant}"
        ]
        
        children = []
        
        # Header with title and action
        header_children = []
        
        # Title with optional icon
        title_children = []
        if self._icon:
            title_children.append({
                "type": "i",
                "classes": [self._icon, "bd-mr-8"]
            })
        title_children.append({
            "type": "span",
            "children": self._title
        })
        
        header_children.append({
            "type": "h4",
            "classes": ["bd-dashlet-title", "bd-fs-lg", "bd-fw-semibold"],
            "children": title_children
        })
        
        if self._action_label:
            header_children.append({
                "type": "a",
                "classes": ["bd-dashlet-action", "bd-text-primary", "bd-text-sm"],
                "props": {"href": "#"},
                "children": self._action_label
            })
        
        children.append({
            "type": "div",
            "classes": ["bd-dashlet-header", "bd-flex", "bd-justify-between", "bd-items-center", "bd-mb-12"],
            "children": header_children
        })
        
        # Content
        if self._loading:
            children.append({
                "type": "div",
                "classes": ["bd-dashlet-loading", "bd-text-center", "bd-py-32"],
                "children": {
                    "type": "span",
                    "classes": ["bd-spinner"],
                    "children": "Loading..."
                }
            })
        else:
            content_children = []
            for item in self._content:
                if isinstance(item, Component):
                    content_children.append(item.to_dict())
                elif isinstance(item, dict):
                    content_children.append(item)
                else:
                    content_children.append({"type": "p", "children": str(item)})
            
            children.append({
                "type": "div",
                "classes": ["bd-dashlet-content"],
                "children": content_children
            })
        
        return Component(
            type="div",
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
