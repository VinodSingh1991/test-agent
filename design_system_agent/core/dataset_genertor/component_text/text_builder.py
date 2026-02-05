"""
Text Builder

Builder for creating simple text components with variants.
Single Responsibility: Build text with size, weight, color variants.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class TextBuilder:
    """Builder for Text components with fluent interface"""
    
    def __init__(self, content: str):
        """Initialize TextBuilder"""
        self._content = content
        self._size = "md"
        self._weight = "normal"
        self._color = "default"
        self._italic = False
        self._underline = False
        self._id: Optional[str] = None
    
    def extra_small(self) -> 'TextBuilder':
        """Set text size to extra small"""
        self._size = "xs"
        return self
    
    def small(self) -> 'TextBuilder':
        """Set text size to small"""
        self._size = "sm"
        return self
    
    def medium(self) -> 'TextBuilder':
        """Set text size to medium"""
        self._size = "md"
        return self
    
    def large(self) -> 'TextBuilder':
        """Set text size to large"""
        self._size = "lg"
        return self
    
    def extra_large(self) -> 'TextBuilder':
        """Set text size to extra large"""
        self._size = "xl"
        return self
    
    def bold(self) -> 'TextBuilder':
        """Set text weight to bold"""
        self._weight = "bold"
        return self
    
    def semibold(self) -> 'TextBuilder':
        """Set text weight to semibold"""
        self._weight = "semibold"
        return self
    
    def light(self) -> 'TextBuilder':
        """Set text weight to light"""
        self._weight = "light"
        return self
    
    def italic(self) -> 'TextBuilder':
        """Make text italic"""
        self._italic = True
        return self
    
    def underline(self) -> 'TextBuilder':
        """Underline text"""
        self._underline = True
        return self
    
    def primary_color(self) -> 'TextBuilder':
        """Set text color to primary"""
        self._color = "primary"
        return self
    
    def muted_color(self) -> 'TextBuilder':
        """Set text color to muted"""
        self._color = "muted"
        return self
    
    def success_color(self) -> 'TextBuilder':
        """Set text color to success"""
        self._color = "success"
        return self
    
    def danger_color(self) -> 'TextBuilder':
        """Set text color to danger"""
        self._color = "danger"
        return self
    
    def with_id(self, id: str) -> 'TextBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the text component"""
        classes = [
            f"bd-text-{self._size}",
            f"bd-fw-{self._weight}",
        ]
        
        if self._color != "default":
            classes.append(f"bd-text-{self._color}")
        
        if self._italic:
            classes.append("bd-italic")
        
        if self._underline:
            classes.append("bd-underline")
        
        return Component(
            type="span",
            classes=classes,
            props={},
            children=self._content,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
