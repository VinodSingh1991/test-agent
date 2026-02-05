"""
Card Builder

Builder for creating card components with header, body, footer.
Single Responsibility: Build card containers with sections.
"""

from typing import Dict, Any, Optional, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class CardBuilder:
    """Builder for Card components with fluent interface"""
    
    def __init__(self, title: Optional[str] = None):
        """
        Initialize CardBuilder
        
        Args:
            title: Optional card title
        """
        self._title = title
        self._header: Optional[Union[str, Dict, Component]] = None
        self._body: List[Union[str, Dict, Component]] = []
        self._footer: Optional[Union[str, Dict, Component]] = None
        self._variant = "default"
        self._elevated = False
        self._bordered = True
        self._id: Optional[str] = None
    
    def with_header(self, content: Union[str, Dict, Component]) -> 'CardBuilder':
        """
        Add header to card
        
        Args:
            content: Header content
        """
        self._header = content
        return self
    
    def add_body_content(self, *content: Union[str, Dict, Component]) -> 'CardBuilder':
        """
        Add content to card body
        
        Args:
            content: Body content items
        """
        self._body.extend(content)
        return self
    
    def with_footer(self, content: Union[str, Dict, Component]) -> 'CardBuilder':
        """
        Add footer to card
        
        Args:
            content: Footer content
        """
        self._footer = content
        return self
    
    def primary(self) -> 'CardBuilder':
        """Set card variant to primary"""
        self._variant = "primary"
        return self
    
    def elevated(self) -> 'CardBuilder':
        """Add elevation shadow to card"""
        self._elevated = True
        return self
    
    def no_border(self) -> 'CardBuilder':
        """Remove card border"""
        self._bordered = False
        return self
    
    def with_id(self, id: str) -> 'CardBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """
        Build the card component
        
        Returns:
            Component instance
        """
        classes = ["bd-card"]
        
        if self._variant != "default":
            classes.append(f"bd-card-{self._variant}")
        
        if self._elevated:
            classes.append("bd-shadow-lg")
        
        if not self._bordered:
            classes.append("bd-border-none")
        
        children = []
        
        # Add header
        if self._header or self._title:
            header_content = self._header if self._header else self._title
            if isinstance(header_content, Component):
                header_content = header_content.to_dict()
            elif isinstance(header_content, str):
                header_content = {
                    "type": "h3",
                    "classes": ["bd-card-title", "bd-fs-xl", "bd-fw-semibold"],
                    "children": header_content
                }
            
            children.append({
                "type": "div",
                "classes": ["bd-card-header", "bd-p-16", "bd-border-b"],
                "children": header_content
            })
        
        # Add body
        if self._body:
            body_children = []
            for item in self._body:
                if isinstance(item, Component):
                    body_children.append(item.to_dict())
                elif isinstance(item, dict):
                    body_children.append(item)
                else:
                    body_children.append({"type": "p", "children": str(item)})
            
            children.append({
                "type": "div",
                "classes": ["bd-card-body", "bd-p-16"],
                "children": body_children
            })
        
        # Add footer
        if self._footer:
            footer_content = self._footer
            if isinstance(footer_content, Component):
                footer_content = footer_content.to_dict()
            elif isinstance(footer_content, str):
                footer_content = {"type": "p", "classes": ["bd-text-muted"], "children": footer_content}
            
            children.append({
                "type": "div",
                "classes": ["bd-card-footer", "bd-p-16", "bd-border-t"],
                "children": footer_content
            })
        
        return Component(
            type="div",
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
