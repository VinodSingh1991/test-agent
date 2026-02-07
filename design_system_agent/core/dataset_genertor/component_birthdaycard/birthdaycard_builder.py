"""
Birthday Card Builder

Builder for creating birthday/celebration card components.
Single Responsibility: Build special cards for birthdays and celebrations.
Outputs TypeScript-compatible ComponentBirthdayCardProps.
"""

from typing import Dict, Any, Optional


class BirthdayCardBuilder:
    """Builder for Birthday Card components with fluent interface"""
    
    def __init__(self, name: str, date: str):
        """
        Initialize BirthdayCardBuilder
        
        Args:
            name: Person's name
            date: Birthday date
        """
        self._props = {
            "type": "BirthdayCard",
            "name": name,
            "date": date
        }
        self._classes = []
    
    def with_avatar(self, avatar: str) -> 'BirthdayCardBuilder':
        """Add avatar (initials or image URL)"""
        self._props["avatar"] = avatar
        return self
    
    def with_age(self, age: int) -> 'BirthdayCardBuilder':
        """Add age"""
        self._props["age"] = age
        return self
    
    def with_message(self, message: str) -> 'BirthdayCardBuilder':
        """Add custom birthday message"""
        self._props["message"] = message
        return self
    
    def with_id(self, id: str) -> 'BirthdayCardBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'BirthdayCardBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the birthday card component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
