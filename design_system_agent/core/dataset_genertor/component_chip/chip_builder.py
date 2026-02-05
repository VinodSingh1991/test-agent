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
        
        children = []
        
        # Avatar or Icon
        if self._avatar:
            is_image = self._avatar.startswith("http") or self._avatar.endswith((".jpg", ".png", ".svg"))
            if is_image:
                children.append({
                    "type": "img",
                    "classes": ["bd-chip-avatar"],
                    "props": {"src": self._avatar, "alt": self._text}
                })
            else:
                children.append({
                    "type": "span",
                    "classes": ["bd-chip-avatar", "bd-avatar-initials"],
                    "children": self._avatar[:2].upper()
                })
        elif self._icon:
            children.append({
                "type": "i",
                "classes": [self._icon, "bd-chip-icon"]
            })
        
        # Text
        children.append({
            "type": "span",
            "classes": ["bd-chip-label"],
            "children": self._text
        })
        
        # Close button
        if self._closeable:
            children.append({
                "type": "button",
                "classes": ["bd-chip-close"],
                "props": {"aria-label": "Remove"},
                "children": "×"
            })
        
        return Component(
            type="div",
            classes=classes,
            props={},
            children=children,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
