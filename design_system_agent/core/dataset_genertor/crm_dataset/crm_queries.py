##############################################
# Banking CRM Pattern Generator – FULL FILE
# Author: Vinod Singh
# Version: 2.0
##############################################

"""
This file contains a complete pattern-based synthetic
query generation system for Banking CRM RAG training.

Key Features:
    ✓ Synonym-based query patterns  
    ✓ Basic / Medium / Advanced complexity  
    ✓ Multi-object + Conditional + Aggregation patterns  
    ✓ Cross-object combinations  
    ✓ UI component mappings  
    ✓ Generates 2000–5000 RAG-ready queries  
"""

# =====================================================
# 1. OBJECTS (Core CRM Entities)
# =====================================================

OBJECTS = {
    "lead": ["name", "status", "priority", "created_date", "assigned_to", "product", "branch"],
    "case": ["case_no", "title", "status", "category", "assigned_to", "customer_id", "created_date"],
    "account": ["account_no", "balance", "type", "branch", "customer_id"],
    "customer": ["name", "age", "city", "type", "total_balance", "relationship_manager"],
    "loan": ["loan_id", "loan_amount", "status", "emi_amount", "customer_id", "branch"],
    "task": ["task_name", "due_date", "status", "assigned_to", "related_to"],
    "appointment": ["subject", "date", "status", "customer_id", "with_user"],
    "branch": ["name", "city", "code", "manager_id"]
}


# =====================================================
# 2. ENUMERATIONS (For dynamic pattern filling)
# =====================================================

ENUMS = {
    "status": ["open", "closed", "in-progress", "pending", "approved", "rejected"],
    "priority": ["high", "medium", "low"],
    "date_range": ["today", "yesterday", "last week", "last month", "last 3 months", "this quarter", "this year"],
    "sort_order": ["asc", "desc"],
    "amount_field": ["amount", "balance", "loan_amount", "emi_amount", "premium_amount"],
    "group_by": ["branch", "manager", "product", "customer_type", "status"],
    "metrics": ["sum", "count", "average", "min", "max"],
    "comparison": ["greater than", "less than", "equal to", "not equal to"],
    "value": ["5000", "25000", "50000", "100000", "200000", "500000", "1000000"]
}


# =====================================================
# 3. SYNONYMS FOR QUERY VERBS
# =====================================================

SYNONYMS = ["show", "list", "get", "fetch", "display", "find"]


# =====================================================
# 4. OBJECT RELATIONSHIPS
# =====================================================

RELATIONS = {
    "lead -> customer": "lead.customer_id = customer.id",
    "customer -> account": "customer.id = account.customer_id",
    "customer -> loan": "customer.id = loan.customer_id",
    "branch -> lead": "branch.id = lead.branch",
    "branch -> account": "branch.id = account.branch",
    "branch -> loan": "branch.id = loan.branch",
    "task -> lead": "task.related_to = lead.id",
    "task -> loan": "task.related_to = loan.id"
}


# =====================================================
# 5. VIEW TYPES & PRESENTATION FORMATS
# =====================================================

VIEW_TYPES = {
    "table": "Tabular data display with rows and columns",
    "list": "Vertical list of items with details",
    "card": "Grid of cards with summary information"
}

# Pattern to View Type mapping
PATTERN_TO_VIEW_TYPE = {
    "LIST_SIMPLE": "table",
    "LIST_ADVANCED": "table",
    "MULTI_OBJECT": "list",
    "AGGREGATE": "card",
    "ADVANCED_AGGREGATE_RELATED": "card",
    "FULL_COMPLEX": "card",
    "COMBINATIONS": "list",
    "TASK_RELATED": "list",
    "PERIODIC_QUERIES": "card",
    "BRANCH_MANAGER_QUERIES": "card",
}


# =====================================================
# 6. VIEW LEVELS & UI COMPONENTS
# =====================================================

VIEW_LEVELS = {
    "basic": ["title", "description", "table"],
    "medium": ["title", "description", "table", "insight", "sum", "next_best_action"],
    "advanced": ["dashlet_graph", "title", "description", "insights", "nba_profile", "list", "badge", "table"]
}

# Pattern to Complexity Level mapping
PATTERN_TO_VIEW_LEVEL = {
    "LIST_SIMPLE": "basic",
    "LIST_ADVANCED": "medium",
    "MULTI_OBJECT": "medium",
    "AGGREGATE": "advanced",
    "ADVANCED_AGGREGATE_RELATED": "advanced",
    "FULL_COMPLEX": "advanced",
    "COMBINATIONS": "medium",
    "TASK_RELATED": "basic",
    "PERIODIC_QUERIES": "advanced",
    "BRANCH_MANAGER_QUERIES": "medium",
}


# =====================================================
# 7. UI COMPONENTS FOR EACH VIEW TYPE
# =====================================================

VIEW_TYPE_COMPONENTS = {
    "table": {
        "primary": "Table",  # Main component for table view
        "required": ["Heading", "Table"],
        "optional": ["Badge", "Button", "Link", "Chip", "Text", "Divider"]
    },
    "list": {
        "primary": "ListCard",  # Main component for list view
        "required": ["Heading", "ListCard"],
        "optional": ["Avatar", "Badge", "Link", "Button", "Divider", "Chip", "Text", "Description"]
    },
    "card": {
        "primary": "Card",  # Main component for card view
        "required": ["Heading", "Card", "Metric"],
        "optional": ["Dashlet", "Badge", "Button", "Divider", "Avatar", "Text", "Link", "Chip"]
    }
}

# Component priority mapping - ensures view-specific components are added
VIEW_TYPE_TO_COMPONENT = {
    "table": ["Table"],      # For table view, always include Table component
    "list": ["ListCard"],    # For list view, always include ListCard component
    "card": ["Card"],        # For card view, always include Card component
}


# =====================================================
# 8. SYNONYM-EXPANDED PATTERN TEMPLATES
# =====================================================

BASE_PATTERNS = {
    "LIST_SIMPLE": [
        "{verb} all {object}",
        "{verb} all {object} {date_range}",
        "{verb} my {object} with status {status}",
        "{verb} {object} where priority is {priority}",
    ],

    "LIST_ADVANCED": [
        "{verb} top 10 {object} where status is {status}",
        "{verb} {object} sorted by {field} {sort_order}",
        "{verb} {object} where {field} is {comparison} {value}",
        "{verb} {object} created {date_range}",
    ],

    "MULTI_OBJECT": [
        "{verb} {object1} with related {object2}",
        "{verb} {object1} where {object2} {field} is {value}",
        "{verb} {object1} + {object2} filtered by {status}",
    ],

    "AGGREGATE": [
        "{verb} {metrics} of {amount_field} in {object}",
        "{verb} {metrics} of {amount_field} for {object} {date_range}",
        "calculate total {amount_field} across all {object}",
        "{verb} {object} grouped by {group_by} with {metrics} of {amount_field}",
    ],

    "ADVANCED_AGGREGATE_RELATED": [
        "{verb} {metrics} of loan amount for customers grouped by branch",
        "total loan amount for customers with account balance {comparison} {value}",
        "{verb} sum of account balance for customers having loans",
        "{verb} branch wise {metrics} of emi amount",
    ],

    "FULL_COMPLEX": [
        "{verb} customers with total balance {comparison} {value} and loan amount {comparison} {value}",
        "{verb} branch wise count of leads where loan status is {status}",
        "{verb} {metrics} of loan amount for customers having pending tasks",
        "{verb} customers who have loans and also leads in {status} status",
        "{verb} total portfolio for each relationship manager",
    ],

    "TASK_RELATED": [
        "{verb} overdue tasks related to {object}",
        "{verb} tasks for {object} assigned to me",
        "{verb} tasks {date_range} for {object} with status {status}",
    ],

    "PERIODIC_QUERIES": [
        "{verb} month wise {metrics} of {object}",
        "{verb} daily breakdown of {object} for {date_range}",
        "{verb} quarterly performance of leads by branch",
    ],

    "BRANCH_MANAGER_QUERIES": [
        "{verb} branch wise {object}",
        "{verb} my branch {object} with status {status}",
        "{verb} accounts in branch with balance {comparison} {value}",
        "{verb} branch summary: {object} count, loan total, deposits total",
    ]
}


# =====================================================
# 9. COMPLEX OBJECT COMBINATIONS
# =====================================================

PATTERN_COMBINATIONS = {
    "LEAD + CUSTOMER": [
        "{verb} leads where customer name contains {value}",
        "{verb} leads where customer has loan status {status}",
    ],

    "CUSTOMER + ACCOUNT": [
        "{verb} customers whose account balance is {comparison} {value}",
        "{verb} customers with total account sum greater than {value}",
    ],

    "CUSTOMER + LOAN": [
        "{verb} loan customers where EMI is {comparison} {value}",
        "{verb} customers having multiple active loans",
    ],

    "BRANCH + LOAN + ACCOUNT": [
        "{verb} branch wise loan + account balance summary",
        "{verb} total deposits vs loan amount grouped by branch",
    ],

    "LEAD + TASK": [
        "{verb} leads with pending tasks",
        "{verb} tasks related to hot priority leads",
    ]
}



# =====================================================
# 10. GENERATE QUERIES FOR A PATTERN
# =====================================================

import random

def generate_pattern_queries(object_type, pattern, count=20):
    templates = BASE_PATTERNS.get(pattern, [])
    fields = OBJECTS.get(object_type, [])
    object_list = list(OBJECTS.keys())

    queries = []

    for _ in range(count):
        template = random.choice(templates)
        verb = random.choice(SYNONYMS)

        query = template.format(
            verb=verb,
            object=object_type,
            object1=object_type,
            object2=random.choice(object_list),
            field=random.choice(fields) if fields else "name",
            status=random.choice(ENUMS["status"]),
            priority=random.choice(ENUMS["priority"]),
            date_range=random.choice(ENUMS["date_range"]),
            sort_order=random.choice(ENUMS["sort_order"]),
            amount_field=random.choice(ENUMS["amount_field"]),
            group_by=random.choice(ENUMS["group_by"]),
            metrics=random.choice(ENUMS["metrics"]),
            comparison=random.choice(ENUMS["comparison"]),
            value=random.choice(ENUMS["value"]),
        )

        queries.append(query)

    return queries


# =====================================================
# 11. FULL GENERATION (All Objects + All Patterns)
# =====================================================

OBJECT_TO_PATTERNS = {
    "lead": ["LIST_SIMPLE", "LIST_ADVANCED", "MULTI_OBJECT", "AGGREGATE", "FULL_COMPLEX"],
    "case": ["LIST_SIMPLE", "LIST_ADVANCED", "MULTI_OBJECT", "AGGREGATE"],
    "account": ["LIST_SIMPLE", "LIST_ADVANCED", "AGGREGATE", "ADVANCED_AGGREGATE_RELATED"],
    "customer": ["LIST_SIMPLE", "LIST_ADVANCED", "AGGREGATE", "ADVANCED_AGGREGATE_RELATED", "FULL_COMPLEX"],
    "loan": ["LIST_SIMPLE", "LIST_ADVANCED", "AGGREGATE", "FULL_COMPLEX"],
    "task": ["LIST_SIMPLE", "LIST_ADVANCED", "TASK_RELATED"],
    "appointment": ["LIST_SIMPLE", "LIST_ADVANCED"],
    "branch": ["LIST_SIMPLE", "AGGREGATE", "BRANCH_MANAGER_QUERIES"],
}


# =====================================================
# 12. GENERATE FULL DATASET (2000+ queries)
# =====================================================

def generate_full_dataset(total=2000):
    """Generate comprehensive dataset with specified total queries"""
    dataset = []
    
    # Calculate how many queries per object to reach target
    num_objects = len(OBJECTS)
    total_patterns = sum(len(patterns) for patterns in OBJECT_TO_PATTERNS.values())
    queries_per_pattern = max(20, (total * 60) // (total_patterns * 100))  # Aim for 60% from main patterns
    
    # Generate main object-pattern queries
    for obj, patterns in OBJECT_TO_PATTERNS.items():
        for pattern in patterns:
            dataset.extend(generate_pattern_queries(obj, pattern, count=queries_per_pattern))
    
    # Add combination patterns (40% of total)
    combinations_target = (total * 40) // 100
    queries_per_combo = max(25, combinations_target // len(PATTERN_COMBINATIONS))
    
    for _, combos in PATTERN_COMBINATIONS.items():
        for template in combos:
            for _ in range(queries_per_combo):
                dataset.append(
                    template.format(
                        verb=random.choice(SYNONYMS),
                        status=random.choice(ENUMS["status"]),
                        comparison=random.choice(ENUMS["comparison"]),
                        value=random.choice(ENUMS["value"]),
                    )
                )
    
    # Shuffle for variety and return exact count
    random.shuffle(dataset)
    return dataset[:total]


# =====================================================
# 13. UTILITY FUNCTIONS
# =====================================================

def get_components_for_view_type(view_type):
    """
    Get all components for a specific view type.
    Ensures the primary component (Table/List/Card) is always included.
    
    Args:
        view_type: "table", "list", or "card"
    
    Returns:
        dict with primary, required, optional, and all_components
    """
    components = VIEW_TYPE_COMPONENTS.get(view_type, {})
    
    return {
        "view_type": view_type,
        "primary_component": components.get("primary", ""),
        "required_components": components.get("required", []),
        "optional_components": components.get("optional", []),
        "all_components": components.get("required", []) + components.get("optional", [])
    }


def get_query_metadata(query, pattern=None):
    """Get metadata for a query including view type and components"""
    if pattern is None:
        # Try to infer pattern from query keywords
        if "top 10" in query or "sorted by" in query:
            pattern = "LIST_ADVANCED"
        elif "show all" in query or "list all" in query:
            pattern = "LIST_SIMPLE"
        elif any(word in query for word in ["sum", "count", "average", "total", "grouped"]):
            pattern = "AGGREGATE"
        elif "with related" in query or "+" in query:
            pattern = "MULTI_OBJECT"
        else:
            pattern = "LIST_SIMPLE"
    
    view_type = PATTERN_TO_VIEW_TYPE.get(pattern, "table")
    view_level = PATTERN_TO_VIEW_LEVEL.get(pattern, "basic")
    components_info = get_components_for_view_type(view_type)
    
    return {
        "query": query,
        "pattern": pattern,
        "view_type": view_type,
        "view_level": view_level,
        "primary_component": components_info["primary_component"],
        "components_required": components_info["required_components"],
        "components_optional": components_info["optional_components"],
        "all_components": components_info["all_components"]
    }


def get_layout_for_query(query, pattern=None):
    """
    Get suggested layout structure based on query and view type.
    Returns the primary component and supporting components.
    
    Example:
        For "show all customers" (table view):
        - Primary: Table
        - Supporting: Heading, Badge, Button, Link
    """
    metadata = get_query_metadata(query, pattern)
    view_type = metadata["view_type"]
    
    # Build layout structure
    layout = {
        "query": query,
        "view_type": view_type,
        "view_level": metadata["view_level"],
        "layout_structure": {
            "header": ["Heading"],
            "main": [metadata["primary_component"]],  # Table/Card/ListCard
            "supporting": []
        }
    }
    
    # Add supporting components based on complexity
    if metadata["view_level"] == "basic":
        layout["layout_structure"]["supporting"] = ["Badge", "Button"]
    elif metadata["view_level"] == "medium":
        layout["layout_structure"]["supporting"] = ["Badge", "Button", "Link", "Chip"]
    else:  # advanced
        if view_type == "card":
            layout["layout_structure"]["supporting"] = ["Metric", "Dashlet", "Badge", "Button", "Avatar"]
        elif view_type == "list":
            layout["layout_structure"]["supporting"] = ["Avatar", "Badge", "Divider", "Button"]
        else:
            layout["layout_structure"]["supporting"] = ["Badge", "Chip", "Button", "Link"]
    
    return layout


def export_with_metadata(filename="crm_queries_with_metadata.json"):
    """Export queries with full metadata in JSON format"""
    import json
    
    queries = generate_full_dataset(2000)
    metadata_list = []
    
    # Determine pattern for each query (simple heuristic)
    for i, query in enumerate(queries):
        metadata = get_query_metadata(query)
        metadata["id"] = i + 1
        metadata["layout"] = get_layout_for_query(query)
        metadata_list.append(metadata)
    
    output = {
        "total_queries": len(queries),
        "view_types": list(VIEW_TYPES.keys()),
        "view_levels": list(VIEW_LEVELS.keys()),
        "view_type_mappings": {
            "table_uses": VIEW_TYPE_TO_COMPONENT["table"],
            "list_uses": VIEW_TYPE_TO_COMPONENT["list"],
            "card_uses": VIEW_TYPE_TO_COMPONENT["card"]
        },
        "queries": metadata_list
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✔ Exported {len(queries)} queries with metadata to {filename}")
    print(f"   • Table view queries use: Table component")
    print(f"   • List view queries use: ListCard component")
    print(f"   • Card view queries use: Card component")


# =====================================================
# 14. EXPORT TO FILE
# =====================================================

def export_queries(filename="crm_queries.txt"):
    queries = generate_full_dataset(2500)

    with open(filename, "w", encoding="utf-8") as f:
        for i, q in enumerate(queries, 1):
            f.write(f"{i}. {q}\n")

    print(f"✔ Exported {len(queries)} CRM queries to {filename}")


# =====================================================
# 15. RUN WHEN EXECUTED
# =====================================================

if __name__ == "__main__":
    export_queries()
    # Optionally export with metadata
    # export_with_metadata()
