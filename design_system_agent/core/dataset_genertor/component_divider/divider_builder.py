"""
Divider Builder

Builder for creating divider/separator components.
Single Responsibility: Build horizontal/vertical dividers.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class DividerBuilder:
    """Builder for Divider components with fluent interface"""
    
    def __init__(self):
        """Initialize DividerBuilder"""
        self._orientation = "horizontal"
        self._variant = "solid"
        self._spacing = "md"
        self._label: Optional[str] = None
        self._id: Optional[str] = None
    
    def horizontal(self) -> 'DividerBuilder':
        """Set divider to horizontal"""
        self._orientation = "horizontal"
        return self
    
    def vertical(self) -> 'DividerBuilder':
        """Set divider to vertical"""
        self._orientation = "vertical"
        return self
    
    def dashed(self) -> 'DividerBuilder':
        """Set divider style to dashed"""
        self._variant = "dashed"
        return self
    
    def dotted(self) -> 'DividerBuilder':
        """Set divider style to dotted"""
        self._variant = "dotted"
        return self
    
    def with_label(self, label: str) -> 'DividerBuilder':
        """Add label to divider"""
        self._label = label
        return self
    
    def small_spacing(self) -> 'DividerBuilder':
        """Set small spacing"""
        self._spacing = "sm"
        return self
    
    def large_spacing(self) -> 'DividerBuilder':
        """Set large spacing"""
        self._spacing = "lg"
        return self
    
    def with_id(self, id: str) -> 'DividerBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the divider component"""
        classes = [
            "bd-divider",
            f"bd-divider-{self._orientation}",
            f"bd-divider-{self._variant}",
            f"bd-my-{self._spacing}" if self._orientation == "horizontal" else f"bd-mx-{self._spacing}"
        ]
        
        if self._label:
            return Component(
                type="Divider",
                classes=["bd-divider-wrapper", f"bd-my-{self._spacing}"],
                props={"label": self._label, "orientation": self._orientation},
                children=[
                    {"type": "hr", "classes": classes[:2] + [self._variant]},
                    {"type": "span", "classes": ["bd-divider-label", "bd-px-8"], "children": self._label},
                    {"type": "hr", "classes": classes[:2] + [self._variant]}
                ],
                id=self._id
            )
        
        return Component(
            type="Divider",
            classes=classes,
            props={"orientation": self._orientation},
            children=None,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
