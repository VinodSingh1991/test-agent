"""
Preset alert patterns for common use cases
"""
from .alert_builder import AlertBuilder

# Variant patterns
INFO_ALERT = AlertBuilder().title("Information").message("This is an informational message").variant("info").build()
SUCCESS_ALERT = AlertBuilder().title("Success").message("Operation completed successfully").variant("success").build()
WARNING_ALERT = AlertBuilder().title("Warning").message("Please review this warning").variant("warning").build()
DANGER_ALERT = AlertBuilder().title("Error").message("An error has occurred").variant("danger").build()

# With icons
INFO_ICON_ALERT = AlertBuilder().title("Info").message("Information message").variant("info").icon("InfoIcon").build()
SUCCESS_ICON_ALERT = AlertBuilder().title("Done").message("Task completed").variant("success").icon("CheckCircleIcon").build()
WARNING_ICON_ALERT = AlertBuilder().title("Caution").message("Warning message").variant("warning").icon("AlertTriangleIcon").build()
ERROR_ICON_ALERT = AlertBuilder().title("Failed").message("Error occurred").variant("danger").icon("XCircleIcon").build()

# Dismissible alerts
DISMISSIBLE_INFO = AlertBuilder().title("Tip").message("You can dismiss this message").variant("info").dismissible().build()
DISMISSIBLE_SUCCESS = AlertBuilder().title("Saved").message("Changes saved successfully").variant("success").dismissible().build()
DISMISSIBLE_WARNING = AlertBuilder().title("Notice").message("Important update").variant("warning").dismissible().build()

# With actions
ACTION_ALERT = AlertBuilder().title("Update Available").message("A new version is available").variant("info").action("Update Now").build()
SUCCESS_ACTION = AlertBuilder().title("Success").message("Profile updated").variant("success").action("View Profile").build()
WARNING_ACTION = AlertBuilder().title("Storage Low").message("You're running out of space").variant("warning").action("Upgrade").build()

# Complete alerts (icon + action + dismissible)
COMPLETE_INFO = (
    AlertBuilder()
    .title("New Feature")
    .message("Check out our new dashboard")
    .variant("info")
    .icon("SparkleIcon")
    .action("Explore")
    .dismissible()
    .build()
)

COMPLETE_SUCCESS = (
    AlertBuilder()
    .title("Welcome")
    .message("Your account has been created")
    .variant("success")
    .icon("CheckCircleIcon")
    .action("Get Started")
    .dismissible()
    .build()
)

COMPLETE_WARNING = (
    AlertBuilder()
    .title("Action Required")
    .message("Please verify your email address")
    .variant("warning")
    .icon("AlertIcon")
    .action("Verify Email")
    .dismissible()
    .build()
)

COMPLETE_DANGER = (
    AlertBuilder()
    .title("Payment Failed")
    .message("Your payment could not be processed")
    .variant("danger")
    .icon("XCircleIcon")
    .action("Retry Payment")
    .dismissible()
    .build()
)

# Common use cases
WELCOME_ALERT = (
    AlertBuilder()
    .title("Welcome!")
    .message("Thanks for joining us")
    .variant("success")
    .icon("PartyIcon")
    .dismissible()
    .build()
)

MAINTENANCE_ALERT = (
    AlertBuilder()
    .title("Scheduled Maintenance")
    .message("Service will be down from 2 AM to 4 AM")
    .variant("warning")
    .icon("ToolIcon")
    .build()
)

ERROR_NOTIFICATION = (
    AlertBuilder()
    .title("Connection Error")
    .message("Unable to connect to server")
    .variant("danger")
    .icon("WifiOffIcon")
    .action("Retry")
    .build()
)

UPDATE_NOTIFICATION = (
    AlertBuilder()
    .title("Update Available")
    .message("Version 2.0 is now available")
    .variant("info")
    .icon("DownloadIcon")
    .action("Download")
    .dismissible()
    .build()
)

# Simple message-only alerts
SIMPLE_INFO = AlertBuilder().message("This is a simple info message").variant("info").build()
SIMPLE_SUCCESS = AlertBuilder().message("Success!").variant("success").build()
SIMPLE_WARNING = AlertBuilder().message("Be careful").variant("warning").build()
SIMPLE_ERROR = AlertBuilder().message("Something went wrong").variant("danger").build()

# All patterns
ALL_ALERT_PATTERNS = {
    "info": INFO_ALERT,
    "success": SUCCESS_ALERT,
    "warning": WARNING_ALERT,
    "danger": DANGER_ALERT,
    "info_icon": INFO_ICON_ALERT,
    "success_icon": SUCCESS_ICON_ALERT,
    "warning_icon": WARNING_ICON_ALERT,
    "error_icon": ERROR_ICON_ALERT,
    "dismissible_info": DISMISSIBLE_INFO,
    "dismissible_success": DISMISSIBLE_SUCCESS,
    "dismissible_warning": DISMISSIBLE_WARNING,
    "action": ACTION_ALERT,
    "success_action": SUCCESS_ACTION,
    "warning_action": WARNING_ACTION,
    "complete_info": COMPLETE_INFO,
    "complete_success": COMPLETE_SUCCESS,
    "complete_warning": COMPLETE_WARNING,
    "complete_danger": COMPLETE_DANGER,
    "welcome": WELCOME_ALERT,
    "maintenance": MAINTENANCE_ALERT,
    "error": ERROR_NOTIFICATION,
    "update": UPDATE_NOTIFICATION,
    "simple_info": SIMPLE_INFO,
    "simple_success": SIMPLE_SUCCESS,
    "simple_warning": SIMPLE_WARNING,
    "simple_error": SIMPLE_ERROR,
}
