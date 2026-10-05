#!/bin/bash

AYYO_ROOT="$HOME/AyyoOS"

echo "😂 AyyoOS Branding"
echo "-------------------------"
echo "Your PC Has a Personality."
echo

if [ -f "$AYYO_ROOT/branding/identity.conf" ]; then
    echo "✓ AyyoOS identity found"
else
    echo "✗ AyyoOS identity missing"
    exit 1
fi

echo "✓ AyyoEngine project found"
echo "✓ Desktop layer ready"
echo
echo "AyyoOS branding system initialized 😂"
