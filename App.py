
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from L.I.S.A. Insight backend!"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return jsonify({
        "summary": "This is where AI analysis will appear.",
        "status": "ready"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway port or default
    app.run(host="0.0.0.0", port=port)

