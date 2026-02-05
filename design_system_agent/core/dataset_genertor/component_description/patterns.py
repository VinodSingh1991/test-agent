"""
Preset description patterns for common use cases
"""
from .description_builder import DescriptionBuilder

# Size patterns
SMALL_DESCRIPTION = DescriptionBuilder("Small descriptive text").small().build()
MEDIUM_DESCRIPTION = DescriptionBuilder("Medium descriptive text").medium().build()
LARGE_DESCRIPTION = DescriptionBuilder("Large descriptive text").large().build()

# Common use cases
FIELD_DESCRIPTION = DescriptionBuilder("Field description").small().build()
SECTION_DESCRIPTION = DescriptionBuilder("Section description").medium().build()
HELP_TEXT = DescriptionBuilder("Help text").small().muted().build()
MUTED_TEXT = DescriptionBuilder("Muted text").muted().build()

# All patterns
ALL_DESCRIPTION_PATTERNS = {
    "small": SMALL_DESCRIPTION,
    "medium": MEDIUM_DESCRIPTION,
    "large": LARGE_DESCRIPTION,
    "field": FIELD_DESCRIPTION,
    "section": SECTION_DESCRIPTION,
    "help": HELP_TEXT,
    "muted": MUTED_TEXT,
}
