"""
Button Builder

Builder for creating button components with fluent API.
Single Responsibility: Build button components with common variants.
Outputs TypeScript-compatible ComponentButtonProps.
"""

from typing import Dict, Any, Optional


class ButtonBuilder:
    """Builder for Button components with fluent interface"""
    
    def __init__(self, label: str):
        """
        Initialize ButtonBuilder
        
        Args:
            label: Button text content
        """
        self._type = "Button"
        self._text = label
        self._icon = ""
        self._props = {
            "type": "button",
            "disabled": False
        }
        self._events = {}
        self._classes = []
    
    def variant(self, variant: str) -> 'ButtonBuilder':
        """Set variant: solid, outline, ghost, link"""
        self._props["variant"] = variant
        return self
    
    def solid(self) -> 'ButtonBuilder':
        return self.variant("solid")
    
    def outline(self) -> 'ButtonBuilder':
        return self.variant("outline")
    
    def ghost(self) -> 'ButtonBuilder':
        return self.variant("ghost")
    
    def link(self) -> 'ButtonBuilder':
        return self.variant("link")
    
    def color(self, color: str) -> 'ButtonBuilder':
        """Set color: brand, success, error, warning, neutral"""
        self._props["color"] = color
        return self
    
    def primary(self) -> 'ButtonBuilder':
        """Set color to brand (alias)"""
        return self.color("brand")
    
    def success(self) -> 'ButtonBuilder':
        return self.color("success")
    
    def danger(self) -> 'ButtonBuilder':
        """Set color to error (alias for danger)"""
        return self.color("error")
    
    def error(self) -> 'ButtonBuilder':
        return self.color("error")
    
    def warning(self) -> 'ButtonBuilder':
        return self.color("warning")
    
    def neutral(self) -> 'ButtonBuilder':
        return self.color("neutral")
    
    def secondary(self) -> 'ButtonBuilder':
        """Set to outline variant with neutral color"""
        return self.outline().neutral()
    
    def size(self, size: str) -> 'ButtonBuilder':
        """Set size: sm, md, lg, xl"""
        self._props["size"] = size
        return self
    
    def small(self) -> 'ButtonBuilder':
        return self.size("sm")
    
    def medium(self) -> 'ButtonBuilder':
        return self.size("md")
    
    def large(self) -> 'ButtonBuilder':
        return self.size("lg")
    
    def extra_large(self) -> 'ButtonBuilder':
        return self.size("xl")
    
    def disabled(self, disabled: bool = True) -> 'ButtonBuilder':
        """Set disabled state"""
        self._props["disabled"] = disabled
        return self
    
    def loading(self, loading: bool = True) -> 'ButtonBuilder':
        """Set loading state"""
        self._props["loading"] = loading
        return self
    
    def full_width(self, full: bool = True) -> 'ButtonBuilder':
        """Set full width"""
        self._props["fullWidth"] = full
        return self
    
    def left_icon(self, icon: str) -> 'ButtonBuilder':
        """Set left icon"""
        self._props["leftIcon"] = icon
        return self
    
    def right_icon(self, icon: str) -> 'ButtonBuilder':
        """Set right icon"""
        self._props["rightIcon"] = icon
        return self
    
    def with_icon(self, icon: str) -> 'ButtonBuilder':
        """Add icon to button (left side)"""
        return self.left_icon(icon)
    
    def icon_only(self, icon: str) -> 'ButtonBuilder':
        """Make button icon-only"""
        self._props["iconOnly"] = True
        self._props["leftIcon"] = icon
        return self
    
    def on_click(self, handler: str) -> 'ButtonBuilder':
        """Add click event handler"""
        self._props["onClick"] = handler
        return self
    
    def button_type(self, btn_type: str) -> 'ButtonBuilder':
        """Set button type: button, submit, reset"""
        self._props["buttonType"] = btn_type
        return self
    
    def as_submit(self) -> 'ButtonBuilder':
        """Set button type to submit"""
        return self.button_type("submit")
    
    def as_reset(self) -> 'ButtonBuilder':
        """Set button type to reset"""
        return self.button_type("reset")
    
    def with_id(self, id: str) -> 'ButtonBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'ButtonBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def with_icon(self, icon: str) -> 'ButtonBuilder':
        """Set icon"""
        self._icon = icon
        return self
    
    def on_click(self, handler: str) -> 'ButtonBuilder':
        """Set onClick event handler"""
        self._events["onClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the button component"""
        result = {
            "type": self._type,
            "props": self._props.copy(),
            "value": {
                "icon": self._icon,
                "text": self._text
            }
        }
        
        if self._classes:
            result["props"]["className"] = " ".join(self._classes)
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
