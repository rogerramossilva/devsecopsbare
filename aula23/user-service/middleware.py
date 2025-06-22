from flask import request, jsonify
import jwt

SECRET = "supersecret"

def require_role(role):
    def decorator(f):
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization")
            if not auth:
                return jsonify({"error": "No token"}), 403
            try:
                token = jwt.decode(auth.split()[1], SECRET, algorithms=["HS256"])
                if token["role"] != role:
                    return jsonify({"error": "Forbidden"}), 403
            except Exception as e:
                print(f"Token inválido: {e}")
                return jsonify({"error": "Invalid token"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
