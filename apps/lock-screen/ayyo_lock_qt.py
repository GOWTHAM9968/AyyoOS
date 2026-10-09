#!/usr/bin/env python3

import sys
from pathlib import Path
import random
import getpass
from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPixmap, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)

MESSAGES = [
    "Welcome back ra boss! 😎",
    "Work cheddama? Leda comedy aa? 😂",
    "AyyoOS ready undi!",
    "Same PC... Different Vibes!",
    "Your PC Has a Personality."
]


class AyyoLock(QWidget):

    def __init__(self):
        super().__init__()

        self.wallpaper = QPixmap(
            str(
                Path.home()
                / "AyyoOS"
                / "branding"
                / "wallpapers"
                / "ayyoos-comedy-main.png"
            )
        )

        # AYYO_FULLSCREEN_V03
        self.setWindowTitle("AyyoOS — Cinematic Lock Preview")
        self.setMinimumSize(750, 550)
        self.resize(1100, 720)
        self.setMinimumSize(750, 550)

        self.setStyleSheet("""
            QWidget {
                color: white;
                font-family: Sans;
            }

            QLabel {
                background: transparent;
            }

            QLabel {
                background: transparent;
            }

              QFrame#loginCard {
              background-color: rgba(18, 20, 42, 185);
              border: 1px solid rgba(255, 255, 255, 90);
              border-radius: 28px;
            }

QPushButton#enterButton {
    background-color: #7555e8;
    color: white;
    border: 1px solid #a99aff;
    border-radius: 16px;
    padding: 16px 35px;
    font-size: 16px;
    font-weight: bold;
}

QPushButton#enterButton:hover {
    background-color: #977bff;
}

QPushButton#enterButton:pressed {
    background-color: #5140ad;
}
            QPushButton#enterButton:hover {
                background-color: #818cf8;
            }
        """)

        main = QVBoxLayout(self)
        main.setContentsMargins(40, 25, 40, 25)
        main.setSpacing(12)

        header = QHBoxLayout()

        logo = QLabel("😂 AyyoOS")
        logo.setStyleSheet(
            "font-size: 30px; font-weight: bold;"
        )

        tagline = QLabel("Your PC Has a Personality.")
        tagline.setStyleSheet(
            "font-size: 14px; color: #b8b8d8;"
        )

        brand = QVBoxLayout()
        brand.addWidget(logo)
        brand.addWidget(tagline)

        header.addLayout(brand)
        header.addStretch()

        version = QLabel("AyyoLock v0.2")
        version.setStyleSheet("color: #aaaacc;")
        header.addWidget(version)

        main.addLayout(header)
        main.addStretch()

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setStyleSheet(
            "font-size: 76px; font-weight: bold;"
        )
        main.addWidget(self.clock)

        self.date = QLabel()
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setStyleSheet(
            "font-size: 20px; color: #ddddff;"
        )
        main.addWidget(self.date)

        main.addSpacing(24)

        center = QHBoxLayout()
        center.addStretch()

        card = QFrame()
        card.setObjectName("loginCard")
        card.setFixedWidth(420)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(35, 30, 35, 30)
        card_layout.setSpacing(16)

        avatar = QLabel("👤")
        avatar.setAlignment(Qt.AlignCenter)
        avatar.setStyleSheet("font-size: 60px;")
        card_layout.addWidget(avatar)

        username = QLabel(getpass.getuser())
        username.setAlignment(Qt.AlignCenter)
        username.setStyleSheet(
            "font-size: 23px; font-weight: bold;"
        )
        card_layout.addWidget(username)

        self.message = QLabel(random.choice(MESSAGES))
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setStyleSheet(
            "font-size: 14px; color: #ccccdd;"
        )
        card_layout.addWidget(self.message)
        enter = QPushButton("🔓 Enter AyyoOS")
        enter.setObjectName("enterButton")
        enter.clicked.connect(self.close)
        card_layout.addWidget(enter)

        center.addWidget(card)
        center.addStretch()

        main.addLayout(center)
        main.addStretch()

        footer = QLabel(
            "😂 AyyoOS • Same PC, Different Vibes • Preview Mode"
        )
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet(
            "font-size: 12px; color: #9999bb;"
        )
        main.addWidget(footer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()
        self.message_timer = QTimer(self)
        self.message_timer.timeout.connect(self.change_message)
        self.message_timer.start(6000)

    def paintEvent(self, event):
        painter = QPainter(self)

        if not self.wallpaper.isNull():
            scaled = self.wallpaper.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            x = (scaled.width() - self.width()) // 2
            y = (scaled.height() - self.height()) // 2

            painter.drawPixmap(
                self.rect(),
                scaled,
                scaled.rect().adjusted(
                    x,
                    y,
                    -(scaled.width() - self.width() - x),
                    -(scaled.height() - self.height() - y)
                )
            )
        else:
            painter.fillRect(
                self.rect(),
                QColor("#101025")
            )

        # Dark overlay for readable text.
        painter.fillRect(
            self.rect(),
            QColor(8, 10, 30, 130)
        )

        painter.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_F11:
            self.setWindowState(
                self.windowState() ^ Qt.WindowFullScreen
            )
        else:
            super().keyPressEvent(event)

    def change_message(self):
        self.message.setText(random.choice(MESSAGES))

    def update_clock(self):
        now = datetime.now()
        self.clock.setText(now.strftime("%I:%M %p"))
        self.date.setText(now.strftime("%A, %d %B %Y"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AyyoLock()
    window.showFullScreen()
    sys.exit(app.exec())
