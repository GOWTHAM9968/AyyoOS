#!/usr/bin/env python3

import tkinter as tk
import fcntl
import sys
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path.home() / "AyyoOS"

# ============================================================
# Single-instance protection
# ============================================================

LOCK_FILE = Path("/tmp/ayyoos-panel.lock")

lock_handle = open(LOCK_FILE, "w")

try:
    fcntl.flock(
        lock_handle,
        fcntl.LOCK_EX | fcntl.LOCK_NB
    )

except BlockingIOError:
    print("AyyoPanel already running boss 😂")
    sys.exit(0)


LAUNCHER = ROOT / "desktop" / "launcher" / "ayyo_launcher.py"
NOTIFICATIONS = (
    ROOT / "apps" / "notification-center" / "ayyo_notification_center.py"
)
QUICK_CONTROLS = (
    ROOT / "apps" / "quick-controls" / "ayyo_quick_controls.py"
)

BG = "#111116"
TEXT = "#ffffff"
MUTED = "#b5b5b5"


def launch(command):
    try:
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass


def open_launcher():
    launch(["python3", str(LAUNCHER)])


def open_notifications():
    launch(["python3", str(NOTIFICATIONS)])


def open_quick_controls():
    launch(["python3", str(QUICK_CONTROLS)])


def open_network_settings():
    launch([
        "gnome-control-center",
        "network"
    ])


def network_state():

    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "STATE", "general"],
            capture_output=True,
            text=True,
            timeout=2
        )

        if result.stdout.strip().lower() == "connected":
            return "📡 Connected"

        return "📡 Offline 😂"

    except Exception:
        return "📡 Unknown"


def notification_count():

    history = (
        ROOT
        / "system"
        / "notifications"
        / "history.json"
    )

    try:
        import json

        data = json.loads(
            history.read_text(
                encoding="utf-8"
            )
        )

        if isinstance(data, list):
            return len(data)

    except Exception:
        pass

    return 0


# ============================================================
# Main Panel
# ============================================================

root = tk.Tk()

root.title("AyyoOS Panel")

screen_width = root.winfo_screenwidth()

root.geometry(
    f"{screen_width}x48+0+0"
)

root.configure(bg=BG)

root.overrideredirect(True)

root.attributes(
    "-topmost",
    True
)


# ============================================================
# Left Side
# ============================================================

left = tk.Frame(
    root,
    bg=BG
)

left.pack(
    side="left",
    fill="y"
)


tk.Button(
    left,
    text="😂 AyyoOS",
    font=("Sans", 12, "bold"),
    bg=BG,
    fg=TEXT,
    activebackground="#222229",
    activeforeground=TEXT,
    bd=0,
    padx=18,
    command=open_launcher
).pack(
    side="left",
    fill="y"
)


# ============================================================
# Right Side
# ============================================================

right = tk.Frame(
    root,
    bg=BG
)

right.pack(
    side="right",
    fill="y"
)


network_button = tk.Button(
    right,
    text="📡 Checking...",
    font=("Sans", 10),
    bg=BG,
    fg=TEXT,
    activebackground="#222229",
    activeforeground=TEXT,
    bd=0,
    padx=12,
    command=open_network_settings
)

network_button.pack(
    side="left",
    fill="y"
)


notification_button = tk.Button(
    right,
    text="🔔 0",
    font=("Sans", 10),
    bg=BG,
    fg=TEXT,
    activebackground="#222229",
    activeforeground=TEXT,
    bd=0,
    padx=12,
    command=open_notifications
)

notification_button.pack(
    side="left",
    fill="y"
)


tk.Button(
    right,
    text="⚡",
    font=("Sans", 12),
    bg=BG,
    fg=TEXT,
    activebackground="#222229",
    activeforeground=TEXT,
    bd=0,
    padx=12,
    command=open_quick_controls
).pack(
    side="left",
    fill="y"
)


clock_label = tk.Label(
    right,
    text="--:--",
    font=("Sans", 10, "bold"),
    bg=BG,
    fg=TEXT,
    padx=15
)

clock_label.pack(
    side="left",
    fill="y"
)


# ============================================================
# Live Updates
# ============================================================

def update_panel():

    clock_label.config(
        text=datetime.now().strftime(
            "%I:%M %p"
        )
    )

    network_button.config(
        text=network_state()
    )

    count = notification_count()

    notification_button.config(
        text=f"🔔 {count}"
    )

    root.after(
        5000,
        update_panel
    )


update_panel()

root.mainloop()
