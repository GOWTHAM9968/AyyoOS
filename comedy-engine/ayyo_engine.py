#!/usr/bin/env python3

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONFIG = ROOT / "config" / "personality.conf"

VALID_MODES = {
    "normal",
    "chill",
    "funny",
    "savage"
}


def read_config():
    config = {
        "mode": "funny",
        "language": "telugu"
    }

    if not CONFIG.exists():
        return config

    for line in CONFIG.read_text(
        encoding="utf-8"
    ).splitlines():

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        config[key.strip()] = value.strip()

    return config


def load_messages(mode):
    if mode not in VALID_MODES:
        mode = "funny"

    path = (
        ROOT
        / "comedy-engine"
        / "personalities"
        / mode
        / "messages.json"
    )

    with path.open(
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def get_message(event):
    config = read_config()

    mode = config.get(
        "mode",
        "funny"
    )

    messages = load_messages(mode)

    choices = messages.get(event)

    if not choices:
        return (
            f"Ayyo! Event '{event}' "
            f"inka ready avvaledu 😂"
        )

    return random.choice(choices)


def main():

    if len(sys.argv) < 2:
        config = read_config()

        print("😂 AyyoOS")
        print(
            f"Personality: "
            f"{config['mode'].upper()}"
        )
        print("Usage: ayyo <event>")
        return

    event = sys.argv[1]

    try:
        print(get_message(event))

    except Exception as error:
        print(
            f"AyyoOS error: {error}"
        )

        sys.exit(1)


if __name__ == "__main__":
    main()
