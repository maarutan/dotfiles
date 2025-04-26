#!/usr/bin/python

CRITICAL = 10
LOW = 20
BATTERY_PATH_DYNAMIC = True
BATTERY_PATH = "/sys/class/power_supply/BAT0"


import os
import time
from subprocess import run
from shutil import which
from pathlib import Path
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


def get_battery_path() -> str:
    if BATTERY_PATH_DYNAMIC:
        power_supply_path = "/sys/class/power_supply/"
        for entry in os.listdir(power_supply_path):
            if entry.startswith("BAT"):
                try:
                    return os.path.join(power_supply_path, entry)
                except:
                    return "Battery not found"
        return "Battery not found"
    else:
        return BATTERY_PATH


def read_file(path: Path) -> str:
    with open(path, "r") as f:
        return f.read().strip()


def bat_lvl() -> str:
    battery_path = Path(get_battery_path())
    capacity_file = battery_path / "capacity"
    return read_file(capacity_file)


def monitor_battery():
    global last_state
    while True:
        battery_path = Path(get_battery_path())
        if battery_path.is_dir():
            capacity = int(read_file(battery_path / "capacity"))
            status = read_file(battery_path / "status")

            if last_state != "FULL" and status == "Full":
                notify(
                    title="Battery full",
                    message="Your battery is fully charged.",
                    lvl="i",
                )
                last_state = "FULL"

            if (
                last_state not in ("LOW", "CRITICAL")
                and status == "Discharging"
                and capacity <= LOW
            ):
                notify(
                    title="Battery low",
                    message=f"Battery level is at {capacity}%. Please charge soon.",
                    lvl="w",
                )
                last_state = "LOW"

            if (
                last_state != "CRITICAL"
                and status == "Discharging"
                and capacity <= CRITICAL
            ):
                notify(
                    title="Battery critical",
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
