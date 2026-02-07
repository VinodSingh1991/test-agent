"""
Label pattern factory functions for common use cases
"""
from .label_builder import LabelBuilder
from typing import Dict, Any


def form_label(text: str, required: bool = False) -> Dict[str, Any]:
    """Form field label"""
    builder = LabelBuilder(text)
    if required:
        builder.required()
    return builder.build()


def bold_label(text: str) -> Dict[str, Any]:
    """Bold label for emphasis"""
    return LabelBuilder(text).bold().build()
