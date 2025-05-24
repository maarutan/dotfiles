#!/usr/bin/python

DELAY_NOTIFY = "5000"  # is ms

OPTIMAL = 80
LOW = 20
CRITICAL = 10

BATTERY_PATH_DYNAMIC = False
# BATTERY_PATH = "/sys/class/power_supply/BAT0"


import os
import time
from subprocess import run
from shutil import which
from pathlib import Path

BATTERY_PATH = Path.home() / "battery"

from typing import Literal


last_state: Literal["NONE", "FULL", "LOW", "CRITICAL"] = "NONE"


def notify(
    iconPath: str | None = None,
    time: str | None = "1000",
    id: str | None = "1111",
    title: str | None = "title",
    message: str | None = "content",
    lvl: str | None = "info".lower(),
) -> None:
    level = {
        "w": "⚠️",
        "i": "ℹ️",
    }
    for k, v in level.items():
        if k == lvl:
            lvl = v

    args = ["notify-send"]
    args.extend(["-i", iconPath]) if iconPath else ""
    args.extend(["-t", time]) if time else ""
    args.extend(["-r", id]) if id else ""
    args.append(f"{lvl} {title}") if title else ""
    args.append(message) if message else ""

    if which("notify-send"):
        run(args)
    else:
        print(f"message: {title}\n     {message}")
        print("\n  WARN !!! not found: libnotify\n")


def get_battery_path() -> Path | None:
    power_supply_path = Path("/sys/class/power_supply/")
    if BATTERY_PATH_DYNAMIC:
        for entry in power_supply_path.iterdir():
            if entry.name.startswith("BAT") and entry.is_dir():
                return entry
        return None
    else:
        path = Path(BATTERY_PATH)
        return path if path.is_dir() else None


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""


def bat_lvl() -> str:
    battery_path = get_battery_path()
    if not battery_path:
        return "0"
    capacity_file = battery_path / "capacity"
    return read_file(capacity_file)


def monitor_battery():
    global last_state
    while True:
        battery_path = Path(get_battery_path())
        if battery_path.is_dir():
            capacity = int(read_file(battery_path / "capacity"))
            status = read_file(battery_path / "status")

            if status == "Charging":
                if last_state != "FULL" and capacity >= OPTIMAL and capacity < 100:
                    notify(
                        title="Battery optimal",
                        time=DELAY_NOTIFY,
                        message="Your battery is charged optimally.",
                        lvl="i",
                    )
                    last_state = "CHARGING"

                elif last_state != "FULL" and capacity == 100:
                    notify(
                        title="Battery full",
                        time=DELAY_NOTIFY,
                        message="Your battery is fully charged.",
                        lvl="i",
                    )
                    last_state = "FULL"

            elif status == "Discharging":
                if last_state != "LOW" and capacity <= LOW:
                    notify(
                        title="Battery low",
                        time=DELAY_NOTIFY,
                        message=f"Battery level is at {capacity}%. Please charge soon.",
                        lvl="w",
                    )
                    last_state = "LOW"

                elif last_state != "CRITICAL" and capacity <= CRITICAL:
                    notify(
                        title="Battery critical",
                        time=DELAY_NOTIFY,
                        message=f"Battery level is at {capacity}%. Charge immediately!",
                        lvl="w",
                    )
                    last_state = "CRITICAL"

            time.sleep(60)


if __name__ == "__main__":
    try:
        monitor_battery()
    except KeyboardInterrupt:
        pass
