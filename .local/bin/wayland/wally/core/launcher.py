from services import wallpaper_selection
from services import thumbnail_image_convert, thumbnail_video_convert
from core import conf_get_root_dir, conf_get_static_dir, conf_get_live_dir
from pathlib import Path
import os
# from services import


class Launcher:
    def __init__(self):
        self.root_dir = conf_get_root_dir()
        self.live = Path(conf_get_live_dir())
        self.static = Path(conf_get_static_dir())
        self.Wsh = wallpaper_selection

        self.thumbnail_image_convert = thumbnail_image_convert
        self.thumbnail_video_convert = thumbnail_video_convert
        self.handler = wallpaper_selection(
            live_path=self.live,
            static_path=self.static,
            root_dir=self.root_dir,
        )
        self.handler.refresh_wallpaper_data()


launcher = Launcher
