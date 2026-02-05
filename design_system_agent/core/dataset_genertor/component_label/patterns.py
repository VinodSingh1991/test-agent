"""
Label pattern factory functions for common use cases
"""
from .label_builder import LabelBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def form_label(text: str, required: bool = False) -> Component:
    """Form field label"""
    builder = LabelBuilder(text)
    if required:
        builder.required()
    return builder.build()


def bold_label(text: str) -> Component:
    """Bold label for emphasis"""
    return LabelBuilder(text).bold().build()
