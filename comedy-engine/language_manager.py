#!/usr/bin/env python3

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "personality.conf"

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


def set_language(language):
    language = language.lower()

    if language not in VALID_LANGUAGES:
        raise ValueError(
            f"Unsupported language: {language}"
        )

    config = read_config()

    CONFIG.write_text(
        f"mode={config.get('mode', 'funny')}\n"
        f"language={language}\n",
        encoding="utf-8"
    )


def main():
    if len(sys.argv) == 1:
        print(read_config().get("language", "telugu"))
        return

    language = sys.argv[1].lower()

    try:
        set_language(language)
        print(f"AyyoOS language: {language.upper()}")

    except ValueError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
