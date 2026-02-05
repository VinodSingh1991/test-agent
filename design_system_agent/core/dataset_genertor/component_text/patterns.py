"""
Text pattern factory functions for common use cases
"""
from .text_builder import TextBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def body_text(text: str) -> Component:
    """Standard body text"""
    return TextBuilder(text).build()


def small_text(text: str) -> Component:
    """Small text"""
    return TextBuilder(text).small().build()


def bold_text(text: str) -> Component:
    """Bold text"""
    return TextBuilder(text).bold().build()


def muted_text(text: str) -> Component:
    """Muted/secondary text"""
    return TextBuilder(text).muted().build()
