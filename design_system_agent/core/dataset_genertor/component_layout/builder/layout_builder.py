"""
Layout Builder

Builder for creating complete layouts with fluent API.
Single Responsibility: Build Layout objects only.
"""

from typing import Dict, Any, List, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Layout, Tab
from design_system_agent.core.dataset_genertor.component_layout.builder.tab_builder import TabBuilder


class LayoutBuilder:
    """Builder for Layout with fluent interface"""
    
    def __init__(self):
        """Initialize LayoutBuilder"""
        self._tabs: List[Tab] = []
    
    def add_tab(self, tab: Union[Tab, TabBuilder]) -> 'LayoutBuilder':
        """
        Add a tab to this layout
        
        Args:
            tab: Tab or TabBuilder instance
            
        Returns:
            Self for method chaining
        """
        if isinstance(tab, TabBuilder):
            self._tabs.append(tab.build())
        else:
            self._tabs.append(tab)
        return self
    
    def add_tabs(self, *tabs: Union[Tab, TabBuilder]) -> 'LayoutBuilder':
        """
        Add multiple tabs to this layout
        
        Args:
            *tabs: Tab or TabBuilder instances
            
        Returns:
            Self for method chaining
        """
        for tab in tabs:
            self.add_tab(tab)
        return self
    
    def build(self) -> Layout:
        """
        Build and return the Layout
        
        Returns:
            Layout instance
        """
        return Layout(tabs=self._tabs.copy())
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation with PascalCase keys
        """
        return self.build().to_dict()
