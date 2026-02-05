"""
Preset list card patterns for common use cases
"""
from .listcard_builder import ListCardBuilder

# Basic list cards
TWO_ITEM_LIST = (
    ListCardBuilder()
    .add_item("/avatar1.jpg", "John Doe", "Software Engineer", "Active")
    .add_item("/avatar2.jpg", "Jane Smith", "Product Manager", "Away")
    .build()
)

THREE_ITEM_LIST = (
    ListCardBuilder()
    .add_item("/avatar1.jpg", "Alice Johnson", "Designer", "Online")
    .add_item("/avatar2.jpg", "Bob Wilson", "Developer", "Busy")
    .add_item("/avatar3.jpg", "Carol Davis", "Manager", "Offline")
    .build()
)

FOUR_ITEM_LIST = (
    ListCardBuilder()
    .add_item("/user1.jpg", "David Lee", "Team Lead", "Online")
    .add_item("/user2.jpg", "Emma Brown", "Developer", "Online")
    .add_item("/user3.jpg", "Frank Miller", "Designer", "Away")
    .add_item("/user4.jpg", "Grace Taylor", "QA Engineer", "Busy")
    .build()
)

# Common use cases - Team list
TEAM_LIST = (
    ListCardBuilder()
    .add_item("/team1.jpg", "Sarah Connor", "Engineering Manager", "Available")
    .add_item("/team2.jpg", "Kyle Reese", "Senior Developer", "In Meeting")
    .add_item("/team3.jpg", "John Connor", "Software Engineer", "Online")
    .add_item("/team4.jpg", "Kate Brewster", "UX Designer", "Away")
    .build()
)

# Contact list
CONTACT_LIST = (
    ListCardBuilder()
    .add_item("/contact1.jpg", "Michael Scott", "Regional Manager", "Active")
    .add_item("/contact2.jpg", "Jim Halpert", "Sales Representative", "Active")
    .add_item("/contact3.jpg", "Pam Beesly", "Receptionist", "Busy")
    .build()
)

# Recent activity list
ACTIVITY_LIST = (
    ListCardBuilder()
    .add_item("/user1.jpg", "Tom Hardy", "Created new task", "2 min ago")
    .add_item("/user2.jpg", "Chris Evans", "Updated project", "15 min ago")
    .add_item("/user3.jpg", "Robert Downey", "Closed 3 issues", "1 hour ago")
    .build()
)

# Leads list
LEADS_LIST = (
    ListCardBuilder()
    .add_item("/lead1.jpg", "Tech Corp", "Enterprise Lead", "Hot")
    .add_item("/lead2.jpg", "StartUp Inc", "SMB Lead", "Warm")
    .add_item("/lead3.jpg", "Global Ltd", "Enterprise Lead", "Cold")
    .build()
)

# Opportunity list
OPPORTUNITY_LIST = (
    ListCardBuilder()
    .add_item("/opp1.jpg", "Cloud Migration", "$150,000", "Negotiation")
    .add_item("/opp2.jpg", "Software License", "$75,000", "Proposal")
    .add_item("/opp3.jpg", "Consulting Services", "$250,000", "Closed Won")
    .build()
)

# Customer list
CUSTOMER_LIST = (
    ListCardBuilder()
    .add_item("/customer1.jpg", "Acme Corporation", "Premium Customer", "Active")
    .add_item("/customer2.jpg", "Tech Solutions", "Standard Customer", "Active")
    .add_item("/customer3.jpg", "Digital Ventures", "Premium Customer", "Trial")
    .build()
)

# Single item list
SINGLE_ITEM_LIST = (
    ListCardBuilder()
    .add_item("/avatar.jpg", "Current User", "Administrator", "Online")
    .build()
)

# All patterns
ALL_LISTCARD_PATTERNS = {
    "two_items": TWO_ITEM_LIST,
    "three_items": THREE_ITEM_LIST,
    "four_items": FOUR_ITEM_LIST,
    "team": TEAM_LIST,
    "contacts": CONTACT_LIST,
    "activity": ACTIVITY_LIST,
    "leads": LEADS_LIST,
    "opportunities": OPPORTUNITY_LIST,
    "customers": CUSTOMER_LIST,
    "single": SINGLE_ITEM_LIST,
}
