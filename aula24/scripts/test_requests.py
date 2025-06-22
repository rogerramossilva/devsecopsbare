import requests

# 1. Login para obter token
login = requests.post("http://localhost:8000/login", json={
    "username": "maria",
    "password": "123"
})
token = login.json().get("access_token")
print("Token recebido:", token)

# 2. Acesso ao serviço de usuário
headers = {"Authorization": f"Bearer {token}"}
r1 = requests.get("http://localhost:8001/user", headers=headers)
print("User-Service:", r1.json())

# 3. Acesso ao serviço admin
r2 = requests.get("http://localhost:8002/admin", headers=headers)
print("Admin-Service:", r2.json())
