#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "personality.conf"

VALID_MODES = [
    "normal",
    "chill",
    "funny",
    "savage"
]


def get_mode():
    if not CONFIG.exists():
        return "funny"

    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        if line.startswith("mode="):
            mode = line.split("=", 1)[1].strip()

            if mode in VALID_MODES:
                return mode

    return "funny"


def set_mode(new_mode):
    new_mode = new_mode.lower()

    if new_mode not in VALID_MODES:
        raise ValueError(
            f"Invalid mode: {new_mode}"
        )

    language = "telugu"

    if CONFIG.exists():
        for line in CONFIG.read_text(
            encoding="utf-8"
        ).splitlines():

            if line.startswith("language="):
                language = line.split(
                    "=", 1
                )[1].strip()

    CONFIG.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    CONFIG.write_text(
        f"mode={new_mode}\n"
        f"language={language}\n",
        encoding="utf-8"
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(get_mode())

    else:
        set_mode(sys.argv[1])
        print(
            f"😂 AyyoOS mode changed to "
            f"{sys.argv[1].upper()}"
        )
