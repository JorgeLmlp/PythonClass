from flask import Flask
from database import db
import os

app = Flask(__name__)

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "banco.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.secret_key = "..."
from routes import user_bp, tarefas_bp
app.register_blueprint(user_bp)
app.register_blueprint(tarefas_bp)
db.init_app(app)

from models import Usuario, Tarefas

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()