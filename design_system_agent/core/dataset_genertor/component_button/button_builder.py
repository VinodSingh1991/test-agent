"""
Button Builder

Builder for creating button components with fluent API.
Single Responsibility: Build button components with common variants.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ButtonBuilder:
    """Builder for Button components with fluent interface"""
    
    def __init__(self, text: str):
        """
        Initialize ButtonBuilder
        
        Args:
            text: Button text content
        """
        self._text = text
        self._variant = "primary"
        self._size = "md"
        self._type = "button"
        self._disabled = False
        self._full_width = False
        self._icon: Optional[str] = None
        self._on_click: Optional[str] = None
        self._id: Optional[str] = None
    
    def primary(self) -> 'ButtonBuilder':
        """Set button variant to primary"""
        self._variant = "primary"
        return self
    
    def secondary(self) -> 'ButtonBuilder':
        """Set button variant to secondary"""
        self._variant = "secondary"
        return self
    
    def success(self) -> 'ButtonBuilder':
        """Set button variant to success"""
        self._variant = "success"
        return self
    
    def danger(self) -> 'ButtonBuilder':
        """Set button variant to danger"""
        self._variant = "danger"
        return self
    
    def warning(self) -> 'ButtonBuilder':
        """Set button variant to warning"""
        self._variant = "warning"
        return self
    
    def small(self) -> 'ButtonBuilder':
        """Set button size to small"""
        self._size = "sm"
        return self
    
    def medium(self) -> 'ButtonBuilder':
        """Set button size to medium"""
        self._size = "md"
        return self
    
    def large(self) -> 'ButtonBuilder':
        """Set button size to lg"""
        self._size = "lg"
        return self
    
    def as_submit(self) -> 'ButtonBuilder':
        """Set button type to submit"""
        self._type = "submit"
        return self
    
    def as_reset(self) -> 'ButtonBuilder':
        """Set button type to reset"""
        self._type = "reset"
        return self
    
    def disabled(self, disabled: bool = True) -> 'ButtonBuilder':
        """
        Set disabled state
        
        Args:
            disabled: Whether button is disabled
        """
        self._disabled = disabled
        return self
    
    def full_width(self, full: bool = True) -> 'ButtonBuilder':
        """
        Set full width
        
        Args:
            full: Whether button should be full width
        """
        self._full_width = full
        return self
    
    def with_icon(self, icon: str) -> 'ButtonBuilder':
        """
        Add icon to button
        
        Args:
            icon: Icon name or class
        """
        self._icon = icon
        return self
    
    def on_click(self, handler: str) -> 'ButtonBuilder':
        """
        Add click event handler
        
        Args:
            handler: Click handler function name
        """
        self._on_click = handler
        return self
    
    def with_id(self, button_id: str) -> 'ButtonBuilder':
        """
        Set button ID
        
        Args:
            button_id: Button identifier
        """
        self._id = button_id
        return self
    
    def build(self) -> Component:
        """
        Build and return the Button component
        
        Returns:
            Component instance
        """
        classes = ["bd-btn", f"bd-btn-{self._variant}"]
        
        if self._size != "md":
            classes.append(f"bd-btn-{self._size}")
        
        if self._full_width:
            classes.append("bd-w-full")
        
        props = {
            "type": self._type,
            "disabled": self._disabled
        }
        
        events = {}
        if self._on_click:
            events["onClick"] = self._on_click
        
        children = self._text
        if self._icon:
            children = {
                "type": "span",
                "classes": ["bd-flex", "bd-items-center", "bd-gap-8"],
                "children": [
                    {"type": "i", "classes": [self._icon]},
                    {"type": "span", "children": self._text}
                ]
            }
        
        return Component(
            type="button",
            classes=classes,
            props=props,
            children=children,
            events=events if events else None,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
