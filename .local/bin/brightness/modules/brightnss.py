from subprocess import run, PIPE
from core.config import Config


class Brightness:
    def get_brightness(self) -> int:
        current_brightness = int(
            run(["brightnessctl", "get"], stdout=PIPE, text=True).stdout.strip()
        )
        max_brightness = int(
            run(["brightnessctl", "max"], stdout=PIPE, text=True).stdout.strip()
        )
        return round(100 * (current_brightness / max_brightness))

    def just_add(self, delta: int):
        current_percent = self.get_brightness()
        new_percent = max(0, min(100, current_percent + delta))
        run(["brightnessctl", "set", f"{new_percent}%"])
        return new_percent
