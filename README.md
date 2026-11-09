# 😂 AyyoOS v0.1
### Your PC Has a Personality!

**A custom Linux desktop experience built with Python, creativity, and a touch of comedy.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Ubuntu-orange)
![UI](https://img.shields.io/badge/UI-Tkinter-green)
![Version](https://img.shields.io/badge/Version-v0.1-gold)
![Status](https://img.shields.io/badge/Status-Development_Preview-yellow)

---

## 🌟 About AyyoOS

AyyoOS is an experimental desktop application project developed by **Vaddi Gowtham**, a B.Tech Cyber Security student.

The project aims to transform a traditional Linux desktop into a fun, interactive, and personalized computing experience.

AyyoOS combines custom desktop components, graphical applications, visual effects, and humorous system messages.

**Our philosophy:** Computers should be useful, customizable, and entertaining.

> **Note:** AyyoOS is currently a Python-based desktop experience running on Ubuntu. It is not a standalone bootable operating system or a replacement for the Linux kernel.

---

## ✨ Key Features

### 🖥️ 1. Custom AyyoOS Desktop
- Personalized desktop interface
- Custom wallpapers and branding
- Floating application shortcuts
- Luxury Bronze glass-inspired design
- Desktop application integration

### 💎 2. Liquid Glass-Inspired UI
- Rounded glass-style application icons
- Bronze and champagne-gold accents
- Interactive hover effects
- Custom icon rendering using Pillow
- Wallpaper-inspired desktop styling

### 🚀 3. AyyoLauncher
- Custom application launcher
- Search functionality
- Application shortcuts
- Personality and language options
- Responsive, scrollable application grid

### 📁 4. AyyoFiles
- Custom file-manager interface
- File and directory navigation
- Desktop shortcut integration

### ⚙️ 5. AyyoSettings
- Custom settings interface
- Desktop personalization concepts
- System settings integration
- Personality configuration

### 😂 6. Comedy Engine
- Humorous system messages
- English and Telugu message resources
- Personality-based desktop experience

### 🔔 7. Notifications and Controls
- Custom notification components
- System status displays
- Control Center prototype

### 🪟 8. Internal Window Manager
- Draggable internal application windows
- Minimize and restore functionality
- Taskbar prototype
- Window switching experiments

The internal window manager operates inside an AyyoOS application window; Ubuntu continues to manage external application windows.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Tkinter | Desktop graphical interface |
| Pillow | Custom icon and image rendering |
| PySide6 | Selected application interfaces |
| Ubuntu Linux | Host operating system |
| JSON | Configuration and language resources |
| Bash | Startup scripts and automation |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
AyyoOS/
├── apps/
│   ├── files/
│   ├── settings/
│   └── power/
├── branding/
│   └── wallpapers/
├── comedy-engine/
├── config/
├── core/
│   └── bin/
├── desktop/
│   ├── launcher/
│   ├── shell/
│   ├── theme/
│   ├── panel/
│   ├── start-menu/
│   └── window-manager/
├── languages/
│   ├── english/
│   └── telugu/
├── system/
├── README.md
└── ayyo.conf
```

*Some components and scripts may differ between development branches.*

---

## 📥 Download and Installation

### Requirements

- Ubuntu Linux desktop
- Python 3
- Tkinter
- Pillow
- Git
- Additional Python packages for certain applications

### Step 1 — Install dependencies

```bash
sudo apt update
sudo apt install git python3 python3-tk python3-pil python3-pil.imagetk
```

### Step 2 — Clone the repository

```bash
git clone https://github.com/GOWTHAM9968/AyyoOS.git
cd AyyoOS
```

### Step 3 — Explore available components

```bash
find desktop apps -maxdepth 3 -name "*.py"
```

### Step 4 — Launch the desktop

For a checkout containing the desktop entry point:

```bash
python3 desktop/shell/ayyo_desktop.py
```

For a checkout containing the startup manager:

```bash
./start-ayyoos.sh
```

**Important:** The startup manager and some newer features may not yet be available on the public `main` branch. This is a development preview; check the available files before launching.

---

## 📸 Screenshots

Screenshots of the desktop, launcher, custom icons, and applications will be added as the interface is finalized.

Suggested gallery:

- AyyoOS Desktop
- Luxury Bronze Icons
- AyyoLauncher
- AyyoFiles
- AyyoSettings
- Control Center

---

## 🗺️ Development Roadmap

- [x] Initial project structure
- [x] Custom desktop prototype
- [x] Application launcher
- [x] English and Telugu message resources
- [x] Custom icon renderer
- [x] Internal window-management prototype
- [ ] Complete integration testing
- [ ] Improve wallpaper-aware glass effects
- [ ] Add automated dependency installation
- [ ] Improve responsive layouts
- [ ] Prepare tested release package
- [ ] Publish a stable downloadable release

---

## ⚠️ Known Limitations

AyyoOS is currently under active development.

- Some applications require additional dependencies.
- Visual effects may vary by display resolution.
- Not every experimental feature is integrated.
- Ubuntu manages external application windows.
- AyyoOS is not yet a standalone Linux distribution.
- Installation and startup workflows require further testing.

---

## 🤝 Contributions

Contributions, suggestions, bug reports, and UI improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Commit your work.
5. Open a pull request.

For bugs or suggestions, use the repository's GitHub Issues section.

---

## 👨‍💻 Developer

**Vaddi Gowtham**

B.Tech — Cyber Security

Interested in:
- Python development
- Linux customization
- Cybersecurity
- Desktop applications
- UI/UX development
- Open-source projects

**GitHub:** https://github.com/GOWTHAM9968

**Project:** https://github.com/GOWTHAM9968/AyyoOS

---

## 📜 License

The repository's license has not yet been confirmed.

Before describing AyyoOS as legally open-source or allowing redistribution under a particular license, add an appropriate `LICENSE` file.

---

## ⭐ Support AyyoOS

If you find AyyoOS interesting:

- Star the repository.
- Share feedback.
- Report bugs.
- Suggest new features.
- Contribute improvements.

### 😂 AyyoOS — Your PC Has a Personality!

**Developed with Python, creativity, and comedy by Vaddi Gowtham.**
