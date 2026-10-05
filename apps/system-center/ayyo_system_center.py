#!/usr/bin/env python3

import tkinter as tk
import subprocess
import shutil
import platform
from pathlib import Path

ROOT = Path.home() / "AyyoOS"


def command(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except Exception:
        return ""


def cpu_info():
    return f"{shutil.os.cpu_count() or '?'} CPU cores"


def ram_info():
    output = command(["free", "-h"])

    for line in output.splitlines():
        if line.startswith("Mem:"):
            parts = line.split()
            return f"{parts[2]} used / {parts[1]} total"

    return "Unavailable"


def storage_info():
    usage = shutil.disk_usage("/")

    total = usage.total / (1024 ** 3)
    used = usage.used / (1024 ** 3)

    percent = (usage.used / usage.total) * 100

    return f"{used:.1f} GB / {total:.1f} GB ({percent:.0f}% used)"


def network_info():
    state = command([
        "nmcli",
        "-t",
        "-f",
        "STATE",
        "general"
    ])

    if state.lower() == "connected":
        return "Connected 🌐"

    if state:
        return f"{state.title()}"

    return "Unavailable"


def audio_info():
    if shutil.which("pactl"):
        output = command([
            "pactl",
            "get-sink-volume",
            "@DEFAULT_SINK@"
        ])

        if output:
            try:
                return output.split("/")[1].strip()
            except Exception:
                return "Available"

    return "Audio control unavailable"


def refresh():
    cpu_value.config(text=cpu_info())
    ram_value.config(text=ram_info())
    storage_value.config(text=storage_info())
    network_value.config(text=network_info())
    audio_value.config(text=audio_info())

    status.config(
        text="😂 AyyoOS checked everything. System still alive boss!"
    )


root = tk.Tk()
root.title("AyyoSystem Center")
root.geometry("720x600")
root.configure(bg="#111318")
root.resizable(False, False)


title = tk.Label(
    root,
    text="😂 AyyoSystem Center",
    font=("Sans", 24, "bold"),
    bg="#111318",
    fg="white"
)
title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Your PC Has a Personality.",
    font=("Sans", 11),
    bg="#111318",
    fg="#aaaaaa"
)
subtitle.pack(pady=(0, 20))


container = tk.Frame(
    root,
    bg="#1b1e24",
    padx=30,
    pady=20
)
container.pack(
    padx=30,
    fill="both",
    expand=True
)


def card(label, row):
    name = tk.Label(
        container,
        text=label,
        font=("Sans", 13, "bold"),
        bg="#1b1e24",
        fg="#dddddd",
        anchor="w"
    )

    name.grid(
        row=row,
        column=0,
        sticky="w",
        pady=15
    )

    value = tk.Label(
        container,
        text="Checking...",
        font=("Sans", 13),
        bg="#1b1e24",
        fg="white",
        anchor="e"
    )

    value.grid(
        row=row,
        column=1,
        sticky="e",
        padx=(50, 0)
    )

    return value


container.columnconfigure(1, weight=1)

cpu_value = card("🧠 CPU", 0)
ram_value = card("💾 RAM", 1)
storage_value = card("📦 Storage", 2)
network_value = card("🌐 Network", 3)
audio_value = card("🔊 Audio", 4)


system_value = tk.Label(
    container,
    text=f"🐧 {platform.system()} {platform.release()}",
    font=("Sans", 11),
    bg="#1b1e24",
    fg="#aaaaaa"
)

system_value.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=20
)


refresh_button = tk.Button(
    root,
    text="🔄 Refresh System",
    font=("Sans", 12, "bold"),
    command=refresh,
    padx=20,
    pady=8
)

refresh_button.pack(pady=15)


status = tk.Label(
    root,
    text="AyyoOS checking your system...",
    bg="#111318",
    fg="#aaaaaa",
    font=("Sans", 10)
)

status.pack(pady=(0, 15))


refresh()

root.mainloop()
