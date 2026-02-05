"""
Alert Builder

Builder for creating alert/banner components.
Single Responsibility: Build alert messages with variants and actions.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class AlertBuilder:
    """Builder for Alert components with fluent interface"""
    
    def __init__(self, message: str):
        """
        Initialize AlertBuilder
        
        Args:
            message: Alert message
        """
        self._message = message
        self._title: Optional[str] = None
        self._variant = "info"
        self._dismissible = False
        self._icon: Optional[str] = None
        self._action_label: Optional[str] = None
        self._id: Optional[str] = None
    
    def with_title(self, title: str) -> 'AlertBuilder':
        """
        Add title to alert
        
        Args:
            title: Alert title
        """
        self._title = title
        return self
    
    def info(self) -> 'AlertBuilder':
        """Set alert variant to info"""
        self._variant = "info"
        return self
    
    def success(self) -> 'AlertBuilder':
        """Set alert variant to success"""
        self._variant = "success"
        return self
    
    def warning(self) -> 'AlertBuilder':
        """Set alert variant to warning"""
        self._variant = "warning"
        return self
    
    def danger(self) -> 'AlertBuilder':
        """Set alert variant to danger"""
        self._variant = "danger"
        return self
    
    def dismissible(self) -> 'AlertBuilder':
        """Make alert dismissible"""
        self._dismissible = True
        return self
    
    def with_icon(self, icon: str) -> 'AlertBuilder':
        """
        Add icon to alert
        
        Args:
            icon: Icon class name or emoji
        """
        self._icon = icon
        return self
    
    def with_action(self, label: str) -> 'AlertBuilder':
        """
        Add action button
        
        Args:
            label: Action button label
        """
        self._action_label = label
        return self
    
    def with_id(self, id: str) -> 'AlertBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the alert component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-alert",
            f"bd-alert-{self._variant}",
            "bd-p-16",
            "bd-rounded"
        ]
        
        if self._dismissible:
            classes.append("bd-alert-dismissible")
        
        children = []
        
        # Main content wrapper
        content_children = []
        
        # Icon
        if self._icon:
            content_children.append({
                "type": "span",
                "classes": ["bd-alert-icon", "bd-mr-12"],
                "children": self._icon
            })
        
        # Text content
        text_children = []
        
        if self._title:
            text_children.append({
                "type": "h5",
                "classes": ["bd-alert-title", "bd-fw-semibold", "bd-mb-4"],
                "children": self._title
            })
        
        text_children.append({
            "type": "p",
            "classes": ["bd-alert-message"],
            "children": self._message
        })
        
        content_children.append({
            "type": "div",
            "classes": ["bd-alert-content", "bd-flex-1"],
            "children": text_children
        })
        
        children.append({
            "type": "div",
            "classes": ["bd-flex", "bd-items-start", "bd-gap-8"],
            "children": content_children
        })
        
        # Actions
        actions = []
        
        if self._action_label:
            actions.append({
                "type": "button",
                "classes": ["bd-btn", "bd-btn-sm", f"bd-btn-{self._variant}", "bd-mr-8"],
                "children": self._action_label
            })
        
        if self._dismissible:
            actions.append({
                "type": "button",
                "classes": ["bd-alert-close", "bd-btn-icon"],
                "props": {"aria-label": "Close"},
                "children": "×"
            })
        
        if actions:
            children.append({
                "type": "div",
                "classes": ["bd-alert-actions", "bd-flex", "bd-items-center", "bd-mt-12"],
                "children": actions
            })
        
        return Component(
            type="div",
            classes=classes,
            props={"role": "alert"},
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
