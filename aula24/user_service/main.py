import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Request
from shared.jwt_utils import JWTMiddleware

app = FastAPI()
app.add_middleware(JWTMiddleware)

@app.get("/user")
def get_user(request: Request):
    user = request.state.user
    return {"message": f"Olá {user['sub']}, você é um {user['role']}"}
