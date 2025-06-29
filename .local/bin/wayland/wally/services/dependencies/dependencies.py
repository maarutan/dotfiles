import os
from shutil import which
from services import X11, Wayland, shell


class CheckDependencies:
    def __init__(self):
        self.wayland = [e.value for e in Wayland]
        self.x11 = [e.value for e in X11]

    def check_your_session_type(self) -> str:
        env = os.environ["XDG_SESSION_TYPE"]
        w = "wayland"
        x = "x11"
        if env == w:
            result = w
        elif env == x:
            result = x
        else:
            result = ""

        return result

    def check_dependencies(self) -> list:
        dependencies = []
        cyst = self.check_your_session_type()
        if cyst == "wayland":
            dependencies = self.wayland
        elif cyst == "x11":
            dependencies = self.x11

        missing_dependencies = []
        for i in dependencies:
            if not which(i):
                missing_dependencies.append(i)

        return missing_dependencies

    def get_your_screen_resolution(self) -> str:
        cyst = self.check_your_session_type()
        if cyst == "wayland":
            s = shell("wlr-randr | grep 'current' | awk '{print $1}'")
            return f"{s}"
        elif cyst == "x11":
            s = shell("xrandr | grep -E '\\*' | awk '{print $1}' | head -n 1")
            return f"{s}"
        else:
            return ""
