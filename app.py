from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route("/")
def home():
    connection = sqlite3.connect("sentinel.db")
    cursor = connection.cursor()

    # Total number of scans
    cursor.execute("SELECT COUNT(*) FROM scan_history")
    total_scans = cursor.fetchone()[0]

    # Total safe files
    cursor.execute(
        "SELECT COUNT(*) FROM scan_history WHERE status = 'Safe'"
    )
    safe_files = cursor.fetchone()[0]

    # Total dangerous files
    cursor.execute(
        "SELECT COUNT(*) FROM scan_history WHERE status = 'Dangerous'"
    )
    dangerous_files = cursor.fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        total_scans=total_scans,
        safe_files=safe_files,
        dangerous_files=dangerous_files
    )


# ---------------- FILE SCANNER ----------------
@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


@app.route("/scan", methods=["POST"])
def scan():
    file = request.files.get("file")

    if not file or file.filename == "":
        return render_template(
            "scanner.html",
            result="❌ No file selected."
        )

    filename = file.filename.lower()

    dangerous = [
        ".exe",
        ".bat",
        ".cmd",
        ".vbs",
        ".js",
        ".scr"
    ]

    status = "Safe"
    message = f"🟢 Scan Complete! '{filename}' looks safe."

    for ext in dangerous:
        if filename.endswith(ext):
            status = "Dangerous"
            message = (
                f"🔴 Warning! '{filename}' "
                "is a potentially dangerous file."
            )
            break

    connection = sqlite3.connect("sentinel.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO scan_history(file_name, status) VALUES (?, ?)",
        (filename, status)
    )

    connection.commit()
    connection.close()

    return render_template(
        "scanner.html",
        result=message
    )


# ---------------- PHONE VALIDATOR ----------------
@app.route("/phone")
def phone():
    return render_template("phone.html")


@app.route("/validate-phone", methods=["POST"])
def validate_phone():
    phone_number = request.form.get("phone", "").strip()

    if phone_number.isdigit() and len(phone_number) == 10:
        result = "✅ Valid Phone Number"
    else:
        result = "❌ Invalid Phone Number"

    return render_template(
        "phone.html",
        result=result
    )


# ---------------- PASSWORD CHECKER ----------------
@app.route("/password")
def password():
    return render_template("password.html")


@app.route("/check-password", methods=["POST"])
def check_password():
    user_password = request.form.get("password", "")

    score = 0

    if len(user_password) >= 8:
        score += 1

    if any(c.isupper() for c in user_password):
        score += 1

    if any(c.islower() for c in user_password):
        score += 1

    if any(c.isdigit() for c in user_password):
        score += 1

    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if any(c in special for c in user_password):
        score += 1

    if score <= 2:
        result = "🔴 Weak Password"
    elif score <= 4:
        result = "🟡 Medium Password"
    else:
        result = "🟢 Strong Password"

    return render_template(
        "password.html",
        result=result
    )


# ---------------- SCAN HISTORY ----------------
@app.route("/history")
def history():
    connection = sqlite3.connect("sentinel.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM scan_history ORDER BY id DESC"
    )

    scan_history = cursor.fetchall()

    connection.close()

    return render_template(
        "history.html",
        history=scan_history
    )


# ---------------- SHA-256 HASH GENERATOR ----------------
@app.route("/hash")
def hash_page():
    return render_template("hash.html")


@app.route("/generate-hash", methods=["POST"])
def generate_hash():
    file = request.files.get("file")

    if not file or file.filename == "":
        return render_template(
            "hash.html",
            result="❌ No file selected."
        )

    filename = file.filename
    file_data = file.read()

    hash_value = hashlib.sha256(file_data).hexdigest()

    return render_template(
        "hash.html",
        filename=filename,
        hash_value=hash_value
    )


# ---------------- FILE INTEGRITY CHECKER ----------------
@app.route("/integrity")
def integrity():
    return render_template("integrity.html")


@app.route("/check-integrity", methods=["POST"])
def check_integrity():
    file = request.files.get("file")
    original_hash = request.form.get("original_hash", "").strip().lower()

    if not file or file.filename == "":
        return render_template(
            "integrity.html",
            result="❌ No file selected."
        )

    file_data = file.read()

    current_hash = hashlib.sha256(file_data).hexdigest()

    if current_hash == original_hash:
        result = "✅ File Integrity Verified — File has not been modified."
    else:
        result = "⚠️ File Modified — SHA-256 hashes do not match."

    return render_template(
        "integrity.html",
        current_hash=current_hash,
        result=result
    )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)