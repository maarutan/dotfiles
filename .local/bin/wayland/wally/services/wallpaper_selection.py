from pathlib import Path
from services import JsonManager
from utils import log_exceptions
from dataclasses import dataclass
import re


@dataclass
class WshArgs:
    data_dict: dict


class WallpaperSelection(WshArgs):
    def __init__(
        self,
        live_path: Path,
        static_path: Path,
        root_dir: Path,
    ) -> None:
        self.live_path = root_dir / live_path
        self.static_path = root_dir / static_path
        self.root_dir = root_dir
        from core import DATABASE_WALLY

        self.json_path = Path(DATABASE_WALLY)
        self.Jm = JsonManager(self.json_path)

        super().__init__(
            data_dict={
                "root_dir": str(self.root_dir),
                "static": {
                    "all_file_names": [],
                    "favorites": [],
                    "current_wallpaper": [],
                    "current_theme": [],
                    "themes": [],
                },
                "live": {
                    "all_file_names": [],
                    "favorites": [],
                    "current_wallpaper": [],
                    "current_theme": [],
                    "themes": [],
                },
            }
        )

    @log_exceptions
    def get_file_list(self, directory: Path) -> list[str]:
        if not directory.exists():
            return []
        return [file.name for file in directory.iterdir() if file.is_file()]

    def classify_files(self, file_list: list[str], subfolder: str) -> dict:
        result = {
            "all_file_names": [],
            "favorites": [],
            "current_wallpaper": [],
            "current_theme": [],
            "themes": [],
        }

        for filename in file_list:
            result["all_file_names"].append(filename)

            is_active = filename.startswith("*")
            is_favorite = "_*_" in filename

            theme_match = re.match(r"^\*?([a-zA-Z0-9]+_)", filename)
            if theme_match:
                theme = theme_match.group(1).rstrip("_")
                if theme not in result["themes"]:
                    result["themes"].append(theme)

            if is_active and not result["current_wallpaper"]:
                full_path = self.root_dir / subfolder / filename
                result["current_wallpaper"].append(str(full_path))
                if theme_match:
                    theme = theme_match.group(1).rstrip("_")
                    if theme not in result["current_wallpaper"]:
                        result["current_theme"].append(theme)

            if is_favorite:
                result["favorites"].append(filename)

        return result

    @log_exceptions
    def refresh_wallpaper_data(self) -> None:
        for kind, path in {"static": self.static_path, "live": self.live_path}.items():
            files = self.get_file_list(path)
            classified = self.classify_files(files, subfolder=kind)
            self.data_dict[kind] = classified

        self.Jm.write(self.data_dict, indent=2)

    def __str__(self):
        return ""


wallpaper_selection = WallpaperSelection
