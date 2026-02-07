"""
Dashlet Builder

Builder for creating dashboard widget components.
Single Responsibility: Build small dashboard widgets with title, content, actions.
Outputs TypeScript-compatible ComponentDashletProps.
"""

from typing import Dict, Any, Optional, List, Union


class DashletBuilder:
    """Builder for Dashlet components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize DashletBuilder
        
        Args:
            title: Dashlet title
        """
        self._type = "Dashlet"
        self._title = title
        self._content = []
        self._description = ""
        self._additional_info = ""
        self._props = {
            "variant": "default"
        }
        self._events = {}
        self._actions: List[Dict[str, str]] = []
        self._classes = []
    
    def with_description(self, description: str) -> 'DashletBuilder':
        """Add description text"""
        self._description = description
        return self
    
    def add_content(self, *content: Union[str, Dict, Any]) -> 'DashletBuilder':
        """Add content to dashlet (can be components, dicts, or strings)"""
        for item in content:
            if isinstance(item, dict):
                self._content.append(item)
            elif hasattr(item, 'build'):
                # If it's a builder, build it
                self._content.append(item.build())
            elif hasattr(item, 'to_dict'):
                # If it has to_dict method
                self._content.append(item.to_dict())
            else:
                # Plain string or other
                self._content.append(str(item))
        return self
    
    def set_content(self, content: Any) -> 'DashletBuilder':
        """Set content directly (replaces existing)"""
        self._content = content
        return self
    
    def add_action(self, label: str, onClick: Optional[str] = None) -> 'DashletBuilder':
        """Add action button/link"""
        if onClick:
            if "onAction" not in self._events:
                self._events["onAction"] = []
            self._events["onAction"].append({"label": label, "handler": onClick})
        self._additional_info = label
        return self
    
    def with_action(self, label: str) -> 'DashletBuilder':
        """Add action button/link (alias)"""
        return self.add_action(label)
    
    def variant(self, variant: str) -> 'DashletBuilder':
        """Set variant: default, accent, outlined"""
        self._props["variant"] = variant
        return self
    
    def default(self) -> 'DashletBuilder':
        return self.variant("default")
    
    def accent(self) -> 'DashletBuilder':
        return self.variant("accent")
    
    def outlined(self) -> 'DashletBuilder':
        return self.variant("outlined")
    
    def primary(self) -> 'DashletBuilder':
        """Set variant to accent (alias)"""
        return self.accent()
    
    def with_id(self, id: str) -> 'DashletBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'DashletBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'DashletBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_click(self, handler: str) -> 'DashletBuilder':
        """Set click event handler"""
        self._events["onClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the dashlet component"""
        props = self._props.copy()
        if self._classes:
            props["className"] = " ".join(self._classes)
        
        result = {
            "type": self._type,
            "props": props,
            "value": {
                "title": self._title,
                "content": self._content,
                "description": self._description,
                "additionalInfo": self._additional_info
            }
        }
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
