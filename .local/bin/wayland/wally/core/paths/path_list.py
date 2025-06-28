import tomllib
import tempfile
from pathlib import Path

HOME = Path().home()
CURRENT_DIR = Path(__file__).parent.parent.parent
PYPROJECT_PATH = Path(__file__).parent.parent.parent / "pyproject.toml"
JSONC_CONFIGURE = HOME / ".config" / "wally" / "config.jsonc"
TMP = Path(tempfile.gettempdir())
WALLY_THUMBNAIL = TMP / "wally_thumbnail"
LOCAL = HOME / ".local"
LOCAL_WALLY = LOCAL / "share" / "wally"
LOCAL_WALLY_JSONC_CONFIG = LOCAL_WALLY / "config.jsonc"


CACHE = HOME / ".cache"
CACHE_WALLY_DIR = CACHE / "wally"


with PYPROJECT_PATH.open("rb") as f:
    pyproject = tomllib.load(f)

if CURRENT_DIR.name == pyproject["project"]["name"]:
    LOGFILE = CURRENT_DIR / f".{CURRENT_DIR.name}.log"
else:
    LOGFILE = HOME / "Pictures" / "wallpapers" / f".{pyproject['project']['name']}.log"
