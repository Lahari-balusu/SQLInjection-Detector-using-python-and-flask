# 🛡️ SQL Injection Detection System

A real-time **SQL Injection Detection System** built using **Python** and the **Flask** framework. This system aims to protect web applications from SQL injection attacks by analyzing user input for malicious patterns before they reach the database layer.

---

## 🌟 Overview

This project implements a lightweight yet powerful security layer for web applications by detecting potential SQL injection attempts using:

- 🔍 Pattern-based detection (via Regular Expressions)
- 🔐 Input validation and sanitization
- 🛠️ Secure query execution practices
- 🌐 Simple and user-friendly Flask-based web interface

Developed as part of a **final year project** by Computer Science & Engineering students.

---

## 🚀 Features

- Real-time SQL injection detection
- Alerts/logs suspicious input
- Configurable regex patterns for detection
- Clean and responsive UI
- Flask REST API support for integration

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Python, Flask
- **Security**: Regular expressions, input sanitization
- **Database**: SQLite (can be replaced with other RDBMS)

---


## 🛠 Installation Guide
### Prerequisites
- Python 3.8+
- pip package manager
- Git (optional)
  Setup Instructions
### Clone the repository:
```
git clone https://github.com/yourusername/sql-injection-detector.git
cd sql-injection-detector
```
**1.Create virtual environment (recommended):**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**2.Install dependencies:**
```
pip install -r requirements.txt
```
**3.Run the application:**
```
python app.py
```
**4.Access the web interface:**
Open your browser and navigate to:
```
http://localhost:5000
```
---
## 📌 Usage Instructions

### ▶️ Basic Operation

1. Launch the application and open your browser to:  
   **[http://localhost:5000](http://localhost:5000)**

2. In the web interface:
   - Enter **SQL queries** or **suspicious inputs** into the input field.
   - Click the **"Check"** button to analyze the input.

3. View the result of the analysis:
   - ✅ **Green**: Safe input  
   - ❌ **Red**: Potential SQL injection detected
---
## 🧪 Sample Testing

Try these test cases to verify detection:

| Input Type        | Sample Input                                        | Expected Result |
|-------------------|-----------------------------------------------------|------------------|
| Safe query        | `SELECT * FROM users WHERE id = 1`                  | ✅ Safe          |
| Classic SQLi      | `' OR 1=1 --`                                        | ❌ Malicious     |
| Union attack      | `UNION SELECT username, password FROM users`        | ❌ Malicious     |
| Tautology         | `admin' OR '1'='1`                                   | ❌ Malicious     |
