"""
Heading Builder

Builder for creating heading components with fluent API.
Single Responsibility: Build heading components (h1-h6).
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class HeadingBuilder:
    """Builder for Heading components with fluent interface"""
    
    def __init__(self, text: str, level: int = 2):
        """
        Initialize HeadingBuilder
        
        Args:
            text: Heading text content
            level: Heading level (1-6), defaults to 2 (h2)
        """
        self._text = text
        self._level = max(1, min(6, level))  # Ensure level is between 1-6
        self._classes = []
        self._id: Optional[str] = None
    
    def h1(self) -> 'HeadingBuilder':
        """Set heading level to h1"""
        self._level = 1
        return self
    
    def h2(self) -> 'HeadingBuilder':
        """Set heading level to h2"""
        self._level = 2
        return self
    
    def h3(self) -> 'HeadingBuilder':
        """Set heading level to h3"""
        self._level = 3
        return self
    
    def h4(self) -> 'HeadingBuilder':
        """Set heading level to h4"""
        self._level = 4
        return self
    
    def h5(self) -> 'HeadingBuilder':
        """Set heading level to h5"""
        self._level = 5
        return self
    
    def h6(self) -> 'HeadingBuilder':
        """Set heading level to h6"""
        self._level = 6
        return self
    
    def bold(self) -> 'HeadingBuilder':
        """Make heading bold"""
        if "bd-fw-bold" not in self._classes:
            self._classes.append("bd-fw-bold")
        return self
    
    def large(self) -> 'HeadingBuilder':
        """Set large font size"""
        self._classes.append("bd-fs-3xl")
        return self
    
    def extra_large(self) -> 'HeadingBuilder':
        """Set extra large font size"""
        self._classes.append("bd-fs-4xl")
        return self
    
    def small(self) -> 'HeadingBuilder':
        """Set small font size"""
        self._classes.append("bd-fs-lg")
        return self
    
    def with_classes(self, *classes: str) -> 'HeadingBuilder':
        """
        Add custom CSS classes
        
        Args:
            *classes: CSS class names
        """
        self._classes.extend(classes)
        return self
    
    def with_id(self, heading_id: str) -> 'HeadingBuilder':
        """
        Set heading ID
        
        Args:
            heading_id: Heading identifier
        """
        self._id = heading_id
        return self
    
    def build(self) -> Component:
        """
        Build and return the Heading component
        
        Returns:
            Component instance
        """
        # Default classes based on level
        default_classes = {
            1: ["bd-fs-4xl", "bd-fw-bold"],
            2: ["bd-fs-2xl", "bd-fw-bold"],
            3: ["bd-fs-xl", "bd-fw-bold"],
            4: ["bd-fs-lg", "bd-fw-semibold"],
            5: ["bd-fs-base", "bd-fw-semibold"],
            6: ["bd-fs-sm", "bd-fw-semibold"]
        }
        
        classes = default_classes.get(self._level, ["bd-fw-bold"]).copy()
        classes.extend(self._classes)
        
        return Component(
            type=f"h{self._level}",
            classes=classes,
            props={},
            children=self._text,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
