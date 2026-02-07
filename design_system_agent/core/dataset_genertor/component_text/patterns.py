"""
Text pattern factory functions for common use cases
"""
from .text_builder import TextBuilder
from typing import Dict, Any


def body_text(text: str) -> Dict[str, Any]:
    """Standard body text"""
    return TextBuilder(text).build()


def small_text(text: str) -> Dict[str, Any]:
    """Small text"""
    return TextBuilder(text).small().build()


def bold_text(text: str) -> Dict[str, Any]:
    """Bold text"""
    return TextBuilder(text).bold().build()


def muted_text(text: str) -> Dict[str, Any]:
    """Muted/secondary text"""
    return TextBuilder(text).muted().build()
