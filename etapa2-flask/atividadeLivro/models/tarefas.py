from database import db
class Tarefas(db.Model):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)
    titulo = db.Column(db.String(255), nullable = False)
    descricao = db.Column(db.Text, nullable = False)
    status = db.Column(db.Boolean(), default = False)
    
    