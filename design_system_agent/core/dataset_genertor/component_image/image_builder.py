"""
Image Builder

Builder for creating image components.
Single Responsibility: Build images with variants and aspect ratios.
"""

from typing import Dict, Any, Optional
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class ImageBuilder:
    """Builder for Image components with fluent interface"""
    
    def __init__(self, src: str, alt: str = ""):
        """Initialize ImageBuilder"""
        self._src = src
        self._alt = alt
        self._width: Optional[str] = None
        self._height: Optional[str] = None
        self._rounded = False
        self._circle = False
        self._thumbnail = False
        self._fluid = False
        self._id: Optional[str] = None
    
    def with_size(self, width: str, height: Optional[str] = None) -> 'ImageBuilder':
        """Set image size"""
        self._width = width
        self._height = height or width
        return self
    
    def rounded(self) -> 'ImageBuilder':
        """Add rounded corners"""
        self._rounded = True
        return self
    
    def circle(self) -> 'ImageBuilder':
        """Make image circular"""
        self._circle = True
        return self
    
    def thumbnail(self) -> 'ImageBuilder':
        """Add thumbnail border"""
        self._thumbnail = True
        return self
    
    def fluid(self) -> 'ImageBuilder':
        """Make image responsive (100% width)"""
        self._fluid = True
        return self
    
    def with_id(self, id: str) -> 'ImageBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the image component"""
        classes = ["bd-image"]
        
        if self._rounded:
            classes.append("bd-rounded")
        if self._circle:
            classes.append("bd-rounded-full")
        if self._thumbnail:
            classes.append("bd-thumbnail")
        if self._fluid:
            classes.append("bd-w-full")
        
        props = {
            "src": self._src,
            "alt": self._alt
        }
        
        if self._width:
            props["width"] = self._width
        if self._height:
            props["height"] = self._height
        
        return Component(
            type="img",
            classes=classes,
            props=props,
            children=None,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
