"""
Insights Builder

Builder for creating AI insights/recommendations components.
Single Responsibility: Build insight cards with recommendations and actions.
"""

from typing import Dict, Any, Optional, List
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class InsightsBuilder:
    """Builder for Insights components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize InsightsBuilder
        
        Args:
            title: Insight title
        """
        self._title = title
        self._description: Optional[str] = None
        self._recommendations: List[str] = []
        self._confidence: Optional[str] = None
        self._severity = "info"  # info, success, warning, danger
        self._action_label: Optional[str] = None
        self._id: Optional[str] = None
    
    def with_description(self, description: str) -> 'InsightsBuilder':
        """
        Add description
        
        Args:
            description: Insight description
        """
        self._description = description
        return self
    
    def add_recommendation(self, *recommendations: str) -> 'InsightsBuilder':
        """
        Add recommendations
        
        Args:
            recommendations: Recommendation items
        """
        self._recommendations.extend(recommendations)
        return self
    
    def with_confidence(self, confidence: str) -> 'InsightsBuilder':
        """
        Add confidence score
        
        Args:
            confidence: Confidence level (e.g., "95%", "High")
        """
        self._confidence = confidence
        return self
    
    def info(self) -> 'InsightsBuilder':
        """Set insight severity to info"""
        self._severity = "info"
        return self
    
    def success(self) -> 'InsightsBuilder':
        """Set insight severity to success"""
        self._severity = "success"
        return self
    
    def warning(self) -> 'InsightsBuilder':
        """Set insight severity to warning"""
        self._severity = "warning"
        return self
    
    def danger(self) -> 'InsightsBuilder':
        """Set insight severity to danger"""
        self._severity = "danger"
        return self
    
    def with_action(self, label: str) -> 'InsightsBuilder':
        """
        Add action button
        
        Args:
            label: Action label
        """
        self._action_label = label
        return self
    
    def with_id(self, id: str) -> 'InsightsBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the insights component
        
        Returns:
            Component instance
        """
        classes = [
            "bd-insights",
            "bd-card",
            "bd-p-16",
            f"bd-border-{self._severity}",
            f"bd-bg-{self._severity}-light"
        ]
        
        children = []
        
        # Header with icon
        icon_map = {
            "info": "💡",
            "success": "✅",
            "warning": "⚠️",
            "danger": "🚨"
        }
        
        children.append({
            "type": "div",
            "classes": ["bd-flex", "bd-items-start", "bd-gap-12", "bd-mb-12"],
            "children": [
                {
                    "type": "span",
                    "classes": ["bd-insights-icon", "bd-fs-2xl"],
                    "children": icon_map.get(self._severity, "💡")
                },
                {
                    "type": "div",
                    "classes": ["bd-flex-1"],
                    "children": [
                        {
                            "type": "h4",
                            "classes": ["bd-insights-title", "bd-fs-lg", "bd-fw-semibold", "bd-mb-4"],
                            "children": self._title
                        },
                        {
                            "type": "p",
                            "classes": ["bd-insights-description", "bd-text-sm"],
                            "children": self._description or ""
                        } if self._description else None
                    ]
                }
            ]
        })
        
        # Recommendations
        if self._recommendations:
            rec_items = []
            for rec in self._recommendations:
                rec_items.append({
                    "type": "li",
                    "classes": ["bd-mb-8"],
                    "children": rec
                })
            
            children.append({
                "type": "div",
                "classes": ["bd-insights-recommendations", "bd-mt-12"],
                "children": [
                    {
                        "type": "p",
                        "classes": ["bd-fw-semibold", "bd-mb-8", "bd-text-sm"],
                        "children": "Recommendations:"
                    },
                    {
                        "type": "ul",
                        "classes": ["bd-list-disc", "bd-pl-20", "bd-text-sm"],
                        "children": rec_items
                    }
                ]
            })
        
        # Footer with confidence and action
        footer_children = []
        
        if self._confidence:
            footer_children.append({
                "type": "span",
                "classes": ["bd-badge", "bd-badge-sm", f"bd-badge-{self._severity}"],
                "children": f"Confidence: {self._confidence}"
            })
        
        if self._action_label:
            footer_children.append({
                "type": "button",
                "classes": ["bd-btn", "bd-btn-sm", f"bd-btn-{self._severity}"],
                "children": self._action_label
            })
        
        if footer_children:
            children.append({
                "type": "div",
                "classes": ["bd-insights-footer", "bd-flex", "bd-justify-between", "bd-items-center", "bd-mt-16"],
                "children": footer_children
            })
        
        return Component(
            type="Insights",
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
