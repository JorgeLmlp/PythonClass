from flask import Flask, render_template, request, make_response
from funcs import User, Cadastro

app = Flask(__name__)

def registerScreen(mensagem = None):
    return render_template('register.html', mensagem = mensagem)
def loginScreen(mensagem = None):
    return render_template('login.html', mensagem = mensagem)

def register():
    username = request.form.get('user')
    password = request.form.get('password')
    newUser = User(username, password)
    if not username or not password:
        return make_response(registerScreen('Por favor, preencha todos os campos.'), 400)

    mensagem, status = Cadastro.registrar(newUser)
    return make_response(registerScreen(mensagem), status)

def login():
    username = request.form.get('user')
    password = request.form.get('password')
    user = User(username, password)
    if not username or not password:
        return make_response(loginScreen('Por favor, preencha todos os campos.'), 400)

    mensagem, status = Cadastro.login(user)
    return make_response(loginScreen(mensagem), status)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/register', methods = ['GET', 'POST'])
def registerPage():
    if request.method == 'POST':
        return register()
    return registerScreen()
@app.route('/login', methods = ['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        return login()
    return loginScreen()    

if __name__ == '__main__':
    app.run(debug=True)
    