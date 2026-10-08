#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime
from pathlib import Path
import random
import getpass

ROOT = Path.home() / "AyyoOS"

BG = "#101015"
CARD = "#1d1d27"
TEXT = "#ffffff"
MUTED = "#b8b8c6"
ACCENT = "#6ee7b7"

MESSAGES = [
    "Oreyy! Welcome back ra 😂",
    "Password marchipoyava? Just kidding 😎",
    "AyyoOS ready undi boss!",
    "Your PC Has a Personality.",
    "Work cheddama? Leda comedy aa? 😂"
]


class AyyoLock:
    def __init__(self, root):
        self.root = root
        self.root.title("AyyoOS Lock Screen Preview")
        self.root.geometry("900x600")
        self.root.minsize(650, 450)
        self.root.configure(bg=BG)

        self.build_ui()
        self.update_clock()

    def build_ui(self):
        container = tk.Frame(self.root, bg=BG)
        container.pack(expand=True, fill="both")

        tk.Label(
            container,
            text="😂 AyyoOS",
            font=("Sans", 30, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(pady=(55, 8))

        tk.Label(
            container,
            text="Your PC Has a Personality.",
            font=("Sans", 12),
            bg=BG,
            fg=MUTED
        ).pack()

        self.clock_label = tk.Label(
            container,
            text="",
            font=("Sans", 56, "bold"),
            bg=BG,
            fg=TEXT
        )
        self.clock_label.pack(pady=(35, 0))

        self.date_label = tk.Label(
            container,
            text="",
            font=("Sans", 15),
            bg=BG,
            fg=MUTED
        )
        self.date_label.pack(pady=(0, 25))

        card = tk.Frame(
            container,
            bg=CARD,
            padx=35,
            pady=22
        )
        card.pack()

        tk.Label(
            card,
            text="👤 " + getpass.getuser(),
            font=("Sans", 17, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(pady=8)

        self.message_label = tk.Label(
            card,
            text=random.choice(MESSAGES),
            font=("Sans", 12),
            bg=CARD,
            fg=MUTED
        )
        self.message_label.pack(pady=12)

        tk.Button(
            card,
            text="🔓 Enter AyyoOS",
            font=("Sans", 13, "bold"),
            bg=ACCENT,
            fg="#101015",
            padx=25,
            pady=10,
            bd=0,
            command=self.unlock
        ).pack(pady=12)

        tk.Label(
            container,
            text="AyyoLock v0.1 • Interface Preview Only",
            font=("Sans", 10),
            bg=BG,
            fg=MUTED
        ).pack(pady=25)

    def update_clock(self):
        now = datetime.now()

        self.clock_label.config(
            text=now.strftime("%I:%M %p")
        )

        self.date_label.config(
            text=now.strftime("%A, %d %B %Y")
        )

        self.root.after(1000, self.update_clock)

    def unlock(self):
        print("😂 AyyoLock preview closed!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AyyoLock(root)
    root.mainloop()
