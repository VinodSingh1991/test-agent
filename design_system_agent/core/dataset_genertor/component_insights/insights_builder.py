"""
Insights Builder

Builder for creating AI insights/recommendations components.
Single Responsibility: Build insight cards with recommendations and actions.
Outputs TypeScript-compatible ComponentInsightsProps.
"""

from typing import Dict, Any, Optional, List, Union


class InsightsBuilder:
    """Builder for Insights components with fluent interface"""
    
    def __init__(self, title: str):
        """
        Initialize InsightsBuilder
        
        Args:
            title: Insight title
        """
        self._props = {
            "type": "Insights",
            "title": title,
            "type": "info",
            "recommendations": []
        }
        self._classes = []
    
    def description(self, description: str) -> 'InsightsBuilder':
        """Set description"""
        self._props["description"] = description
        return self
    
    def with_description(self, description: str) -> 'InsightsBuilder':
        """Add description (alias)"""
        return self.description(description)
    
    def recommendations(self, recommendations: List[str]) -> 'InsightsBuilder':
        """Set recommendations"""
        self._props["recommendations"] = recommendations
        return self
    
    def add_recommendation(self, *recommendations: str) -> 'InsightsBuilder':
        """Add recommendations"""
        self._props["recommendations"].extend(recommendations)
        return self
    
    def confidence(self, confidence: Union[str, float]) -> 'InsightsBuilder':
        """Set confidence score (e.g., 95 or "High")"""
        self._props["confidence"] = confidence
        return self
    
    def with_confidence(self, confidence: str) -> 'InsightsBuilder':
        """Add confidence score (alias)"""
        return self.confidence(confidence)
    
    def type(self, type: str) -> 'InsightsBuilder':
        """Set type: info, success, warning, error"""
        self._props["type"] = type
        return self
    
    def info(self) -> 'InsightsBuilder':
        """Set type to info"""
        self._props["type"] = "info"
        return self
    
    def success(self) -> 'InsightsBuilder':
        """Set type to success"""
        self._props["type"] = "success"
        return self
    
    def warning(self) -> 'InsightsBuilder':
        """Set type to warning"""
        self._props["type"] = "warning"
        return self
    
    def danger(self) -> 'InsightsBuilder':
        """Set type to error"""
        self._props["type"] = "error"
        return self
    
    def action(self, label: str, on_click: Optional[str] = None) -> 'InsightsBuilder':
        """Add action button"""
        action = {"label": label}
        if on_click:
            action["onClick"] = on_click
        self._props["action"] = action
        return self
    
    def with_action(self, label: str) -> 'InsightsBuilder':
        """Add action button (alias)"""
        return self.action(label)
    
    def severity(self, severity: str) -> 'InsightsBuilder':
        """Set severity: low, medium, high, critical"""
        self._props["severity"] = severity
        return self
    
    def icon(self, icon: str) -> 'InsightsBuilder':
        """Set icon"""
        self._props["icon"] = icon
        return self
    
    def with_id(self, id: str) -> 'InsightsBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'InsightsBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the insights component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes)
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()

