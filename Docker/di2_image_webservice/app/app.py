from flask import Flask, jsonify, request
import os
import datetime

app = Flask(__name__)

@app.get("/")
def home():
    return f"Di2 webservice OK | your_ip={request.remote_addr}\n"

@app.get("/health")
def health():
    return jsonify(
        status="ok",
        time=datetime.datetime.utcnow().isoformat() + "Z",
        version=os.getenv("APP_VERSION", "dev")
    )

if __name__ == "__main__":
    # In Docker altijd luisteren op 0.0.0.0
    app.run(host="0.0.0.0", port=5050)
