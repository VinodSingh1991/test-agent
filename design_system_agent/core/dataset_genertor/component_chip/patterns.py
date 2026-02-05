"""
Chip pattern factory functions for common use cases
"""
from .chip_builder import ChipBuilder
from design_system_agent.core.dataset_genertor.component_layout.builder.models import Component


def primary_chip(text: str) -> Component:
    """Primary chip/tag"""
    return ChipBuilder(text).primary().build()


def secondary_chip(text: str) -> Component:
    """Secondary chip/tag"""
    return ChipBuilder(text).secondary().build()


def success_chip(text: str) -> Component:
    """Success chip/tag"""
    return ChipBuilder(text).success().build()


def warning_chip(text: str) -> Component:
    """Warning chip/tag"""
    return ChipBuilder(text).warning().build()


def danger_chip(text: str) -> Component:
    """Danger chip/tag"""
    return ChipBuilder(text).danger().build()
