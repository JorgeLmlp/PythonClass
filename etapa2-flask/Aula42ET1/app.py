from flask import Flask, render_template, request
from funcs import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

def registerScreen():
    return render_template('register.html')

def register():
        username =  request.form.get('user')
        password = request.form.get('password')
        newUser = User(username, password)
        while not username or not password:
            return 'Por favor, preencha todos os campos.', 400
        
        Cadastro.registrar(newUser)
        mensagem = Cadastro.registrar(newUser)
        return mensagem

@app.route('/register', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        return register()
    return registerScreen()
    

if __name__ == '__main__':
    app.run(debug=True)
    