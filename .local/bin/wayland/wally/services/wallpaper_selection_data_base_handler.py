from pathlib import Path
from services import JsonManager


class WallpaperSelectionDataBaseHandler:
    def __init__(self, path: Path) -> None:
        self.Jm = JsonManager(path)
        self.path = path
        self.data = self.Jm.get_data()

    def get_abs_path_All_file_names(self, category: str) -> list:
        data = self.data[category]["all_file_names"]
        return [str(Path(self.data["root_dir"]).joinpath(category, i)) for i in data]

    def get_abs_path_Favorites(self, category: str) -> list:
        data = self.data[category]["favorites"]
        return [str(Path(self.data["root_dir"]).joinpath(category, i)) for i in data]

    def get_themes(self, category: str) -> list:
        return self.data[category]["themes"]

    def get_current_wallpaper(self, category: str) -> str:
        return self.data[category]["current_wallpaper"][0]


WSDataBaseHandler = WallpaperSelectionDataBaseHandler
