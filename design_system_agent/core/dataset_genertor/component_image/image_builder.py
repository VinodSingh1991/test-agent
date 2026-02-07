"""
Image Builder

Builder for creating image components.
Single Responsibility: Build images with variants and aspect ratios.
Outputs TypeScript-compatible ComponentImageProps.
"""

from typing import Dict, Any, Optional, Union


class ImageBuilder:
    """Builder for Image components with fluent interface"""
    
    def __init__(self, src: str, alt: str = ""):
        """Initialize ImageBuilder"""
        self._props = {
            "type": "Image",
            "src": src,
            "alt": alt
        }
        self._classes = []
    
    def width(self, width: Union[str, int]) -> 'ImageBuilder':
        """Set width"""
        self._props["width"] = width
        return self
    
    def height(self, height: Union[str, int]) -> 'ImageBuilder':
        """Set height"""
        self._props["height"] = height
        return self
    
    def with_size(self, width: Union[str, int], height: Optional[Union[str, int]] = None) -> 'ImageBuilder':
        """Set image size"""
        self._props["width"] = width
        self._props["height"] = height or width
        return self
    
    def aspect_ratio(self, ratio: str) -> 'ImageBuilder':
        """Set aspect ratio: square, video, portrait, landscape"""
        self._props["aspectRatio"] = ratio
        return self
    
    def object_fit(self, fit: str) -> 'ImageBuilder':
        """Set object fit: cover, contain, fill, none"""
        self._props["objectFit"] = fit
        return self
    
    def rounded(self, rounded: Union[bool, str] = True) -> 'ImageBuilder':
        """Add rounded corners. Can be bool or string (sm, md, lg, full)"""
        if isinstance(rounded, bool):
            self._props["rounded"] = "md" if rounded else None
        else:
            self._props["rounded"] = rounded
        return self
    
    def circle(self) -> 'ImageBuilder':
        """Make image circular"""
        self._props["rounded"] = "full"
        return self
    
    def loading(self, loading: str) -> 'ImageBuilder':
        """Set loading: lazy, eager"""
        self._props["loading"] = loading
        return self
    
    def thumbnail(self, thumbnail: bool = True) -> 'ImageBuilder':
        """Add thumbnail border"""
        self._props["thumbnail"] = thumbnail
        return self
    
    def fluid(self, fluid: bool = True) -> 'ImageBuilder':
        """Make image responsive (100% width)"""
        self._props["fluid"] = fluid
        return self
    
    def with_id(self, id: str) -> 'ImageBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'ImageBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the image component"""
        if self._classes:
            self._props["className"] = " ".join(self._classes) 
        return self._props.copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
