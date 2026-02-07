"""
Table Builder

Builder for creating table components.
Single Responsibility: Build tables with headers and rows.
Outputs TypeScript-compatible ComponentTableProps.
"""

from typing import Dict,Any, Optional, List


class TableBuilder:
    """Builder for Table components with fluent interface"""
    
    def __init__(self):
        """Initialize TableBuilder"""
        self._type = "Table"
        self._columns = []
        self._rows = []
        self._additional_info = ""
        self._props = {
            "bordered": False,
            "striped": False,
            "hoverable": True,
            "loading": False
        }
        self._events = {}
        self._classes = []
    
    def columns(self, columns: List[Dict[str, Any]]) -> 'TableBuilder':
        """
        Set table columns
        Each column: {key, title, dataIndex?, width?, align?, sortable?, render?}
        """
        self._columns = columns
        return self
    
    def set_columns(self, *column_titles: str) -> 'TableBuilder':
        """
        Set simple columns from titles
        
        Args:
            *column_titles: Column header titles
        """
        self._columns = [
            {"key": title.lower().replace(" ", "_"), "title": title}
            for title in column_titles
        ]
        return self
    
    def set_headers(self, *headers: str) -> 'TableBuilder':
        """Set table headers (alias for set_columns)"""
        return self.set_columns(*headers)
    
    def data(self, data: List[Dict[str, Any]]) -> 'TableBuilder':
        """Set table data (array of records)"""
        self._rows = data
        return self
    
    def add_row(self, row_data: Dict[str, Any]) -> 'TableBuilder':
        """Add a row to table data"""
        self._rows.append(row_data)
        return self
    
    def row_key(self, key: str) -> 'TableBuilder':
        """Set row key field"""
        self._props["rowKey"] = key
        return self
    
    def pagination(self, enabled: bool = True, page_size: int = 10) -> 'TableBuilder':
        """Enable pagination"""
        self._props["pagination"] = {
            "enabled": enabled,
            "pageSize": page_size
        }
        return self
    
    def bordered(self, bordered: bool = True) -> 'TableBuilder':
        """Add borders"""
        self._props["bordered"] = bordered
        return self
    
    def no_border(self) -> 'TableBuilder':
        """Remove borders"""
        self._props["bordered"] = False
        return self
    
    def striped(self, striped: bool = True) -> 'TableBuilder':
        """Make rows striped"""
        self._props["striped"] = striped
        return self
    
    def hoverable(self, hoverable: bool = True) -> 'TableBuilder':
        """Enable hover effect"""
        self._props["hoverable"] = hoverable
        return self
    
    def compact(self, compact: bool = True) -> 'TableBuilder':
        """Use compact spacing"""
        self._props["compact"] = compact
        return self
    
    def loading(self, loading: bool = True) -> 'TableBuilder':
        """Set loading state"""
        self._props["loading"] = loading
        return self
    
    def empty_text(self, text: str) -> 'TableBuilder':
        """Set empty state text"""
        self._props["emptyText"] = text
        return self
    
    def size(self, size: str) -> 'TableBuilder':
        """Set size: sm, md, lg"""
        self._props["size"] = size
        return self
    
    def with_id(self, id: str) -> 'TableBuilder':
        """Set component ID"""
        self._props["id"] = id
        return self
    
    def with_classes(self, *classes: str) -> 'TableBuilder':
        """Add custom CSS classes"""
        self._classes.extend(classes)
        return self
    
    def additional_info(self, info: str) -> 'TableBuilder':
        """Set additional info"""
        self._additional_info = info
        return self
    
    def on_row_click(self, handler: str) -> 'TableBuilder':
        """Set row click event handler"""
        self._events["onRowClick"] = handler
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the table component"""
        props = self._props.copy()
        if self._classes:
            props["className"] = " ".join(self._classes)
        
        result = {
            "type": self._type,
            "props": props,
            "value": {
                "columns": self._columns,
                "rows": self._rows,
                "additionalInfo": self._additional_info
            }
        }
        
        if self._events:
            result["events"] = self._events.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Build and convert to dictionary"""
        return self.build()
