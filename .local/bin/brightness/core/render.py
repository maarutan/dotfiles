from modules import (
    NotifySend,
    Brightness,
    SmoothTurn,
)
from core.config import Config
from core.icons import IconPath


class Render:
    def __init__(self):
        self.bness = Brightness()
        self.ntsend = NotifySend
        self.conf = Config()
        self.st = SmoothTurn
        self.ip = IconPath()

        ntsend_icon = self.conf.get_option("notify_icon")
        self.icons_vol = self.ip.get_brightness_icon() if ntsend_icon else None

    async def add_brightness(self, status: str):
        status = "-" if status == "-" else ""
        delta = (
            -int(self.conf.get_option("turn_sub"))
            if status == "-"
            else int(self.conf.get_option("turn_add"))
        )

        if self.conf.get_option("turn_smooth"):
            st_instance = self.st(
                delay=float(self.conf.get_option("turn_delay")),
                stop_step=abs(delta),
                function_st=lambda: (
                    self.ntsend(
                        icon=self.icons_vol,
                        message=self.conf.get_option("redner_brightness").format(
                            brightness=self.bness.just_add(+1 if delta > 0 else -1)
                        ),
                        timeout=int(self.conf.get_option("notify_timeout")),
                        id=int(self.conf.get_option("notify_id")),
                        progress=bool(self.conf.get_option("notify_progress_bar")),
                        progress_value=self.bness.get_brightness(),
                    ).send(),
                ),
            )
            await st_instance.run()
        else:
            set_new_brightness = self.bness.just_add(delta)

            self.ntsend(
                icon=self.icons_vol,
                message=self.conf.get_option("redner_brightness").format(
                    brightness=set_new_brightness
                ),
                timeout=int(self.conf.get_option("notify_timeout")),
                id=int(self.conf.get_option("notify_id")),
                progress=bool(self.conf.get_option("notify_progress_bar")),
                progress_value=set_new_brightness,
            ).send()
