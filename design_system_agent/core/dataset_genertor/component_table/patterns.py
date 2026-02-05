"""
Preset table patterns for common use cases
"""
from .table_builder import TableBuilder

# Basic table
BASIC_TABLE = (
    TableBuilder()
    .add_header("Name").add_header("Email").add_header("Role")
    .add_row(["John Doe", "john@example.com", "Admin"])
    .add_row(["Jane Smith", "jane@example.com", "User"])
    .build()
)

# Striped table
STRIPED_TABLE = (
    TableBuilder()
    .striped()
    .add_header("Product").add_header("Price").add_header("Stock")
    .add_row(["Product A", "$99", "In Stock"])
    .add_row(["Product B", "$149", "Low Stock"])
    .add_row(["Product C", "$199", "Out of Stock"])
    .build()
)

# Bordered table
BORDERED_TABLE = (
    TableBuilder()
    .bordered()
    .add_header("Date").add_header("Event").add_header("Status")
    .add_row(["2024-01-01", "Meeting", "Completed"])
    .add_row(["2024-01-02", "Review", "Pending"])
    .build()
)

# Hoverable table
HOVERABLE_TABLE = (
    TableBuilder()
    .hoverable()
    .striped()
    .add_header("ID").add_header("Name").add_header("Status")
    .add_row(["001", "Task A", "Active"])
    .add_row(["002", "Task B", "Completed"])
    .add_row(["003", "Task C", "Pending"])
    .build()
)

# Compact table
COMPACT_TABLE = (
    TableBuilder()
    .compact()
    .add_header("Code").add_header("Description")
    .add_row(["A1", "Item A"])
    .add_row(["B2", "Item B"])
    .add_row(["C3", "Item C"])
    .build()
)

# Full-featured table
DATA_TABLE = (
    TableBuilder()
    .striped()
    .bordered()
    .hoverable()
    .add_header("Username").add_header("Email").add_header("Role").add_header("Status")
    .add_row(["admin", "admin@example.com", "Administrator", "Active"])
    .add_row(["user1", "user1@example.com", "User", "Active"])
    .add_row(["user2", "user2@example.com", "User", "Inactive"])
    .build()
)

# Common use cases
USER_TABLE = (
    TableBuilder()
    .striped()
    .hoverable()
    .add_header("Name").add_header("Email").add_header("Role")
    .add_row(["Alice Johnson", "alice@example.com", "Manager"])
    .add_row(["Bob Wilson", "bob@example.com", "Developer"])
    .build()
)

INVOICE_TABLE = (
    TableBuilder()
    .bordered()
    .add_header("Item").add_header("Quantity").add_header("Price").add_header("Total")
    .add_row(["Product A", "2", "$50", "$100"])
    .add_row(["Product B", "1", "$75", "$75"])
    .add_row(["Subtotal", "", "", "$175"])
    .build()
)

REPORT_TABLE = (
    TableBuilder()
    .striped()
    .compact()
    .add_header("Metric").add_header("Value").add_header("Change")
    .add_row(["Revenue", "$50,000", "+12%"])
    .add_row(["Users", "1,234", "+5%"])
    .add_row(["Sessions", "5,678", "-2%"])
    .build()
)

# All patterns
ALL_TABLE_PATTERNS = {
    "basic": BASIC_TABLE,
    "striped": STRIPED_TABLE,
    "bordered": BORDERED_TABLE,
    "hoverable": HOVERABLE_TABLE,
    "compact": COMPACT_TABLE,
    "data": DATA_TABLE,
    "users": USER_TABLE,
    "invoice": INVOICE_TABLE,
    "report": REPORT_TABLE,
}
