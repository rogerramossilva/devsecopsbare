from flask import Flask, request, jsonify, redirect
from auth import check_auth, login_user
from utils import fetch_external_url, simulate_sql_search
import json

app = Flask(__name__)

with open('db.json') as f:
    db = json.load(f)

@app.route('/')
def index():
    return jsonify({"message": "API Vulnerável ativa"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    token = login_user(username, password)
    if token:
        return jsonify({"token": token})
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    auth_header = request.headers.get('Authorization')
    current_user = check_auth(auth_header)
    if current_user:
        for user in db['users']:
            if user['id'] == user_id:
                return jsonify(user)
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"error": "Não autorizado"}), 403

@app.route('/fetch-url', methods=['POST'])
def fetch_url():
    data = request.json
    url = data.get('url')
    content = fetch_external_url(url)
    return jsonify({"result": content})

@app.route('/search')
def search():
    query = request.args.get('query')
    results = simulate_sql_search(query)
    return jsonify({"results": results})

@app.route('/comment', methods=['POST'])
def comment():
    data = request.json
    comment = data.get('comment')
    db['comments'].append(comment)
    return jsonify({"message": "Comentário recebido", "comment": comment})

@app.route('/change-email', methods=['POST'])
def change_email():
    email = request.form.get('email')
    db['users'][0]['email'] = email
    return jsonify({"message": f"Email alterado para {email}"})

if __name__ == '__main__':
    app.run(debug=True)