"""
Preset dashlet patterns for common use cases
"""
from .dashlet_builder import DashletBuilder

# Basic dashlets
SIMPLE_DASHLET = DashletBuilder().title("Simple Dashlet").content("Dashlet content").build()
WITH_ACTION = DashletBuilder().title("Dashlet").content("Content here").action("View More").build()
LOADING_DASHLET = DashletBuilder().title("Loading").content("Please wait...").loading().build()

# Icon dashlets
ICON_DASHLET = DashletBuilder().title("With Icon").icon("ChartIcon").content("Dashboard content").build()
ICON_ACTION_DASHLET = (
    DashletBuilder()
    .title("Complete Dashlet")
    .icon("AnalyticsIcon")
    .content("Analytics data")
    .action("View Details")
    .build()
)

# Common use cases - Metrics dashlet
REVENUE_DASHLET = (
    DashletBuilder()
    .title("Total Revenue")
    .icon("DollarIcon")
    .content("$125,000")
    .action("View Report")
    .build()
)

USERS_DASHLET = (
    DashletBuilder()
    .title("Active Users")
    .icon("UsersIcon")
    .content("1,234 users")
    .action("View All")
    .build()
)

SALES_DASHLET = (
    DashletBuilder()
    .title("Sales Today")
    .icon("ShoppingIcon")
    .content("89 orders")
    .action("Details")
    .build()
)

# Status dashlets
PERFORMANCE_DASHLET = (
    DashletBuilder()
    .title("Performance")
    .icon("ActivityIcon")
    .content("98% uptime")
    .build()
)

ALERTS_DASHLET = (
    DashletBuilder()
    .title("Alerts")
    .icon("AlertIcon")
    .content("3 warnings")
    .action("Review")
    .build()
)

# Task dashlets
TODO_DASHLET = (
    DashletBuilder()
    .title("Tasks")
    .icon("ChecklistIcon")
    .content("5 pending tasks")
    .action("View Tasks")
    .build()
)

NOTIFICATIONS_DASHLET = (
    DashletBuilder()
    .title("Notifications")
    .icon("BellIcon")
    .content("12 new notifications")
    .action("View All")
    .build()
)

# Loading states
LOADING_DATA = (
    DashletBuilder()
    .title("Loading Data")
    .icon("SpinnerIcon")
    .content("Fetching latest data...")
    .loading()
    .build()
)

# Empty state
EMPTY_DASHLET = (
    DashletBuilder()
    .title("No Data")
    .icon("EmptyIcon")
    .content("No data available")
    .build()
)

# All patterns
ALL_DASHLET_PATTERNS = {
    "simple": SIMPLE_DASHLET,
    "with_action": WITH_ACTION,
    "loading": LOADING_DASHLET,
    "icon": ICON_DASHLET,
    "icon_action": ICON_ACTION_DASHLET,
    "revenue": REVENUE_DASHLET,
    "users": USERS_DASHLET,
    "sales": SALES_DASHLET,
    "performance": PERFORMANCE_DASHLET,
    "alerts": ALERTS_DASHLET,
    "todo": TODO_DASHLET,
    "notifications": NOTIFICATIONS_DASHLET,
    "loading_data": LOADING_DATA,
    "empty": EMPTY_DASHLET,
}
