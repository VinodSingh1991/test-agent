"""
Chip Builder

Builder for creating chip/tag components (similar to badge but interactive).
Single Responsibility: Build interactive chips with optional close button.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ChipBuilder:
    """Builder for Chip components with fluent interface"""
    
    def __init__(self, text: str):
        """Initialize ChipBuilder"""
        self._text = text
        self._variant = "default"
        self._size = "md"
        self._closeable = False
        self._icon: Optional[str] = None
        self._avatar: Optional[str] = None
        self._clickable = False
        self._id: Optional[str] = None
    
    def primary(self) -> 'ChipBuilder':
        """Set chip variant to primary"""
        self._variant = "primary"
        return self
    
    def secondary(self) -> 'ChipBuilder':
        """Set chip variant to secondary"""
        self._variant = "secondary"
        return self
    
    def success(self) -> 'ChipBuilder':
        """Set chip variant to success"""
        self._variant = "success"
        return self
    
    def warning(self) -> 'ChipBuilder':
        """Set chip variant to warning"""
        self._variant = "warning"
        return self
    
    def danger(self) -> 'ChipBuilder':
        """Set chip variant to danger"""
        self._variant = "danger"
        return self
    
    def small(self) -> 'ChipBuilder':
        """Set chip size to small"""
        self._size = "sm"
        return self
    
    def large(self) -> 'ChipBuilder':
        """Set chip size to large"""
        self._size = "lg"
        return self
    
    def closeable(self) -> 'ChipBuilder':
        """Make chip closeable"""
        self._closeable = True
        return self
    
    def clickable(self) -> 'ChipBuilder':
        """Make chip clickable"""
        self._clickable = True
        return self
    
    def with_icon(self, icon: str) -> 'ChipBuilder':
        """Add icon to chip"""
        self._icon = icon
        return self
    
    def with_avatar(self, avatar: str) -> 'ChipBuilder':
        """Add avatar to chip"""
        self._avatar = avatar
        return self
    
    def with_id(self, id: str) -> 'ChipBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the chip component"""
        classes = [
            "bd-chip",
            f"bd-chip-{self._variant}",
            f"bd-chip-{self._size}"
        ]
        
        if self._clickable:
            classes.append("bd-chip-clickable")
        
        # Use value structure with icon and text
        icon_value = ""
        if self._icon:
            icon_value = self._icon
        elif self._avatar:
            icon_value = self._avatar
        
        value = {
            "icon": icon_value,
            "text": self._text
        }
        
        return Component(
            type="Chip",
            classes=classes,
            props={},
            value=value,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
