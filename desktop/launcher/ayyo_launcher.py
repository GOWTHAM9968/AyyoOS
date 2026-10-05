#!/usr/bin/env python3

import tkinter as tk
import subprocess
import getpass
from pathlib import Path

ROOT = Path.home() / "AyyoOS"
CONFIG = ROOT / "config" / "personality.conf"
MODE_MANAGER = ROOT / "comedy-engine" / "mode_manager.py"


def launch(command):
    try:
        subprocess.Popen(command)
    except Exception as error:
        status.config(text=f"Ayyo! {error} 😂")


def get_mode():
    try:
        result = subprocess.run(
            ["python3", str(MODE_MANAGER)],
            capture_output=True,
            text=True
        )

        mode = result.stdout.strip()

        if mode:
            return mode

    except Exception:
        pass

    return "funny"


def change_mode(mode):
    try:
        subprocess.run(
            ["python3", str(MODE_MANAGER), mode],
            check=True
        )

        mode_label.config(
            text=f"🎭 {mode.upper()}"
        )

        status.config(
            text=f"Personality changed to {mode.upper()} 😂"
        )

    except Exception as error:
        status.config(text=f"Ayyo! {error}")


def personality_menu():

    window = tk.Toplevel(root)

    window.title("AyyoOS Personality")
    window.geometry("350x390")
    window.configure(bg="#111116")
    window.resizable(False, False)

    tk.Label(
        window,
        text="🎭 Personality",
        font=("Sans", 20, "bold"),
        bg="#111116",
        fg="white"
    ).pack(pady=25)

    modes = [
        ("🙂 Normal", "normal"),
        ("😎 Chill", "chill"),
        ("😂 Funny", "funny"),
        ("🔥 Savage", "savage")
    ]

    for text, mode in modes:

        tk.Button(
            window,
            text=text,
            width=20,
            height=2,
            font=("Sans", 12),
            command=lambda m=mode: change_mode(m)
        ).pack(pady=5)


def language_menu():

    window = tk.Toplevel(root)

    window.title("AyyoOS Language")
    window.geometry("330x260")
    window.configure(bg="#111116")
    window.resizable(False, False)

    tk.Label(
        window,
        text="🌐 Language",
        font=("Sans", 20, "bold"),
        bg="#111116",
        fg="white"
    ).pack(pady=25)

    tk.Button(
        window,
        text="🇮🇳 Telugu",
        width=20,
        height=2
    ).pack(pady=6)

    tk.Button(
        window,
        text="English",
        width=20,
        height=2
    ).pack(pady=6)


def search_apps(event=None):

    query = search_entry.get().lower().strip()

    apps = {
        "files": ["nautilus"],
        "browser": ["xdg-open", "https://www.google.com"],
        "terminal": ["gnome-terminal"],
        "settings": ["gnome-control-center"]
    }

    if query in apps:
        launch(apps[query])
        status.config(text=f"Opening {query}...")


def power_menu():

    window = tk.Toplevel(root)

    window.title("AyyoOS Power")
    window.geometry("330x300")
    window.configure(bg="#111116")
    window.resizable(False, False)

    tk.Label(
        window,
        text="⏻ Power",
        font=("Sans", 20, "bold"),
        bg="#111116",
        fg="white"
    ).pack(pady=25)

    tk.Button(
        window,
        text="🔒 Lock",
        width=20,
        height=2,
        command=lambda: launch(
            ["loginctl", "lock-session"]
        )
    ).pack(pady=5)

    tk.Button(
        window,
        text="↻ Restart",
        width=20,
        height=2,
        command=lambda: launch(
            ["gnome-session-quit", "--reboot"]
        )
    ).pack(pady=5)

    tk.Button(
        window,
        text="⏻ Shut Down",
        width=20,
        height=2,
        command=lambda: launch(
            ["gnome-session-quit", "--power-off"]
        )
    ).pack(pady=5)


root = tk.Tk()

root.title("Ayyo Start")
root.geometry("520x650")
root.resizable(False, False)
root.configure(bg="#111116")


# Header

header = tk.Frame(
    root,
    bg="#111116"
)

header.pack(
    fill="x",
    padx=30,
    pady=(25, 5)
)


tk.Label(
    header,
    text="😂 AyyoOS",
    font=("Sans", 25, "bold"),
    bg="#111116",
    fg="white"
).pack(side="left")


mode_label = tk.Label(
    header,
    text=f"🎭 {get_mode().upper()}",
    font=("Sans", 10, "bold"),
    bg="#111116",
    fg="white"
)

mode_label.pack(
    side="right",
    pady=10
)


tk.Label(
    root,
    text="Your PC Has a Personality.",
    font=("Sans", 11),
    bg="#111116",
    fg="#aaaaaa"
).pack()


# Search

search_entry = tk.Entry(
    root,
    font=("Sans", 13),
    width=35
)

search_entry.pack(
    pady=25,
    ipady=8
)

search_entry.insert(
    0,
    "Search: files, browser, terminal, settings"
)

search_entry.bind(
    "<Return>",
    search_apps
)


# Apps

apps = tk.Frame(
    root,
    bg="#111116"
)

apps.pack(pady=5)


button_options = {
    "font": ("Sans", 12),
    "width": 16,
    "height": 3,
    "bd": 0
}


tk.Button(
    apps,
    text="📁\nAyyoFiles",
    command=lambda: launch(["nautilus"]),
    **button_options
).grid(row=0, column=0, padx=8, pady=8)


tk.Button(
    apps,
    text="🌐\nBrowser",
    command=lambda: launch(
        ["xdg-open", "https://www.google.com"]
    ),
    **button_options
).grid(row=0, column=1, padx=8, pady=8)


tk.Button(
    apps,
    text="💻\nAyyoTerminal",
    command=lambda: launch(["gnome-terminal"]),
    **button_options
).grid(row=1, column=0, padx=8, pady=8)


tk.Button(
    apps,
    text="⚙️\nAyyoSettings",
    command=lambda: launch(["gnome-control-center"]),
    **button_options
).grid(row=1, column=1, padx=8, pady=8)


tk.Button(
    apps,
    text="🎭\nPersonality",
    command=personality_menu,
    **button_options
).grid(row=2, column=0, padx=8, pady=8)


tk.Button(
    apps,
    text="🌐\nLanguage",
    command=language_menu,
    **button_options
).grid(row=2, column=1, padx=8, pady=8)


status = tk.Label(
    root,
    text="Boss... em kavali? 😂",
    font=("Sans", 10),
    bg="#111116",
    fg="white"
)

status.pack(pady=12)


# Footer

footer = tk.Frame(
    root,
    bg="#19191f"
)

footer.pack(
    side="bottom",
    fill="x"
)


tk.Label(
    footer,
    text=f"👤 {getpass.getuser()}",
    font=("Sans", 11),
    bg="#19191f",
    fg="white"
).pack(
    side="left",
    padx=20,
    pady=15
)


tk.Button(
    footer,
    text="⏻",
    font=("Sans", 16),
    command=power_menu
).pack(
    side="right",
    padx=20,
    pady=8
)


root.mainloop()
