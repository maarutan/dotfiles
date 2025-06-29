from dataclasses import dataclass
from time import localtime
from core.paths.path_list import LOGFILE
from services import FileManager


@dataclass
class Message:
    status: str
    content: str


class MessageHandler(Message):
    def __init__(self):
        self.message_statuses = {
            "i": "info",
            "w": "warning",
            "e": "error",
            "d": "debug",
        }
        self.fm = FileManager(LOGFILE)

    def current_time(self) -> str:
        """Returns the current time"""

        now = localtime()
        return f"{now.tm_mday:02d}.{now.tm_mon:02d}.{now.tm_year} | {now.tm_hour:01d}:{now.tm_min:02d}:{now.tm_sec:02d}"

    def render_message(
        self,
        status: str = "i",
        content: str = "",
    ) -> None:
        message = Message(status, content)
        for k, v in self.message_statuses.items():
            if k == message.status.lower() or v == message.status.lower():
                message.status = v.title()
                break
        else:
            message.status = "Undefined"

        if ":" in message.content:
            msg, path = message.content.split(":", 1)
            msg = msg.strip() + ":"
            path = path.strip()
        else:
            msg = message.content
            path = ""

        logo_width = 6
        msg_width = 28

        logo_str = f"{message.status:<{logo_width}}"
        msg_str = f"{message.content:<{msg_width}}"

        content = f"{logo_str} | {msg_str} | {self.current_time()}\n"

        self.fm.append(content)
        print("check logfile")


mh = MessageHandler()
logger = mh.render_message
