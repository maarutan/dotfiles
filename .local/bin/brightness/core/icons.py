import dataclasses
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from core.config import Config
from modules import (
    Brightness,
    FileManager,
)
from core.path.list import (
    ICONS_THEME_DIR,
    CACHE_FILE_SYSTEM_THEME,
    RELATIVE_CACHE_FILE_SYSTEM_THEME,
)


@dataclass
class IconsTheme:
    icons: dict = dataclasses.field(default_factory=dict)


class IconPath(IconsTheme):
    def __init__(self):
        super().__init__()
        self.conf = Config()
        self.fm = FileManager
        self.brness = Brightness()

        self.current_theme = self.conf.get_option("theme")
        self.theme_list = self.get_theme(only_name=True)

        if self.current_theme not in self.theme_list:
            print(
                f"[WARN] Theme '{self.current_theme}' not found. Falling back to 'default'"
            )
            self.current_theme = "default"

        self.path = ICONS_THEME_DIR / self.current_theme / self.get_system_theme()
        self.icons = {i: f"brness_{i}.svg" for i in range(1, 101)}

    def get_theme(self, only_name: bool) -> list:
        """if `only_name=true` return only theme name else absolute path"""
        themes = []
        for i in ICONS_THEME_DIR.iterdir():
            themes.append(i.name if only_name else i.absolute())
        return themes

    def get_system_theme(self) -> str:
        if not CACHE_FILE_SYSTEM_THEME.exists():
            CACHE_FILE_SYSTEM_THEME.parent.mkdir(parents=True, exist_ok=True)
            CACHE_FILE_SYSTEM_THEME.write_text("dark")
        return (
            CACHE_FILE_SYSTEM_THEME.read_text().strip()
            if CACHE_FILE_SYSTEM_THEME
            else RELATIVE_CACHE_FILE_SYSTEM_THEME.read_text().strip()
        )

    def get_brightness_icon(self) -> Optional[Path]:
        brightness = self.brness.get_brightness()
        int_keys = sorted([k for k in self.icons.keys()], reverse=True)

        for key in int_keys:
            if brightness >= key:
                result = self.path / self.icons[key]
                if self.fm(Path(result)).is_exists():
                    return result
                for alt_key in range(key - 1, 0, -1):
                    if alt_key in self.icons:
                        alt_result = self.path / self.icons[alt_key]
                        if self.fm(Path(alt_result)).is_exists():
                            return alt_result
                break

        if self.icons:
            fallback_key = max(self.icons.keys())
            fallback = self.path / self.icons[fallback_key]
            if self.fm(fallback).is_exists():
                return fallback
        return None
