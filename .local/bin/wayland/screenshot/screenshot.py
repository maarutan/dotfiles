#!/usr/bin/env python

from pathlib import Path
from subprocess import PIPE, check_output, Popen, run
from shutil import which
from datetime import datetime
import os

# Define paths
home = Path.home()
XDG_PICTURES_DIR = os.environ.get("XDG_PICTURES_DIR", str(home / "Pictures"))
saved_screenshots = Path(XDG_PICTURES_DIR)
screenshots_dir = saved_screenshots / "Screenshots"
screenshots_dir.mkdir(exist_ok=True, parents=True)

# Path to the shutter sound
shot_sound = Path(__file__).parent / "misc" / "shot.mp3"


def check_dependencies() -> tuple[list[str], list[str]]:
    """
    Check for required external dependencies.
    Returns a tuple of (installed, missing) commands.
    """
    dependencies = ["grim", "slurp", "mpv", "swappy"]
    found = []
    missing = []

    for dep in dependencies:
        (found if which(dep) else missing).append(dep)

    return (found, missing)


def screenshot_and_edit():
    coords = check_output(["slurp"]).decode().strip()
    if not coords:
        print("❎ Area selection cancelled.")
        return

    # Play shutter sound
    if shot_sound.exists():
        Popen(["mpv", "--no-terminal", "--quiet", str(shot_sound)])

    # Save screenshot to file
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = screenshots_dir / f"snapshot_{now}.png"
    with open(filename, "wb") as f:
        Popen(["grim", "-g", coords, "-"], stdout=f).wait()

    # Open in swappy for annotation

    Popen(["swappy", "-f", str(filename)]).wait()
    run(
        [
            "notify-send",
            "📸 Screenshot Saved",
            f"{filename}",
            "-i",
            filename,
        ]
    )


if __name__ == "__main__":
    found, missing = check_dependencies()
    if missing:
        print("❌ Missing dependencies:", ", ".join(missing))
        exit(1)

    screenshot_and_edit()
