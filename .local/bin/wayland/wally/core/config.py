import os
from pathlib import Path
from services import (
    FileManager,
    JsonManager,
)
from .paths.path_list import (
    HOME,
    LOCAL_WALLY_JSONC_CONFIG,
    JSONC_CONFIGURE,
)
from utils import log_exceptions


class ConfigHandler:
    def __init__(self):
        self.config_path = JSONC_CONFIGURE
        self.Fm = FileManager(self.config_path)
        self.FmLw = FileManager(LOCAL_WALLY_JSONC_CONFIG)
        self.Jm = JsonManager(self.config_path)
        self.JmLw = JsonManager(LOCAL_WALLY_JSONC_CONFIG)
        self.default_config = """{
  "root_dir": "~/.wally",
  "static_dir": "static",
  "live_dir": "live",
  "live_extensions": [ 
    "mp4",
    "gif"
  ],
  "static_extensions": [ 
    "jpg",
    "jpeg",
    "png",
    "webp"
  ]
}"""
        self.generate_config()
        self.local_config_data = None
        self.global_config_data = None

    @log_exceptions
    def generate_config(self) -> None:
        self.FmLw.if_not_exists_create()
        if self.FmLw.is_exists() and not self.FmLw.read():
            self.FmLw.write(self.default_config)

        if not self.Fm.read():
            self.Fm.write(self.default_config)

    @log_exceptions
    def get_config(self, local: bool = False) -> dict:
        if local:
            if self.local_config_data is None:
                self.local_config_data = self.JmLw.get_data() or {}
            return self.local_config_data
        else:
            if self.global_config_data is None:
                self.global_config_data = self.Jm.get_data() or {}
            return self.global_config_data

    @log_exceptions
    def get_config_option(self, item: str, local: bool = False) -> str:
        data = self.get_config(local=local)
        return data.get(item, "")

    @log_exceptions
    def get_expanded_path(self, key: str, local: bool = False) -> Path:
        raw_path = self.get_config_option(key, local=local)
        return Path(os.path.expanduser(raw_path))

    @log_exceptions
    def get_valid_config(self, item: str, expanded: bool = False) -> Path:
        config = self.get_config(local=False)
        use_local = not config or item not in config
        if expanded:
            return Path(self.get_expanded_path(item, local=use_local))
        else:
            return Path(self.get_relative_path(item, local=use_local))

    @log_exceptions
    def get_relative_path(self, key: str, local: bool = False) -> Path:
        raw_path = self.get_config_option(key, local=local)
        abs_path = self.get_valid_config("root_dir", expanded=True)
        return Path.joinpath(abs_path, raw_path)

    @log_exceptions
    def get_live_extensions(self):
        return self.get_config_option("live_extensions")

    @log_exceptions
    def get_static_extensions(self):
        return self.get_config_option("static_extensions")


config_handler = ConfigHandler()

conf_get_data = config_handler.get_config

conf_get_root_dir = lambda: config_handler.get_valid_config("root_dir", expanded=True)
conf_get_static_dir = lambda: config_handler.get_valid_config(
    "static_dir", expanded=False
)
conf_get_live_dir = lambda: config_handler.get_valid_config("live_dir", expanded=False)

DATABASE_WALLY = conf_get_root_dir() / "database.json"
