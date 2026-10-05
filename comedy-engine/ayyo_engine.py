#!/usr/bin/env python3

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SUPPORTED_LANGUAGES = {
    "english": ROOT / "languages" / "english" / "messages.json",
    "telugu": ROOT / "languages" / "telugu" / "messages.json",
}

def load_messages(language):
    path = SUPPORTED_LANGUAGES.get(language)

    if path is None:
        raise ValueError(f"Unsupported language: {language}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def get_message(event, language="telugu"):
    messages = load_messages(language)
    choices = messages.get(event)

    if not choices:
        return f"Ayyo! Event '{event}' inka ready avvaledu 😂"

    return random.choice(choices)

def main():
    if len(sys.argv) < 2:
        print("AyyoOS 😂")
        print("Usage: ayyo <event> [language]")
        return

    event = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) >= 3 else "telugu"

    try:
        message = get_message(event, language)
        print("\n😂 AyyoOS")
        print("----------------------------")
        print(message)
        print()

    except Exception as error:
        print(f"AyyoOS error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
