#!/usr/bin/env python

OPTIMAL = 80
MEDIUM = 50
LOW = 20
CRITICAL = 10

DELAY_LOOP = 60  # sleep secend ( while loop )

BATTERY_PATH = "BAT1"  # battery can various from `BAT0` to `BAT1,2,3,4....`
DYNAMIC_FIND_BATTERY = True

DEBUG = True
DE_BAT_LVL = 100


def scripts():  # start your scripts looking at the level of the battery
    scr_handler(
        100,  # level
        # "notify-send hello",  # my first scripts
        "",  # second scripts
    )
    scr_handler(OPTIMAL, "")
    scr_handler(MEDIUM, "")
    scr_handler(LOW, "")
    scr_handler(CRITICAL, "")


import os
from pathlib import Path
from subprocess import Popen
from time import sleep


def async_shell(cmd) -> None:
    Popen(cmd, shell=True)


def does_path_exists(path: Path) -> bool:
    if Path(path).exists():
        return True
    else:
        return False


def scr_handler(threshold: int, *command) -> None:
    current_level = get_battery_lvl()
    if not DEBUG:
        if threshold <= current_level:
            for i in command:
                async_shell(i)
    else:
        if threshold <= DE_BAT_LVL:
            for i in command:
                async_shell(i)


def read_file(path: Path) -> str:
    with open(path, "r") as f:
        return f.read()


def get_path_battery() -> Path:
    power_supply_path = Path("/sys/class/power_supply/")
    if DYNAMIC_FIND_BATTERY:
        for entry in power_supply_path.iterdir():
            if entry.name.startswith("BAT") and entry.is_dir():
                return entry
        return Path("")

    else:
        return Path(power_supply_path / BATTERY_PATH)


def get_battery_lvl() -> int:
    path_bat = get_path_battery()
    if does_path_exists(path_bat):
        return int(read_file(path_bat / "capacity"))
    else:
        return 0


def monitor_battery():
    optimal_counter = 0
    medium_counter = 0
    low_counter = 0
    critical_counter = 0

    while True:
        sleep(DELAY_LOOP)


def main():
    scripts()


if __name__ == "__main__":
    main()
