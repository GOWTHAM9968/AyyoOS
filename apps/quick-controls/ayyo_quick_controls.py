#!/usr/bin/env python3

import tkinter as tk
import subprocess
import shutil


def run(command):
    try:
        subprocess.Popen(command)
    except Exception:
        pass


def output(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except Exception:
        return ""


def network_status():
    state = output([
        "nmcli", "-t", "-f", "STATE", "general"
    ])

    if state.lower() == "connected":
        return "🌐 Internet Connected"

    return "📡 Internet Disconnected"


def audio_status():
    if not shutil.which("pactl"):
        return "🔊 Audio control unavailable"

    value = output([
        "pactl",
        "get-sink-volume",
        "@DEFAULT_SINK@"
    ])

    if "%" in value:
        try:
            volume = value.split("/")[1].strip()
            return f"🔊 Volume {volume}"
        except Exception:
            pass

    return "🔊 Audio Ready"


def refresh():
    network_label.config(text=network_status())
    audio_label.config(text=audio_status())
    status.config(text="😂 Status refreshed boss!")


root = tk.Tk()

root.title("Ayyo Quick Controls")
root.geometry("500x500")
root.configure(bg="#111318")
root.resizable(False, False)


tk.Label(
    root,
    text="😂 Ayyo Quick Controls",
    font=("Sans", 22, "bold"),
    bg="#111318",
    fg="white"
).pack(pady=(25, 5))


tk.Label(
    root,
    text="Control room ready boss 😎",
    font=("Sans", 11),
    bg="#111318",
    fg="#aaaaaa"
).pack(pady=(0, 25))


network_label = tk.Label(
    root,
    text="Checking network...",
    font=("Sans", 14),
    bg="#111318",
    fg="white"
)

network_label.pack(pady=10)


audio_label = tk.Label(
    root,
    text="Checking audio...",
    font=("Sans", 14),
    bg="#111318",
    fg="white"
)

audio_label.pack(pady=10)


button_options = {
    "font": ("Sans", 12, "bold"),
    "width": 24,
    "pady": 8
}


tk.Button(
    root,
    text="📡 Network Settings",
    command=lambda: run([
        "gnome-control-center",
        "network"
    ]),
    **button_options
).pack(pady=7)


tk.Button(
    root,
    text="🔊 Sound Settings",
    command=lambda: run([
        "gnome-control-center",
        "sound"
    ]),
    **button_options
).pack(pady=7)


tk.Button(
    root,
    text="⚙️ System Settings",
    command=lambda: run([
        "gnome-control-center"
    ]),
    **button_options
).pack(pady=7)


tk.Button(
    root,
    text="🔄 Refresh",
    command=refresh,
    **button_options
).pack(pady=7)


status = tk.Label(
    root,
    text="AyyoOS checking controls...",
    bg="#111318",
    fg="#aaaaaa",
    font=("Sans", 10)
)

status.pack(pady=15)


refresh()

root.mainloop()
