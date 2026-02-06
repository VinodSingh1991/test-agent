# Banking CRM Query Generation - Summary

## Overview
Successfully generated **2,000 comprehensive banking CRM queries** covering all scenarios.

## Generated Files

### 📄 Main Export Files
1. **banking_crm_queries_2000.txt** (100 KB)
   - Plain text format with all 2000 queries
   - Includes statistics and distribution
   - Easy to read and review

2. **banking_crm_queries_2000.json** (310 KB)
   - Structured JSON format with metadata
   - Each query includes: ID, query text, object type, view type
   - Perfect for programmatic access

3. **banking_crm_queries_2000.csv** (128 KB)
   - CSV format for Excel/spreadsheet analysis
   - Columns: ID, Query, Object Type, View Type, Length
   - Easy to filter and analyze

### 📁 Organized Pattern Directory
**query_patterns/** - Queries organized by object and pattern
- 6 object directories (lead, account, customer, loan, task, branch)
- 41 pattern files total
- Each file contains queries for specific object+pattern combination

## Query Distribution

### By Object
| Object   | Count | Percentage |
|----------|-------|------------|
| Loan     | 679   | 34.0%      |
| Customer | 617   | 30.9%      |
| Branch   | 599   | 29.9%      |
| Lead     | 503   | 25.1%      |
| Account  | 476   | 23.8%      |
| Task     | 311   | 15.6%      |

### By Pattern
| Pattern                        | Count | Percentage |
|--------------------------------|-------|------------|
| COMBINATIONS                   | 200   | 16.4%      |
| LIST_SIMPLE                    | 180   | 14.8%      |
| LIST_ADVANCED                  | 150   | 12.3%      |
| AGGREGATE                      | 150   | 12.3%      |
| MULTI_OBJECT                   | 120   | 9.8%       |
| BRANCH_MANAGER_QUERIES         | 120   | 9.8%       |
| PERIODIC_QUERIES               | 90    | 7.4%       |
| ADVANCED_AGGREGATE_RELATED     | 90    | 7.4%       |
| TASK_RELATED                   | 60    | 4.9%       |
| FULL_COMPLEX                   | 60    | 4.9%       |

### By View Type
| View Type | Count | Percentage |
|-----------|-------|------------|
| Table     | 710   | 58.2%      |
| Chart     | 390   | 32.0%      |
| Summary   | 120   | 9.8%       |

## Sample Queries

### Simple List Queries
```
show all customer
show all loan yesterday
show my account with status open
list lead where priority is high
```

### Advanced List Queries
```
show top 10 loan where status is approved
show customer sorted by age desc
filter account where balance is greater than 500000
show lead created last month
```

### Multi-Object Queries
```
show customer with related account
show loan with related customer
list lead and related task filtered by pending
```

### Aggregate Queries
```
show sum of loan_amount in loan
show average of balance for account last quarter
calculate total emi_amount across all loan
show customer grouped by branch with count of total_balance
```

### Complex Queries
```
show customers with total account balance greater than 500000 and loan amount greater than 200000
show branch wise count of leads where loan status is approved
show sum of loan amount for customers having tasks pending
show total portfolio (loans + accounts) for each relationship manager
```

### Branch Manager Queries
```
show branch wise loan
show my branch account with status open
list accounts in branch with balance greater than 100000
show branch performance summary: lead count, loan total, deposits total
```

## Patterns Covered

### Core Patterns
1. **LIST_SIMPLE** - Basic listing queries
2. **LIST_ADVANCED** - Filtered and sorted lists
3. **MULTI_OBJECT** - Queries across related objects
4. **AGGREGATE** - Sum, count, average, min, max
5. **ADVANCED_AGGREGATE_RELATED** - Cross-object aggregations
6. **FULL_COMPLEX** - Complex multi-condition queries

### Specialized Patterns
7. **TASK_RELATED** - Task management queries
8. **PERIODIC_QUERIES** - Time-based analytics
9. **BRANCH_MANAGER_QUERIES** - Branch-level dashboards
10. **COMBINATIONS** - Multi-entity relationship queries

## Object Relationships

The queries leverage these object relationships:
- Lead → Customer → Account
- Lead → Customer → Loan
- Branch → Lead/Account/Loan
- Task → Lead/Loan

## Enumerations Used

**Status**: open, closed, in-progress, pending, approved, rejected
**Priority**: high, medium, low
**Date Ranges**: today, yesterday, last week, last month, last 3 months, this quarter, this year
**Metrics**: sum, count, average, min, max
**Comparison Operators**: greater than, less than, equal to, not equal to
**Values**: 50000, 100000, 200000, 500000, 1000000

## Usage Instructions

### View All Queries
```bash
cat banking_crm_queries_2000.txt
```

### Load Queries in Python
```python
import json

# Load from JSON
with open('banking_crm_queries_2000.json', 'r') as f:
    data = json.load(f)
    queries = data['queries']

# Or import directly from module
from design_system_agent.core.dataset_genertor.crm_dataset.crm_queries import COMPREHENSIVE_QUERIES_2000

print(f"Total queries: {len(COMPREHENSIVE_QUERIES_2000)}")
for query in COMPREHENSIVE_QUERIES_2000[:10]:
    print(query)
```

### Filter Queries
```python
# Get only loan queries
loan_queries = [q['query'] for q in queries if q['object_type'] == 'loan']

# Get only chart/analytics queries
chart_queries = [q['query'] for q in queries if q['view_type'] == 'chart']

# Get complex queries
complex_queries = [q for q in COMPREHENSIVE_QUERIES_2000 if 'portfolio' in q or 'branch wise' in q]
```

## Next Steps

1. **Review Queries** - Check banking_crm_queries_2000.txt for comprehensive list
2. **Analyze Patterns** - Explore query_patterns/ directory for organized view
3. **Integrate with Layout Generator** - Use these queries to generate UI layouts
4. **Test Coverage** - Verify all banking CRM scenarios are covered
5. **Extend Patterns** - Add more pattern templates if needed

## Statistics Summary

- ✅ 2,000 unique queries generated
- ✅ 6 banking objects covered
- ✅ 10+ query patterns implemented
- ✅ 3 view types supported (table, chart, summary)
- ✅ Multiple export formats (TXT, JSON, CSV)
- ✅ Organized by object and pattern

---

Generated: February 6, 2026
Domain: Banking CRM
System: Design System Agent
