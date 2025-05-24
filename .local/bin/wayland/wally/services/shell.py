from subprocess import run, Popen
from typing import Union


def shell(cmd: Union[str, list[str]], asynco: bool = False) -> str | None:
    use_shell = isinstance(cmd, str)

    if asynco:
        Popen(cmd, shell=use_shell, text=True)
        return None
    else:
        result = run(cmd, shell=use_shell, text=True, capture_output=True)
        return result.stdout.strip()
