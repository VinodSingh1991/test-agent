"""
Table Builder

Builder for creating table components.
Single Responsibility: Build tables with headers and rows.
"""

from typing import Dict, Any, Optional, List
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


class TableBuilder:
    """Builder for Table components with fluent interface"""
    
    def __init__(self):
        """Initialize TableBuilder"""
        self._headers: List[str] = []
        self._rows: List[List[str]] = []
        self._striped = False
        self._bordered = True
        self._hoverable = False
        self._compact = False
        self._id: Optional[str] = None
    
    def set_headers(self, *headers: str) -> 'TableBuilder':
        """Set table headers"""
        self._headers = list(headers)
        return self
    
    def add_row(self, *cells: str) -> 'TableBuilder':
        """Add table row"""
        self._rows.append(list(cells))
        return self
    
    def striped(self) -> 'TableBuilder':
        """Enable striped rows"""
        self._striped = True
        return self
    
    def no_border(self) -> 'TableBuilder':
        """Remove borders"""
        self._bordered = False
        return self
    
    def hoverable(self) -> 'TableBuilder':
        """Enable row hover effect"""
        self._hoverable = True
        return self
    
    def compact(self) -> 'TableBuilder':
        """Use compact spacing"""
        self._compact = True
        return self
    
    def with_id(self, id: str) -> 'TableBuilder':
        """Set component ID"""
        self._id = id
        return self
    
    def build(self) -> Component:
        """Build the table component"""
        classes = ["bd-table"]
        
        if self._striped:
            classes.append("bd-table-striped")
        if self._bordered:
            classes.append("bd-table-bordered")
        if self._hoverable:
            classes.append("bd-table-hover")
        if self._compact:
            classes.append("bd-table-compact")
        
        children = []
        
        # Table header
        if self._headers:
            header_cells = []
            for header in self._headers:
                header_cells.append({
                    "type": "th",
                    "classes": ["bd-table-header-cell", "bd-fw-semibold", "bd-p-12"],
                    "children": header
                })
            
            children.append({
                "type": "thead",
                "classes": ["bd-table-header"],
                "children": {
                    "type": "tr",
                    "children": header_cells
                }
            })
        
        # Table body
        if self._rows:
            body_rows = []
            for row_data in self._rows:
                row_cells = []
                for cell in row_data:
                    row_cells.append({
                        "type": "td",
                        "classes": ["bd-table-cell", "bd-p-12"],
                        "children": cell
                    })
                
                body_rows.append({
                    "type": "tr",
                    "classes": ["bd-table-row"],
                    "children": row_cells
                })
            
            children.append({
                "type": "tbody",
                "classes": ["bd-table-body"],
                "children": body_rows
            })
        
        return Component(
            type="table",
            classes=classes,
            props={},
            children=children,
            id=self._id
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build().to_dict()
