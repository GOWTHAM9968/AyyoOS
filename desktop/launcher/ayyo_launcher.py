#!/usr/bin/env python3
from datetime import datetime

import tkinter as tk
import subprocess
import getpass
from pathlib import Path


# ============================================================
# AyyoOS Paths
# ============================================================

ROOT = Path.home() / "AyyoOS"

MODE_MANAGER = (
    ROOT / "comedy-engine" / "mode_manager.py"
)

LANGUAGE_MANAGER = (
    ROOT / "comedy-engine" / "language_manager.py"
)

AYYO_SETTINGS = (
    ROOT / "apps" / "settings" / "ayyo_settings.py"
)

AYYO_SYSTEM_CENTER = (
    ROOT / "apps" / "system-center" / "ayyo_system_center.py"
)

AYYO_QUICK_CONTROLS = (
    ROOT / "apps" / "quick-controls" / "ayyo_quick_controls.py"
)

AYYO_NOTIFICATION_CENTER = (
    ROOT / "apps" / "notification-center" / "ayyo_notification_center.py"
)

CONFIG = (
    ROOT / "config" / "personality.conf"
)


# ============================================================
# General launcher
# ============================================================

def launch(command):

    try:
        subprocess.Popen(command)

    except Exception as error:

        status.config(
            text=f"Ayyo! App open avvaledu 😂  {error}"
        )


# ============================================================
# Read AyyoOS configuration
# ============================================================

def read_config():

    data = {
        "mode": "funny",
        "language": "telugu"
    }

    if CONFIG.exists():

        try:

            for line in CONFIG.read_text(
                encoding="utf-8"
            ).splitlines():

                if "=" in line:

                    key, value = line.split("=", 1)

                    data[key.strip()] = value.strip()

        except Exception:
            pass

    return data


# ============================================================
# Personality
# ============================================================

def get_mode():

    return read_config().get(
        "mode",
        "funny"
    )


def change_mode(mode):

    try:

        subprocess.run(
            [
                "python3",
                str(MODE_MANAGER),
                mode
            ],
            check=True
        )

        mode_label.config(
            text=f"🎭 {mode.upper()}"
        )

        status.config(
            text=f"Personality changed to {mode.upper()} 😂"
        )

    except Exception as error:

        status.config(
            text=f"Ayyo! Mode change avvaledu 😂 {error}"
        )


def personality_menu():

    window = tk.Toplevel(root)

    window.title(
        "AyyoOS Personality"
    )

    window.geometry(
        "380x430"
    )

    window.configure(
        bg="#111116"
    )

    window.resizable(
        False,
        False
    )


    tk.Label(
        window,
        text="🎭 Personality",
        font=("Sans", 21, "bold"),
        bg="#111116",
        fg="white"
    ).pack(
        pady=(30, 5)
    )


    tk.Label(
        window,
        text=f"Current: {get_mode().upper()}",
        font=("Sans", 11),
        bg="#111116",
        fg="#aaaaaa"
    ).pack(
        pady=(0, 20)
    )


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
            width=22,
            height=2,
            font=("Sans", 12),
            command=lambda m=mode: (
                change_mode(m),
                window.destroy()
            )
        ).pack(
            pady=6
        )


# ============================================================
# Language
# ============================================================

def get_language():

    return read_config().get(
        "language",
        "telugu"
    )


def change_language(language):

    if not LANGUAGE_MANAGER.exists():

        status.config(
            text="Language Manager inka ready avvaledu boss 😂"
        )

        return


    try:

        subprocess.run(
            [
                "python3",
                str(LANGUAGE_MANAGER),
                language
            ],
            check=True
        )

        language_label.config(
            text=f"🌐 {language.upper()}"
        )

        status.config(
            text=f"Language changed to {language.upper()} 🌐"
        )

    except Exception as error:

        status.config(
            text=f"Ayyo! Language change avvaledu 😂 {error}"
        )


def language_menu():

    window = tk.Toplevel(root)

    window.title(
        "AyyoOS Language"
    )

    window.geometry(
        "360x300"
    )

    window.configure(
        bg="#111116"
    )

    window.resizable(
        False,
        False
    )


    tk.Label(
        window,
        text="🌐 Language",
        font=("Sans", 21, "bold"),
        bg="#111116",
        fg="white"
    ).pack(
        pady=(30, 5)
    )


    tk.Label(
        window,
        text=f"Current: {get_language().upper()}",
        font=("Sans", 11),
        bg="#111116",
        fg="#aaaaaa"
    ).pack(
        pady=(0, 20)
    )


    tk.Button(
        window,
        text="🇮🇳 Telugu",
        width=22,
        height=2,
        font=("Sans", 12),
        command=lambda: (
            change_language("telugu"),
            window.destroy()
        )
    ).pack(
        pady=6
    )


    tk.Button(
        window,
        text="English",
        width=22,
        height=2,
        font=("Sans", 12),
        command=lambda: (
            change_language("english"),
            window.destroy()
        )
    ).pack(
        pady=6
    )


# ============================================================
# Search
# ============================================================

def clear_search(event=None):

    if search_entry.get().startswith(
        "Search:"
    ):

        search_entry.delete(
            0,
            tk.END
        )


def search_apps(event=None):

    query = (
        search_entry
        .get()
        .lower()
        .strip()
    )


    if not query:

        return


    if query in [
        "files",
        "file",
        "ayyofiles"
    ]:

        launch(
            ["nautilus"]
        )

        status.config(
            text="Opening AyyoFiles 📁"
        )


    elif query in [
        "browser",
        "web",
        "internet"
    ]:

        launch(
            [
                "xdg-open",
                "https://www.google.com"
            ]
        )

        status.config(
            text="Opening Browser 🌐"
        )


    elif query in [
        "terminal",
        "ayyoterminal"
    ]:

        launch(
            ["gnome-terminal"]
        )

        status.config(
            text="Opening AyyoTerminal 💻"
        )


    elif query in [
        "settings",
        "ayyosettings"
    ]:

        open_ayyo_settings()


    elif query in [
        "personality",
        "mode"
    ]:

        personality_menu()


    elif query in [
        "language",
        "telugu",
        "english"
    ]:

        language_menu()


    elif query in [
        "system",
        "status",
        "system center",
        "systemcenter",
        "ayyo system center"
    ]:

        open_system_center()


    elif query in [
        "notification",
        "notifications",
        "notification center",
        "alerts",
        "alert"
    ]:

        open_notification_center()


    elif query in [
        "quick",
        "controls",
        "quick controls",
        "quickcontrols"
    ]:

        open_quick_controls()


    elif query in [
        "wifi",
        "wi-fi",
        "network",
        "internet settings"
    ]:

        launch(
            [
                "gnome-control-center",
                "network"
            ]
        )

        status.config(
            text="Opening Network Settings 📡"
        )


    elif query in [
        "sound",
        "audio",
        "volume",
        "sound settings"
    ]:

        launch(
            [
                "gnome-control-center",
                "sound"
            ]
        )

        status.config(
            text="Opening Sound Settings 🔊"
        )


    else:

        status.config(
            text=f"Ayyo! '{query}' app dorakaledu 😂"
        )


# ============================================================
# AyyoSettings
# ============================================================

def open_ayyo_settings():

    if AYYO_SETTINGS.exists():

        launch(
            [
                "python3",
                str(AYYO_SETTINGS)
            ]
        )

        status.config(
            text="Opening AyyoSettings ⚙️"
        )

    else:

        status.config(
            text="AyyoSettings file dorakaledu boss 😂"
        )


# ============================================================
# AyyoSystem Center
# ============================================================

def open_system_center():

    if AYYO_SYSTEM_CENTER.exists():

        launch(
            [
                "python3",
                str(AYYO_SYSTEM_CENTER)
            ]
        )

        status.config(
            text="Opening AyyoSystem Center 🖥️"
        )

    else:

        status.config(
            text="System Center file dorakaledu boss 😂"
        )


# ============================================================
# Ayyo Quick Controls
# ============================================================

def open_quick_controls():

    if AYYO_QUICK_CONTROLS.exists():

        launch(
            [
                "python3",
                str(AYYO_QUICK_CONTROLS)
            ]
        )

        status.config(
            text="Opening Quick Controls ⚡"
        )

    else:

        status.config(
            text="Quick Controls file dorakaledu boss 😂"
        )


# ============================================================
# Ayyo Notification Center
# ============================================================

def open_notification_center():

    if AYYO_NOTIFICATION_CENTER.exists():

        launch(
            [
                "python3",
                str(AYYO_NOTIFICATION_CENTER)
            ]
        )

        status.config(
            text="Opening Notification Center 🔔"
        )

    else:

        status.config(
            text="Notification Center file dorakaledu boss 😂"
        )


# ============================================================
# Power Menu
# ============================================================

def power_menu():

    window = tk.Toplevel(root)

    window.title(
        "AyyoOS Power"
    )

    window.geometry(
        "350x350"
    )

    window.configure(
        bg="#111116"
    )

    window.resizable(
        False,
        False
    )


    tk.Label(
        window,
        text="⏻ Power",
        font=("Sans", 21, "bold"),
        bg="#111116",
        fg="white"
    ).pack(
        pady=(30, 20)
    )


    tk.Button(
        window,
        text="🔒 Lock",
        width=22,
        height=2,
        font=("Sans", 11),
        command=lambda: launch(
            [
                "loginctl",
                "lock-session"
            ]
        )
    ).pack(
        pady=6
    )


    tk.Button(
        window,
        text="🚪 Log Out",
        width=22,
        height=2,
        font=("Sans", 11),
        command=lambda: launch(
            [
                "gnome-session-quit",
                "--logout"
            ]
        )
    ).pack(
        pady=6
    )


    tk.Button(
        window,
        text="↻ Restart",
        width=22,
        height=2,
        font=("Sans", 11),
        command=lambda: launch(
            [
                "gnome-session-quit",
                "--reboot"
            ]
        )
    ).pack(
        pady=6
    )


    tk.Button(
        window,
        text="⏻ Shut Down",
        width=22,
        height=2,
        font=("Sans", 11),
        command=lambda: launch(
            [
                "gnome-session-quit",
                "--power-off"
            ]
        )
    ).pack(
        pady=6
    )


# ============================================================
# Main Window
# ============================================================

root = tk.Tk()

root.title(
    "Ayyo Start"
)

root.geometry(
    "540x680"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#111116"
)


# ============================================================
# Header
# ============================================================

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
).pack(
    side="left"
)


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


language_label = tk.Label(
    root,
    text=f"🌐 {get_language().upper()}",
    font=("Sans", 9),
    bg="#111116",
    fg="#888888"
)

language_label.pack(
    pady=(4, 0)
)


# ============================================================
# Search Bar
# ============================================================

search_entry = tk.Entry(
    root,
    font=("Sans", 12),
    width=39,
    relief="flat"
)

search_entry.pack(
    padx=30,
    pady=20,
    ipady=9
)


search_entry.insert(
    0,
    "Search: files, browser, terminal, settings"
)


search_entry.bind(
    "<FocusIn>",
    clear_search
)


search_entry.bind(
    "<Return>",
    search_apps
)


# ============================================================
# App Grid
# ============================================================

apps = tk.Frame(
    root,
    bg="#111116"
)

apps.pack(
    pady=5
)


button_options = {

    "font": ("Sans", 11),

    "width": 17,

    "height": 3,

    "bd": 0

}


# Row 1

tk.Button(
    apps,
    text="📁\nAyyoFiles",
    command=lambda: launch(
        ["nautilus"]
    ),
    **button_options
).grid(
    row=0,
    column=0,
    padx=8,
    pady=8
)


tk.Button(
    apps,
    text="🌐\nBrowser",
    command=lambda: launch(
        [
            "xdg-open",
            "https://www.google.com"
        ]
    ),
    **button_options
).grid(
    row=0,
    column=1,
    padx=8,
    pady=8
)


# Row 2

tk.Button(
    apps,
    text="💻\nAyyoTerminal",
    command=lambda: launch(
        ["gnome-terminal"]
    ),
    **button_options
).grid(
    row=1,
    column=0,
    padx=8,
    pady=8
)


tk.Button(
    apps,
    text="⚙️\nAyyoSettings",
    command=open_ayyo_settings,
    **button_options
).grid(
    row=1,
    column=1,
    padx=8,
    pady=8
)


# Row 3

tk.Button(
    apps,
    text="🎭\nPersonality",
    command=personality_menu,
    **button_options
).grid(
    row=2,
    column=0,
    padx=8,
    pady=8
)


tk.Button(
    apps,
    text="🌐\nLanguage",
    command=language_menu,
    **button_options
).grid(
    row=2,
    column=1,
    padx=8,
    pady=8
)


# Row 4

tk.Button(
    apps,
    text="🖥️\nSystem Center",
    command=open_system_center,
    **button_options
).grid(
    row=3,
    column=0,
    padx=8,
    pady=8
)


tk.Button(
    apps,
    text="⚡\nQuick Controls",
    command=open_quick_controls,
    **button_options
).grid(
    row=3,
    column=1,
    padx=8,
    pady=8
)


# Row 5 - Notification Center

tk.Button(
    apps,
    text="🔔\nNotifications",
    command=open_notification_center,
    **button_options
).grid(
    row=4,
    column=0,
    columnspan=2,
    padx=8,
    pady=8
)


# ============================================================
# Status
# ============================================================

status = tk.Label(
    root,
    text="Boss... em kavali? 😂",
    font=("Sans", 10),
    bg="#111116",
    fg="white"
)

status.pack(
    pady=12
)


# ============================================================
# Footer
# ============================================================

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


# ============================================================
# Live AyyoOS Status
# ============================================================

live_status = tk.Label(
    footer,
    text="📡 Checking...   🕐 --:--",
    font=("Sans", 10, "bold"),
    bg="#19191f",
    fg="white"
)

live_status.pack(
    side="left",
    expand=True,
    padx=10,
    pady=15
)


def update_live_status():

    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "STATE", "general"],
            capture_output=True,
            text=True,
            timeout=2
        )

        connected = (
            result.stdout.strip().lower()
            == "connected"
        )

        network = (
            "📡 Connected"
            if connected
            else "📡 Offline 😂"
        )

    except Exception:
        network = "📡 Unknown"

    current_time = datetime.now().strftime("%I:%M %p")

    live_status.config(
        text=f"{network}   🕐 {current_time}"
    )

    root.after(
        5000,
        update_live_status
    )


update_live_status()


tk.Button(
    footer,
    text="⏻",
    font=("Sans", 16),
    bd=0,
    command=power_menu
).pack(
    side="right",
    padx=20,
    pady=8
)


# ============================================================
# Start Ayyo
# ============================================================

root.mainloop()
