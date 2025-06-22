
from werkzeug.security import generate_password_hash

USERS = {
    "admin": {"id": 1, "username": "admin", "password_hash": generate_password_hash("admin123")},
    "user": {"id": 2, "username": "user", "password_hash": generate_password_hash("user123")}
}

def get_user_by_id(uid):
    for user in USERS.values():
        if user["id"] == uid:
            return user
    return None
