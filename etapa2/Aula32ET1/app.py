from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
    dados = [
        {"nome": "Ana", "email": "ana@email.com", 'nota' : 7},
        {"nome": "joao", "email": "joao@email.com", 'nota' : 3}
        
             ]
    return render_template('index.html', dados = dados)

if __name__ == '__main__':
    app.run(debug = True)
