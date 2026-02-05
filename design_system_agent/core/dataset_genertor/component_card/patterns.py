"""
Preset card patterns for common use cases
"""
from .card_builder import CardBuilder

# Basic cards
SIMPLE_CARD = CardBuilder().add_body_item("Simple card content").build()
ELEVATED_CARD = CardBuilder().elevated().add_body_item("Elevated card with shadow").build()
BORDERED_CARD = CardBuilder().bordered().add_body_item("Bordered card").build()

# Header only
HEADER_CARD = CardBuilder().header("Card Title").add_body_item("Card content goes here").build()

# Footer only
FOOTER_CARD = CardBuilder().add_body_item("Card content").footer("Card footer text").build()

# Full cards
FULL_CARD = (
    CardBuilder()
    .header("Complete Card")
    .add_body_item("This is the main content")
    .add_body_item("Multiple body items supported")
    .footer("Footer with actions")
    .build()
)

FULL_ELEVATED_CARD = (
    CardBuilder()
    .header("Premium Card")
    .elevated()
    .add_body_item("Premium content here")
    .footer("Premium footer")
    .build()
)

FULL_BORDERED_CARD = (
    CardBuilder()
    .header("Bordered Card")
    .bordered()
    .add_body_item("Bordered content")
    .footer("Bordered footer")
    .build()
)

# Common use cases - Profile card
PROFILE_CARD = (
    CardBuilder()
    .header("User Profile")
    .elevated()
    .add_body_item("Name: John Doe")
    .add_body_item("Email: john@example.com")
    .add_body_item("Role: Administrator")
    .footer("Last login: 2 hours ago")
    .build()
)

# Stats card
STATS_CARD = (
    CardBuilder()
    .header("Statistics")
    .bordered()
    .add_body_item("Total Users: 1,234")
    .add_body_item("Active Sessions: 567")
    .add_body_item("Revenue: $89,000")
    .build()
)

# Info card
INFO_CARD = (
    CardBuilder()
    .header("Information")
    .elevated()
    .add_body_item("Important information goes here")
    .add_body_item("Please read carefully")
    .footer("Updated: Today")
    .build()
)

# Product card
PRODUCT_CARD = (
    CardBuilder()
    .header("Premium Product")
    .elevated()
    .bordered()
    .add_body_item("High quality product")
    .add_body_item("Price: $99.99")
    .footer("Add to Cart")
    .build()
)

# Notification card
NOTIFICATION_CARD = (
    CardBuilder()
    .header("Notifications")
    .add_body_item("You have 5 new messages")
    .add_body_item("3 pending tasks")
    .footer("View All")
    .build()
)

# Simple content cards
TEXT_CARD = CardBuilder().add_body_item("Simple text content card").build()
MULTI_ITEM_CARD = (
    CardBuilder()
    .add_body_item("First item")
    .add_body_item("Second item")
    .add_body_item("Third item")
    .build()
)

# All patterns
ALL_CARD_PATTERNS = {
    "simple": SIMPLE_CARD,
    "elevated": ELEVATED_CARD,
    "bordered": BORDERED_CARD,
    "header": HEADER_CARD,
    "footer": FOOTER_CARD,
    "full": FULL_CARD,
    "full_elevated": FULL_ELEVATED_CARD,
    "full_bordered": FULL_BORDERED_CARD,
    "profile": PROFILE_CARD,
    "stats": STATS_CARD,
    "info": INFO_CARD,
    "product": PRODUCT_CARD,
    "notification": NOTIFICATION_CARD,
    "text": TEXT_CARD,
    "multi_item": MULTI_ITEM_CARD,
}
