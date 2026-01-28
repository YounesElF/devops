from flask import Flask, request, jsonify
import sqlite3
import os
import datetime

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "/data/notes.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_utc TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.get("/health")
def health():
    return jsonify(status="ok", db=DB_PATH)

@app.post("/notes")
def add_note():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()

    if not text:
        return jsonify(error="Provide JSON: {'text': '...'}"), 400

    created_utc = datetime.datetime.utcnow().isoformat() + "Z"

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (text, created_utc) VALUES (?, ?)", (text, created_utc))
    conn.commit()
    note_id = cur.lastrowid
    conn.close()

    return jsonify(id=note_id, text=text, created_utc=created_utc), 201

@app.get("/notes")
def list_notes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, text, created_utc FROM notes ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    notes = [{"id": r[0], "text": r[1], "created_utc": r[2]} for r in rows]
    return jsonify(notes=notes)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5050)

