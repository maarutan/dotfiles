import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from services.shell import shell


if __name__ == "__main__":
    shell("echo 'hello world'", asynco=True)
    shell(["notify-send", "hello world"])
