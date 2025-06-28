import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.paths.path_list import JSONC_CONFIGURE
from services import JsonManager
from core import conf_get_data

Jm = JsonManager

if __name__ == "__main__":
    print(conf_get_data())
