from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)
SECRET = "supersecret"

@app.route("/order/<int:order_id>")
def get_order(order_id):
    auth = request.headers.get("Authorization")
    try:
        token = jwt.decode(auth.split()[1], SECRET, algorithms=["HS256"])
        if token["user_id"] != order_id:
            return jsonify({"error": "Access denied"}), 403
    except Exception as e:
        print(f"Token inválido: {e}")
        return jsonify({"error": "Invalid token"}), 403
    return jsonify({"order_id": order_id, "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
