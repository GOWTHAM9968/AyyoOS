#!/usr/bin/env python3

import tkinter as tk
import subprocess
from pathlib import Path

ROOT = Path.home() / "AyyoOS"
MODE_MANAGER = ROOT / "comedy-engine" / "mode_manager.py"


def run(command):
    try:
        subprocess.Popen(command)
    except Exception as error:
        status.config(text=f"Ayyo! {error} 😂")


def open_files():
    run(["nautilus"])


def open_terminal():
    run(["gnome-terminal"])


def open_settings():
    run(["gnome-control-center"])


def get_current_mode():
    try:
        result = subprocess.run(
            ["python3", str(MODE_MANAGER)],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    except Exception:
        return "funny"


def set_personality(mode):
    try:
        subprocess.run(
            ["python3", str(MODE_MANAGER), mode],
            check=True
        )

        current_mode.set(mode)

        mode_status.config(
            text=f"✓ {mode.upper()} MODE ACTIVE"
        )

        status.config(
            text=f"Boss... {mode.upper()} personality set 😂"
        )

    except Exception as error:
        status.config(
            text=f"Ayyo! Mode change failed: {error}"
        )


def open_personality():
    window = tk.Toplevel(root)

    window.title("AyyoOS Personality")
    window.geometry("420x430")
    window.resizable(False, False)
    window.configure(bg="#111116")

    tk.Label(
        window,
        text="🎭 Personality Mode",
        font=("Sans", 22, "bold"),
        bg="#111116",
        fg="white"
    ).pack(pady=(30, 5))

    tk.Label(
        window,
        text="How should AyyoOS behave?",
        font=("Sans", 11),
        bg="#111116",
        fg="#bbbbbb"
    ).pack(pady=(0, 20))

    modes = [
        ("🙂 Normal", "normal"),
        ("😎 Chill", "chill"),
        ("😂 Funny", "funny"),
        ("🔥 Savage", "savage")
    ]

    for label, mode in modes:

        tk.Button(
            window,
            text=label,
            font=("Sans", 13),
            width=22,
            height=2,
            command=lambda m=mode: set_personality(m)
        ).pack(pady=5)

    global mode_status

    mode_status = tk.Label(
        window,
        text=f"✓ {current_mode.get().upper()} MODE ACTIVE",
        font=("Sans", 11, "bold"),
        bg="#111116",
        fg="white"
    )

    mode_status.pack(pady=20)


def language():
    status.config(
        text="🌐 Telugu + English"
    )


def close_launcher():
    root.destroy()


root = tk.Tk()

root.title("AyyoOS Launcher")
root.geometry("520x620")
root.resizable(False, False)
root.configure(bg="#111116")

current_mode = tk.StringVar(
    value=get_current_mode()
)


tk.Label(
    root,
    text="😂 AyyoOS",
    font=("Sans", 28, "bold"),
    bg="#111116",
    fg="white"
).pack(pady=(35, 5))


tk.Label(
    root,
    text="Your PC Has a Personality.",
    font=("Sans", 12),
    bg="#111116",
    fg="#bbbbbb"
).pack(pady=(0, 25))


button_style = {
    "font": ("Sans", 14),
    "width": 25,
    "height": 2,
    "bd": 0
}


tk.Button(
    root,
    text="📁  AyyoFiles",
    command=open_files,
    **button_style
).pack(pady=6)


tk.Button(
    root,
    text="⚙️  AyyoSettings",
    command=open_settings,
    **button_style
).pack(pady=6)


tk.Button(
    root,
    text="💻  AyyoTerminal",
    command=open_terminal,
    **button_style
).pack(pady=6)


tk.Button(
    root,
    text="🎭  Personality Mode",
    command=open_personality,
    **button_style
).pack(pady=6)


tk.Button(
    root,
    text="🌐  Language",
    command=language,
    **button_style
).pack(pady=6)


status = tk.Label(
    root,
    text=f"Current personality: {current_mode.get().upper()}",
    font=("Sans", 11),
    bg="#111116",
    fg="white"
)

status.pack(pady=22)


tk.Button(
    root,
    text="✕ Close",
    command=close_launcher,
    font=("Sans", 11),
    width=15
).pack()


root.mainloop()
