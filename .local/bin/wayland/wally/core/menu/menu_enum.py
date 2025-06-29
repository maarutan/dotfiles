from enum import Enum


class MainMenu(Enum):
    WALLPAPERS = "wallpapers"
    PATHS = "paths"
    EXIT = "exit"


class WallpapersMenu(Enum):  # ----{{{{
    FAVORITES = "favorites"
    THEME = "theme"
    RANDOM = "random"
    ALL = "all"
    BACK = "back"


class FavoritesMenu(Enum):
    CHOICE = "choice"
    ADD = "add"
    REMOVE = "remove"
    BACK = "back"


class ThemeMenu(Enum):
    CHOICE = "choice"
    ADD = "add"
    REMOVE = "remove"
    BACK = "back"


class RandomMenu(Enum):
    FAVORITES = "favorites"
    THEME = "theme"
    ALL = "all"
    BACK = "back"


# ----------}}}}
