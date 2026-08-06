from flask import render_template, request, redirect, session
from models import Usuario
from database import db


def registraUsuario():

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha
        )

        erro = usuario.mascararCampos()

        if erro:
            return render_template("registro.html", erro=erro)

        db.session.add(usuario)
        db.session.commit()

        return redirect("/")

    return render_template("registro.html")


def loginUsuario():

    erro = None

    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.verificarSenha(senha):
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome

            return redirect("/dashboard")

        erro = "Email ou senha inválidos"

    return render_template("index.html", erro=erro)

