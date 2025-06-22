from flask import Flask, jsonify
from middleware import require_role

app = Flask(__name__)

@app.route("/users")
@require_role("admin")
def get_users():
    return jsonify(["maria", "joao", "ana"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
