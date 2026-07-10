from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- FILE SCANNER ----------------
@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


@app.route("/scan", methods=["POST"])
def scan():

    file = request.files["file"]

    if not file or file.filename == "":
        return render_template("scanner.html", result="❌ No file selected.")

    filename = file.filename.lower()

    dangerous = [".exe", ".bat", ".cmd", ".vbs", ".js", ".scr"]

    status = "Safe"
    message = f"🟢 Scan Complete! '{filename}' looks safe."

    for ext in dangerous:
        if filename.endswith(ext):
            status = "Dangerous"
            message = f"🔴 Warning! '{filename}' is a potentially dangerous file."
            break

    connection = sqlite3.connect("sentinel.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO scan_history(file_name, status) VALUES (?, ?)",
        (filename, status)
    )

    connection.commit()
    connection.close()

    return render_template("scanner.html", result=message)


# ---------------- PHONE VALIDATOR ----------------
@app.route("/phone")
def phone():
    return render_template("phone.html")


@app.route("/validate-phone", methods=["POST"])
def validate_phone():

    phone = request.form["phone"]

    if phone.isdigit() and len(phone) == 10:
        result = "✅ Valid Phone Number"
    else:
        result = "❌ Invalid Phone Number"

    return render_template("phone.html", result=result)


# ---------------- PASSWORD CHECKER ----------------
@app.route("/password")
def password():
    return render_template("password.html")


@app.route("/check-password", methods=["POST"])
def check_password():

    password = request.form["password"]

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if any(c in special for c in password):
        score += 1

    if score <= 2:
        result = "🔴 Weak Password"

    elif score <= 4:
        result = "🟡 Medium Password"

    else:
        result = "🟢 Strong Password"

    return render_template("password.html", result=result)


# ---------------- SCAN HISTORY ----------------
@app.route("/history")
def history():

    connection = sqlite3.connect("sentinel.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM scan_history")

    history = cursor.fetchall()

    connection.close()

    return render_template("history.html", history=history)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)