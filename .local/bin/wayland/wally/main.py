# from pathlib import Path
from pathlib import Path
from time import sleep
from core import launcher
from core import menu_wally
from core.paths.path_list import HOME
from services import notify_send
from services import thumbnail_image_convert, thumbnail_video_convert
from core import (
    conf_get_root_dir,
    conf_get_live_dir,
    conf_get_static_dir,
    # always bottom
    path_handler,
)

# from services.shell import shell  # path handler will create path if not exists
from services import wallpaper_selection
from services import WSDataBaseHandler

if __name__ == "__main__":
    print(menu_wally())
    print(
        WSDataBaseHandler(
            Path("/home/maaru/Pictures/wallpapers/database.json")
        ).get_current_wallpaper("static")
    )
    launcher()
