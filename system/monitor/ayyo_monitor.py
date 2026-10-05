#!/usr/bin/env python3

import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
NOTIFIER = ROOT / "core" / "bin" / "ayyo-notify"


def network_state():
    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "STATE", "general"],
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout.strip().lower()

    except Exception:
        return "unknown"


def notify(event):
    subprocess.run(
        [str(NOTIFIER), event],
        check=False
    )


def main():

    print("😂 AyyoMonitor v0.1")
    print("----------------------------")
    print("Watching network status...")
    print("Press Ctrl+C to stop.\n")

    previous_state = network_state()

    print(f"Current network: {previous_state}")

    while True:

        time.sleep(5)

        current_state = network_state()

        if current_state != previous_state:

            print(
                f"Network changed: "
                f"{previous_state} -> {current_state}"
            )

            if current_state == "connected":
                notify("wifi_on")

            else:
                notify("wifi_off")

            previous_state = current_state


if __name__ == "__main__":
    main()
