#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk
import fcntl
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path.home() / "AyyoOS"
AYYO_PANEL = ROOT / "desktop" / "panel" / "ayyo_panel.py"
# AyyoOS Desktop single-instance protection
LOCK_FILE = Path("/tmp/ayyoos-desktop.lock")
lock_handle = open(LOCK_FILE, "w")

try:
    fcntl.flock(
        lock_handle,
        fcntl.LOCK_EX | fcntl.LOCK_NB
    )
except BlockingIOError:
    print("Ayyo Desktop already running boss 😂")
    sys.exit(0)


SETTINGS = ROOT / "apps" / "settings" / "ayyo_settings.py"
SYSTEM_CENTER = ROOT / "apps" / "system-center" / "ayyo_system_center.py"
NOTIFICATIONS = (
    ROOT / "apps" / "notification-center" / "ayyo_notification_center.py"
)

BG = "#101015"
TEXT = "#ffffff"
MUTED = "#b7b7c2"


def launch(command):
    try:
        subprocess.Popen(command)
    except Exception as error:
        print(f"Ayyo launch error: {error}")

def start_ayyo_panel():
    """Start AyyoPanel if it is not already running."""
    try:
        result = subprocess.run(
            ["pgrep", "-f", "[a]yyo_panel.py"],
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode == 0:
            print("😂 AyyoPanel already running!")
            return

        if AYYO_PANEL.exists():
            subprocess.Popen(
                ["python3", str(AYYO_PANEL)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print("😂 AyyoPanel started!")

    except Exception as error:
        print(f"AyyoPanel startup warning: {error}")


def open_files():
    launch(["nautilus"])


def open_browser():
    """Open the default browser."""
    if shutil.which("xdg-open"):
        launch(["xdg-open", "https://www.google.com"])
    elif shutil.which("firefox"):
        launch(["firefox", "https://www.google.com"])
    else:
        print("Ayyo! No browser launcher found 😂")


def open_terminal():
    """Open an available terminal emulator."""
    for terminal in (
        "kgx",
        "gnome-terminal",
        "x-terminal-emulator",
        "xfce4-terminal",
        "xterm"
    ):
        if shutil.which(terminal):
            launch([terminal])
            return

    print("Ayyo! No terminal emulator found 😂")


def open_settings():
    launch(["python3", str(SETTINGS)])


def open_system_center():
    launch(["python3", str(SYSTEM_CENTER)])


def open_notifications():
    launch(["python3", str(NOTIFICATIONS)])


def open_trash():
    launch(["nautilus", "trash:///"])


root = tk.Tk()

root.title("AyyoOS Desktop")
root.configure(bg=BG)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Leave room for AyyoPanel at the top.
root.geometry(f"{width - 80}x{height - 130}+20+65")
# Let the Linux window manager manage the desktop.
root.overrideredirect(False)
root.attributes("-topmost", False)

# Main AyyoOS desktop container
desktop = tk.Frame(root, bg=BG)
desktop.pack(fill="both", expand=True)
# AyyoOS official desktop wallpaper

wallpaper_path = (
    ROOT / "branding" / "wallpapers" / "ayyoos-comedy-main.png"
)

if wallpaper_path.exists():
    image = Image.open(wallpaper_path).convert("RGB")
    image = image.resize(
        (width, height - 48),
        Image.Resampling.LANCZOS
    )

    wallpaper_photo = ImageTk.PhotoImage(image)

    wallpaper_label = tk.Label(
        desktop,
        image=wallpaper_photo,
        borderwidth=0
    )

    wallpaper_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    wallpaper_label.lower()


# ------------------------------------------------------------
# Branding
# ------------------------------------------------------------

brand = tk.Label(
    desktop,
    text="😂 AyyoOS",
    font=("Sans", 28, "bold"),
    bg=BG,
    fg=TEXT
)

brand.place(relx=0.5, rely=0.08, anchor="center")


tagline = tk.Label(
    desktop,
    text="Your PC Has a Personality.",
    font=("Sans", 12),
    bg=BG,
    fg=MUTED
)

tagline.place(relx=0.5, rely=0.13, anchor="center")


# ------------------------------------------------------------
# Desktop shortcuts
# ------------------------------------------------------------
shortcut_area = tk.Frame(
    desktop,
    bg=BG
)

shortcut_area.place(
    x=20,
    y=25
)
def shortcut(icon, name, command, row):
    # Fixed-size shortcut tile with stable hover behavior.
    item = tk.Frame(
        shortcut_area,
        bg=BG,
        width=120,
        height=88,
        highlightthickness=0
    )

    item.grid(
        row=row,
        column=0,
        padx=8,
        pady=4
    )

    item.grid_propagate(False)

    icon_label = tk.Label(
        item,
        text=icon,
        font=("Sans", 28),
        bg=BG,
        fg=TEXT
    )
    icon_label.pack(pady=(4, 0))

    name_label = tk.Label(
        item,
        text=name,
        font=("Sans", 10),
        bg=BG,
        fg=TEXT
    )
    name_label.pack()

    def set_highlight(active):
        color = "#292935" if active else BG
        for widget in (item, icon_label, name_label):
            widget.configure(bg=color)

    def on_enter(event):
        set_highlight(True)

    def on_leave(event):
        # Delay clearing so moving between child widgets
        # does not cause hover flickering.
        def check_pointer():
            x, y = item.winfo_pointerxy()
            left = item.winfo_rootx()
            top = item.winfo_rooty()

            inside = (
                left <= x < left + item.winfo_width()
                and top <= y < top + item.winfo_height()
            )

            set_highlight(inside)

        item.after(20, check_pointer)

    for widget in (item, icon_label, name_label):
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        widget.bind(
            "<Double-Button-1>",
            lambda event, action=command: action()
        )


shortcut("💻", "This PC", open_files, 0)
shortcut("📁", "AyyoFiles", open_files, 1)
shortcut("🌐", "Browser", open_browser, 2)
shortcut("⌨️", "Terminal", open_terminal, 3)
shortcut("⚙️", "Settings", open_settings, 4)
shortcut("🗑️", "Trash", open_trash, 5)


# ------------------------------------------------------------
# Right-click desktop menu
# ------------------------------------------------------------

menu = tk.Menu(
    root,
    tearoff=0,
    bg="#18181f",
    fg=TEXT,
    activebackground="#30303a",
    activeforeground=TEXT
)

menu.add_command(
    label="📁 Open AyyoFiles",
    command=open_files
)

menu.add_command(
    label="⌨️ Open Terminal",
    command=open_terminal
)

menu.add_separator()

menu.add_command(
    label="⚙️ AyyoSettings",
    command=open_settings
)

menu.add_command(
    label="💻 System Center",
    command=open_system_center
)

menu.add_command(
    label="🔔 Notifications",
    command=open_notifications
)

menu.add_separator()

menu.add_command(
    label="😂 Refresh Ayyo Desktop",
    command=lambda: print("Desktop fresh ayindi boss 😂")
)


def show_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


desktop.bind("<Button-3>", show_menu)


# ------------------------------------------------------------
# Clock / welcome area
# ------------------------------------------------------------

welcome = tk.Label(
    desktop,
    text="",
    font=("Sans", 11),
    bg=BG,
    fg=MUTED
)

welcome.place(
    relx=0.98,
    rely=0.96,
    anchor="se"
)


def update_status():
    now = datetime.now()

    welcome.config(
        text=(
            "AyyoOS 0.1 Alpha  •  "
            + now.strftime("%A, %d %B")
        )
    )

   # root.after(60000, update_status)


update_status()
def configure_desktop_layer():
    try:
        subprocess.run(
            [
                "wmctrl",
                "-r",
                "AyyoOS Desktop",
                "-b",
                "add,below,sticky"
            ],
            check=False,
            timeout=3
        )

        subprocess.run(
            [
                "wmctrl",
                "-r",
                "AyyoOS Desktop",
                "-b",
                "add,skip_taskbar,skip_pager"
            ],
            check=False,
            timeout=3
        )

        print("😂 Ayyo Desktop layering configured")

    except Exception as error:
        print(f"Desktop layering warning: {error}")


root.after(1000, configure_desktop_layer)
# Start AyyoPanel alongside the desktop.
root.after(1000, start_ayyo_panel)

# Escape closes the desktop during development.
root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()
