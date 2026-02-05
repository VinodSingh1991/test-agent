"""
Preset insights patterns for common use cases
"""
from .insights_builder import InsightsBuilder

# Severity-based patterns
INFO_INSIGHT = (
    InsightsBuilder()
    .title("Performance Update")
    .description("System is performing optimally")
    .severity("info")
    .confidence(85)
    .build()
)

WARNING_INSIGHT = (
    InsightsBuilder()
    .title("Usage Alert")
    .description("Storage usage is above 80%")
    .severity("warning")
    .confidence(92)
    .build()
)

CRITICAL_INSIGHT = (
    InsightsBuilder()
    .title("Critical Issue")
    .description("System resources are critically low")
    .severity("critical")
    .confidence(98)
    .build()
)

# With recommendations
INSIGHT_WITH_RECOMMENDATIONS = (
    InsightsBuilder()
    .title("Optimization Opportunity")
    .description("We've identified ways to improve performance")
    .add_recommendation("Enable caching for faster load times")
    .add_recommendation("Optimize database queries")
    .add_recommendation("Compress static assets")
    .severity("info")
    .confidence(88)
    .build()
)

WARNING_WITH_RECOMMENDATIONS = (
    InsightsBuilder()
    .title("Security Warning")
    .description("Potential security vulnerabilities detected")
    .add_recommendation("Update outdated dependencies")
    .add_recommendation("Enable two-factor authentication")
    .add_recommendation("Review access permissions")
    .severity("warning")
    .confidence(95)
    .build()
)

CRITICAL_WITH_RECOMMENDATIONS = (
    InsightsBuilder()
    .title("Immediate Action Required")
    .description("Critical issues require immediate attention")
    .add_recommendation("Increase server capacity")
    .add_recommendation("Clear system cache")
    .add_recommendation("Restart affected services")
    .severity("critical")
    .confidence(99)
    .build()
)

# Common use cases - Sales insights
SALES_INSIGHT = (
    InsightsBuilder()
    .title("Sales Trend")
    .description("Sales have increased by 15% this quarter")
    .add_recommendation("Focus on top-performing products")
    .add_recommendation("Expand marketing in high-growth regions")
    .severity("info")
    .confidence(90)
    .build()
)

LOW_CONVERSION_INSIGHT = (
    InsightsBuilder()
    .title("Low Conversion Rate")
    .description("Conversion rate has dropped by 8% this month")
    .add_recommendation("Review checkout process")
    .add_recommendation("Optimize landing pages")
    .add_recommendation("A/B test call-to-action buttons")
    .severity("warning")
    .confidence(87)
    .build()
)

# Customer insights
CUSTOMER_CHURN_INSIGHT = (
    InsightsBuilder()
    .title("Churn Risk Detected")
    .description("5 high-value customers show signs of disengagement")
    .add_recommendation("Reach out with personalized offers")
    .add_recommendation("Schedule check-in calls")
    .add_recommendation("Gather feedback on pain points")
    .severity("warning")
    .confidence(93)
    .build()
)

CUSTOMER_SATISFACTION_INSIGHT = (
    InsightsBuilder()
    .title("High Satisfaction")
    .description("Customer satisfaction scores increased by 12%")
    .add_recommendation("Share success internally")
    .add_recommendation("Request testimonials")
    .severity("info")
    .confidence(91)
    .build()
)

# Performance insights
PERFORMANCE_DEGRADATION = (
    InsightsBuilder()
    .title("Performance Degradation")
    .description("Page load time increased by 25%")
    .add_recommendation("Profile slow queries")
    .add_recommendation("Optimize images")
    .add_recommendation("Review server resources")
    .severity("warning")
    .confidence(89)
    .build()
)

UPTIME_INSIGHT = (
    InsightsBuilder()
    .title("Excellent Uptime")
    .description("99.9% uptime maintained this month")
    .severity("info")
    .confidence(100)
    .build()
)

# Cost insights
COST_SPIKE = (
    InsightsBuilder()
    .title("Cost Increase")
    .description("Cloud costs increased by 30% this month")
    .add_recommendation("Review unused resources")
    .add_recommendation("Optimize storage usage")
    .add_recommendation("Consider reserved instances")
    .severity("warning")
    .confidence(96)
    .build()
)

COST_SAVINGS = (
    InsightsBuilder()
    .title("Cost Optimization")
    .description("Potential savings of $5,000/month identified")
    .add_recommendation("Scale down underutilized instances")
    .add_recommendation("Archive old data")
    .severity("info")
    .confidence(94)
    .build()
)

# Simple insights
SIMPLE_INFO_INSIGHT = (
    InsightsBuilder()
    .title("System Update")
    .description("All systems operating normally")
    .severity("info")
    .confidence(100)
    .build()
)

SIMPLE_WARNING_INSIGHT = (
    InsightsBuilder()
    .title("Attention Needed")
    .description("Review recommended")
    .severity("warning")
    .confidence(80)
    .build()
)

# All patterns
ALL_INSIGHTS_PATTERNS = {
    "info": INFO_INSIGHT,
    "warning": WARNING_INSIGHT,
    "critical": CRITICAL_INSIGHT,
    "with_recommendations": INSIGHT_WITH_RECOMMENDATIONS,
    "warning_recommendations": WARNING_WITH_RECOMMENDATIONS,
    "critical_recommendations": CRITICAL_WITH_RECOMMENDATIONS,
    "sales": SALES_INSIGHT,
    "low_conversion": LOW_CONVERSION_INSIGHT,
    "churn_risk": CUSTOMER_CHURN_INSIGHT,
    "satisfaction": CUSTOMER_SATISFACTION_INSIGHT,
    "performance": PERFORMANCE_DEGRADATION,
    "uptime": UPTIME_INSIGHT,
    "cost_spike": COST_SPIKE,
    "cost_savings": COST_SAVINGS,
    "simple_info": SIMPLE_INFO_INSIGHT,
    "simple_warning": SIMPLE_WARNING_INSIGHT,
}
