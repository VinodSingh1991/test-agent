"""
CRM Pattern-Based Query Generation
Generates queries dynamically using pattern templates and OBJECTS array.
Focus: Detail View, List View, Dashboard, Card View
Query Types: Get/Show only (no actions or forms)
"""

# ============================================================
# CORE CONFIGURATION
# ============================================================

# CRM Object Types - Core entities in the system
OBJECTS = [
    "Lead",
    "Opportunity",
    "Account",
    "Contact",
    "Case",
    "Task"
]

# View type counts for dataset generation
VIEW_TYPE_DISTRIBUTION = {
    "detail": 40,      # 40 detail view records
    "list": 50,        # 50 list view records
    "dashboard": 30,   # 30 dashboard records
    "card": 30,        # 30 card view records
}

# ============================================================
# PATTERN-BASED QUERY GENERATION SYSTEM
# ============================================================

# Pattern Templates - Generate queries dynamically for each object type
PATTERN_TEMPLATES = {
    # Basic Detail - Single record detailed view
    "basic_detail": [
        "show {object} details for {identifier}",
        "get {object} information for {identifier}",
        "display {object} record {identifier}",
        "show {object} overview for {identifier}",
        "get detailed {object} view for {identifier}",
    ],
    
    # Summarize - Quick summary view with key info
    "summarize": [
        "summarize {object} {identifier}",
        "get {object} summary for {identifier}",
        "show quick {object} overview",
        "display {object} snapshot",
        "get {object} brief for {identifier}",
    ],
    
    # Detail in Card View - Detailed info in card/tile format
    "detail_card": [
        "show {object} details as card",
        "get {object} {identifier} in card view",
        "display {object} information as tile",
        "show {object} card with details",
        "get {object} detail card for {identifier}",
    ],
    
    # List View - Multiple records in table/list
    "list": [
        "show all {object}s",
        "get {object} list",
        "display all {object} records",
        "show {object}s by {filter}",
        "get filtered {object}s",
        "list all {object}s",
    ],
    
    # List with Summary - List view with summary metrics
    "list_summary": [
        "show all {object}s with summary",
        "get {object} list with totals",
        "display {object}s with metrics",
        "show {object} overview list",
        "get {object}s with statistics",
    ],
    
    # Grid/Card View - Multiple records as cards/tiles
    "grid_card": [
        "show {object}s in card view",
        "get {object}s as cards",
        "display {object}s in grid",
        "show {object}s as tiles",
        "get {object} grid view",
        "display {object}s in kanban",
    ],
    
    # Timeline View - Chronological activity view
    "timeline": [
        "show {object} timeline",
        "get {object} activity history",
        "display {object} chronological view",
        "show {object} events timeline",
    ],
    
    # Hierarchy View - Parent-child relationships
    "hierarchy": [
        "show {object} hierarchy",
        "get {object} tree view",
        "display {object} relationships",
        "show {object} organization chart",
    ],
    
    # Analytics/Metrics - Data aggregation and insights
    "analytics": [
        "show {object} analytics",
        "get {object} metrics",
        "display {object} statistics",
        "show {object} performance data",
        "get {object} insights",
    ],
    
    # Related Records - Show related entities
    "related": [
        "show {object} with related records",
        "get {object} and relationships",
        "display {object} with connections",
        "show {object} related items",
    ],
    
    # =============== NEW RICH COMPONENT PATTERNS ===============
    
    # Contact List Card - List with avatars and badges
    "contact_list_card": [
        "show {object} contacts with avatars",
        "get {object} team members list",
        "display {object} stakeholders card",
        "show {object} people involved",
    ],
    
    # Metrics Dashboard - KPI metrics with trends
    "metrics_dashboard": [
        "show {object} key metrics",
        "get {object} KPI dashboard",
        "display {object} performance metrics",
        "show {object} metrics with trends",
    ],
    
    # Insights & Recommendations - AI insights
    "insights": [
        "show {object} insights",
        "get {object} recommendations",
        "display {object} AI suggestions",
        "show {object} intelligent insights",
    ],
    
    # Alerts & Notifications - Important alerts
    "alerts": [
        "show {object} alerts",
        "get {object} notifications",
        "display {object} warnings",
        "show {object} important notices",
    ],
    
    # Activity Feed - Recent activities with badges
    "activity_feed": [
        "show {object} recent activity",
        "get {object} activity feed",
        "display {object} latest updates",
        "show {object} recent changes",
    ],
    
    # Birthday/Celebrations - Special occasions
    "celebrations": [
        "show {object} birthdays",
        "get {object} anniversaries",
        "display {object} celebrations",
        "show {object} special occasions",
    ],
    
    # Dashlet Widgets - Small dashboard widgets
    "dashlet": [
        "show {object} quick view widget",
        "get {object} dashlet",
        "display {object} mini widget",
        "show {object} compact view",
    ],
}

# Generate queries for each object type using patterns
def generate_pattern_queries(object_type: str, pattern: str, count: int = 5) -> list:
    """Generate queries for a specific object and pattern"""
    queries = []
    templates = PATTERN_TEMPLATES.get(pattern, [])
    
    # Sample identifiers for variety
    identifiers = ["record 101", "ABC Corp", "John Smith", "item 12345", "latest"]
    filters = ["status", "priority", "date", "owner", "region"]
    
    for i, template in enumerate(templates[:count]):
        query = template.format(
            object=object_type.lower(),
            identifier=identifiers[i % len(identifiers)],
            filter=filters[i % len(filters)]
        )
        queries.append(query)
    
    return queries

# Object-Pattern Matrix: Define which patterns apply to which objects
OBJECT_PATTERN_MATRIX = {
    "Lead": [
        "basic_detail", "summarize", "detail_card", "list", "list_summary", 
        "grid_card", "timeline", "analytics", "metrics_dashboard", 
        "insights", "alerts", "activity_feed", "dashlet"
    ],
    "Opportunity": [
        "basic_detail", "summarize", "detail_card", "list", "list_summary", 
        "grid_card", "timeline", "analytics", "related", "metrics_dashboard",
        "insights", "alerts", "activity_feed", "dashlet", "contact_list_card"
    ],
    "Account": [
        "basic_detail", "summarize", "detail_card", "list", "list_summary", 
        "grid_card", "hierarchy", "analytics", "related", "metrics_dashboard",
        "insights", "contact_list_card", "activity_feed", "dashlet"
    ],
    "Contact": [
        "basic_detail", "summarize", "detail_card", "list", "list_summary", 
        "grid_card", "related", "contact_list_card", "celebrations", 
        "activity_feed", "dashlet"
    ],
    "Case": [
        "basic_detail", "summarize", "detail_card", "list", "list_summary", 
        "grid_card", "timeline", "metrics_dashboard", "alerts", 
        "activity_feed", "dashlet"
    ],
    "Task": [
        "basic_detail", "list", "list_summary", "grid_card", "timeline",
        "alerts", "activity_feed", "dashlet"
    ],
}

# Generate all pattern-based queries
PATTERN_BASED_QUERIES = {}
for obj in OBJECTS:
    PATTERN_BASED_QUERIES[obj] = {}
    patterns = OBJECT_PATTERN_MATRIX.get(obj, ["basic_detail", "list"])
    
    for pattern in patterns:
        PATTERN_BASED_QUERIES[obj][pattern] = generate_pattern_queries(obj, pattern, 3)

# Flatten for easy access
ALL_PATTERN_QUERIES = []
for obj, patterns in PATTERN_BASED_QUERIES.items():
    for pattern, queries in patterns.items():
        ALL_PATTERN_QUERIES.extend(queries)

# Pattern to View Type mapping
PATTERN_TO_VIEW_TYPE = {
    "basic_detail": "detail",
    "summarize": "summary",
    "detail_card": "detail_card",
    "list": "list",
    "list_summary": "list_summary",
    "grid_card": "card",
    "timeline": "timeline",
    "hierarchy": "hierarchy",
    "analytics": "analytics",
    "related": "related",
    # New rich component patterns
    "contact_list_card": "list_card",
    "metrics_dashboard": "dashboard",
    "insights": "insights",
    "alerts": "alerts",
    "activity_feed": "feed",
    "celebrations": "celebrations",
    "dashlet": "dashlet",
}

# Component requirements for each pattern - Rich combinations for detailed UIs
PATTERN_COMPONENTS = {
    # Core detail view - Comprehensive record display
    "basic_detail": [
        "Heading",        # Page title
        "Badge",          # Status indicators
        "Divider",        # Section separators
        "Label",          # Field labels
        "Text",           # Field values
        "Table",          # Structured data
        "Avatar",         # User/record image
        "Button",         # Action buttons
        "Link",           # Related links
        "Chip",           # Tags/categories
    ],
    
    # Summary view - Quick overview with key metrics
    "summarize": [
        "Heading",        # Title
        "Text",           # Summary text
        "Metric",         # Key numbers
        "Badge",          # Status
        "Divider",        # Separator
        "Button",         # Quick action
    ],
    
    # Detail in card - Card-based detailed view
    "detail_card": [
        "Card",           # Card container
        "Heading",        # Card title
        "Avatar",         # Profile image
        "Badge",          # Status badges
        "Text",           # Description
        "Divider",        # Section divider
        "Label",          # Field labels
        "Chip",           # Tags
        "Button",         # Actions
        "Link",           # Related links
    ],
    
    # List view - Tabular data display
    "list": [
        "Heading",        # List title
        "Table",          # Data table
        "Badge",          # Status column
        "Chip",           # Filter chips
        "Button",         # Row actions
        "Avatar",         # User column
        "Link",           # Detail links
    ],
    
    # List with summary - List + aggregated metrics
    "list_summary": [
        "Heading",        # Title
        "Metric",         # Summary metrics
        "Divider",        # Separator
        "Table",          # Data table
        "Badge",          # Status
        "Chip",           # Filters
        "Button",         # Actions
    ],
    
    # Grid/Card view - Multiple cards in grid
    "grid_card": [
        "Heading",        # Grid title
        "Card",           # Card items
        "Image",          # Card images
        "Badge",          # Status badges
        "Text",           # Card content
        "Button",         # Card actions
        "Chip",           # Tags
        "Avatar",         # User avatars
    ],
    
    # Timeline view - Chronological activity
    "timeline": [
        "Heading",        # Timeline title
        "Stack",          # Vertical layout
        "Avatar",         # Activity user
        "Text",           # Activity description
        "Badge",          # Activity type
        "Divider",        # Time separators
        "Link",           # Activity links
        "Chip",           # Activity tags
    ],
    
    # Hierarchy view - Tree structure
    "hierarchy": [
        "Heading",        # Hierarchy title
        "Stack",          # Tree layout
        "Divider",        # Level separators
        "Badge",          # Node status
        "Text",           # Node labels
        "Avatar",         # Node images
        "Button",         # Expand/collapse
    ],
    
    # Analytics/Metrics - Data insights dashboard
    "analytics": [
        "Heading",        # Dashboard title
        "Metric",         # KPI metrics
        "Dashlet",        # Metric widgets
        "Table",          # Detailed data
        "Badge",          # Status indicators
        "Divider",        # Section separators
        "Button",         # Export/filter
        "Chip",           # Filters
    ],
    
    # Related records - Connected entities
    "related": [
        "Heading",        # Section title
        "ListCard",       # Related items list
        "Avatar",         # Item avatars
        "Badge",          # Item status
        "Link",           # Navigation links
        "Button",         # Add/remove actions
        "Chip",           # Relationship types
        "Divider",        # Section dividers
    ],
    
    # =============== RICH COMPONENT PATTERNS ===============
    
    # Contact list card - People/stakeholders view
    "contact_list_card": [
        "Heading",        # List title
        "ListCard",       # Contact cards
        "Avatar",         # Contact photos
        "Badge",          # Online status
        "Text",           # Contact details
        "Link",           # Profile links
        "Chip",           # Contact tags
        "Button",         # Contact actions
        "Divider",        # Group separators
    ],
    
    # Metrics dashboard - KPI overview
    "metrics_dashboard": [
        "Heading",        # Dashboard title
        "Metric",         # KPI cards
        "Dashlet",        # Metric widgets
        "Card",           # Grouped metrics
        "Badge",          # Trend indicators
        "Divider",        # Section separators
        "Button",         # Refresh/filter
        "Table",          # Detailed breakdown
    ],
    
    # Insights & recommendations - AI suggestions
    "insights": [
        "Heading",        # Insights title
        "Insights",       # Insight cards
        "Alert",          # Important insights
        "Badge",          # Priority/severity
        "Button",         # Action buttons
        "Divider",        # Section separators
        "Text",           # Descriptions
        "Chip",           # Categories
    ],
    
    # Alerts & notifications - Important messages
    "alerts": [
        "Heading",        # Alerts title
        "Alert",          # Alert messages
        "Badge",          # Alert severity
        "Button",         # Acknowledge/dismiss
        "Divider",        # Alert separators
        "Avatar",         # Alert source
        "Link",           # Related links
    ],
    
    # Activity feed - Recent updates
    "activity_feed": [
        "Heading",        # Feed title
        "Stack",          # Vertical activity list
        "Avatar",         # Activity user
        "Badge",          # Activity type
        "Text",           # Activity description
        "Link",           # Activity links
        "Divider",        # Time separators
        "Button",         # Load more
        "Chip",           # Activity filters
    ],
    
    # Birthday/Celebrations - Special occasions
    "celebrations": [
        "Heading",        # Celebrations title
        "BirthdayCard",   # Birthday cards
        "Avatar",         # Person photos
        "Badge",          # Occasion type
        "Card",           # Celebration cards
        "Button",         # Send wishes
        "Divider",        # Date separators
    ],
    
    # Dashlet widgets - Compact dashboard widgets
    "dashlet": [
        "Dashlet",        # Widget container
        "Metric",         # Widget metric
        "Badge",          # Status indicator
        "Button",         # Widget action
        "Avatar",         # Widget icon
        "Link",           # Details link
    ],
}
