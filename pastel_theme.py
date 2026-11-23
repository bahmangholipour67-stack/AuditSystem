"""Enterprise Professional design tokens for AuditSystem.

The historical module name is retained for backward compatibility; the active
palette is now a restrained enterprise navy/blue/white system.
"""

PALETTE = {
    # Application surfaces
    "sage": "#E5F2EA",
    "blue": "#E8F0FA",
    "lavender": "#EEF0F8",
    "peach": "#F8EEE7",
    "ivory": "#EEF1F5",
    "gray": "#E5E9EF",
    "surface": "#FFFFFF",
    "text": "#263445",
    "muted": "#687789",
    "border": "#C8D0DA",
    "rose": "#F8E7E9",
    # Enterprise accents
    "navy": "#1F3B5B",
    "navy_deep": "#17304C",
    "navy_hover": "#243D63",
    "navy_selected": "#2E527F",
    "blue_primary": "#315F8C",
    "blue_hover": "#1F548F",
    "blue_light": "#E8EFF6",
    "green": "#287A57",
    "green_light": "#E5F2EA",
    "white": "#FFFFFF",
    "sidebar_text": "#F4F7FB",
    "sidebar_muted": "#B9C7D8",
    "sidebar_border": "#304664",
}

FONTS = {
    "family": "Tahoma",
    "body": ("Tahoma", 10),
    "small": ("Tahoma", 9),
    "heading": ("Tahoma", 14, "bold"),
    "section": ("Tahoma", 11, "bold"),
}

# Compatibility names retained for older views and mixins.
LEGACY_PALETTE = {
    "navy": PALETTE["navy"],
    "navy_deep": PALETTE["navy_deep"],
    "ivory": PALETTE["ivory"],
    "gold": PALETTE["blue_primary"],
    "gold_light": PALETTE["blue_light"],
    "blue_gray": PALETTE["gray"],
    "paper": PALETTE["surface"],
    "text": PALETTE["text"],
    "muted": PALETTE["muted"],
    "border": PALETTE["border"],
}
