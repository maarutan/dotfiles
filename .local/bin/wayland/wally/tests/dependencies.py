import sys, os
from pathlib import Path
from shutil import which

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.dependencies import CheckDependencies

if __name__ == "__main__":
    Cd = CheckDependencies()
    print(Cd.check_dependencies())
