"""
Preset list patterns for common use cases
"""
from .list_builder import ListBuilder

# Ordered vs Unordered
ORDERED_LIST = ListBuilder().ordered().add_item("First item").add_item("Second item").add_item("Third item").build()
UNORDERED_LIST = ListBuilder().add_item("Item one").add_item("Item two").add_item("Item three").build()

# With icons
ICON_LIST = ListBuilder().add_item_with_icon("CheckIcon", "Completed task").add_item_with_icon("CheckIcon", "Another task").build()
CHECK_LIST = ListBuilder().add_item_with_icon("CheckCircleIcon", "Feature one").add_item_with_icon("CheckCircleIcon", "Feature two").build()
BULLET_LIST = ListBuilder().add_item_with_icon("DotIcon", "Point one").add_item_with_icon("DotIcon", "Point two").build()

# Common use cases
FEATURE_LIST = ListBuilder().add_item_with_icon("CheckIcon", "Fast performance").add_item_with_icon("CheckIcon", "Easy to use").add_item_with_icon("CheckIcon", "Secure").build()
TODO_LIST = ListBuilder().ordered().add_item("Complete task 1").add_item("Review task 2").add_item("Submit task 3").build()
NAVIGATION_LIST = ListBuilder().add_item("Home").add_item("About").add_item("Contact").build()
STEPS_LIST = ListBuilder().ordered().add_item("Sign up").add_item("Verify email").add_item("Complete profile").build()

# Different lengths
SHORT_LIST = ListBuilder().add_item("Item 1").add_item("Item 2").build()
MEDIUM_LIST = ListBuilder().add_item("Item 1").add_item("Item 2").add_item("Item 3").add_item("Item 4").add_item("Item 5").build()
LONG_LIST = ListBuilder().add_item("Item 1").add_item("Item 2").add_item("Item 3").add_item("Item 4").add_item("Item 5").add_item("Item 6").add_item("Item 7").add_item("Item 8").build()

# All patterns
ALL_LIST_PATTERNS = {
    "ordered": ORDERED_LIST,
    "unordered": UNORDERED_LIST,
    "icon": ICON_LIST,
    "check": CHECK_LIST,
    "bullet": BULLET_LIST,
    "features": FEATURE_LIST,
    "todo": TODO_LIST,
    "navigation": NAVIGATION_LIST,
    "steps": STEPS_LIST,
    "short": SHORT_LIST,
    "medium": MEDIUM_LIST,
    "long": LONG_LIST,
}
