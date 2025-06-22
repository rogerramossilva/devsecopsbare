
from flask import request, jsonify, g
import jwt
from werkzeug.security import check_password_hash
from data import USERS
from config import SECRET_KEY

def require_auth(f):
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"message": "Token ausente"}), 401
        token = auth.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user = {"id": payload["id"]}
        except:
            return jsonify({"message": "Token inválido"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

def login_route(app):
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = USERS.get(username)
        if user and password and check_password_hash(user["password_hash"], password):
            token = jwt.encode({"id": user["id"]}, SECRET_KEY, algorithm="HS256")
            return jsonify({"token": token})
        return jsonify({"message": "Credenciais inválidas"}), 401
