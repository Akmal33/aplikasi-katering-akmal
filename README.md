# Catering Expense and Income Tracking System

A comprehensive system for tracking catering business finances with multiple platform support:

1. **Web Application (PWA)** - Progressive Web App that can be installed on any device
2. **Mobile Application** - Android app built with Kivy
3. **Desktop Application** - Console and GUI versions for desktop use

## Features

- Track daily income and expenses
- Automatic balance calculation
- Excel export functionality
- Multi-platform support (Web, Mobile, Desktop)
- Real-time financial reporting

## System Architecture

### 1. Progressive Web App (PWA)
- Built with Flask, HTML5, CSS3, and JavaScript
- Installable on any device
- Offline support with service workers
- Responsive design for all screen sizes

### 2. Mobile Application
- Built with Kivy and Python
- Packaged as Android APK using Buildozer
- Native mobile experience
- Touch-friendly interface

### 3. Desktop Applications
- Console version for quick operations
- GUI version with Tkinter
- Excel integration for data storage

## Installation

### Web Application (PWA)
```bash
pip install -r requirements.txt
python app.py
```

### Mobile Application
```bash
# Requires Linux environment
pip install buildozer
buildozer android debug
```

### Desktop Applications
```bash
# Run console version
python console_demo.py

# Run GUI version
python catering_finance_tracker.py
```

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Mobile**: Kivy, Buildozer
- **Data Storage**: Excel (openpyxl)
- **PWA Features**: Service Workers, Web App Manifest

## License

This project is licensed under the MIT License - see the LICENSE file for details.