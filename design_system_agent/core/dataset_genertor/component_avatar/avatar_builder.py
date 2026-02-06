"""
Avatar Builder

Builder for creating avatar components for user profiles.
Single Responsibility: Build avatar components with images or initials.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class AvatarBuilder:
    """Builder for Avatar components with fluent interface"""
    
    def __init__(self, content: str):
        """
        Initialize AvatarBuilder
        
        Args:
            content: Avatar content (name initials or image URL)
        """
        self._content = content
        self._size = "md"
        self._shape = "circle"
        self._variant = "default"
        self._is_image = content.startswith("http") or content.endswith((".jpg", ".png", ".svg"))
        self._status: Optional[str] = None
        self._id: Optional[str] = None
    
    def small(self) -> 'AvatarBuilder':
        """Set avatar size to small (32px)"""
        self._size = "sm"
        return self
    
    def medium(self) -> 'AvatarBuilder':
        """Set avatar size to medium (40px)"""
        self._size = "md"
        return self
    
    def large(self) -> 'AvatarBuilder':
        """Set avatar size to large (56px)"""
        self._size = "lg"
        return self
    
    def extra_large(self) -> 'AvatarBuilder':
        """Set avatar size to extra large (80px)"""
        self._size = "xl"
        return self
    
    def square(self) -> 'AvatarBuilder':
        """Make avatar square shaped"""
        self._shape = "square"
        return self
    
    def circle(self) -> 'AvatarBuilder':
        """Make avatar circle shaped"""
        self._shape = "circle"
        return self
    
    def primary(self) -> 'AvatarBuilder':
        """Set avatar background to primary color"""
        self._variant = "primary"
        return self
    
    def success(self) -> 'AvatarBuilder':
        """Set avatar background to success color"""
        self._variant = "success"
        return self
    
    def with_status(self, status: str) -> 'AvatarBuilder':
        """
        Add status indicator
        
        Args:
            status: Status type (online, offline, away, busy)
        """
        self._status = status
        return self
    
    def with_id(self, id: str) -> 'AvatarBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the avatar component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-avatar",
            f"bd-avatar-{self._size}",
            f"bd-avatar-{self._shape}",
        ]
        
        if not self._is_image:
            classes.append(f"bd-avatar-{self._variant}")
        
        children = []
        
        # Avatar content (image or initials)
        if self._is_image:
            children.append({
                "type": "img",
                "props": {
                    "src": self._content,
                    "alt": "Avatar"
                },
                "classes": ["bd-avatar-img"]
            })
        else:
            # Initials
            children.append({
                "type": "span",
                "classes": ["bd-avatar-initials"],
                "children": self._content[:2].upper()
            })
        
        # Add status indicator
        if self._status:
            children.append({
                "type": "span",
                "classes": ["bd-avatar-status", f"bd-status-{self._status}"]
            })
        
        return Component(
            type="Avatar",
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
