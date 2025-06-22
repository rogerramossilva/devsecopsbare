import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Request
from shared.jwt_utils import JWTMiddleware

app = FastAPI()
app.add_middleware(JWTMiddleware, require_admin=True)

@app.get("/admin")
def get_admin(request: Request):
    user = request.state.user
    return {"message": f"Acesso concedido ao admin {user['sub']}"}
