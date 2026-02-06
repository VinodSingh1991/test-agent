"""
Birthday Card Builder

Builder for creating birthday/celebration card components.
Single Responsibility: Build special cards for birthdays and celebrations.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class BirthdayCardBuilder:
    """Builder for Birthday Card components with fluent interface"""
    
    def __init__(self, name: str, date: str):
        """
        Initialize BirthdayCardBuilder
        
        Args:
            name: Person's name
            date: Birthday date
        """
        self._name = name
        self._date = date
        self._avatar: Optional[str] = None
        self._age: Optional[int] = None
        self._message: Optional[str] = None
        self._show_gift_icon = True
        self._id: Optional[str] = None
    
    def with_avatar(self, avatar: str) -> 'BirthdayCardBuilder':
        """
        Add avatar
        
        Args:
            avatar: Avatar initials or image URL
        """
        self._avatar = avatar
        return self
    
    def with_age(self, age: int) -> 'BirthdayCardBuilder':
        """
        Add age
        
        Args:
            age: Person's age
        """
        self._age = age
        return self
    
    def with_message(self, message: str) -> 'BirthdayCardBuilder':
        """
        Add custom message
        
        Args:
            message: Birthday message
        """
        self._message = message
        return self
    
    def no_gift_icon(self) -> 'BirthdayCardBuilder':
        """Hide gift icon"""
        self._show_gift_icon = False
        return self
    
    def with_id(self, id: str) -> 'BirthdayCardBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the birthday card component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-birthday-card",
            "bd-card",
            "bd-p-16",
            "bd-text-center",
            "bd-bg-gradient-primary"
        ]
        
        children = []
        
        # Gift icon
        if self._show_gift_icon:
            children.append({
                "type": "div",
                "classes": ["bd-birthday-icon", "bd-mb-12"],
                "children": {
                    "type": "span",
                    "classes": ["bd-icon-gift", "bd-fs-4xl"],
                    "children": "🎁"
                }
            })
        
        # Avatar
        if self._avatar:
            is_image = self._avatar.startswith("http") or self._avatar.endswith((".jpg", ".png", ".svg"))
            
            if is_image:
                children.append({
                    "type": "img",
                    "classes": ["bd-avatar", "bd-avatar-xl", "bd-avatar-circle", "bd-mb-12", "bd-mx-auto"],
                    "props": {"src": self._avatar, "alt": self._name}
                })
            else:
                children.append({
                    "type": "div",
                    "classes": ["bd-avatar", "bd-avatar-xl", "bd-avatar-circle", "bd-avatar-primary", "bd-mb-12", "bd-mx-auto"],
                    "children": {
                        "type": "span",
                        "classes": ["bd-avatar-initials"],
                        "children": self._avatar[:2].upper()
                    }
                })
        
        # Title
        title_text = f"Happy Birthday, {self._name}!"
        if self._age:
            title_text = f"Happy {self._age}th Birthday, {self._name}!"
        
        children.append({
            "type": "h3",
            "classes": ["bd-fs-2xl", "bd-fw-bold", "bd-mb-8"],
            "children": title_text
        })
        
        # Date
        children.append({
            "type": "p",
            "classes": ["bd-text-muted", "bd-mb-12"],
            "children": self._date
        })
        
        # Message
        if self._message:
            children.append({
                "type": "p",
                "classes": ["bd-birthday-message", "bd-fs-md", "bd-italic"],
                "children": f'"{self._message}"'
            })
        
        # Action button
        children.append({
            "type": "button",
            "classes": ["bd-btn", "bd-btn-primary", "bd-mt-16"],
            "children": "Send Wishes"
        })
        
        return Component(
            type="BirthdayCard",
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
