#!/usr/bin/env python3

import os

MIN_UID = 1000
MAX_UID = 65534

HIDE_SHELLS = {
    "/sbin/nologin",
    "/usr/sbin/nologin",
    "/bin/false",
    "/usr/bin/false",
    "/run/current-system/sw/bin/nologin",
}


def should_display(uid: int, shell: str) -> bool:
    return MIN_UID <= uid <= MAX_UID and shell not in HIDE_SHELLS


def extract_shell_name(shell_path: str) -> str:
    return os.path.basename(shell_path)


def main():
    shell_count_letter = 0
    username_count_letter = 0
    uid_count_letter = 0
    max_line = 0
    output_lines = []

    with open("/etc/passwd", "r", encoding="utf-8") as passwd_file:
        for line in passwd_file:
            parts = line.strip().split(":")
            if len(parts) < 7:
                continue
            username, _, uid_str, *_, shell = parts
            try:
                uid = int(uid_str)
            except ValueError:
                continue

            if should_display(uid, shell):
                shell = extract_shell_name(shell)

                shell_count_letter += len(shell)
                username_count_letter += len(username)
                uid_count_letter += len(str(uid))

                result = f" {username}    UID={uid},   shell={shell}"
                max_line = max(max_line, len(result))
                output_lines.append(result)

    print("-" * max_line)
    for line in output_lines:
        print(line)
    print("-" * max_line)


if __name__ == "__main__":
    main()
