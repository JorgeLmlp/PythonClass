from flask import Blueprint
from controllers.user_controller import registraUsuario, loginUsuario

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/registro/usuario", methods=["GET", "POST"])(registraUsuario)
user_bp.route("/", methods=["GET", "POST"])(loginUsuario)