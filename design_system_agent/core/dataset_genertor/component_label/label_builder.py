"""
Label Builder

Builder for creating form label components.
Single Responsibility: Build labels for form fields.
Outputs TypeScript-compatible ComponentLabelProps.
"""

from typing import Dict, Any, Optional


class LabelBuilder:
    """Builder for Label components with fluent interface"""
    
    def __init__(self, text: str, for_id: Optional[str] = None):
        """Initialize LabelBuilder"""
        self._props = {
            "type": "Label",
            "text": text
        }
        if for_id:
            self._props["for"] = for_id
        self._classes = []
    
    def required(self, required: bool = True) -> 'LabelBuilder':
        """Mark field as required"""
        self._props["required"] = required
        return self
    
    def hint(self, hint: str) -> 'LabelBuilder':
        """Add hint text"""
        self._props["hint"] = hint
        return self
    
    def with_hint(self, hint: str) -> 'LabelBuilder':
        """Add hint text (alias)"""
        return self.hint(hint)
    
    def size(self, size: str) -> 'LabelBuilder':
        """Set size: xs, sm, md, lg"""
        self._props["size"] = size
        return self
    
    def weight(self, weight: str) -> 'LabelBuilder':
        """Set weight: normal, medium, semibold, bold"""
        self._props["weight"] = weight
        return self
    
    def color(self, color: str) -> 'LabelBuilder':
        """Set text color"""
        self._props["color"] = color
        return self
    
    def small(self) -> 'LabelBuilder':
        """Set label size to small"""
        self._props["size"] = "sm"
        return self
    
    def large(self) -> 'LabelBuilder':
        """Set label size to large"""
        self._props["size"] = "lg"
        return self
    
    def disabled(self, disabled: bool = True) -> 'LabelBuilder':
        """Mark as disabled"""
        self._props["disabled"] = disabled
        return self
    
    def with_id(self, id: str) -> 'LabelBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'LabelBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the label component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
