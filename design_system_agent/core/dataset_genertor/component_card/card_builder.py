"""
Card Builder

Builder for creating card components with header, body, footer.
Single Responsibility: Build card containers with sections.
Outputs TypeScript-compatible ComponentCardProps.
"""

from typing import Dict, Any, Optional, List, Union


class CardBuilder:
    """Builder for Card components with fluent interface"""
    
    def __init__(self, title: Optional[str] = None):
        """
        Initialize CardBuilder
        
        Args:
            title: Optional card title
        """
        self._type = "Card"
        self._title = title or ""
        self._description = ""
        self._content = ""
        self._footer = ""
        self._additional_info = ""
        self._props = {
            "variant": "elevated",
            "hoverable": False,
            "clickable": False
        }
        self._events = {}
        self._classes = []
    
    def title(self, title: str) -> 'CardBuilder':
        """Set card title"""
        self._title = title
        return self
    
    def description(self, description: str) -> 'CardBuilder':
        """Set card description"""
        self._description = description
        return self
    
    def content(self, content: Union[str, List[Dict[str, Any]]]) -> 'CardBuilder':
        """Set card content"""
        self._content = content
        return self
    
    def footer(self, footer: Union[str, List[Dict[str, Any]]]) -> 'CardBuilder':
        """Set card footer"""
        self._footer = footer
        return self
    
    def image(self, image: str, position: str = "top") -> 'CardBuilder':
        """Set card image with position: top, left, right, background"""
        self._props["image"] = image
        self._props["imagePosition"] = position
        return self
    
    def variant(self, variant: str) -> 'CardBuilder':
        """Set variant: elevated, outlined, filled"""
        self._props["variant"] = variant
        return self
    
    def elevated(self) -> 'CardBuilder':
        """Set variant to elevated"""
        self._props["variant"] = "elevated"
        return self
    
    def outlined(self) -> 'CardBuilder':
        """Set variant to outlined"""
        self._props["variant"] = "outlined"
        return self
    
    def hoverable(self, hoverable: bool = True) -> 'CardBuilder':
        """Enable hover effect"""
        self._props["hoverable"] = hoverable
        return self
    
    def clickable(self, clickable: bool = True) -> 'CardBuilder':
        """Make card clickable"""
        self._props["clickable"] = clickable
        return self
    
    def padding(self, padding: Union[int, str]) -> 'CardBuilder':
        """Set padding"""
        self._props["padding"] = padding
        return self
    
    def with_id(self, id: str) -> 'CardBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'CardBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'CardBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_click(self, handler: str) -> 'CardBuilder':
        """Set click event handler"""
        self._events["onClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the card component"""
        props = self._props.copy()
        if self._classes:
            props["className"] = " ".join(self._classes)
        
        result = {
            "type": self._type,
            "props": props,
            "value": {
                "title": self._title,
                "description": self._description,
                "content": self._content,
                "footer": self._footer,
                "additionalInfo": self._additional_info
            }
        }
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
