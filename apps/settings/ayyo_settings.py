#!/usr/bin/env python3

import tkinter as tk
import subprocess
import platform
from pathlib import Path

ROOT = Path.home() / "AyyoOS"
CONFIG = ROOT / "config" / "personality.conf"
MODE_MANAGER = ROOT / "comedy-engine" / "mode_manager.py"
LANGUAGE_MANAGER = ROOT / "comedy-engine" / "language_manager.py"


def run(command):
    try:
        subprocess.Popen(command)
    except Exception as error:
        show_page(
            "Ayyo! 😂",
            f"Could not open feature:\n{error}"
        )


def read_config():
    data = {
        "mode": "funny",
        "language": "telugu"
    }

    if CONFIG.exists():
        for line in CONFIG.read_text(
            encoding="utf-8"
        ).splitlines():

            if "=" in line:
                key, value = line.split("=", 1)
                data[key.strip()] = value.strip()

    return data


def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def page_title(title, subtitle=""):
    tk.Label(
        content,
        text=title,
        font=("Sans", 23, "bold"),
        bg="#15151c",
        fg="white"
    ).pack(anchor="w", padx=30, pady=(30, 5))

    if subtitle:
        tk.Label(
            content,
            text=subtitle,
            font=("Sans", 11),
            bg="#15151c",
            fg="#aaaaaa"
        ).pack(anchor="w", padx=30, pady=(0, 25))


def show_page(title, message):
    clear_content()
    page_title(title)

    tk.Label(
        content,
        text=message,
        font=("Sans", 13),
        justify="left",
        bg="#15151c",
        fg="white"
    ).pack(anchor="w", padx=30, pady=15)


def appearance():
    clear_content()

    page_title(
        "🎨 Appearance",
        "Make AyyoOS look like your system."
    )

    tk.Label(
        content,
        text="AyyoOS Comedy Edition",
        font=("Sans", 15, "bold"),
        bg="#15151c",
        fg="white"
    ).pack(anchor="w", padx=30, pady=10)

    tk.Button(
        content,
        text="😂 Apply Comedy Wallpaper",
        font=("Sans", 12),
        command=apply_wallpaper
    ).pack(anchor="w", padx=30, pady=10)


def apply_wallpaper():
    wallpaper = (
        ROOT
        / "branding"
        / "wallpapers"
        / "ayyoos-comedy-main.png"
    )

    uri = f"file://{wallpaper}"

    subprocess.run([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri",
        uri
    ])

    subprocess.run([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri-dark",
        uri
    ])


def personality():
    clear_content()

    config = read_config()

    page_title(
        "🎭 Personality",
        f"Current mode: {config['mode'].upper()}"
    )

    modes = [
        ("🙂 Normal", "normal"),
        ("😎 Chill", "chill"),
        ("😂 Funny", "funny"),
        ("🔥 Savage", "savage")
    ]

    for label, mode in modes:

        tk.Button(
            content,
            text=label,
            font=("Sans", 12),
            width=22,
            height=2,
            command=lambda m=mode: change_mode(m)
        ).pack(anchor="w", padx=30, pady=5)


def change_mode(mode):
    subprocess.run([
        "python3",
        str(MODE_MANAGER),
        mode
    ])

    personality()


def language():
    clear_content()

    config = read_config()

    page_title(
        "🌐 Language",
        f"Current language: {config['language'].upper()}"
    )

    tk.Button(
        content,
        text="🇮🇳 Telugu",
        width=22,
        height=2,
        command=lambda: change_language("telugu")
    ).pack(anchor="w", padx=30, pady=6)

    tk.Button(
        content,
        text="English",
        width=22,
        height=2,
        command=lambda: change_language("english")
    ).pack(anchor="w", padx=30, pady=6)


def change_language(language_name):
    subprocess.run([
        "python3",
        str(LANGUAGE_MANAGER),
        language_name
    ])

    language()


def network():
    clear_content()

    page_title(
        "📶 Network",
        "Internet and Wi-Fi controls."
    )

    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "STATE", "general"],
            capture_output=True,
            text=True
        )

        state = result.stdout.strip()

    except Exception:
        state = "Unknown"

    tk.Label(
        content,
        text=f"Network status: {state}",
        font=("Sans", 14),
        bg="#15151c",
        fg="white"
    ).pack(anchor="w", padx=30, pady=10)

    tk.Button(
        content,
        text="Open Advanced Network Settings",
        command=lambda: run([
            "gnome-control-center",
            "network"
        ])
    ).pack(anchor="w", padx=30, pady=10)


def sound():
    clear_content()

    page_title(
        "🔊 Sound",
        "AyyoOS audio controls."
    )

    tk.Button(
        content,
        text="Open Audio Controls",
        command=lambda: run([
            "gnome-control-center",
            "sound"
        ])
    ).pack(anchor="w", padx=30, pady=10)


def notifications():
    clear_content()

    page_title(
        "🔔 Notifications",
        "Manage AyyoOS notifications."
    )

    tk.Button(
        content,
        text="😂 Test Ayyo Notification",
        command=lambda: run([
            str(ROOT / "core/bin/ayyo-notify"),
            "wifi_on"
        ])
    ).pack(anchor="w", padx=30, pady=10)


def about():
    clear_content()

    config = read_config()

    page_title(
        "😂 About AyyoOS",
        "Your PC Has a Personality."
    )

    info = (
        "AyyoOS\n\n"
        "Version: 0.1 Alpha\n"
        "Codename: Ayyo\n\n"
        f"Personality: {config['mode'].upper()}\n"
        f"Language: {config['language'].upper()}\n\n"
        f"Kernel: {platform.release()}\n"
        f"Architecture: {platform.machine()}\n\n"
        "Comedy Edition 😂"
    )

    tk.Label(
        content,
        text=info,
        justify="left",
        font=("Sans", 12),
        bg="#15151c",
        fg="white"
    ).pack(anchor="w", padx=30, pady=10)


root = tk.Tk()

root.title("AyyoSettings")
root.geometry("850x580")
root.minsize(750, 500)
root.configure(bg="#101015")


sidebar = tk.Frame(
    root,
    width=230,
    bg="#101015"
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="😂 AyyoOS",
    font=("Sans", 21, "bold"),
    bg="#101015",
    fg="white"
).pack(pady=(30, 5))


tk.Label(
    sidebar,
    text="SETTINGS",
    font=("Sans", 9, "bold"),
    bg="#101015",
    fg="#888888"
).pack(pady=(0, 25))


menu_items = [
    ("🎨  Appearance", appearance),
    ("🎭  Personality", personality),
    ("🌐  Language", language),
    ("📶  Network", network),
    ("🔊  Sound", sound),
    ("🔔  Notifications", notifications),
    ("😂  About AyyoOS", about)
]


for label, command in menu_items:

    tk.Button(
        sidebar,
        text=label,
        font=("Sans", 11),
        anchor="w",
        width=20,
        height=2,
        bd=0,
        command=command
    ).pack(padx=15, pady=3)


content = tk.Frame(
    root,
    bg="#15151c"
)

content.pack(
    side="right",
    fill="both",
    expand=True
)


about()

root.mainloop()
