from core.config import Config


class Sound:
    def __init__(self) -> None:
        self.conf = Config()
        self.path = self.conf.get_option("sound_path")
