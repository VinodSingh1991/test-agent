"""
Preset metric patterns for common use cases
"""
from .metric_builder import MetricBuilder

# Basic metrics
SIMPLE_METRIC = MetricBuilder().value("1,234").label("Total Users").build()
REVENUE_METRIC = MetricBuilder().value("$125,000").label("Revenue").build()
COUNT_METRIC = MetricBuilder().value("567").label("Active Sessions").build()

# With positive trends
METRIC_UP_5 = MetricBuilder().value("1,234").label("Sales").change("+5% ↑").build()
METRIC_UP_10 = MetricBuilder().value("$50,000").label("Revenue").change("+10% ↑").build()
METRIC_UP_15 = MetricBuilder().value("2,500").label("Subscribers").change("+15% ↑").build()

# With negative trends
METRIC_DOWN_3 = MetricBuilder().value("789").label("Returns").change("-3% ↓").build()
METRIC_DOWN_8 = MetricBuilder().value("45").label("Errors").change("-8% ↓").build()
METRIC_DOWN_12 = MetricBuilder().value("123").label("Bounces").change("-12% ↓").build()

# Neutral trends
METRIC_NEUTRAL = MetricBuilder().value("500").label("Pending").change("0% →").build()
METRIC_STABLE = MetricBuilder().value("$10,000").label("Balance").change("+0.5% →").build()

# Variant patterns
PRIMARY_METRIC = MetricBuilder().value("9,876").label("Total Orders").variant("primary").change("+8% ↑").build()
SUCCESS_METRIC = MetricBuilder().value("98%").label("Uptime").variant("success").change("+2% ↑").build()
DANGER_METRIC = MetricBuilder().value("15").label("Critical Issues").variant("danger").change("+3% ↑").build()
WARNING_METRIC = MetricBuilder().value("78%").label("Storage Used").variant("warning").change("+5% ↑").build()

# Common use cases - Sales metrics
TOTAL_SALES = MetricBuilder().value("$89,450").label("Total Sales").change("+12% ↑").build()
NEW_CUSTOMERS = MetricBuilder().value("234").label("New Customers").change("+18% ↑").build()
AVERAGE_ORDER = MetricBuilder().value("$145").label("Avg Order Value").change("+7% ↑").build()
CONVERSION_RATE = MetricBuilder().value("3.2%").label("Conversion Rate").change("+0.5% ↑").build()

# User metrics
ACTIVE_USERS = MetricBuilder().value("1,543").label("Active Users").change("+9% ↑").build()
NEW_SIGNUPS = MetricBuilder().value("87").label("New Signups").change("+15% ↑").build()
CHURN_RATE = MetricBuilder().value("2.1%").label("Churn Rate").change("-0.3% ↓").build()
SESSION_DURATION = MetricBuilder().value("4m 32s").label("Avg Session").change("+25s ↑").build()

# Performance metrics
PAGE_LOAD = MetricBuilder().value("1.2s").label("Page Load Time").change("-0.3s ↓").build()
API_RESPONSE = MetricBuilder().value("125ms").label("API Response").change("-15ms ↓").build()
UPTIME = MetricBuilder().value("99.9%").label("Uptime").variant("success").change("+0.1% ↑").build()
ERROR_RATE = MetricBuilder().value("0.05%").label("Error Rate").variant("success").change("-0.02% ↓").build()

# Financial metrics
MONTHLY_REVENUE = MetricBuilder().value("$125,000").label("Monthly Revenue").change("+12% ↑").build()
PROFIT_MARGIN = MetricBuilder().value("32%").label("Profit Margin").change("+2% ↑").build()
OPERATING_COST = MetricBuilder().value("$45,000").label("Operating Cost").change("-5% ↓").build()
ROI = MetricBuilder().value("185%").label("ROI").variant("success").change("+15% ↑").build()

# Engagement metrics
POSTS_CREATED = MetricBuilder().value("456").label("Posts Created").change("+23% ↑").build()
COMMENTS = MetricBuilder().value("1,234").label("Comments").change("+18% ↑").build()
LIKES = MetricBuilder().value("5,678").label("Total Likes").change("+32% ↑").build()
SHARES = MetricBuilder().value("890").label("Shares").change("+12% ↑").build()

# Large numbers
MILLION_METRIC = MetricBuilder().value("1.2M").label("Total Views").change("+15% ↑").build()
THOUSAND_METRIC = MetricBuilder().value("45K").label("Followers").change("+8% ↑").build()
BILLION_METRIC = MetricBuilder().value("$2.5B").label("Market Cap").change("+5% ↑").build()

# Percentage metrics
HIGH_PERCENTAGE = MetricBuilder().value("95%").label("Satisfaction").variant("success").change("+3% ↑").build()
MID_PERCENTAGE = MetricBuilder().value("75%").label("Completion").change("+5% ↑").build()
LOW_PERCENTAGE = MetricBuilder().value("15%").label("Discount").change("-2% ↓").build()

# All patterns
ALL_METRIC_PATTERNS = {
    "simple": SIMPLE_METRIC,
    "revenue": REVENUE_METRIC,
    "count": COUNT_METRIC,
    "up_5": METRIC_UP_5,
    "up_10": METRIC_UP_10,
    "up_15": METRIC_UP_15,
    "down_3": METRIC_DOWN_3,
    "down_8": METRIC_DOWN_8,
    "down_12": METRIC_DOWN_12,
    "neutral": METRIC_NEUTRAL,
    "stable": METRIC_STABLE,
    "primary": PRIMARY_METRIC,
    "success": SUCCESS_METRIC,
    "danger": DANGER_METRIC,
    "warning": WARNING_METRIC,
    "total_sales": TOTAL_SALES,
    "new_customers": NEW_CUSTOMERS,
    "avg_order": AVERAGE_ORDER,
    "conversion": CONVERSION_RATE,
    "active_users": ACTIVE_USERS,
    "signups": NEW_SIGNUPS,
    "churn": CHURN_RATE,
    "session": SESSION_DURATION,
    "page_load": PAGE_LOAD,
    "api_response": API_RESPONSE,
    "uptime": UPTIME,
    "error_rate": ERROR_RATE,
    "monthly_revenue": MONTHLY_REVENUE,
    "profit": PROFIT_MARGIN,
    "cost": OPERATING_COST,
    "roi": ROI,
    "posts": POSTS_CREATED,
    "comments": COMMENTS,
    "likes": LIKES,
    "shares": SHARES,
    "million": MILLION_METRIC,
    "thousand": THOUSAND_METRIC,
    "billion": BILLION_METRIC,
    "high_percent": HIGH_PERCENTAGE,
    "mid_percent": MID_PERCENTAGE,
    "low_percent": LOW_PERCENTAGE,
}
