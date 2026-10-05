#!/bin/bash

AUTOSTART_FILE="$HOME/.config/autostart/ayyo-panel.desktop"

if [ -f "$AUTOSTART_FILE" ]; then
    rm "$AUTOSTART_FILE"
    echo "AyyoPanel autostart removed."
else
    echo "AyyoPanel autostart already absent."
fi

pkill -f "ayyo_panel.py" 2>/dev/null || true

echo "😂 AyyoPanel stopped boss!"
