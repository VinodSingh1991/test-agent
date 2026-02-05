"""
Training Data Builder

Builder for creating training data with fluent API.
Single Responsibility: Build TrainingData objects only.
"""

from typing import Dict, Any, Union
from design_system_agent.core.dataset_genertor.component_layout.builder.models import TrainingData, Layout
from design_system_agent.core.dataset_genertor.component_layout.builder.layout_builder import LayoutBuilder


class TrainingDataBuilder:
    """Builder for TrainingData with fluent interface"""
    
    def __init__(self, query: str):
        """
        Initialize TrainingDataBuilder
        
        Args:
            query: User query/prompt
        """
        self._query = query
        self._layout: Layout = None
    
    def with_layout(self, layout: Union[Layout, LayoutBuilder]) -> 'TrainingDataBuilder':
        """
        Set the layout for this training data
        
        Args:
            layout: Layout or LayoutBuilder instance
            
        Returns:
            Self for method chaining
        """
        if isinstance(layout, LayoutBuilder):
            self._layout = layout.build()
        else:
            self._layout = layout
        return self
    
    def build(self) -> TrainingData:
        """
        Build and return the TrainingData
        
        Returns:
            TrainingData instance
        """
        if self._layout is None:
            raise ValueError("TrainingData must have a layout. Use with_layout() to set it.")
        
        return TrainingData(
            query=self._query,
            layout=self._layout
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Build and convert to dictionary
        
        Returns:
            Dictionary representation
        """
        return self.build().to_dict()
