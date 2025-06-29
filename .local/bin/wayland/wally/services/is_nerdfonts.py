from subprocess import check_output
from utils import log_exceptions


class NerdFontChecker:
    def __init__(self):
        self.fonts = []

    @log_exceptions
    def load_fonts(self) -> None:
        output = check_output(["fc-list", ":", "family"], text=True)
        self.fonts = [line.strip() for line in output.split("\n") if line.strip()]

    @log_exceptions
    def has_nerd_fonts(self) -> bool:
        if not self.fonts:
            self.load_fonts()
        for font in self.fonts:
            if "nerd" in font.lower():
                return True
        return False


is_nerdfonts = NerdFontChecker().has_nerd_fonts
