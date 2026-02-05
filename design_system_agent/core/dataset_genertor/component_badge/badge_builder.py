"""
Badge Builder

Builder for creating badge/tag components with fluent API.
Single Responsibility: Build badge components for status, labels, counts.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class BadgeBuilder:
    """Builder for Badge components with fluent interface"""
    
    def __init__(self, text: str):
        """
        Initialize BadgeBuilder
        
        Args:
            text: Badge text content
        """
        self._text = text
        self._variant = "default"
        self._size = "md"
        self._pill = False
        self._icon: Optional[str] = None
        self._id: Optional[str] = None
    
    def primary(self) -> 'BadgeBuilder':
        """Set badge variant to primary"""
        self._variant = "primary"
        return self
    
    def secondary(self) -> 'BadgeBuilder':
        """Set badge variant to secondary"""
        self._variant = "secondary"
        return self
    
    def success(self) -> 'BadgeBuilder':
        """Set badge variant to success"""
        self._variant = "success"
        return self
    
    def warning(self) -> 'BadgeBuilder':
        """Set badge variant to warning"""
        self._variant = "warning"
        return self
    
    def danger(self) -> 'BadgeBuilder':
        """Set badge variant to danger"""
        self._variant = "danger"
        return self
    
    def info(self) -> 'BadgeBuilder':
        """Set badge variant to info"""
        self._variant = "info"
        return self
    
    def small(self) -> 'BadgeBuilder':
        """Set badge size to small"""
        self._size = "sm"
        return self
    
    def medium(self) -> 'BadgeBuilder':
        """Set badge size to medium"""
        self._size = "md"
        return self
    
    def large(self) -> 'BadgeBuilder':
        """Set badge size to large"""
        self._size = "lg"
        return self
    
    def pill_shape(self) -> 'BadgeBuilder':
        """Make badge pill-shaped (fully rounded)"""
        self._pill = True
        return self
    
    def with_icon(self, icon: str) -> 'BadgeBuilder':
        """
        Add icon to badge
        
        Args:
            icon: Icon class name
        """
        self._icon = icon
        return self
    
    def with_id(self, id: str) -> 'BadgeBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the badge component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-badge",
            f"bd-badge-{self._variant}",
        ]
        
        if self._size != "md":
            classes.append(f"bd-badge-{self._size}")
        
        if self._pill:
            classes.append("bd-badge-pill")
        
        children = self._text
        if self._icon:
            children = {
                "type": "span",
                "classes": ["bd-flex", "bd-items-center", "bd-gap-4"],
                "children": [
                    {"type": "i", "classes": [self._icon]},
                    {"type": "span", "children": self._text}
                ]
            }
        
        return Component(
            type="span",
            classes=classes,
            props={},
            children=children,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
