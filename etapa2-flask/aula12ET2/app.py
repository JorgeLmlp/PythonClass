from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    'decorators python'


@app.route('/decorator')
def decorator():
    return """
    Um decorator (decorador) em Python é uma função que recebe outra função como 
    argumento, estende seu comportamento sem modificá-la explicitamente e retorna uma nova função.Para que serveReutilização de código: 
    Evita duplicação de lógicas comuns.Separação de conceitos: Isola funções secundárias da lógica principal.Modificação limpa: Altera o comportamento de funções e
    xistentes de forma visualmente simples.Aplicações comuns: Criação de logs, controle de acesso (autenticação), medição de tempo de execução e cache de dados.Como 
    funciona na sintaxe PythonUtiliza-se o símbolo @ acima da definição da função que será modificada.

"""

if __name__ == '__main__':
    app.run(debug=True)
    
    