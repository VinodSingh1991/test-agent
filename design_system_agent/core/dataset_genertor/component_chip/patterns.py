"""
Chip pattern factory functions for common use cases
"""
from .chip_builder import ChipBuilder
from typing import Dict, Any


def primary_chip(text: str) -> Dict[str, Any]:
    """Primary chip/tag"""
    return ChipBuilder(text).primary().build()


def secondary_chip(text: str) -> Dict[str, Any]:
    """Secondary chip/tag"""
    return ChipBuilder(text).secondary().build()


def success_chip(text: str) -> Dict[str, Any]:
    """Success chip/tag"""
    return ChipBuilder(text).success().build()


def warning_chip(text: str) -> Dict[str, Any]:
    """Warning chip/tag"""
    return ChipBuilder(text).warning().build()


def danger_chip(text: str) -> Dict[str, Any]:
    """Danger chip/tag"""
    return ChipBuilder(text).danger().build()
