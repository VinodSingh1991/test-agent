"""
Row Builder

Builder for creating rows with fluent API.
Single Responsibility: Build Row objects only.
"""

from typing import Dict, Any, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Row, Column
from design_system_agent.core.dataset_genertor.component_layout.builder.column_builder import ColumnBuilder


class RowBuilder:
    """Builder for Row with fluent interface"""
    
    def __init__(self, row_id: str, row_name: str):
        """
        Initialize RowBuilder
        
        Args:
            row_id: Row ID
            row_name: Row name
        """
        self._id = row_id
        self._name = row_name
        self._cols: List[Column] = []
    
    def add_column(self, column: Union[Column, ColumnBuilder]) -> 'RowBuilder':
        """
        Add a column to this row
        
        Args:
            column: Column or ColumnBuilder instance
            
        Returns:
            Self for method chaining
        """
        if isinstance(column, ColumnBuilder):
            self._cols.append(column.build())
        else:
            self._cols.append(column)
        return self
    
    def add_columns(self, *columns: Union[Column, ColumnBuilder]) -> 'RowBuilder':
        """
        Add multiple columns to this row
        
        Args:
            *columns: Column or ColumnBuilder instances
            
        Returns:
            Self for method chaining
        """
        for column in columns:
            self.add_column(column)
        return self
    
    def build(self) -> Row:
        """
        Build and return the Row
        
        Returns:
            Row instance
        """
        return Row(
            id=self._id,
            name=self._name,
            cols=self._cols.copy()
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation with PascalCase keys
        """
        return self.build().to_dict()
