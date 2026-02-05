"""
Script to generate corrected component patterns with proper builder constructor signatures
"""
import os
from pathlib import Path

# Get the component base directory
base_dir = Path(__file__).parent / "design_system_agent" / "core" / "dataset_genertor"

# Define corrected patterns for all 21 components

HEADING_PATTERNS = '''"""
Preset heading patterns for common use cases
"""
from .heading_builder import HeadingBuilder

# Size-based patterns
H1_HEADING = HeadingBuilder("Main Heading", 1).build()
H2_HEADING = HeadingBuilder("Section Heading", 2).build()
H3_HEADING = HeadingBuilder("Subsection Heading", 3).build()
H4_HEADING = HeadingBuilder("Detail Heading", 4).build()
H5_HEADING = HeadingBuilder("Minor Heading", 5).build()
H6_HEADING = HeadingBuilder("Small Heading", 6).build()

# Common styled patterns
PRIMARY_HEADING = HeadingBuilder("Primary Heading", 2).color("primary").build()
SECONDARY_HEADING = HeadingBuilder("Secondary Heading", 3).color("secondary").build()
DANGER_HEADING = HeadingBuilder("Danger Heading", 3).color("danger").build()

# Weight variations  
BOLD_HEADING = HeadingBuilder("Bold Heading", 2).weight("bold").build()
SEMIBOLD_HEADING = HeadingBuilder("Semibold Heading", 3).weight("semibold").build()
LIGHT_HEADING = HeadingBuilder("Light Heading", 4).weight("light").build()

# Common use cases
PAGE_TITLE = HeadingBuilder("Page Title", 1).weight("bold").color("primary").build()
SECTION_TITLE = HeadingBuilder("Section Title", 2).weight("semibold").build()
CARD_TITLE = HeadingBuilder("Card Title", 3).weight("semibold").build()
PANEL_TITLE = HeadingBuilder("Panel Title", 4).weight("medium").build()

# All patterns
ALL_HEADING_PATTERNS = {
    "h1": H1_HEADING,
    "h2": H2_HEADING,
    "h3": H3_HEADING,
    "h4": H4_HEADING,
    "h5": H5_HEADING,
    "h6": H6_HEADING,
    "primary": PRIMARY_HEADING,
    "secondary": SECONDARY_HEADING,
    "danger": DANGER_HEADING,
    "bold": BOLD_HEADING,
    "semibold": SEMIBOLD_HEADING,
    "light": LIGHT_HEADING,
    "page_title": PAGE_TITLE,
    "section_title": SECTION_TITLE,
    "card_title": CARD_TITLE,
    "panel_title": PANEL_TITLE,
}
'''

DESCRIPTION_PATTERNS = '''"""
Preset description patterns for common use cases
"""
from .description_builder import DescriptionBuilder

# Size patterns
SMALL_DESCRIPTION = DescriptionBuilder("Small descriptive text").small().build()
MEDIUM_DESCRIPTION = DescriptionBuilder("Medium descriptive text").medium().build()
LARGE_DESCRIPTION = DescriptionBuilder("Large descriptive text").large().build()

# Common use cases
FIELD_DESCRIPTION = DescriptionBuilder("Field description text").small().build()
SECTION_DESCRIPTION = DescriptionBuilder("Section description text").medium().build()
HELP_TEXT = DescriptionBuilder("Help text for users").small().muted().build()
MUTED_TEXT = DescriptionBuilder("Muted secondary text").muted().build()

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
'''

TEXT_PATTERNS = '''"""
Preset text patterns for common use cases
"""
from .text_builder import TextBuilder

# Size patterns
EXTRA_SMALL_TEXT = TextBuilder("Extra small text").size("xs").build()
SMALL_TEXT = TextBuilder("Small text").size("sm").build()
MEDIUM_TEXT = TextBuilder("Medium text").size("md").build()
LARGE_TEXT = TextBuilder("Large text").size("lg").build()
EXTRA_LARGE_TEXT = TextBuilder("Extra large text").size("xl").build()

# Weight patterns
LIGHT_TEXT = TextBuilder("Light text").weight("light").build()
NORMAL_TEXT = TextBuilder("Normal text").weight("normal").build()
MEDIUM_WEIGHT_TEXT = TextBuilder("Medium text").weight("medium").build()
BOLD_TEXT = TextBuilder("Bold text").weight("bold").build()

# Color patterns
PRIMARY_TEXT = TextBuilder("Primary text").color("primary").build()
SECONDARY_TEXT = TextBuilder("Secondary text").color("secondary").build()
SUCCESS_TEXT = TextBuilder("Success text").color("success").build()
DANGER_TEXT = TextBuilder("Danger text").color("danger").build()

# Style patterns
ITALIC_TEXT = TextBuilder("Italic text").italic().build()
UNDERLINED_TEXT = TextBuilder("Underlined text").underline().build()

# Common combinations
LABEL_TEXT = TextBuilder("Label").size("sm").weight("medium").build()
VALUE_TEXT = TextBuilder("Value").size("md").weight("normal").build()
HINT_TEXT = TextBuilder("Hint").size("xs").color("secondary").build()
ERROR_TEXT = TextBuilder("Error").size("sm").color("danger").build()

# All patterns
ALL_TEXT_PATTERNS = {
    "xs": EXTRA_SMALL_TEXT,
    "sm": SMALL_TEXT,
    "md": MEDIUM_TEXT,
    "lg": LARGE_TEXT,
    "xl": EXTRA_LARGE_TEXT,
    "light": LIGHT_TEXT,
    "normal": NORMAL_TEXT,
    "medium": MEDIUM_WEIGHT_TEXT,
    "bold": BOLD_TEXT,
    "primary": PRIMARY_TEXT,
    "secondary": SECONDARY_TEXT,
    "success": SUCCESS_TEXT,
    "danger": DANGER_TEXT,
    "italic": ITALIC_TEXT,
    "underlined": UNDERLINED_TEXT,
    "label": LABEL_TEXT,
    "value": VALUE_TEXT,
    "hint": HINT_TEXT,
    "error": ERROR_TEXT,
}
'''

LINK_PATTERNS = '''"""
Preset link patterns for common use cases
"""
from .link_builder import LinkBuilder

# Variant patterns
PRIMARY_LINK = LinkBuilder("Primary Link").variant("primary").build()
SECONDARY_LINK = LinkBuilder("Secondary Link").variant("secondary").build()
MUTED_LINK = LinkBuilder("Muted Link").variant("muted").build()

# External link patterns
EXTERNAL_LINK = LinkBuilder("External Link", "https://example.com").external().build()
EXTERNAL_PRIMARY_LINK = LinkBuilder("External", "https://example.com").variant("primary").external().build()

# Icon patterns
LINK_WITH_ICON = LinkBuilder("Link with Icon").icon("LinkIcon").build()
EXTERNAL_ICON_LINK = LinkBuilder("Visit", "https://example.com").icon("ExternalLinkIcon").external().build()

# Underline patterns
UN DER_LINK = LinkBuilder("Underlined Link").underline().build()
NO_UNDERLINE_LINK = LinkBuilder("No Underline Link").no_underline().build()

# Common use cases
NAV_LINK = LinkBuilder("Navigation").variant("primary").no_underline().build()
FOOTER_LINK = LinkBuilder("Footer Link").variant("secondary").build()
INLINE_LINK = LinkBuilder("inline link").underline().build()
CTA_LINK = LinkBuilder("Learn More →").variant("primary").build()
DOC_LINK = LinkBuilder("Documentation", "https://docs.example.com").external().build()

# All patterns
ALL_LINK_PATTERNS = {
    "primary": PRIMARY_LINK,
    "secondary": SECONDARY_LINK,
    "muted": MUTED_LINK,
    "external": EXTERNAL_LINK,
    "external_primary": EXTERNAL_PRIMARY_LINK,
    "with_icon": LINK_WITH_ICON,
    "external_icon": EXTERNAL_ICON_LINK,
    "underlined": UNDERLINED_LINK,
    "no_underline": NO_UNDERLINE_LINK,
    "nav": NAV_LINK,
    "footer": FOOTER_LINK,
    "inline": INLINE_LINK,
    "cta": CTA_LINK,
    "doc": DOC_LINK,
}
'''

# Write patterns to files
patterns = {
    "component_heading": HEADING_PATTERNS,
    "component_description": DESCRIPTION_PATTERNS,
    "component_text": TEXT_PATTERNS,
    "component_link": LINK_PATTERNS,
}

for component_name, pattern_content in patterns.items():
    pattern_file = base_dir / component_name / "patterns.py"
    print(f"Writing {pattern_file}...")
    with open(pattern_file, "w", encoding="utf-8") as f:
        f.write(pattern_content)

print("\\n✅ Typography patterns corrected!")
print("Run this script again after adding more pattern definitions above.")
