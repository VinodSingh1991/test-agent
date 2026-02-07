"""
Text Builder

Builder for creating simple text components with variants.
Single Responsibility: Build text with size, weight, color variants.
Outputs TypeScript-compatible ComponentTextProps.
"""

from typing import Dict, Any, Optional


class TextBuilder:
    """Builder for Text components with fluent interface"""
    
    def __init__(self, content: str):
        """Initialize TextBuilder"""
        self._props = {
            "type": "Text",
            "content": content
        }
        self._classes = []
    
    def size(self, size: str) -> 'TextBuilder':
        """Set size: xs, sm, md, lg, xl"""
        self._props["size"] = size
        return self
    
    def weight(self, weight: str) -> 'TextBuilder':
        """Set weight: normal, medium, semibold, bold"""
        self._props["weight"] = weight
        return self
    
    def color(self, color: str) -> 'TextBuilder':
        """Set text color"""
        self._props["color"] = color
        return self
    
    def align(self, align: str) -> 'TextBuilder':
        """Set alignment: left, center, right, justify"""
        self._props["align"] = align
        return self
    
    def truncate(self, truncate: bool = True) -> 'TextBuilder':
        """Enable text truncation"""
        self._props["truncate"] = truncate
        return self
    
    def max_lines(self, lines: int) -> 'TextBuilder':
        """Set max lines for clamping"""
        self._props["maxLines"] = lines
        return self
    
    def italic(self, italic: bool = True) -> 'TextBuilder':
        """Make text italic"""
        self._props["italic"] = italic
        return self
    
    def underline(self, underline: bool = True) -> 'TextBuilder':
        """Underline text"""
        self._props["underline"] = underline
        return self
    
    def extra_small(self) -> 'TextBuilder':
        """Set text size to extra small"""
        self._props["size"] = "xs"
        return self
    
    def small(self) -> 'TextBuilder':
        """Set text size to small"""
        self._props["size"] = "sm"
        return self
    
    def medium(self) -> 'TextBuilder':
        """Set text size to medium"""
        self._props["size"] = "md"
        return self
    
    def large(self) -> 'TextBuilder':
        """Set text size to large"""
        self._props["size"] = "lg"
        return self
    
    def extra_large(self) -> 'TextBuilder':
        """Set text size to extra large"""
        self._props["size"] = "xl"
        return self
    
    def bold(self) -> 'TextBuilder':
        """Set text weight to bold"""
        self._props["weight"] = "bold"
        return self
    
    def semibold(self) -> 'TextBuilder':
        """Set text weight to semibold"""
        self._props["weight"] = "semibold"
        return self
    
    def light(self) -> 'TextBuilder':
        """Set text weight to light"""
        self._props["weight"] = "light"
        return self
    
    def primary_color(self) -> 'TextBuilder':
        """Set text color to primary"""
        self._props["color"] = "brand"
        return self
    
    def muted_color(self) -> 'TextBuilder':
        """Set text color to muted"""
        self._props["color"] = "gray"
        return self
    
    def success_color(self) -> 'TextBuilder':
        """Set text color to success"""
        self._props["color"] = "success"
        return self
    
    def danger_color(self) -> 'TextBuilder':
        """Set text color to error"""
        self._props["color"] = "error"
        return self
    
    def with_id(self, id: str) -> 'TextBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'TextBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the text component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
