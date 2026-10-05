#!/usr/bin/env python3

import tkinter as tk
from pathlib import Path
import sys
from datetime import datetime

ROOT = Path.home() / "AyyoOS"

NOTIFICATION_MODULE = (
    ROOT / "system" / "notifications"
)

sys.path.insert(
    0,
    str(NOTIFICATION_MODULE)
)

from notification_history import (
    get_history,
    clear_history
)


# ============================================================
# Window
# ============================================================

root = tk.Tk()

root.title("Ayyo Notification Center")
root.geometry("620x650")
root.minsize(520, 500)

BG = "#111116"
PANEL = "#19191f"
CARD = "#222229"
TEXT = "#ffffff"
SUBTEXT = "#aaaaaa"

root.configure(bg=BG)


# ============================================================
# Header
# ============================================================

header = tk.Frame(
    root,
    bg=BG
)

header.pack(
    fill="x",
    padx=22,
    pady=(20, 10)
)


tk.Label(
    header,
    text="🔔 Ayyo Notification Center",
    font=("Sans", 20, "bold"),
    bg=BG,
    fg=TEXT
).pack(
    anchor="w"
)


tk.Label(
    header,
    text="Mee PC em chestundo ikkada telustundi boss 😂",
    font=("Sans", 10),
    bg=BG,
    fg=SUBTEXT
).pack(
    anchor="w",
    pady=(4, 0)
)


# ============================================================
# Controls
# ============================================================

controls = tk.Frame(
    root,
    bg=BG
)

controls.pack(
    fill="x",
    padx=22,
    pady=8
)


# ============================================================
# Scrollable notification area
# ============================================================

container = tk.Frame(
    root,
    bg=BG
)

container.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=(5, 15)
)


canvas = tk.Canvas(
    container,
    bg=BG,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    container,
    orient="vertical",
    command=canvas.yview
)

notification_frame = tk.Frame(
    canvas,
    bg=BG
)


notification_frame.bind(
    "<Configure>",
    lambda event: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas_window = canvas.create_window(
    (0, 0),
    window=notification_frame,
    anchor="nw"
)


def resize_cards(event):

    canvas.itemconfigure(
        canvas_window,
        width=event.width
    )


canvas.bind(
    "<Configure>",
    resize_cards
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# ============================================================
# Helpers
# ============================================================

def format_time(value):

    try:

        dt = datetime.fromisoformat(value)

        return dt.strftime(
            "%d %b • %I:%M %p"
        )

    except Exception:

        return value or "Unknown time"


def category_icon(category):

    icons = {
        "network": "📡",
        "wifi": "📡",
        "power": "🔋",
        "battery": "🔋",
        "audio": "🔊",
        "security": "🛡️",
        "update": "🔄",
        "test": "🧪",
        "system": "⚙️"
    }

    return icons.get(
        str(category).lower(),
        "🔔"
    )


# ============================================================
# Load notifications
# ============================================================

def refresh_notifications():

    for widget in notification_frame.winfo_children():
        widget.destroy()

    history = get_history()

    count_label.config(
        text=f"{len(history)} notification(s)"
    )

    if not history:

        tk.Label(
            notification_frame,
            text="🔕",
            font=("Sans", 34),
            bg=BG,
            fg=TEXT
        ).pack(
            pady=(70, 10)
        )

        tk.Label(
            notification_frame,
            text="Notification emi ledu boss 😂",
            font=("Sans", 14, "bold"),
            bg=BG,
            fg=TEXT
        ).pack()

        tk.Label(
            notification_frame,
            text="PC silent ga undi... suspicious ga undi 😎",
            font=("Sans", 10),
            bg=BG,
            fg=SUBTEXT
        ).pack(
            pady=5
        )

        return

    for item in history:

        card = tk.Frame(
            notification_frame,
            bg=CARD,
            padx=15,
            pady=12
        )

        card.pack(
            fill="x",
            pady=6
        )

        category = item.get(
            "category",
            "system"
        )

        icon = category_icon(category)

        title = item.get(
            "title",
            "AyyoOS"
        )

        message = item.get(
            "message",
            ""
        )

        time_value = format_time(
            item.get(
                "time",
                ""
            )
        )

        tk.Label(
            card,
            text=f"{icon}  {title}",
            font=("Sans", 12, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text=message,
            font=("Sans", 10),
            bg=CARD,
            fg=TEXT,
            justify="left",
            wraplength=500
        ).pack(
            anchor="w",
            pady=(7, 5)
        )

        tk.Label(
            card,
            text=time_value,
            font=("Sans", 9),
            bg=CARD,
            fg=SUBTEXT
        ).pack(
            anchor="w"
        )


def clear_notifications():

    clear_history()

    status_label.config(
        text="History clean chesam boss 🧹😂"
    )

    refresh_notifications()


# ============================================================
# Control buttons
# ============================================================

count_label = tk.Label(
    controls,
    text="0 notification(s)",
    font=("Sans", 10),
    bg=BG,
    fg=SUBTEXT
)

count_label.pack(
    side="left"
)


tk.Button(
    controls,
    text="🔄 Refresh",
    command=refresh_notifications,
    bd=0,
    padx=12,
    pady=6
).pack(
    side="right",
    padx=5
)


tk.Button(
    controls,
    text="🧹 Clear All",
    command=clear_notifications,
    bd=0,
    padx=12,
    pady=6
).pack(
    side="right",
    padx=5
)


# ============================================================
# Footer
# ============================================================

status_label = tk.Label(
    root,
    text="AyyoOS notifications ready 🔔",
    font=("Sans", 9),
    bg=PANEL,
    fg=TEXT,
    pady=10
)

status_label.pack(
    side="bottom",
    fill="x"
)


refresh_notifications()

root.mainloop()
