"""
Alert Builder

Builder for creating alert/banner components.
Single Responsibility: Build alert messages with variants and actions.
Outputs TypeScript-compatible ComponentAlertProps.
"""

from typing import Dict, Any, Optional


class AlertBuilder:
    """Builder for Alert components with fluent interface"""
    
    def __init__(self, message: str):
        """
        Initialize AlertBuilder
        
        Args:
            message: Alert message
        """
        self._type = "Alert"
        self._text = message
        self._icon = ""
        self._props = {}
        self._events = {}
        self._classes = []
    
    def with_title(self, title: str) -> 'AlertBuilder':
        """Add title to alert"""
        self._props["title"] = title
        return self
    
    def alert_type(self, alert_type: str) -> 'AlertBuilder':
        """Set alert type: info, success, warning, error"""
        self._props["alertType"] = alert_type
        return self
    
    def info(self) -> 'AlertBuilder':
        """Set alert type to info"""
        return self.alert_type("info")
    
    def success(self) -> 'AlertBuilder':
        """Set alert type to success"""
        return self.alert_type("success")
    
    def warning(self) -> 'AlertBuilder':
        """Set alert type to warning"""
        return self.alert_type("warning")
    
    def error(self) -> 'AlertBuilder':
        """Set alert type to error"""
        return self.alert_type("error")
    
    def danger(self) -> 'AlertBuilder':
        """Set alert type to error (alias for danger)"""
        return self.error()
    
    def variant(self, variant: str) -> 'AlertBuilder':
        """Set variant: subtle, solid, left-accent"""
        self._props["variant"] = variant
        return self
    
    def subtle(self) -> 'AlertBuilder':
        return self.variant("subtle")
    
    def solid(self) -> 'AlertBuilder':
        return self.variant("solid")
    
    def left_accent(self) -> 'AlertBuilder':
        return self.variant("left-accent")
    
    def closeable(self, closeable: bool = True) -> 'AlertBuilder':
        """Make alert closeable/dismissible"""
        self._props["closeable"] = closeable
        return self
    
    def dismissible(self) -> 'AlertBuilder':
        """Make alert dismissible (alias for closeable)"""
        return self.closeable(True)
    
    def with_icon(self, icon: str) -> 'AlertBuilder':
        """Add icon to alert"""
        self._props["icon"] = icon
        return self
    
    def with_action(self, label: str, onClick: Optional[str] = None) -> 'AlertBuilder':
        """Add action button"""
        action = {"label": label}
        if onClick:
            action["onClick"] = onClick
        self._props["action"] = action
        return self
    
    def with_id(self, id: str) -> 'AlertBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'AlertBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def with_icon(self, icon: str) -> 'AlertBuilder':
        """Set icon"""
        self._icon = icon
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the alert component"""
        result = {
            "type": self._type,
            "props": self._props.copy(),
            "value": {
                "icon": self._icon,
                "text": self._text
            }
        }
        
        if self._classes:
            result["props"]["className"] = " ".join(self._classes)
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
