#!/usr/bin/env python3

import json
from datetime import datetime
from pathlib import Path

ROOT = Path.home() / "AyyoOS"

HISTORY_FILE = (
    ROOT
    / "system"
    / "notifications"
    / "history.json"
)

MAX_NOTIFICATIONS = 100


def ensure_history():

    HISTORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not HISTORY_FILE.exists():

        HISTORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )


def load_history():

    ensure_history()

    try:

        data = json.loads(
            HISTORY_FILE.read_text(
                encoding="utf-8"
            )
        )

        if isinstance(data, list):
            return data

    except (
        json.JSONDecodeError,
        OSError
    ):
        pass

    return []


def save_history(history):

    ensure_history()

    HISTORY_FILE.write_text(
        json.dumps(
            history,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


def add_notification(
    title,
    message,
    category="system"
):

    history = load_history()

    notification = {
        "title": title,
        "message": message,
        "category": category,
        "time": datetime.now().isoformat(
            timespec="seconds"
        )
    }

    history.insert(
        0,
        notification
    )

    history = history[
        :MAX_NOTIFICATIONS
    ]

    save_history(history)

    return notification


def clear_history():

    save_history([])


def get_history():

    return load_history()


if __name__ == "__main__":

    add_notification(
        "AyyoOS",
        "Notification history working boss 😂",
        "test"
    )

    print(
        json.dumps(
            get_history(),
            indent=4,
            ensure_ascii=False
        )
    )
