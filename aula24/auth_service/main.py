from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

app = FastAPI()
SECRET_KEY = "minha-chave-supersecreta"

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    if data.username != "maria" or data.password != "123":
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    payload = {
        "sub": data.username,
        "role": "admin" if data.username == "admin" else "user",
        "exp": datetime.utcnow() + timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
