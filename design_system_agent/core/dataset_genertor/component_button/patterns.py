"""
Button pattern factory functions for common use cases
"""
from typing import Optional
from .button_builder import ButtonBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def primary_button(text: str, icon: Optional[str] = None) -> Component:
    """Primary action button"""
    builder = ButtonBuilder(text).primary()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def secondary_button(text: str, icon: Optional[str] = None) -> Component:
    """Secondary action button"""
    builder = ButtonBuilder(text).secondary()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def danger_button(text: str, icon: Optional[str] = None) -> Component:
    """Dangerous action button (delete, remove, etc.)"""
    builder = ButtonBuilder(text).danger()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def success_button(text: str, icon: Optional[str] = None) -> Component:
    """Success action button (save, confirm, etc.)"""
    builder = ButtonBuilder(text).success()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def warning_button(text: str, icon: Optional[str] = None) -> Component:
    """Warning action button"""
    builder = ButtonBuilder(text).warning()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def outline_button(text: str, icon: Optional[str] = None) -> Component:
    """Outline variant button"""
    builder = ButtonBuilder(text).outline()
    if icon:
        builder.with_icon(icon)
    return builder.build()
