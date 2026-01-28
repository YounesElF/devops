from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", version=os.getenv("APP_VERSION", "dev"))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Belangrijk in containers: 0.0.0.0
    app.run(host="0.0.0.0", port=5555)
