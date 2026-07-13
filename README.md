# 🛡️ SentinelOS

SentinelOS is a Flask-based cybersecurity utility dashboard that combines file risk checks, SHA-256 hashing, file integrity verification, password strength analysis, and scan history management in a single web application.

The project was built to explore practical concepts in cybersecurity utilities, cryptographic hashing, backend development, database operations, and responsive web application design.

---

## ✨ Features

### 📁 File Scanner
- Scans uploaded files based on potentially risky file extensions.
- Classifies scan records as `Safe` or `Dangerous`.
- Stores scan results in an SQLite database.
- Records the date and time of each scan.

> **Note:** The current scanner performs extension-based risk classification. It is not a full antivirus or malware-analysis engine.

### 🔐 SHA-256 Hash Generator
- Generates a SHA-256 hash for an uploaded file.
- Uses Python's `hashlib` library.
- Provides a unique cryptographic digest that can be used for file verification.

### 🛡️ File Integrity Checker
- Generates the current SHA-256 hash of an uploaded file.
- Compares it with a previously generated hash.
- Detects whether the file content has changed.

### 🔑 Password Strength Checker
- Evaluates passwords using multiple criteria:
  - Minimum length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Classifies passwords as Weak, Medium, or Strong.

### 📞 Phone Number Validator
- Validates whether the entered phone number contains exactly 10 digits.

### 📜 Scan History
- Stores file scan records in SQLite.
- Displays file name, status, and scan timestamp.
- Supports complete CRUD-related operations:
  - Create scan records
  - Read scan history
  - Update scan status
  - Delete individual records
- Supports clearing the complete scan history.

### 📊 Security Dashboard
- Displays:
  - Total scans
  - Safe files
  - Dangerous files
- Statistics are dynamically calculated from the SQLite database.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Hashing:** SHA-256 using Python `hashlib`
- **Version Control:** Git and GitHub

---

## 📂 Project Structure

```text
SentinelOS/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── Templates/
    ├── index.html
    ├── scanner.html
    ├── phone.html
    ├── password.html
    ├── history.html
    ├── hash.html
    └── integrity.html
    ⚙️ Installation and Setup
1. Clone the repository
git clone https://github.com/ShipraSharma08/Sentine1OS.git
cd SentinelOS
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
python app.py
6. Open the application
Open the local address displayed by Flask in your browser, typically:
http://127.0.0.1:5000
The SQLite database and required scan_history table are initialized automatically when the application starts.
🔍 How File Integrity Verification Works
Upload a file to the SHA-256 Hash Generator.
Generate and save its SHA-256 hash.
Later, upload the file to the File Integrity Checker.
Enter the original SHA-256 hash.
SentinelOS generates the file's current hash and compares both values.
Matching hashes indicate that the file content has not changed.
🎯 What I Learned
While building SentinelOS, I worked with:
Flask routing and form handling
File uploads in a web application
SHA-256 cryptographic hashing
File integrity verification
SQLite database operations
CRUD functionality
Dynamic dashboard statistics
Responsive UI design
Git and GitHub version control
⚠️ Project Scope
SentinelOS is an educational cybersecurity utility project.
The file scanner currently uses extension-based risk classification and should not be considered a replacement for a production antivirus or malware-analysis engine.
🚀 Possible Future Improvements
File hash reputation checking using a trusted threat-intelligence API
Network security utilities
Authentication and user-specific scan history
Advanced file analysis
Search and filtering for scan history
Production deployment
👤 Author
Shipra Sharma
B.Tech Pursuing in IT,Interested in Networking and Information security
