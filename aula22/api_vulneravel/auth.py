import jwt
from datetime import datetime, timedelta

SECRET = "segredo123"

def login_user(username, password):
    # bypass se user for admin (sem senha)
    if username == "admin" and (not password or password == "admin"):
        token = jwt.encode({
            "user": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }, SECRET, algorithm="HS256")
        return token
    return None

def check_auth(auth_header):
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ")[1]
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return decoded['user']
    except:
        return None