"""
Heading Builder

Builder for creating heading components with fluent API.
Single Responsibility: Build heading components (h1-h6).
Outputs TypeScript-compatible ComponentHeadingProps.
"""

from typing import Dict, Any, Optional


class HeadingBuilder:
    """Builder for Heading components with fluent interface"""
    
    def __init__(self, text: str, level: int = 2):
        """
        Initialize HeadingBuilder
        
        Args:
            text: Heading text content
            level: Heading level (1-6), defaults to 2 (h2)
        """
        self._type = "Heading"
        self._text = text
        self._icon = ""
        self._props = {
            "level": max(1, min(6, level))
        }
        self._events = {}
        self._classes = []
    
    def h1(self) -> 'HeadingBuilder':
        """Set heading level to h1"""
        self._props["level"] = 1
        return self
    
    def with_icon(self, icon: str) -> 'HeadingBuilder':
        """Set icon"""
        self._icon = icon
        return self
    
    def h2(self) -> 'HeadingBuilder':
        """Set heading level to h2"""
        self._props["level"] = 2
        return self
    
    def h3(self) -> 'HeadingBuilder':
        """Set heading level to h3"""
        self._props["level"] = 3
        return self
    
    def h4(self) -> 'HeadingBuilder':
        """Set heading level to h4"""
        self._props["level"] = 4
        return self
    
    def h5(self) -> 'HeadingBuilder':
        """Set heading level to h5"""
        self._props["level"] = 5
        return self
    
    def h6(self) -> 'HeadingBuilder':
        """Set heading level to h6"""
        self._props["level"] = 6
        return self
    
    def size(self, size: str) -> 'HeadingBuilder':
        """Set size: xs, sm, md, lg, xl, 2xl, 3xl"""
        self._props["size"] = size
        return self
    
    def weight(self, weight: str) -> 'HeadingBuilder':
        """Set weight: normal, medium, semibold, bold"""
        self._props["weight"] = weight
        return self
    
    def bold(self) -> 'HeadingBuilder':
        """Make heading bold"""
        self._props["weight"] = "bold"
        return self
    
    def color(self, color: str) -> 'HeadingBuilder':
        """Set text color"""
        self._props["color"] = color
        return self
    
    def align(self, align: str) -> 'HeadingBuilder':
        """Set alignment: left, center, right"""
        self._props["align"] = align
        return self
    
    def truncate(self, truncate: bool = True) -> 'HeadingBuilder':
        """Enable text truncation"""
        self._props["truncate"] = truncate
        return self
    
    def large(self) -> 'HeadingBuilder':
        """Set large font size"""
        self._props["size"] = "2xl"
        return self
    
    def extra_large(self) -> 'HeadingBuilder':
        """Set extra large font size"""
        self._props["size"] = "3xl"
        return self
    
    def small(self) -> 'HeadingBuilder':
        """Set small font size"""
        self._props["size"] = "md"
        return self
    
    def with_classes(self, *classes: str) -> 'HeadingBuilder':
        """
        Add custom CSS classes
        
        Args:
            *classes: CSS class names
        """
        self._classes.extend(classes)
        return self
    
    def with_id(self, heading_id: str) -> 'HeadingBuilder':
        """
        Set heading ID
        
        Args:
            heading_id: Heading identifier
        """
        self._props["id"] = heading_id
        return self
    
    def build(self) -> Dict[str, Any]:
        """
        Build and return the Heading component
        
        Returns:
            Dictionary representation
        """
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
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build()
