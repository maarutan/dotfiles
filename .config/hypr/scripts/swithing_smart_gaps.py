import os
from pathlib import Path
import re
from subprocess import run, Popen
from argparse import ArgumentParser
from shutil import rmtree
import json
from time import sleep, localtime

DIR_SETTINGS = Path(__file__).parent.parent / "settings"
SMART_GAPS_DIR = DIR_SETTINGS / "smart_gaps"

CONFIG_FILE = SMART_GAPS_DIR / "smartgaps.conf"
# type
INSIDE_FILE = SMART_GAPS_DIR / "type" / "inside" / "enable.conf"
OUTSIDE_FILE = SMART_GAPS_DIR / "type" / "outside" / "enable.conf"
DEFAULT_FILE = SMART_GAPS_DIR / "default.conf"

SMART_GAPS_STORAGE = SMART_GAPS_DIR / "config.jsonc"
LOGGFILE = SMART_GAPS_DIR / "smartLogger.log"


def get_type(content: str) -> Path:
    f = FileManager
    path = Path(SMART_GAPS_DIR / "type")
    types = os.listdir(path)

    if content in types:
        return Path(path / content).joinpath()
    else:
        Logger(path=LOGGFILE, status="e", content=f"does not exist: {content}")
        return Path("")


def does_path_exists(item: Path) -> bool:
    if Path(item).exists():
        return True
    else:
        return False


def check_paths(content) -> str | None:
    dir = []
    file = []
    if does_path_exists(content):
        if Path(content).is_file():
            file.append(content)
        elif Path(content).is_dir():
            dir.append(content)

    for d in dir:
        d_path = Path(d).resolve()
        if not does_path_exists(d_path):
            d_path.mkdir(parents=True, exist_ok=True)
            print(f"created:  {d_path} ")
        else:
            Logger(path=LOGGFILE, status="i", content=f"exists:  {d_path} ")
            return f"exists:  {d_path} "

    for f in file:
        f_path = Path(f).resolve()
        if not does_path_exists(f_path):
            f_path.touch(exist_ok=True)
        else:
            Logger(path=LOGGFILE, status="i", content=f"exists:  {f_path} ")
            return f"exists:  {f_path} "


class FileManager:
    def __init__(
        self,
        path: Path = Path(""),
        content: str = "",
    ) -> None:
        """Constructor for FileManager class."""
        self.path = path
        self.content = content

    def write(self) -> None:
        "Writes a file specified by path"
        try:
            with open(self.path, "w") as f:
                f.write(self.content)
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"write_file failed: {e}")

    def append(self) -> None:
        "Appends a file specified by path"
        try:
            with open(self.path, "a") as f:
                f.write(self.content)
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"append_file failed: {e}")

    def read(self) -> str:
        try:
            with open(self.path, "r") as f:
                return f.read()
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"read_file failed: {e}")
            return ""

    def delete_file(self) -> None:
        "Deletes a file specified by path"
        try:
            if self.path.is_file():
                self.path.unlink()
            else:
                Logger(
                    path=LOGGFILE,
                    status="i",
                    content=f"Path is not a file: {self.path}",
                )
            #     self.delete_dir()

        except Exception as e:
            Logger(
                path=LOGGFILE,
                status="i",
                content=f"delete_file failed for {self.path}: {e}",
            )

    def delete_dir(self) -> None:
        "Deletes a directory specified by path"
        try:
            if self.path.is_dir():
                rmtree(self.path)
            else:
                Logger(
                    path=LOGGFILE,
                    status="e",
                    content=f"Path is not a directory: {self.path}",
                )

        except Exception as e:
            Logger(
                path=LOGGFILE,
                status="e",
                content=f"delete_dir failed for {self.path}: {e}",
            )

    def __str__(self) -> str:
        "Returns a string representation of the class"
        return (
            f"FileManager(path={self.path}, content={self.content})\n"
            "Please use: write, append, read, delete_file, delete_dir\n"
            "For example: f = FileManager(path, content)\n"
            "f.write(), f.append(), f.read(), f.delete_file(), f.delete_dir()"
        )


class Logger:
    def __init__(
        self,
        path: Path = Path(""),
        status: str = "info",
        content: str = "",
    ) -> None:
        """Constructor for Logger class"""

        self.path = path
        self.status = status.lower()
        self.content = content
        self.state = {
            "info": "i",
            "warn": "w",
            "error": "e",
            "debug": "d",
        }

        self.F = FileManager(path=self.path)
        try:
            self.handle_log()
        except Exception as e:
            print(f"class Logger failed: {e}")

    def current_time(self) -> str:
        """Returns the current time"""

        now = localtime()
        return f"{now.tm_mday:02d}.{now.tm_mon:02d}.{now.tm_year} {now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}"

    def write(self, content: str = "") -> None:
        """Palimorphism from the inheriting class FileManager method write"""
        try:
            self.F.content = content if content else self.content
            self.F.append()
        except Exception as e:
            print(f"class Logger failed: {e}")

    def handle_log(self):
        """Handles the log based on the status"""
        cmd = self.status

        def render_handle_log() -> None:
            logo = ""
            for k, v in self.state.items():
                if cmd == v or cmd == k:
                    logo = k.upper()

            crt = self.current_time()

            if ":" in self.content:
                msg, path = self.content.split(":", 1)
                msg = msg.strip() + ":"
                path = path.strip()
            else:
                msg = self.content
                path = ""

            logo_width = 6
            msg_width = 28
            path_width = 55

            logo_str = f"{logo:<{logo_width}}"
            msg_str = f"{msg:<{msg_width}}"
            path_str = f"{path:<{path_width}}"

            content = f"{logo_str}| {msg_str}| {path_str}| {crt}\n"
            self.write(content)

        if cmd != "":
            render_handle_log()
        else:
            print("class Logger failed: status is empty")

    def __str__(self) -> str:
        """Returns a string representation of the class"""
        return (
            f"class Logger:\nLogger write content in the file specified path\n"
            f"Please use: \n"
            f"  l = Logger\n"
            f"  l(path, status, content)\n"
            f"---------------------------\n"
            f"content write to that:\n"
            f"  INFO: | content | {self.current_time()}\n"
        )


class JsonManager:
    def __init__(self, path: Path = Path("")) -> None:
        """Constructor for baseJson class."""
        f = FileManager
        self.path = path
        try:
            if not does_path_exists(self.path):
                f(self.path, "{}").write()
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"init_json failed: {e}")

    def read_json_without_comments(self) -> dict:
        """Reads a jsonc specified by path."""
        try:
            with open(self.path, "r") as f:
                jsonc_content = f.read()
                jsonc_content = re.sub(r"//.*", "", jsonc_content)
                jsonc_content = re.sub(r",\s*(]|})", r"\1", jsonc_content)
                data = json.loads(jsonc_content)
                return data
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"read_json failed: {e}")
            return {}

    def read(self) -> dict:
        """Reads a json specified by path."""
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"read_json failed: {e}")
            return {}

    def write(self, data) -> None:
        """Writes a json specified by path."""
        try:
            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"write_json failed: {e}")

    def get_data(self) -> dict:
        """Reads a json specified by path."""
        if does_path_exists(self.path):
            try:
                data = self.read()
            except Exception as e:
                Logger(path=LOGGFILE, status="e", content=f"read_json failed: {e}")
                data = {}
        else:
            data = {}
        return data

    def append(self, item) -> None:
        """Appends an item to a json specified by path."""
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise TypeError("JSON root is not a list — can't append item.")
            data.append(item)
            self.write(data)
        except Exception as e:
            Logger(path=LOGGFILE, status="e", content=f"append failed: {e}")


class TypeHandler:
    def __init__(self) -> None:
        self.f = FileManager
        self.j = JsonManager
        self.config = CONFIG_FILE

    def get_type_config(self):
        return self.j().get_data()

    def enable(self) -> None:
        i = self.f().read()
        self.f(self.config, i).write()
        self.f(SMART_GAPS_STORAGE, "enable").write()
        # run(["hyprctl", "reload"])

    def disable(self) -> None:
        i = self.f().read()
        self.f(self.config, i).write()
        self.f(SMART_GAPS_STORAGE, "disable").write()

        # run(["hyprctl", "reload"])

    def toggle(self) -> None:
        i = SMART_GAPS_STORAGE
        if does_path_exists(i) and read_file(i) == "enable":
            self.f(SMART_GAPS_STORAGE, "disable").write()
            self.disable()
        else:
            self.f(SMART_GAPS_STORAGE, "enable").write()
            self.enable()


if __name__ == "__main__":
    print(get_type("inside"))
    # toggle()
