"""
Preset avatar patterns for common use cases
"""
from .avatar_builder import AvatarBuilder

# Size patterns
SMALL_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").build()
MEDIUM_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("md").build()
LARGE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("lg").build()
EXTRA_LARGE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("xl").build()

# Shape patterns
CIRCLE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").shape("circle").build()
SQUARE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").shape("square").build()

# Status patterns
ONLINE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").status("online").build()
OFFLINE_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").status("offline").build()
AWAY_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").status("away").build()
BUSY_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").status("busy").build()

# Size × Shape combinations
SMALL_CIRCLE = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").shape("circle").build()
SMALL_SQUARE = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").shape("square").build()
LARGE_CIRCLE = AvatarBuilder().src("/avatar.jpg").alt("User").size("lg").shape("circle").build()
LARGE_SQUARE = AvatarBuilder().src("/avatar.jpg").alt("User").size("lg").shape("square").build()

# Size × Status combinations
SMALL_ONLINE = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").status("online").build()
MEDIUM_ONLINE = AvatarBuilder().src("/avatar.jpg").alt("User").size("md").status("online").build()
LARGE_ONLINE = AvatarBuilder().src("/avatar.jpg").alt("User").size("lg").status("online").build()

# Common use cases
USER_AVATAR = AvatarBuilder().src("/user.jpg").alt("User").size("md").shape("circle").build()
PROFILE_AVATAR = AvatarBuilder().src("/profile.jpg").alt("Profile").size("lg").shape("circle").status("online").build()
LIST_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").shape("circle").build()
NAVBAR_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("User").size("sm").shape("circle").status("online").build()
COMMENT_AVATAR = AvatarBuilder().src("/avatar.jpg").alt("Commenter").size("md").shape("circle").build()

# All patterns
ALL_AVATAR_PATTERNS = {
    "small": SMALL_AVATAR,
    "medium": MEDIUM_AVATAR,
    "large": LARGE_AVATAR,
    "xl": EXTRA_LARGE_AVATAR,
    "circle": CIRCLE_AVATAR,
    "square": SQUARE_AVATAR,
    "online": ONLINE_AVATAR,
    "offline": OFFLINE_AVATAR,
    "away": AWAY_AVATAR,
    "busy": BUSY_AVATAR,
    "small_circle": SMALL_CIRCLE,
    "small_square": SMALL_SQUARE,
    "large_circle": LARGE_CIRCLE,
    "large_square": LARGE_SQUARE,
    "small_online": SMALL_ONLINE,
    "medium_online": MEDIUM_ONLINE,
    "large_online": LARGE_ONLINE,
    "user": USER_AVATAR,
    "profile": PROFILE_AVATAR,
    "list": LIST_AVATAR,
    "navbar": NAVBAR_AVATAR,
    "comment": COMMENT_AVATAR,
}
