from flask_sqlalchemy import SQLAlchemy
from .base import ModeloBase
from .coleta_noticia import ColetaNoticia
from .noticia import Noticia

__all__ = ["ColetaNoticia", "Noticia"]
