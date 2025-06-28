import subprocess
import json
import time

FOCUS_CLASSES = [
    "Rofi",
    "rofi",
]


def get_windows():
    # Получаем список окон через hyprctl
    proc = subprocess.run(["hyprctl", "-j", "clients"], capture_output=True, text=True)
    if proc.returncode != 0:
        return []
    try:
        windows = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return []
    return windows


def focus_window(window_id):
    subprocess.run(["hyprctl", "dispatch", f"workspacefocuswindow {window_id}"])


def main():
    while True:
        windows = get_windows()
        target = None
        for w in windows:
            cls = w.get("class", "")
            print(f"Window class: {cls}, keys: {list(w.keys())}")  # отладка
            if cls in FOCUS_CLASSES and "id" in w:
                target = w
                break
        if target:
            print(f"Focusing window ID {target['id']} with class {target['class']}")
            focus_window(target["id"])
        time.sleep(1)


if __name__ == "__main__":
    main()
