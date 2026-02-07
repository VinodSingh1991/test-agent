"""
Badge pattern factory functions for common use cases
"""
from typing import Dict, Any
from .badge_builder import BadgeBuilder


def success_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Success status badge"""
    builder = BadgeBuilder(text).success()
    if pill:
        builder.pill_shape()
    return builder.build()


def warning_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Warning status badge"""
    builder = BadgeBuilder(text).warning()
    if pill:
        builder.pill_shape()
    return builder.build()


def danger_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Danger/error status badge"""
    builder = BadgeBuilder(text).danger()
    if pill:
        builder.pill_shape()
    return builder.build()


def info_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Info status badge"""
    builder = BadgeBuilder(text).info()
    if pill:
        builder.pill_shape()
    return builder.build()


def primary_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Primary status badge"""
    builder = BadgeBuilder(text).primary()
    if pill:
        builder.pill_shape()
    return builder.build()


def secondary_badge(text: str, pill: bool = False) -> Dict[str, Any]:
    """Secondary status badge"""
    builder = BadgeBuilder(text).secondary()
    if pill:
        builder.pill_shape()
    return builder.build()
