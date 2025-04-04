# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import requests
import os

app = Flask(__name__)
CORS(app)  # Adicionar suporte a CORS

# URL do arquivo CSV específico
CSV_URL = 'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv'

def download_csv(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# Baixar o CSV se não existir
csv_filename = 'operadoras.csv'
if not os.path.exists(csv_filename):
    download_csv(CSV_URL, csv_filename)

# Carregar dados do CSV
try:
    df = pd.read_csv(csv_filename, sep=';', encoding='latin1', on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Erro ao ler o CSV: {e}")
    df = pd.DataFrame()  # Cria um DataFrame vazio em caso de erro

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        return jsonify(results.to_dict(orient='records'))
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)