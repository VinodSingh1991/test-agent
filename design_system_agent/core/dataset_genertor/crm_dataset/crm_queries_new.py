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

OBJECTS = ["lead", "case", "account", "customer", "loan", "task", "appointment", "branch"]
INTENT_PATTERNS = ["show", "get", "list", "fetch", "display", "find"]
VIEWS_PATTERNS = ["table", "list", "card", "dashboard", "summary", "insight", "profile", "graph", "chart"]
RELATIONS_PATTERNS = ["with related", "where related", "grouped by", "joined with"]

# =====================================================
# 2. SYNONYMS (For Natural Language Variability)
SYNONYMS = {
    "show": ["show", "get", "list", "fetch", "display", "find"],
    "table": ["table", "list", "card", "dashboard", "summary", "insight", "profile", "graph", "chart"],
    "with related": ["with related", "where related", "grouped by", "joined with"],
    "lead": ["lead", "potential customer", "sales lead"],
    "case": ["case", "support ticket", "issue"],
    "account": ["account", "client account", "customer account"],
    "customer": ["customer", "client", "account holder"],
    "loan": ["loan", "credit application", "mortgage"],
    "task": ["task", "to-do", "activity"],
    "appointment": ["appointment", "meeting", "schedule"],
    "branch": ["branch", "office location", "bank branch"]
}

# =====================================================
# 3. PATTERN TEMPLATES (For Query Generation)

PATTERN_TEMPLATES = {
    # Basic Patterns
    "basic": [
        "{intent} {object}",
        "{intent} {object} in {view}",
        "{intent} {object} with related {related_object}",
        "{intent} {object} where related {related_object}",
        "{intent} {object} grouped by {related_object}",
        "{intent} {object} joined with {related_object}"
    ],  
    # Medium Complexity Patterns
    "medium": [
        "{intent} {object} in {view} with related {related_object}",
        "{intent} {object} where related {related_object} in {view}",
        "{intent} {object} grouped by {related_object} in {view}",
        "{intent} {object} joined with {related_object} in {view}"
    ],

    # Advanced Patterns
    "advanced": [
        "{intent} {object} in {view} with related {related_object} where related {related_object}",
        "{intent} {object} where related {related_object} grouped by {related_object} in {view}",
        "{intent} {object} joined with {related_object} grouped by {related_object} in {view}"
    ],
}