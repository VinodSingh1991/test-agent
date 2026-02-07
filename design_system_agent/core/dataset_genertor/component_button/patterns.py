"""
Button pattern factory functions for common use cases
"""
from typing import Optional, Dict, Any
from .button_builder import ButtonBuilder



def primary_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Primary action button"""
    builder = ButtonBuilder(text).primary()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def secondary_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Secondary action button"""
    builder = ButtonBuilder(text).secondary()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def danger_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Dangerous action button (delete, remove, etc.)"""
    builder = ButtonBuilder(text).danger()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def success_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Success action button (save, confirm, etc.)"""
    builder = ButtonBuilder(text).success()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def warning_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Warning action button"""
    builder = ButtonBuilder(text).warning()
    if icon:
        builder.with_icon(icon)
    return builder.build()


def outline_button(text: str, icon: Optional[str] = None) -> Dict[str, Any]:
    """Outline variant button"""
    builder = ButtonBuilder(text).outline()
    if icon:
        builder.with_icon(icon)
    return builder.build()
