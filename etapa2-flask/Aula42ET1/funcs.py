import os
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PATH_JSON = os.path.join(DATA_DIR, 'usuarios.json')


class User:
    def __init__(self, user : str, password : str):
        self.user = user
        self.password = password



class Cadastro:
    @staticmethod    
    def registrar(user : User):
        if not os.path.isdir(DATA_DIR):
            os.makedirs(DATA_DIR)
        dados = []
        
        if os.path.exists(PATH_JSON):
            with open(PATH_JSON, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                    if not isinstance(dados, list): 
                        dados = []
                except json.JSONDecodeError:
                    dados = []
                    
        userDict = {
            'user': user.user,
            'password' : user.password
        }
        for i in dados: 
            if i['user'] == userDict['user']:
                return 'usuario já existe', 409

        dados.append(userDict)
        with open(PATH_JSON, 'w', encoding='utf-8') as r:
            json.dump(dados, r, ensure_ascii=False, indent=4)
        return 'usuario registrado com sucesso', 200

    @staticmethod
    def login(user : User):
        dados = []
        if not os.path.exists(PATH_JSON):
            return 'usuario ou senha incorretos', 401
        with open(PATH_JSON, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
                if not isinstance(dados, list): 
                    return 'usuario ou senha incorretos', 401
            except json.JSONDecodeError:
                return 'usuario ou senha incorretos', 401
            
        for i in dados: 
            if i['user'] == user.user and i['password'] == user.password:
                return 'login bem sucedido', 200
        return 'usuario ou senha incorretos', 401           