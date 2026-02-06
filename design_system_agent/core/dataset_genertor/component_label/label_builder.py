"""
Label Builder

Builder for creating form label components.
Single Responsibility: Build labels for form fields.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class LabelBuilder:
    """Builder for Label components with fluent interface"""
    
    def __init__(self, text: str, for_id: Optional[str] = None):
        """Initialize LabelBuilder"""
        self._text = text
        self._for_id = for_id
        self._required = False
        self._hint: Optional[str] = None
        self._size = "md"
        self._id: Optional[str] = None
    
    def required(self) -> 'LabelBuilder':
        """Mark field as required"""
        self._required = True
        return self
    
    def with_hint(self, hint: str) -> 'LabelBuilder':
        """Add hint text"""
        self._hint = hint
        return self
    
    def small(self) -> 'LabelBuilder':
        """Set label size to small"""
        self._size = "sm"
        return self
    
    def large(self) -> 'LabelBuilder':
        """Set label size to large"""
        self._size = "lg"
        return self
    
    def with_id(self, id: str) -> 'LabelBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the label component"""
        classes = ["bd-label", f"bd-text-{self._size}", "bd-fw-medium"]
        
        props = {}
        if self._for_id:
            props["for"] = self._for_id
        
        # Use value structure with icon and text
        # Combine label text with required indicator and hint
        text_content = self._text
        if self._required:
            text_content = f"{self._text} *"
        if self._hint:
            text_content = f"{text_content} ({self._hint})"
        
        value = {
            "icon": "",
            "text": text_content
        }
        
        return Component(
            type="Label",
            classes=classes,
            props=props,
            value=value,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
