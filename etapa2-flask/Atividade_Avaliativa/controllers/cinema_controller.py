from flask import Blueprint, redirect, render_template, request, url_for
from datetime import datetime
from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")
dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
def index():
    total_filmes = Filme.query.count()
    total_salas = Sala.query.count()
    total_sessoes = Sessao.query.count()
    return render_template(
        "dashboard/index.html",
        total_filmes=total_filmes,
        total_salas=total_salas,
        total_sessoes=total_sessoes,
    )


@cinema_bp.route("/")
def lista_sessoes():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()
    

    if request.method == "POST":
        nova_sessao = Sessao(
            filme_id=request.form["filme_id"],
            sala_id=request.form["sala_id"],
            data_hora=datetime.strptime(request.form["data_hora"], "%Y-%m-%dT%H:%M"),
            preco=float(request.form["preco"]),
        )
        db.session.add(nova_sessao)
        db.session.commit()
        return redirect(url_for("cinema.lista_sessoes"))
    
    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )