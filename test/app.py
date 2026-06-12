from flask import Flask, render_template, jsonify
from get_api import getDadosApi

app = Flask(__name__)

@app.route('/')
def main():
    return 'mainpage'


@app.route('/rickandmorty')
def rickandmorty():
    try:
        dados = getDadosApi()
    except ValueError:
        dados = None
        raise ValueError    
    return render_template('index.html', dados=dados)

@app.route('/api/rickandmorty', methods=['GET'])
def api_rickandmorty():
    dados = getDadosApi()
    return jsonify(dados), 200

if __name__ == "__main__":
    app.run()