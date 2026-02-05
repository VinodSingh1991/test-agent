"""
Tab Builder

Builder for creating tabs with fluent API.
Single Responsibility: Build Tab objects only.
"""

from typing import Dict, Any, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Tab, Section
from design_system_agent.core.dataset_genertor.component_layout.builder.section_builder import SectionBuilder


class TabBuilder:
    """Builder for Tab with fluent interface"""
    
    def __init__(self, tab_name: str, tab_id: str):
        """
        Initialize TabBuilder
        
        Args:
            tab_name: Tab name
            tab_id: Tab ID
        """
        self._name = tab_name
        self._id = tab_id
        self._sections: List[Section] = []
    
    def add_section(self, section: Union[Section, SectionBuilder]) -> 'TabBuilder':
        """
        Add a section to this tab
        
        Args:
            section: Section or SectionBuilder instance
            
        Returns:
            Self for method chaining
        """
        if isinstance(section, SectionBuilder):
            self._sections.append(section.build())
        else:
            self._sections.append(section)
        return self
    
    def add_sections(self, *sections: Union[Section, SectionBuilder]) -> 'TabBuilder':
        """
        Add multiple sections to this tab
        
        Args:
            *sections: Section or SectionBuilder instances
            
        Returns:
            Self for method chaining
        """
        for section in sections:
            self.add_section(section)
        return self
    
    def build(self) -> Tab:
        """
        Build and return the Tab
        
        Returns:
            Tab instance
        """
        return Tab(
            name=self._name,
            id=self._id,
            sections=self._sections.copy()
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation with PascalCase keys
        """
        return self.build().to_dict()
