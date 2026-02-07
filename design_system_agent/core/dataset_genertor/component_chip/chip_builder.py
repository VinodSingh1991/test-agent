"""
Chip Builder

Builder for creating chip/tag components (similar to badge but interactive).
Single Responsibility: Build interactive chips with optional close button.
Outputs TypeScript-compatible ComponentChipProps.
"""

from typing import Dict, Any, Optional


class ChipBuilder:
    """Builder for Chip components with fluent interface"""
    
    def __init__(self, label: str):
        """Initialize ChipBuilder"""
        self._props = {
            "type": "Chip",
            "label": label,
            "variant": "filled",
            "color": "brand",
            "size": "md",
            "closeable": False,
            "clickable": False
        }
        self._classes = []
    
    def variant(self, variant: str) -> 'ChipBuilder':
        """Set variant: filled, outlined"""
        self._props["variant"] = variant
        return self
    
    def color(self, color: str) -> 'ChipBuilder':
        """Set color: brand, success, error, warning, info, gray"""
        self._props["color"] = color
        return self
    
    def size(self, size: str) -> 'ChipBuilder':
        """Set size: sm, md, lg"""
        self._props["size"] = size
        return self
    
    def closeable(self, closeable: bool = True) -> 'ChipBuilder':
        """Make chip closeable"""
        self._props["closeable"] = closeable
        return self
    
    def clickable(self, clickable: bool = True) -> 'ChipBuilder':
        """Make chip clickable"""
        self._props["clickable"] = clickable
        return self
    
    def icon(self, icon: str) -> 'ChipBuilder':
        """Set icon"""
        self._props["icon"] = icon
        return self
    
    def avatar(self, avatar: str) -> 'ChipBuilder':
        """Set avatar"""
        self._props["avatar"] = avatar
        return self
    
    def on_close(self, callback: str) -> 'ChipBuilder':
        """Set close callback"""
        self._props["onClose"] = callback
        return self
    
    def on_click(self, callback: str) -> 'ChipBuilder':
        """Set click callback"""
        self._props["onClick"] = callback
        return self
    
    def with_icon(self, icon: str) -> 'ChipBuilder':
        return self.icon(icon)
    
    def with_avatar(self, avatar: str) -> 'ChipBuilder':
        return self.avatar(avatar)
    
    def success(self) -> 'ChipBuilder':
        return self.color("success")
    
    def warning(self) -> 'ChipBuilder':
        return self.color("warning")
    
    def danger(self) -> 'ChipBuilder':
        return self.color("error")
    
    def primary(self) -> 'ChipBuilder':
        """Set color to brand (alias)"""
        return self.color("brand")
    
    def secondary(self) -> 'ChipBuilder':
        """Set color to gray (alias)"""
        return self.color("gray")
    
    def small(self) -> 'ChipBuilder':
        return self.size("sm")
    
    def large(self) -> 'ChipBuilder':
        return self.size("lg")
    
    def with_id(self, id: str) -> 'ChipBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'ChipBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the chip component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
