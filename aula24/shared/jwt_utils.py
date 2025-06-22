import jwt
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

SECRET_KEY = "minha-chave-supersecreta"

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError()
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError()

class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, require_admin=False):
        super().__init__(app)
        self.require_admin = require_admin

    async def dispatch(self, request: Request, call_next):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Token não enviado"})

        token = auth.split(" ")[1]

        try:
            payload = decode_token(token)
        except jwt.ExpiredSignatureError:
            return JSONResponse(status_code=401, content={"detail": "Token expirado"})
        except jwt.InvalidTokenError:
            return JSONResponse(status_code=401, content={"detail": "Token inválido"})

        if self.require_admin and payload.get("role") != "admin":
            return JSONResponse(status_code=403, content={"detail": "Acesso restrito a admins"})

        request.state.user = payload
        return await call_next(request)
