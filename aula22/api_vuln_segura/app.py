
from flask import Flask, request, jsonify, g
import requests
from markupsafe import escape
from auth import require_auth, login_route
from data import get_user_by_id
from util import is_internal_address

app = Flask(__name__)
login_route(app)

@app.route("/users/<int:user_id>")
@require_auth
def get_user(user_id):
    if g.user["id"] != user_id:
        return jsonify({"message": "Acesso negado"}), 403
    user = get_user_by_id(user_id)
    return jsonify(user)

@app.route("/fetch-url", methods=["POST"])
def fetch_url():
    url = request.json.get("url")
    if is_internal_address(url):
        return jsonify({"message": "Endereço proibido"}), 403
    try:
        r = requests.get(url, timeout=3)
        return jsonify({"result": r.text[:200]})
    except:
        return jsonify({"error": "Erro ao buscar URL"}), 500

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    if not query.isalnum():
        return jsonify({"message": "Parâmetro inválido"}), 400
    results = [item for item in ["livro", "caneta", "caderno"] if query in item]
    return jsonify({"results": results})

@app.route("/comment", methods=["POST"])
def comment():
    comment = request.json.get("comment", "")
    sanitized = escape(comment)
    return jsonify({"message": "Comentário recebido", "comment": sanitized})

@app.route("/change-email", methods=["POST"])
@require_auth
def change_email():
    referer = request.headers.get("Referer", "")
    if not referer.startswith("http://localhost:5000"):
        return jsonify({"message": "CSRF bloqueado"}), 403
    new_email = request.form.get("email")
    return jsonify({"message": f"Email alterado para {new_email}"})

if __name__ == "__main__":
    app.run(debug=True)
