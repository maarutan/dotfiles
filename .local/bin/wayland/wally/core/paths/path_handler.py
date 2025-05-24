from pathlib import Path
from services import FileManager
from core import (
    conf_get_root_dir,
    conf_get_static_dir,
    conf_get_live_dir,
    DATABASE_WALLY,
)
from .path_list import (
    LOGFILE,
    LOCAL_WALLY,
    LOCAL,
    JSONC_CONFIGURE,
    TMP,
    WALLY_THUMBNAIL,
    LOCAL_WALLY_JSONC_CONFIG,
    CACHE,
    CACHE_WALLY_DIR,
)


check_exist = [
    conf_get_root_dir(),
    conf_get_static_dir(),
    conf_get_live_dir(),
    DATABASE_WALLY,
    LOGFILE,
    JSONC_CONFIGURE,
    TMP,
    WALLY_THUMBNAIL,
    CACHE,
    LOCAL_WALLY_JSONC_CONFIG,
    LOCAL_WALLY,
    LOCAL,
    CACHE_WALLY_DIR,
]


Fm = FileManager
for i in check_exist:
    Fm(i).if_not_exists_create()
