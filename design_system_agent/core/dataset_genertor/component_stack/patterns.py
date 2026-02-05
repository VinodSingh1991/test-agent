"""
Preset stack patterns for common use cases
"""
from .stack_builder import StackBuilder

# Direction patterns
VERTICAL_STACK = StackBuilder().vertical().build()
HORIZONTAL_STACK = StackBuilder().horizontal().build()

# Spacing patterns
TIGHT_STACK = StackBuilder().vertical().spacing("tight").build()
NORMAL_STACK = StackBuilder().vertical().spacing("normal").build()
RELAXED_STACK = StackBuilder().vertical().spacing("relaxed").build()

TIGHT_HORIZONTAL = StackBuilder().horizontal().spacing("tight").build()
NORMAL_HORIZONTAL = StackBuilder().horizontal().spacing("normal").build()
RELAXED_HORIZONTAL = StackBuilder().horizontal().spacing("relaxed").build()

# Alignment patterns
START_ALIGNED = StackBuilder().vertical().align("start").build()
CENTER_ALIGNED = StackBuilder().vertical().align("center").build()
END_ALIGNED = StackBuilder().vertical().align("end").build()

HORIZONTAL_START = StackBuilder().horizontal().align("start").build()
HORIZONTAL_CENTER = StackBuilder().horizontal().align("center").build()
HORIZONTAL_END = StackBuilder().horizontal().align("end").build()

# With children patterns
FORM_FIELD_STACK = (
    StackBuilder()
    .vertical()
    .spacing("tight")
    .add_child({"type": "Label", "props": {"text": "Username"}})
    .add_child({"type": "Input", "props": {"placeholder": "Enter username"}})
    .build()
)

BUTTON_GROUP = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("end")
    .add_child({"type": "Button", "props": {"text": "Cancel", "variant": "outline"}})
    .add_child({"type": "Button", "props": {"text": "Save", "variant": "primary"}})
    .build()
)

CARD_CONTENT = (
    StackBuilder()
    .vertical()
    .spacing("normal")
    .add_child({"type": "Heading", "props": {"text": "Title", "level": 3}})
    .add_child({"type": "Text", "props": {"text": "Description text here"}})
    .add_child({"type": "Button", "props": {"text": "Learn More"}})
    .build()
)

# Common use cases - Form layouts
FORM_STACK = (
    StackBuilder()
    .vertical()
    .spacing("normal")
    .build()
)

INLINE_FORM = (
    StackBuilder()
    .horizontal()
    .spacing("tight")
    .align("start")
    .build()
)

# Navigation layouts
NAV_STACK = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("center")
    .build()
)

VERTICAL_NAV = (
    StackBuilder()
    .vertical()
    .spacing("tight")
    .align("start")
    .build()
)

# Card layouts
VERTICAL_CARD_CONTENT = (
    StackBuilder()
    .vertical()
    .spacing("relaxed")
    .build()
)

HORIZONTAL_CARD_CONTENT = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("center")
    .build()
)

# List layouts
LIST_ITEM_STACK = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("center")
    .build()
)

VERTICAL_LIST = (
    StackBuilder()
    .vertical()
    .spacing("tight")
    .build()
)

# Action groups
ACTION_BAR = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("end")
    .build()
)

TOOLBAR = (
    StackBuilder()
    .horizontal()
    .spacing("tight")
    .align("start")
    .build()
)

# Header layouts
PAGE_HEADER = (
    StackBuilder()
    .vertical()
    .spacing("tight")
    .align("start")
    .build()
)

SPLIT_HEADER = (
    StackBuilder()
    .horizontal()
    .spacing("normal")
    .align("center")
    .build()
)

# All patterns
ALL_STACK_PATTERNS = {
    "vertical": VERTICAL_STACK,
    "horizontal": HORIZONTAL_STACK,
    "tight": TIGHT_STACK,
    "normal": NORMAL_STACK,
    "relaxed": RELAXED_STACK,
    "tight_h": TIGHT_HORIZONTAL,
    "normal_h": NORMAL_HORIZONTAL,
    "relaxed_h": RELAXED_HORIZONTAL,
    "start": START_ALIGNED,
    "center": CENTER_ALIGNED,
    "end": END_ALIGNED,
    "h_start": HORIZONTAL_START,
    "h_center": HORIZONTAL_CENTER,
    "h_end": HORIZONTAL_END,
    "form_field": FORM_FIELD_STACK,
    "button_group": BUTTON_GROUP,
    "card_content": CARD_CONTENT,
    "form": FORM_STACK,
    "inline_form": INLINE_FORM,
    "nav": NAV_STACK,
    "v_nav": VERTICAL_NAV,
    "v_card": VERTICAL_CARD_CONTENT,
    "h_card": HORIZONTAL_CARD_CONTENT,
    "list_item": LIST_ITEM_STACK,
    "v_list": VERTICAL_LIST,
    "action_bar": ACTION_BAR,
    "toolbar": TOOLBAR,
    "page_header": PAGE_HEADER,
    "split_header": SPLIT_HEADER,
}
