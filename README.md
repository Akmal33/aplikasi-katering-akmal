# Catering Expense and Income Tracking System

A comprehensive system for tracking catering business finances with multiple platform support:

1. **Web Application (PWA)** - Progressive Web App that can be installed on any device
2. **Mobile Application** - Android app built with Kivy
3. **Desktop Application** - GUI desktop application with Tkinter

## Features

- Track daily income and expenses
- Automatic balance calculation
- Local database storage (SQLite)
- Excel export functionality (optional)
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
- GUI version with Tkinter
- Local SQLite database for data storage
- Excel integration for data export

## Database Schema

The application uses SQLite as its local database with the following schema:

### Transactions Table
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    day TEXT NOT NULL,
    description TEXT NOT NULL,
    income REAL DEFAULT 0,
    expense REAL DEFAULT 0,
    balance REAL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Finance Summary Table
```sql
CREATE TABLE finance_summary (
    id INTEGER PRIMARY KEY,
    total_income REAL DEFAULT 0,
    total_expense REAL DEFAULT 0,
    current_balance REAL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Installation

### Prerequisites
```bash
pip install -r requirements.txt
```

### Web Application (PWA)
```bash
python app.py
```
Then open your browser to http://localhost:5000

### Mobile Application
```bash
# Requires Linux environment
pip install buildozer
buildozer android debug
```

### Desktop Application
```bash
python desktop_app.py
```

## Technology Stack

- **Backend**: Python, Flask, SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Mobile**: Kivy, Buildozer
- **Desktop**: Tkinter
- **Data Storage**: SQLite (primary), Excel (export)

## License

This project is licensed under the MIT License - see the LICENSE file for details.