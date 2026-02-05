"""
Section Builder

Builder for creating sections with fluent API.
Single Responsibility: Build Section objects only.
"""

from typing import Dict, Any, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Section, Row
from design_system_agent.core.dataset_genertor.component_layout.builder.row_builder import RowBuilder


class SectionBuilder:
    """Builder for Section with fluent interface"""
    
    def __init__(self, section_name: str, section_id: str):
        """
        Initialize SectionBuilder
        
        Args:
            section_name: Section name
            section_id: Section ID
        """
        self._name = section_name
        self._id = section_id
        self._rows: List[Row] = []
    
    def add_row(self, row: Union[Row, RowBuilder]) -> 'SectionBuilder':
        """
        Add a row to this section
        
        Args:
            row: Row or RowBuilder instance
            
        Returns:
            Self for method chaining
        """
        if isinstance(row, RowBuilder):
            self._rows.append(row.build())
        else:
            self._rows.append(row)
        return self
    
    def add_rows(self, *rows: Union[Row, RowBuilder]) -> 'SectionBuilder':
        """
        Add multiple rows to this section
        
        Args:
            *rows: Row or RowBuilder instances
            
        Returns:
            Self for method chaining
        """
        for row in rows:
            self.add_row(row)
        return self
    
    def build(self) -> Section:
        """
        Build and return the Section
        
        Returns:
            Section instance
        """
        return Section(
            name=self._name,
            id=self._id,
            rows=self._rows.copy()
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation with PascalCase keys
        """
        return self.build().to_dict()
