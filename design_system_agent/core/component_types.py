"""
Component Type Registry
Defines all available component types, their categories, and default properties
Based on CRM Layout Dataset - 19 Active Components
"""

class ComponentType:
    """Component type definitions with metadata"""
    
    # ========================================
    # ACTIVE COMPONENTS (Used in CRM Layouts)
    # ========================================
    
    # Typography & Text Components
    HEADING = "Heading"          # H1, H2, H3, H4, H5, H6 headings
    TEXT = "Text"                # Body text, paragraphs
    LABEL = "Label"              # Form labels, metadata labels
    
    # Interactive Components
    BUTTON = "Button"            # Primary, secondary, tertiary, danger buttons
    LINK = "Link"                # Text links, navigation links
    
    # Display Components
    BADGE = "Badge"              # Status badges (success, warning, danger, info)
    CHIP = "Chip"                # Removable tags, filters
    AVATAR = "Avatar"            # User avatars, profile images
    IMAGE = "Image"              # General images
    DIVIDER = "Divider"          # Horizontal/vertical separators
    
    # Container Components
    CARD = "Card"                # Content cards, panel cards
    STACK = "Stack"              # Vertical/horizontal stacks, flex containers
    
    # Data Display Components
    LIST = "List"                # Ordered/unordered lists (ul/ol)
    TABLE = "Table"              # Data tables with rows and columns
    METRIC = "Metric"            # KPI metrics, statistics
    DASHLET = "Dashlet"          # Dashboard widgets, mini charts
    
    # Complex/Composite Components
    LISTCARD = "ListCard"        # List item cards with avatar, title, metadata
    BIRTHDAYCARD = "BirthdayCard" # Special celebration cards
    INSIGHTS = "Insights"        # AI insights, recommendations
    ALERT = "Alert"              # Alert messages, notifications
    
    # ========================================
    # LEGACY/UNUSED COMPONENTS (For Reference)
    # ========================================
    
    # Form Components (not currently used)
    INPUT = "input"
    TEXTAREA = "textarea"
    SELECT = "select"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    FORM = "form"
    
    # Layout Components (not currently used)
    DIV = "div"
    SECTION = "section"
    CONTAINER = "container"
    GRID = "grid"
    
    # Other Composite Components (not currently used)
    CHART = "chart"
    TIMELINE = "timeline"
    MODAL = "modal"
    DROPDOWN = "dropdown"
    TABS = "tabs"
    TOOLTIP = "tooltip"
    PAGINATION = "pagination"


# Component Categories for grouping and filtering
COMPONENT_CATEGORIES = {
    "typography": [
        ComponentType.HEADING,
        ComponentType.TEXT,
        ComponentType.LABEL,
    ],
    "interactive": [
        ComponentType.BUTTON,
        ComponentType.LINK,
    ],
    "display": [
        ComponentType.BADGE,
        ComponentType.CHIP,
        ComponentType.AVATAR,
        ComponentType.IMAGE,
        ComponentType.DIVIDER,
    ],
    "containers": [
        ComponentType.CARD,
        ComponentType.STACK,
    ],
    "data": [
        ComponentType.LIST,
        ComponentType.TABLE,
        ComponentType.METRIC,
        ComponentType.DASHLET,
    ],
    "complex": [
        ComponentType.LISTCARD,
        ComponentType.BIRTHDAYCARD,
        ComponentType.INSIGHTS,
        ComponentType.ALERT,
    ],
}

ACTIVE_COMPONENTS = [
    ComponentType.ALERT,
    ComponentType.AVATAR,
    ComponentType.BADGE,
    ComponentType.BIRTHDAYCARD,
    ComponentType.BUTTON,
    ComponentType.CARD,
    ComponentType.CHIP,
    ComponentType.DASHLET,
    ComponentType.DIVIDER,
    ComponentType.HEADING,
    ComponentType.IMAGE,
    ComponentType.INSIGHTS,
    ComponentType.LABEL,
    ComponentType.LINK,
    ComponentType.LIST,
    ComponentType.LINK,
    ComponentType.LISTCARD,
    ComponentType.METRIC,
    ComponentType.STACK,
    ComponentType.TABLE,
    ComponentType.TEXT,
]


def get_component_category(component_type: str) -> str:
    """
    Get the category of a component type
    
    Args:
        component_type: Component type name
        
    Returns:
        Category name or "unknown"
    """
    for category, components in COMPONENT_CATEGORIES.items():
        if component_type in components:
            return category
    return "unknown"


def is_active_component(component_type: str) -> bool:
    """
    Check if a component is actively used in CRM layouts
    
    Args:
        component_type: Component type name
        
    Returns:
        True if component is actively used
    """
    return component_type in ACTIVE_COMPONENTS


def get_all_components() -> list:
    """Get list of all active component types"""
    return ACTIVE_COMPONENTS.copy()


def get_components_by_category(category: str) -> list:
    """
    Get all components in a specific category
    
    Args:
        category: Category name (typography, interactive, display, containers, data, complex)
        
    Returns:
        List of component types in the category
    """
    return COMPONENT_CATEGORIES.get(category, []).copy()