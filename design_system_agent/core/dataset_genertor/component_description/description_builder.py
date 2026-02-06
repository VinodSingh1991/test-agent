"""
Description Builder

Builder for creating description/paragraph components with fluent API.
Single Responsibility: Build paragraph/description text components.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class DescriptionBuilder:
    """Builder for Description/Paragraph components with fluent interface"""
    
    def __init__(self, text: str):
        """
        Initialize DescriptionBuilder
        
        Args:
            text: Description text content
        """
        self._text = text
        self._classes = []
        self._id: Optional[str] = None
    
    def muted(self) -> 'DescriptionBuilder':
        """Make text muted/gray"""
        if "bd-text-gray-600" not in self._classes:
            self._classes.append("bd-text-gray-600")
        return self
    
    def small(self) -> 'DescriptionBuilder':
        """Make text small"""
        if "bd-fs-sm" not in self._classes:
            self._classes.append("bd-fs-sm")
        return self
    
    def large(self) -> 'DescriptionBuilder':
        """Make text large"""
        if "bd-fs-lg" not in self._classes:
            self._classes.append("bd-fs-lg")
        return self
    
    def bold(self) -> 'DescriptionBuilder':
        """Make text bold"""
        if "bd-fw-bold" not in self._classes:
            self._classes.append("bd-fw-bold")
        return self
    
    def italic(self) -> 'DescriptionBuilder':
        """Make text italic"""
        if "bd-italic" not in self._classes:
            self._classes.append("bd-italic")
        return self
    
    def with_margin(self) -> 'DescriptionBuilder':
        """Add bottom margin"""
        if "bd-mb-16" not in self._classes:
            self._classes.append("bd-mb-16")
        return self
    
    def center(self) -> 'DescriptionBuilder':
        """Center align text"""
        if "bd-text-center" not in self._classes:
            self._classes.append("bd-text-center")
        return self
    
    def with_classes(self, *classes: str) -> 'DescriptionBuilder':
        """
        Add custom CSS classes
        
        Args:
            *classes: CSS class names
        """
        self._classes.extend(classes)
        return self
    
    def with_id(self, desc_id: str) -> 'DescriptionBuilder':
        """
        Set description ID
        
        Args:
            desc_id: Description identifier
        """
        self._id = desc_id
        return self
    
    def build(self) -> Component:
        """
        Build and return the Description component
        
        Returns:
            Component instance
        """
        # Default classes for description
        default_classes = ["bd-text-gray-600"] if not self._classes else []
        classes = default_classes + self._classes
        
        # Use value structure with icon and text
        value = {
            "icon": "",
            "text": self._text
        }
        
        return Component(
            type="Description",
            classes=classes,
            props={},
            value=value,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
