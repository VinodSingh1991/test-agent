"""
Preset image patterns for common use cases
"""
from .image_builder import ImageBuilder

# Size patterns
SMALL_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").size("sm").build()
MEDIUM_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").size("md").build()
LARGE_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").size("lg").build()
EXTRA_LARGE_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").size("xl").build()

# Shape patterns
ROUNDED_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").rounded().build()
CIRCLE_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").circle().build()
THUMBNAIL_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").thumbnail().build()

# Fluid pattern
FLUID_IMAGE = ImageBuilder().src("/image.jpg").alt("Image").fluid().build()
RESPONSIVE_IMAGE = ImageBuilder().src("/image.jpg").alt("Responsive").fluid().rounded().build()

# Size × Shape combinations
SMALL_ROUNDED = ImageBuilder().src("/image.jpg").alt("Image").size("sm").rounded().build()
SMALL_CIRCLE = ImageBuilder().src("/image.jpg").alt("Image").size("sm").circle().build()
MEDIUM_ROUNDED = ImageBuilder().src("/image.jpg").alt("Image").size("md").rounded().build()
LARGE_CIRCLE = ImageBuilder().src("/image.jpg").alt("Image").size("lg").circle().build()

# Common use cases
PROFILE_IMAGE = ImageBuilder().src("/profile.jpg").alt("Profile").size("lg").circle().build()
PRODUCT_IMAGE = ImageBuilder().src("/product.jpg").alt("Product").size("md").rounded().build()
THUMBNAIL = ImageBuilder().src("/thumb.jpg").alt("Thumbnail").thumbnail().build()
AVATAR_IMAGE = ImageBuilder().src("/avatar.jpg").alt("Avatar").size("sm").circle().build()
BANNER_IMAGE = ImageBuilder().src("/banner.jpg").alt("Banner").fluid().build()
CARD_IMAGE = ImageBuilder().src("/card.jpg").alt("Card").size("md").rounded().build()
GALLERY_IMAGE = ImageBuilder().src("/gallery.jpg").alt("Gallery").size("md").build()
LOGO_IMAGE = ImageBuilder().src("/logo.png").alt("Logo").size("sm").build()

# All patterns
ALL_IMAGE_PATTERNS = {
    "small": SMALL_IMAGE,
    "medium": MEDIUM_IMAGE,
    "large": LARGE_IMAGE,
    "xl": EXTRA_LARGE_IMAGE,
    "rounded": ROUNDED_IMAGE,
    "circle": CIRCLE_IMAGE,
    "thumbnail": THUMBNAIL_IMAGE,
    "fluid": FLUID_IMAGE,
    "responsive": RESPONSIVE_IMAGE,
    "small_rounded": SMALL_ROUNDED,
    "small_circle": SMALL_CIRCLE,
    "medium_rounded": MEDIUM_ROUNDED,
    "large_circle": LARGE_CIRCLE,
    "profile": PROFILE_IMAGE,
    "product": PRODUCT_IMAGE,
    "thumb": THUMBNAIL,
    "avatar": AVATAR_IMAGE,
    "banner": BANNER_IMAGE,
    "card": CARD_IMAGE,
    "gallery": GALLERY_IMAGE,
    "logo": LOGO_IMAGE,
}
