"""
Metric/KPI Builder

Builder for creating metric/KPI display components.
Single Responsibility: Build metric cards with value, label, change indicator.
Outputs TypeScript-compatible ComponentMetricProps.
"""

from typing import Dict, Any, Optional, Union


class MetricBuilder:
    """Builder for Metric/KPI components with fluent interface"""
    
    def __init__(self, label: str, value: Union[str, int, float]):
        """
        Initialize MetricBuilder
        
        Args:
            label: Metric label (e.g., "Revenue", "Conversion Rate")
            value: Metric value (e.g., "2.5M", 85, 1234)
        """
        self._type = "Metric"
        self._label = label
        self._value = str(value)
        self._icon = ""
        self._description = ""
        self._additional_info = ""
        self._props = {
            "size": "md",
            "color": "brand"
        }
        self._events = {}
        self._classes = []
    
    def trend(self, value: float, direction: str, is_positive: bool = None) -> 'MetricBuilder':
        """
        Add trend information
        Args:
            value: Trend value (e.g., 12.5 for +12.5%)
            direction: up, down, or neutral
            is_positive: Whether the trend is good (optional, uses direction if not set)
        """
        self._props["trend"] = {
            "value": value,
            "direction": direction,
            "isPositive": is_positive if is_positive is not None else (direction == "up")
        }
        return self
    
    def icon(self, icon: str) -> 'MetricBuilder':
        """Set icon"""
        self._icon = icon
        return self
    
    def with_icon(self, icon: str) -> 'MetricBuilder':
        """Set icon (alias)"""
        return self.icon(icon)
    
    def color(self, color: str) -> 'MetricBuilder':
        """Set color: brand, success, error, warning, info, gray"""
        self._props["color"] = color
        return self
    
    def size(self, size: str) -> 'MetricBuilder':
        """Set size: sm, md, lg"""
        self._props["size"] = size
        return self
    
    def prefix(self, prefix: str) -> 'MetricBuilder':
        """Set prefix (e.g., '$' for currency)"""
        self._props["prefix"] = prefix
        return self
    
    def suffix(self, suffix: str) -> 'MetricBuilder':
        """Set suffix (e.g., '%' for percentage)"""
        self._props["suffix"] = suffix
        return self
    
    def description(self, description: str) -> 'MetricBuilder':
        """Set description text"""
        self._description = description
        return self
    
    def success(self) -> 'MetricBuilder':
        """Set color to success"""
        self._props["color"] = "success"
        return self
    
    def warning(self) -> 'MetricBuilder':
        """Set color to warning"""
        self._props["color"] = "warning"
        return self
    
    def danger(self) -> 'MetricBuilder':
        """Set color to error"""
        self._props["color"] = "error"
        return self
    
    def with_id(self, id: str) -> 'MetricBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'MetricBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'MetricBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_click(self, handler: str) -> 'MetricBuilder':
        """Set click event handler"""
        self._events["onClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the metric component"""
        props = self._props.copy()
        if self._classes:
            props["className"] = " ".join(self._classes)
        
        result = {
            "type": self._type,
            "props": props,
            "value": {
                "label": self._label,
                "value": self._value,
                "icon": self._icon,
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
