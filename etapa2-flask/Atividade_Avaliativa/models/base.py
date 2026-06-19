from . import db
class ModeloBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    