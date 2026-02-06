"""
Data Models for Component Layout

This module defines the data structures for the hierarchical layout:
Tabs → Sections → Rows → Cols → Children
"""

from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field


@dataclass
class Component:
    """Represents a UI component with type, classes, props, children/value, events"""
    type: str
    classes: List[str] = field(default_factory=list)
    props: Dict[str, Any] = field(default_factory=dict)
    children: Optional[Union[str, List[Any], Dict[str, Any]]] = None
    value: Optional[Dict[str, str]] = None  # For primitive components: {icon: "", text: ""}
    events: Optional[Dict[str, str]] = None
    id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "type": self.type,
            "classes": self.classes,
            "props": self.props,
        }
        # Use value for primitive components, children for complex components
        if self.value is not None:
            result["value"] = self.value
        elif self.children is not None:
            result["children"] = self.children
        if self.events:
            result["events"] = self.events
        if self.id:
            result["id"] = self.id
        return result


@dataclass
class Column:
    """Represents a column within a row"""
    name: str
    id: str
    children: Union[Component, Dict[str, Any]]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with PascalCase keys"""
        children_dict = self.children.to_dict() if isinstance(self.children, Component) else self.children
        return {
            "ColsName": self.name,
            "ColsId": self.id,
            "Children": children_dict
        }


@dataclass
class Row:
    """Represents a row within a section"""
    id: str
    name: str
    cols: List[Column] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with PascalCase keys"""
        return {
            "RowId": self.id,
            "RowName": self.name,
            "Cols": [col.to_dict() for col in self.cols]
        }


@dataclass
class Section:
    """Represents a section within a tab"""
    name: str
    id: str
    rows: List[Row] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with PascalCase keys"""
        return {
            "SectionName": self.name,
            "SectionId": self.id,
            "Rows": [row.to_dict() for row in self.rows]
        }


@dataclass
class Tab:
    """Represents a tab in the layout"""
    name: str
    id: str
    sections: List[Section] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with PascalCase keys"""
        return {
            "TabName": self.name,
            "TabId": self.id,
            "Sections": [section.to_dict() for section in self.sections]
        }


@dataclass
class Layout:
    """Root layout structure"""
    tabs: List[Tab] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with PascalCase keys"""
        return {
            "Tabs": [tab.to_dict() for tab in self.tabs]
        }


@dataclass
class TrainingData:
    """Training data with query and layout"""
    query: str
    layout: Layout
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "query": self.query,
            "layout": self.layout.to_dict()
        }
