from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # remote_addr wordt ook in de slides gebruikt in de template
    client_ip = request.remote_addr
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", client_ip=client_ip, now=now)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
