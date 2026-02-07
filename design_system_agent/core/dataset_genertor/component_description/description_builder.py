"""
Description Builder

Builder for creating description/paragraph components with fluent API.
Single Responsibility: Build paragraph/description text components.
Outputs TypeScript-compatible ComponentDescriptionProps.
"""

from typing import Dict, Any, Optional


class DescriptionBuilder:
    """Builder for Description/Paragraph components with fluent interface"""
    
    def __init__(self, text: str):
        """
        Initialize DescriptionBuilder
        
        Args:
            text: Description text content
        """
        self._type = "Text"
        self._text = text
        self._icon = ""
        self._props = {}
        self._events = {}
        self._classes = []
    
    def size(self, size: str) -> 'DescriptionBuilder':
        """Set size: xs, sm, md, lg"""
        self._props["size"] = size
        return self
    
    def weight(self, weight: str) -> 'DescriptionBuilder':
        """Set weight: normal, medium, semibold"""
        self._props["weight"] = weight
        return self
    
    def color(self, color: str) -> 'DescriptionBuilder':
        """Set text color"""
        self._props["color"] = color
        return self
    
    def align(self, align: str) -> 'DescriptionBuilder':
        """Set alignment: left, center, right"""
        self._props["align"] = align
        return self
    
    def max_lines(self, lines: int) -> 'DescriptionBuilder':
        """Set max lines for clamping"""
        self._props["maxLines"] = lines
        return self
    
    def muted(self) -> 'DescriptionBuilder':
        """Make text muted/gray"""
        self._props["color"] = "gray"
        return self
    
    def small(self) -> 'DescriptionBuilder':
        """Make text small"""
        self._props["size"] = "sm"
        return self
    
    def large(self) -> 'DescriptionBuilder':
        """Make text large"""
        self._props["size"] = "lg"
        return self
    
    def bold(self) -> 'DescriptionBuilder':
        """Make text bold"""
        self._props["weight"] = "semibold"
        return self
    
    def italic(self, italic: bool = True) -> 'DescriptionBuilder':
        """Make text italic"""
        self._props["italic"] = italic
        return self
    
    def center(self) -> 'DescriptionBuilder':
        """Center align text"""
        self._props["align"] = "center"
        return self
    
    def with_classes(self, *classes: str) -> 'DescriptionBuilder':
        """
        Add custom CSS classes
        
        Args:\n            *classes: CSS class names
        """
        self._classes.extend(classes)
        return self
    
    def with_id(self, desc_id: str) -> 'DescriptionBuilder':
        """
        Set description ID
        
        Args:
            desc_id: Description identifier
        """
        self._props["id"] = desc_id
        return self
    
    def build(self) -> Dict[str, Any]:
        """
        Build and return the Description component
        
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
