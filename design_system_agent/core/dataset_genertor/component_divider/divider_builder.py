"""
Divider Builder

Builder for creating divider/separator components.
Single Responsibility: Build horizontal/vertical dividers.
Outputs TypeScript-compatible ComponentDividerProps.
"""

from typing import Dict, Any, Optional


class DividerBuilder:
    """Builder for Divider components with fluent interface"""
    
    def __init__(self):
        """Initialize DividerBuilder"""
        self._props = {
            "type": "Divider",
            "orientation": "horizontal",
            "variant": "solid",
            "spacing": "md"
        }
        self._classes = []
    
    def horizontal(self) -> 'DividerBuilder':
        """Set divider to horizontal"""
        self._props["orientation"] = "horizontal"
        return self
    
    def vertical(self) -> 'DividerBuilder':
        """Set divider to vertical"""
        self._props["orientation"] = "vertical"
        return self
    
    def variant(self, variant: str) -> 'DividerBuilder':
        """Set variant: solid, dashed, dotted"""
        self._props["variant"] = variant
        return self
    
    def dashed(self) -> 'DividerBuilder':
        """Set divider style to dashed"""
        self._props["variant"] = "dashed"
        return self
    
    def dotted(self) -> 'DividerBuilder':
        """Set divider style to dotted"""
        self._props["variant"] = "dotted"
        return self
    
    def label(self, label: str) -> 'DividerBuilder':
        """Add label to divider"""
        self._props["label"] = label
        return self
    
    def with_label(self, label: str) -> 'DividerBuilder':
        """Add label to divider (alias)"""
        return self.label(label)
    
    def label_position(self, position: str) -> 'DividerBuilder':
        """Set label position: left, center, right"""
        self._props["labelPosition"] = position
        return self
    
    def spacing(self, spacing: str) -> 'DividerBuilder':
        """Set spacing: none, xs, sm, md, lg, xl"""
        self._props["spacing"] = spacing
        return self
    
    def small_spacing(self) -> 'DividerBuilder':
        """Set small spacing"""
        self._props["spacing"] = "sm"
        return self
    
    def medium_spacing(self) -> 'DividerBuilder':
        """Set medium spacing"""
        self._props["spacing"] = "md"
        return self
    
    def large_spacing(self) -> 'DividerBuilder':
        """Set large spacing"""
        self._props["spacing"] = "lg"
        return self
    
    def color(self, color: str) -> 'DividerBuilder':
        """Set color"""
        self._props["color"] = color
        return self
    
    def thickness(self, thickness: str) -> 'DividerBuilder':
        """Set thickness: thin, normal, thick"""
        self._props["thickness"] = thickness
        return self
    
    def with_id(self, id: str) -> 'DividerBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'DividerBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the divider component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
