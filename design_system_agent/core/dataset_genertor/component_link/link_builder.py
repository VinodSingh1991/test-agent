"""
Link Builder

Builder for creating hyperlink components.
Single Responsibility: Build clickable links with variants.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class LinkBuilder:
    """Builder for Link components with fluent interface"""
    
    def __init__(self, text: str, href: str = "#"):
        """Initialize LinkBuilder"""
        self._text = text
        self._href = href
        self._variant = "default"
        self._underline = True
        self._external = False
        self._icon: Optional[str] = None
        self._id: Optional[str] = None
    
    def primary(self) -> 'LinkBuilder':
        """Set link color to primary"""
        self._variant = "primary"
        return self
    
    def secondary(self) -> 'LinkBuilder':
        """Set link color to secondary"""
        self._variant = "secondary"
        return self
    
    def muted(self) -> 'LinkBuilder':
        """Set link color to muted"""
        self._variant = "muted"
        return self
    
    def no_underline(self) -> 'LinkBuilder':
        """Remove underline"""
        self._underline = False
        return self
    
    def external(self) -> 'LinkBuilder':
        """Mark as external link"""
        self._external = True
        return self
    
    def with_icon(self, icon: str) -> 'LinkBuilder':
        """Add icon to link"""
        self._icon = icon
        return self
    
    def with_id(self, id: str) -> 'LinkBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the link component"""
        classes = ["bd-link", f"bd-link-{self._variant}"]
        
        if not self._underline:
            classes.append("bd-no-underline")
        
        props = {"href": self._href}
        
        if self._external:
            props["target"] = "_blank"
            props["rel"] = "noopener noreferrer"
        
        # Use value structure with icon and text
        icon_value = self._icon if self._icon else ""
        if self._external and not self._icon:
            icon_value = "external-link"
        
        value = {
            "icon": icon_value,
            "text": self._text
        }
        
        return Component(
            type="Link",
            classes=classes,
            props=props,
            value=value,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
