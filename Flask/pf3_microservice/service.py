from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", time=datetime.utcnow().isoformat() + "Z"), 200

@app.post("/echo")
def echo():
    # verwacht JSON body
    data = request.get_json(silent=True)
    if data is None:
        return jsonify(error="Please send JSON body"), 400

    # microservice doet “iets”: voegt server_time toe
    data["server_time"] = datetime.utcnow().isoformat() + "Z"
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060)
