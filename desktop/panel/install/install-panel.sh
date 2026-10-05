#!/bin/bash

set -e

AYYO_ROOT="$HOME/AyyoOS"
AUTOSTART_DIR="$HOME/.config/autostart"
AUTOSTART_FILE="$AUTOSTART_DIR/ayyo-panel.desktop"

mkdir -p "$AUTOSTART_DIR"

cat > "$AUTOSTART_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=AyyoOS Desktop Panel
Comment=AyyoOS live desktop status panel
Exec=/usr/bin/python3 $AYYO_ROOT/desktop/panel/ayyo_panel.py
Terminal=false
X-GNOME-Autostart-enabled=true
StartupNotify=false
EOF

chmod +x "$AYYO_ROOT/desktop/panel/ayyo_panel.py"

echo "😂 AyyoPanel installed boss!"
echo "Autostart: $AUTOSTART_FILE"
