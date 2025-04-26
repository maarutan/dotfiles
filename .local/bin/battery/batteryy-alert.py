#!/usr/bin/python

BATTERY_PATH_DYNAMIC = True
BATTERY_PATH = "/sys/class/power_supply/BAT0"


import os
from subprocess import run
from shutil import which
from pathlib import Path


def notify(
    iconPath: str | None = None,
    time: str = "1000",
    id: str = "1111",
    title: str = "title",
    message: str = "content",
) -> None:
    icon = f"-i {iconPath}" if iconPath else ""
    time = f"-t {time}" if time else ""
    id = f"-r {id}" if id else ""
    if which("notify-send"):
        run(["notify-send", icon, time, id, title, message])
    else:
        print(f"message: {title}\n     {message}")
        print("\n  WARN !!! not found: libnotify\n")


def read_file(path: Path) -> str:
    with open(path) as f:
        return f.read()


# def get_battery() -> None:
#     if BATTERY_PATH_DYNAMIC:
#     else:
notify()
