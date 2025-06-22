import requests

def fetch_external_url(url):
    try:
        response = requests.get(url, timeout=2)
        return response.text[:300]  # limita a resposta
    except:
        return "Erro ao buscar URL"

def simulate_sql_search(query):
    produtos = ["livro", "caneta", "caderno"]
    if "'" in query or "--" in query:
        return produtos  # simula SQLi
    return [p for p in produtos if query.lower() in p]