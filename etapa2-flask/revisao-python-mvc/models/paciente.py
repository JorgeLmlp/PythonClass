from datetime import datetime
from database import db

class Paciente(db.Model):
    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    condicao_medica = db.Column(db.String(200), nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'condicao_medica': self.condicao_medica,
            'criado_em': self.criado_em
        }