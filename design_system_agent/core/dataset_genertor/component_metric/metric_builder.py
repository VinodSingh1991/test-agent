"""
Metric/KPI Builder

Builder for creating metric/KPI display components.
Single Responsibility: Build metric cards with value, label, change indicator.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class MetricBuilder:
    """Builder for Metric/KPI components with fluent interface"""
    
    def __init__(self, value: str, label: str):
        """
        Initialize MetricBuilder
        
        Args:
            value: Metric value (e.g., "$2.5M", "85%", "1,234")
            label: Metric label (e.g., "Revenue", "Conversion Rate")
        """
        self._value = value
        self._label = label
        self._change: Optional[str] = None
        self._change_direction: Optional[str] = None  # "up", "down", "neutral"
        self._icon: Optional[str] = None
        self._variant = "default"
        self._id: Optional[str] = None
    
    def with_change(self, change: str, direction: str = "neutral") -> 'MetricBuilder':
        """
        Add change indicator
        
        Args:
            change: Change value (e.g., "+12%", "-5%")
            direction: Direction ("up", "down", "neutral")
        """
        self._change = change
        self._change_direction = direction
        return self
    
    def with_icon(self, icon: str) -> 'MetricBuilder':
        """
        Add icon to metric
        
        Args:
            icon: Icon class name
        """
        self._icon = icon
        return self
    
    def primary(self) -> 'MetricBuilder':
        """Set metric variant to primary"""
        self._variant = "primary"
        return self
    
    def success(self) -> 'MetricBuilder':
        """Set metric variant to success"""
        self._variant = "success"
        return self
    
    def warning(self) -> 'MetricBuilder':
        """Set metric variant to warning"""
        self._variant = "warning"
        return self
    
    def danger(self) -> 'MetricBuilder':
        """Set metric variant to danger"""
        self._variant = "danger"
        return self
    
    def with_id(self, id: str) -> 'MetricBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the metric component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-metric",
            f"bd-metric-{self._variant}",
            "bd-p-16",
            "bd-rounded"
        ]
        
        children = []
        
        # Icon and Label row
        header_children = []
        if self._icon:
            header_children.append({
                "type": "i",
                "classes": [self._icon, "bd-text-muted"]
            })
        header_children.append({
            "type": "span",
            "classes": ["bd-metric-label", "bd-text-sm", "bd-text-muted"],
            "children": self._label
        })
        
        children.append({
            "type": "div",
            "classes": ["bd-flex", "bd-items-center", "bd-gap-8", "bd-mb-8"],
            "children": header_children
        })
        
        # Value
        children.append({
            "type": "div",
            "classes": ["bd-metric-value", "bd-fs-3xl", "bd-fw-bold"],
            "children": self._value
        })
        
        # Change indicator
        if self._change:
            change_classes = ["bd-metric-change", "bd-flex", "bd-items-center", "bd-gap-4", "bd-mt-8", "bd-text-sm"]
            
            if self._change_direction == "up":
                change_classes.append("bd-text-success")
                icon = "↑"
            elif self._change_direction == "down":
                change_classes.append("bd-text-danger")
                icon = "↓"
            else:
                change_classes.append("bd-text-muted")
                icon = "→"
            
            children.append({
                "type": "div",
                "classes": change_classes,
                "children": [
                    {"type": "span", "children": icon},
                    {"type": "span", "children": self._change}
                ]
            })
        
        return Component(
            type="Metric",
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
