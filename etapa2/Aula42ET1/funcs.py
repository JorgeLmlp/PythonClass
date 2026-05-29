import os
import json
from flask import request
BASE_DIR = r'H:\Python\etapa2\Aula42ET1'
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
        dados.append(userDict)
        
        
        with open(PATH_JSON, 'w', encoding= 'utf-8') as r:
            json.dump(dados, r, ensure_ascii=False, indent=4)
            return 'usuario registrado com sucesso'
            

    
           