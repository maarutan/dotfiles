from services import shell
from dataclasses import dataclass


@dataclass
class Notify:
    message: str | None
    timeout: int | None
    id: int | None
    icon: str | None = None
    status: str = ""


class NotifySend:
    def __init__(self):
        self.status_messages = {
            "i": "ℹ️",
            "w": "⚠️",
            "e": "🚩",
            "": "",
        }

    def send(
        self,
        message: str | None,
        icon: str | None = None,
        timeout: int | None = None,
        id: int | None = None,
        status: str = "",
    ):
        status_symbol = self.status_messages.get(f"{status}".lower(), "Undefined")
        notify = Notify(
            message=message, status=status_symbol, timeout=timeout, id=id, icon=icon
        )

        args = ["notify-send"]
        args.extend(["-i", notify.icon]) if notify.icon else None
        args.extend(["-t", str(notify.timeout)]) if notify.timeout else None
        args.extend(["-r", str(notify.id)]) if notify.id else None
        args.extend([f"'{notify.status}"])
        args.append(f"{notify.message}'")
        join_args = " ".join(args)
        shell(join_args)


notify_send = NotifySend().send
