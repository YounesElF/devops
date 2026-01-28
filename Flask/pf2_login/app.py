from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "login.db"

def db_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = db_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS USER_PLAIN (
            USERNAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL
        );
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS USER_HASH (
            USERNAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD_HASH TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def home():
    return "Pf2 login API running", 200

@app.route("/delete/all", methods=["DELETE"])
def delete_all():
    conn = db_conn()
    c = conn.cursor()
    c.execute("DELETE FROM USER_PLAIN;")
    c.execute("DELETE FROM USER_HASH;")
    conn.commit()
    conn.close()
    return "All users deleted\n", 200

@app.route("/signup/v1", methods=["POST"])
def signup_v1():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify(error="missing username/password"), 400

    conn = db_conn()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES (?, ?);",
            (username, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists (v1)\n", 409

    conn.close()
    return "Signup success (v1)\n", 200

@app.route("/login/v1", methods=["POST"])
def login_v1():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify(error="missing username/password"), 400

    conn = db_conn()
    c = conn.cursor()
    c.execute("SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME=?;", (username,))
    row = c.fetchone()
    conn.close()

    if row and row[0] == password:
        return "Login success (v1)\n", 200
    return "Login failed (v1) ❌\n", 401

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

@app.route("/signup/v2", methods=["POST"])
def signup_v2():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify(error="missing username/password"), 400

    pw_hash = sha256(password)

    conn = db_conn()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO USER_HASH (USERNAME, PASSWORD_HASH) VALUES (?, ?);",
            (username, pw_hash)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists (v2)\n", 409

    conn.close()
    return "Signup success (v2)\n", 200

@app.route("/login/v2", methods=["POST"])
def login_v2():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify(error="missing username/password"), 400

    pw_hash = sha256(password)

    conn = db_conn()
    c = conn.cursor()
    c.execute("SELECT PASSWORD_HASH FROM USER_HASH WHERE USERNAME=?;", (username,))
    row = c.fetchone()
    conn.close()

    if row and row[0] == pw_hash:
        return "Login success (v2)\n", 200
    return "Login failed (v2) ❌\n", 401

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5555, debug=True)
