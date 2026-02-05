"""
Badge pattern factory functions for common use cases
"""
from .badge_builder import BadgeBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def success_badge(text: str, pill: bool = False) -> Component:
    """Success status badge"""
    builder = BadgeBuilder(text).success()
    if pill:
        builder.pill_shape()
    return builder.build()


def warning_badge(text: str, pill: bool = False) -> Component:
    """Warning status badge"""
    builder = BadgeBuilder(text).warning()
    if pill:
        builder.pill_shape()
    return builder.build()


def danger_badge(text: str, pill: bool = False) -> Component:
    """Danger/error status badge"""
    builder = BadgeBuilder(text).danger()
    if pill:
        builder.pill_shape()
    return builder.build()


def info_badge(text: str, pill: bool = False) -> Component:
    """Info status badge"""
    builder = BadgeBuilder(text).info()
    if pill:
        builder.pill_shape()
    return builder.build()


def primary_badge(text: str, pill: bool = False) -> Component:
    """Primary status badge"""
    builder = BadgeBuilder(text).primary()
    if pill:
        builder.pill_shape()
    return builder.build()


def secondary_badge(text: str, pill: bool = False) -> Component:
    """Secondary status badge"""
    builder = BadgeBuilder(text).secondary()
    if pill:
        builder.pill_shape()
    return builder.build()
