from core import (
    FavoritesMenu,
    MainMenu,
    RandomMenu,
    ThemeMenu,
    WallpapersMenu,
)
from services import (
    is_nerdfonts,
    rofi,
)
from services import (
    JsonManager,
    FileManager,
    WSDataBaseHandler,
)
from utils import log_exceptions
from dataclasses import dataclass
from sys import exit


class MenuHandler:
    def __init__(self):
        self.Fm = FileManager
        self.DBws = WSDataBaseHandler
        self.main_options = [e.value for e in MainMenu]
        self.wallpapers_options = [e.value for e in WallpapersMenu]
        self.wallpaper_favorites_options = [e.value for e in FavoritesMenu]
        self.wallpaper_theme_options = [e.value for e in ThemeMenu]
        self.wallpaper_random_options = [e.value for e in RandomMenu]
        self.run()

    @log_exceptions
    def wallpapers_options_handler(self):
        rm = rofi(self.wallpapers_options).dmenu()
        match rm:
            case "favorites":
                self.favorites_options_handler()
            case "theme":
                self.theme_options_handler()
            case "random":
                self.random_wallpaper_options_handler()
            case "all":
                self.all_options_handler()
            case "back":
                self.menu_state_handler()
            case _:
                self.menu_state_handler()

    def theme_options_handler(self):
        rm = rofi(self.wallpaper_theme_options).dmenu()
        match rm:
            case "back":
                self.wallpapers_options_handler()
            case _:
                self.wallpapers_options_handler()

    def all_options_handler(self): ...

    def random_wallpaper_options_handler(self):
        rm = rofi(self.wallpaper_random_options).dmenu()
        match rm:
            case "favorites":
                self.random_wp_favorites_handler()
            case "theme":
                self.random_wp_theme_handerler()
            case "all":
                self.random_wp_all_handerler()
            case "back":
                self.wallpapers_options_handler()
            case _:
                self.wallpapers_options_handler()

    def random_wp_favorites_handler(self): ...

    def random_wp_theme_handerler(self): ...

    def random_wp_all_handerler(self): ...

    def favorites_options_handler(self):
        rm = rofi(self.wallpaper_favorites_options).dmenu()
        match rm:
            case "choice":
                self.favorites_choice_handler()
            case "add":
                self.favorites_add_remove_handler(add=True)
            case "remove":
                self.favorites_add_remove_handler(remove=True)
            case "back":
                self.wallpapers_options_handler()
            case _:
                self.wallpapers_options_handler()

    def favorites_choice_handler(self):
        # rm = rofi()dmenu()
        ...

    def favorites_add_remove_handler(
        self,
        remove: bool = False,
        add: bool = True,
    ):
        # rm = rofi()dmenu()
        ...

    @log_exceptions
    def menu_state_handler(self):
        rofi_menu = rofi
        rm = rofi_menu(self.main_options).dmenu()

        match rm:
            case MainMenu.WALLPAPERS.value:
                self.wallpapers_options_handler()
            case "paths":
                print("paths")
            case "exit":
                exit()
            case _:
                exit()

    def run(self):
        self.menu_state_handler()

    def __str__(self):
        return ""


menu_wally = MenuHandler
