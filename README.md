# 🧮 Academic Scientific Calculator | University Edition

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge&logo=python&logoColor=white)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None%20(Pure%20Standard%20Library)-brightgreen?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Theme](https://img.shields.io/badge/Theme-Catppuccin%20Mocha-mauve.svg?style=for-the-badge&logo=catppuccin&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)

A production-grade, high-precision desktop scientific calculator meticulously engineered for **STEM students, researchers, and professional engineers**. Built entirely using Python's native standard libraries with zero external pip dependencies, featuring a stunning modern dark UI, live constant tooltips, and robust mathematical expression evaluation.

</div>

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features & Capabilities](#-key-features--capabilities)
- [Project File Architecture](#-project-file-architecture)
- [Technical Deep Dive & Design Patterns](#-technical-deep-dive--design-patterns)
- [Built-In Physical & Chemical Constants Reference](#-built-in-physical--chemical-constants-reference)
- [Comprehensive Installation Guide](#-installation-guide)
- [Usage & Keyboard Shortcuts](#-keyboard-shortcuts)
- [Theming & Color Palette Specification](#-theming--color-palette-specification)
- [Troubleshooting & Common Issues](#-troubleshooting--common-issues)
- [Roadmap & Future Versions](#-roadmap--future-versions)
- [License](#-license)

---

## 🌟 About The Project

Traditional operating system calculators and generic web-based widgets often fall short when tackling rigorous university-level coursework in physics, physical chemistry, advanced calculus, and engineering mechanics. Students find themselves constantly switching between browser tabs to look up fundamental physical constants, converting angle modes manually, or dealing with poorly formatted outputs.

**Academic Scientific Calculator (University Edition)** was developed to bridge this gap. By combining an intuitive grid layout inspired by high-end hardware graphing calculators with a secure, highly optimized Python backend, this application provides an all-in-one computational environment right on your desktop. Best of all, because it relies exclusively on Python's built-in modules (`tkinter`, `math`, and `re`), it requires zero complex configuration, virtual environments, or external package installations.

---

## ✨ Key Features & Capabilities

### 1. ⚛️ Comprehensive Universal Constants Suite
Instantly insert fundamental physical and chemical constants into any calculation with a single button press. Each constant is hardcoded using its most precise internationally accepted CODATA values:
- **Thermodynamics & Statistical Mechanics:** Avogadro's Number ($N_A$), Universal Gas Constant ($R$), Boltzmann Constant ($k_B$).
- **Electromagnetism & Quantum Physics:** Speed of Light in Vacuum ($c$), Planck's Constant ($h$), Elementary Charge ($q_e$).
- **Mechanics & Gravitation:** Newtonian Gravitational Constant ($G$), Standard Acceleration due to Gravity ($g$).
- **Mathematical Constants:** Pi ($\pi$) and Euler's Number ($e$).

### 2. 🧠 Dynamic Interactive Status Bar & Tooltips
Never guess what a constant represents. Whenever you select a constant button, the live status bar at the top of the interface instantly updates to display the full name, exact decimal representation, and official SI unit of measurement.

### 3. 📐 Advanced Trigonometry & Angle Modes
- Seamlessly toggle between **Radians (RAD)** and **Degrees (DEG)** with a visual status indicator button.
- Full support for direct trigonometric functions (`sin`, `cos`, `tan`) and their respective inverse functions (`asin`, `acos`, `atan`) with automatic unit conversion handling behind the scenes.

### 4. 🔬 Scientific & Algebraic Functionality
- **Logarithms & Exponentials:** Natural logarithm (`ln`), base-10 logarithm (`log10`), exponential growth (`e^x`, `10^x`), and custom powers (`x^y`).
- **Roots & Powers:** Square roots ($\sqrt{x}$), cube roots ($\sqrt[3]{x}$), and square exponents ($x^2$).
- **Advanced Operations:** Factorials ($n!$) calculated dynamically via custom regular expression replacement, absolute value bars ($\vert{}x\vert{}$), percentage conversion (`%`), and scientific notation input (`EE`).
- **Memory Retention:** The `ANS` button allows you to instantly recall the result of your previous computation for chained problem-solving.

### 5. ⌨️ Dual Control Input System
- **Mouse Navigation:** Fully responsive grid layout with custom hover states and clean color-coded button grouping.
- **Hardware Keyboard Support:** Type directly using your physical keyboard (`0-9`, `+`, `-`, `*`, `/`, `(`, `)`, `%`), press `Enter` to evaluate, `Backspace` to delete characters, and `Escape` to clear the screen entirely.

---

## 📂 Project File Architecture

The repository is structured with modular clarity in mind:

```text
Academic-Scientific-Calculator/
│
├── calculator.py          # Main application script (GUI & Core logic)
├── README.md              # Comprehensive documentation (You are here)
└── LICENSE                # MIT Open Source license file
