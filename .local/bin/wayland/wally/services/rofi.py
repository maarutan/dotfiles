from subprocess import run
from pathlib import Path
from typing import Optional


class Rofi:
    def __init__(
        self,
        items: Optional[list[str]] = None,
        theme: Optional[Path] = None,
    ) -> None:
        self.theme = theme
        self.items = items

    def drun(self) -> Optional[str]:
        cmd = ["rofi", "-show", "drun"]
        cmd += ["-theme", str(self.theme)] if self.theme else []
        result = run(cmd, text=True, capture_output=True).stdout.strip()
        if result:
            return result
        else:
            return None

    def dmenu(self) -> Optional[str]:
        cmd = ["rofi", "-dmenu"]
        cmd += ["-theme", str(self.theme)] if self.theme else []
        result = run(
            cmd,
            input="\n".join(self.items if self.items else ""),
            text=True,
            capture_output=True,
        )

        if result.returncode == 0:
            return result.stdout.strip() or None
        else:
            return None


rofi = Rofi
