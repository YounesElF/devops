cat > app.py << 'EOF'
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "JX1 no-git pipeline OK\n"

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
EOF

