"""
Badge Builder

Builder for creating badge/tag components with fluent API.
Single Responsibility: Build badge components for status, labels, counts.
Outputs TypeScript-compatible ComponentBadgeProps.
"""

from typing import Dict, Any, Optional


class BadgeBuilder:
    """Builder for Badge components with fluent interface"""
    
    def __init__(self, label: str):
        """
        Initialize BadgeBuilder
        \n        Args:
            label: Badge text content
        """
        self._type = "Badge"
        self._text = label
        self._icon = ""
        self._props = {}
        self._events = {}
        self._classes = []
    
    def variant(self, variant: str) -> 'BadgeBuilder':
        """Set variant: solid, outline, soft"""
        self._props["variant"] = variant
        return self
    
    def color(self, color: str) -> 'BadgeBuilder':
        """Set color: brand, success, error, warning, info, gray, neutral"""
        self._props["color"] = color
        return self
    
    def size(self, size: str) -> 'BadgeBuilder':
        """Set size: sm, md, lg"""
        self._props["size"] = size
        return self
    
    def rounded(self, rounded: bool = True) -> 'BadgeBuilder':
        """Make badge rounded (pill shape)"""
        self._props["rounded"] = rounded
        return self
    
    def dot(self, dot: bool = True) -> 'BadgeBuilder':
        """Show dot indicator"""
        self._props["dot"] = dot
        return self
    
    def pulse(self, pulse: bool = True) -> 'BadgeBuilder':
        """Enable pulse animation"""
        self._props["pulse"] = pulse
        return self
    
    def success(self) -> 'BadgeBuilder':
        return self.color("success")
    
    def error(self) -> 'BadgeBuilder':
        return self.color("error")
    
    def danger(self) -> 'BadgeBuilder':
        return self.color("error")
    
    def warning(self) -> 'BadgeBuilder':
        return self.color("warning")
    
    def info(self) -> 'BadgeBuilder':
        return self.color("info")
    
    def primary(self) -> 'BadgeBuilder':
        return self.color("brand")
    
    def pill_shape(self) -> 'BadgeBuilder':
        """Make badge pill-shaped (alias for rounded)"""
        return self.rounded(True)
    
    def small(self) -> 'BadgeBuilder':
        return self.size("sm")
    
    def medium(self) -> 'BadgeBuilder':
        return self.size("md")
    
    def large(self) -> 'BadgeBuilder':
        return self.size("lg")
    
    def with_id(self, id: str) -> 'BadgeBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'BadgeBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def with_icon(self, icon: str) -> 'BadgeBuilder':
        """Set icon"""
        self._icon = icon
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the badge component"""
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
