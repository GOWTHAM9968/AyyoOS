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

VALID_LANGUAGES = {
    "english",
    "telugu"
}


def read_config():
    config = {
        "mode": "funny",
        "language": "telugu"
    }

    if CONFIG.exists():
        for line in CONFIG.read_text(encoding="utf-8").splitlines():
            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_language_messages(language):
    if language not in VALID_LANGUAGES:
        language = "english"

    path = ROOT / "languages" / language / "messages.json"

    return load_json(path)


def load_personality_messages(mode):
    if mode not in VALID_MODES:
        mode = "funny"

    path = (
        ROOT
        / "comedy-engine"
        / "personalities"
        / mode
        / "messages.json"
    )

    if not path.exists():
        return {}

    return load_json(path)


def get_message(event):
    config = read_config()

    mode = config.get("mode", "funny")
    language = config.get("language", "telugu")

    language_messages = load_language_messages(language)

    # Normal mode stays clean and straightforward.
    if mode == "normal":
        personality_messages = load_personality_messages("normal")

        choices = personality_messages.get(event)

        if choices:
            return random.choice(choices)

    # Telugu/English language packs control the base wording.
    choices = language_messages.get(event)

    if not choices:
        return f"Ayyo! Event '{event}' inka ready avvaledu 😂"

    message = random.choice(choices)

    if mode == "chill":
        return f"{message} 😎"

    if mode == "savage":
        return f"{message} 🔥"

    return message


def main():

    if len(sys.argv) < 2:

        config = read_config()

        print("😂 AyyoOS")
        print(
            f"Personality: "
            f"{config.get('mode', 'funny').upper()}"
        )
        print(
            f"Language: "
            f"{config.get('language', 'telugu').upper()}"
        )
        print("Usage: ayyo <event>")

        return

    event = sys.argv[1]

    try:
        print(get_message(event))

    except Exception as error:
        print(f"AyyoOS error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
