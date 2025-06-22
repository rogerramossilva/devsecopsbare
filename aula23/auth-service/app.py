from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET = "supersecret"

@app.route("/token", methods=["POST"])
def generate_token():
    data = request.json
    token = jwt.encode({
        "user": data["user"],
        "role": data["role"],
        "user_id": data.get("user_id", 0),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    }, SECRET, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
