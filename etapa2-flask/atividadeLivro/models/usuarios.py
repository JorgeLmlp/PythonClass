from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    nome = db.Column(db.String(50) , nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    senha = db.Column(db.String(255), nullable = False)
    
    def mascararCampos(self):
        if not "@" in self.email:
            return ("email invalido")
        if not ".com" in self.email:
            return("email deve conter @dominio.com")
        self.senha = generate_password_hash(self.senha)
    def verificarSenha(self, senha_digitada):
        return check_password_hash(self.senha, senha_digitada)
        
        
