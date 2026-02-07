"""
Link Builder

Builder for creating hyperlink components.
Single Responsibility: Build clickable links with variants.
Outputs TypeScript-compatible ComponentLinkProps.
"""

from typing import Dict, Any, Optional


class LinkBuilder:
    """Builder for Link components with fluent interface"""
    
    def __init__(self, text: str, href: str = "#"):
        """
        Initialize LinkBuilder
        
        Args:
            text: Link text content
            href: Link URL
        """
        self._props = {
            "type": "Link",
            "href": href,
            "text": text,
            "external": False,
            "variant": "default",
            "color": "brand",
            "size": "md",
            "disabled": False
        }
        self._classes = []
    
    def href(self, url: str) -> 'LinkBuilder':
        """Set link URL"""
        self._props["href"] = url
        return self
    
    def variant(self, variant: str) -> 'LinkBuilder':
        """Set variant: default, button"""
        self._props["variant"] = variant
        return self
    
    def as_button(self) -> 'LinkBuilder':
        """Style link as button"""
        return self.variant("button")
    
    def color(self, color: str) -> 'LinkBuilder':
        """Set color: brand, muted, inherit"""
        self._props["color"] = color
        return self
    
    def primary(self) -> 'LinkBuilder':
        """Set color to brand (alias)"""
        return self.color("brand")
    
    def muted(self) -> 'LinkBuilder':
        return self.color("muted")
    
    def inherit_color(self) -> 'LinkBuilder':
        """Inherit color from parent"""
        return self.color("inherit")
    
    def size(self, size: str) -> 'LinkBuilder':
        """Set size: sm, md, lg"""
        self._props["size"] = size
        return self
    
    def small(self) -> 'LinkBuilder':
        return self.size("sm")
    
    def medium(self) -> 'LinkBuilder':
        return self.size("md")
    
    def large(self) -> 'LinkBuilder':
        return self.size("lg")
    
    def external(self, is_external: bool = True) -> 'LinkBuilder':
        """Mark as external link"""
        self._props["external"] = is_external
        if is_external:
            self._props["target"] = "_blank"
            self._props["rel"] = "noopener noreferrer"
        return self
    
    def target(self, target: str) -> 'LinkBuilder':
        """Set target: _blank, _self, _parent, _top"""
        self._props["target"] = target
        return self
    
    def rel(self, rel: str) -> 'LinkBuilder':
        """Set rel attribute"""
        self._props["rel"] = rel
        return self
    
    def disabled(self, disabled: bool = True) -> 'LinkBuilder':
        """Set disabled state"""
        self._props["disabled"] = disabled
        return self
    
    def left_icon(self, icon: str) -> 'LinkBuilder':
        """Set left icon"""
        self._props["leftIcon"] = icon
        return self
    
    def right_icon(self, icon: str) -> 'LinkBuilder':
        """Set right icon"""
        self._props["rightIcon"] = icon
        return self
    
    def with_icon(self, icon: str) -> 'LinkBuilder':
        """Add icon to link (left side)"""
        return self.left_icon(icon)
    
    def no_underline(self) -> 'LinkBuilder':
        """Remove underline (using className)"""
        self._classes.append("no-underline")
        return self
    
    def with_id(self, id: str) -> 'LinkBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'LinkBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the link component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
