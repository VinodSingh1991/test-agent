"""
Avatar Builder

Builder for creating avatar components for user profiles.
Single Responsibility: Build avatar components with images or initials.
Outputs TypeScript-compatible ComponentAvatarProps.
"""

from typing import Dict, Any, Optional


class AvatarBuilder:
    """Builder for Avatar components with fluent interface"""
    
    def __init__(self, content: str):
        """
        Initialize AvatarBuilder
        
        Args:
            content: Avatar content (name/initials or image URL)
        """
        is_image = content.startswith("http") or content.endswith((".jpg", ".png", ".svg", ".gif"))
        self._props = {
            "type": "Avatar",
            "size": "md",
            "shape": "circle",
            "color": "brand"
        }
        if is_image:
            self._props["src"] = content
        else:
            self._props["initials"] = content[:2].upper()
            self._props["name"] = content
        self._classes = []
    
    def size(self, size: str) -> 'AvatarBuilder':
        """Set size: xs, sm, md, lg, xl, 2xl"""
        self._props["size"] = size
        return self
    
    def shape(self, shape: str) -> 'AvatarBuilder':
        """Set shape: circle, square"""
        self._props["shape"] = shape
        return self
    
    def color(self, color: str) -> 'AvatarBuilder':
        """Set color: brand, success, error, warning, info, gray"""
        self._props["color"] = color
        return self
    
    def status(self, status: str) -> 'AvatarBuilder':
        """Set status: online, offline, away, busy"""
        self._props["status"] = status
        return self
    
    def border(self, border: bool = True) -> 'AvatarBuilder':
        """Add border"""
        self._props["border"] = border
        return self
    
    def small(self) -> 'AvatarBuilder':
        self._props["size"] = "sm"
        return self
    
    def medium(self) -> 'AvatarBuilder':
        self._props["size"] = "md"
        return self
    
    def large(self) -> 'AvatarBuilder':
        self._props["size"] = "lg"
        return self
    
    def extra_large(self) -> 'AvatarBuilder':
        self._props["size"] = "xl"
        return self
    
    def square(self) -> 'AvatarBuilder':
        self._props["shape"] = "square"
        return self
    
    def circle(self) -> 'AvatarBuilder':
        self._props["shape"] = "circle"
        return self
    
    def with_status(self, status: str) -> 'AvatarBuilder':
        return self.status(status)
    
    def with_id(self, id: str) -> 'AvatarBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'AvatarBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the avatar component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
        
    
