from flask import render_template, request, redirect, session
from models.tarefas import Tarefas
from database import db


def listarTarefas():
<<<<<<< HEAD

=======
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")

    tarefas = Tarefas.query.filter_by(
        user_id=usuario_id
    ).all()

    return render_template(
        "dashboard.html",
        tarefas=tarefas
    )


<<<<<<< HEAD

def criarTarefa():

=======
def criarTarefa():
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")

<<<<<<< HEAD

    if request.method == "POST":

        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")


        tarefa = Tarefas(
            user_id=usuario_id,
            titulo=titulo,
            descricao=descricao
        )


        db.session.add(tarefa)
        db.session.commit()


        return redirect("/dashboard")


    return render_template("nova_tarefa.html")



def editarTarefa(id):

    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")


    tarefa = Tarefas.query.filter_by(
        id=id,
        user_id=usuario_id
    ).first()


    if not tarefa:
        return redirect("/dashboard")


    if request.method == "POST":

        tarefa.titulo = request.form.get("titulo")
        tarefa.descricao = request.form.get("descricao")
        tarefa.status = request.form.get("status") == "on"


        db.session.commit()

        return redirect("/dashboard")


    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa
    )



def excluirTarefa(id):

    usuario_id = session.get("usuario_id")


    if not usuario_id:
        return redirect("/")


    tarefa = Tarefas.query.filter_by(
        id=id,
        user_id=usuario_id
    ).first()


    if tarefa:

        db.session.delete(tarefa)
        db.session.commit()


    return redirect("/dashboard")

from flask import render_template, request, redirect, session
from models.tarefas import Tarefas
from database import db


def criarTarefa():

    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")


    if request.method == "POST":

        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")


=======
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")

>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
        tarefa = Tarefas(
            user_id=usuario_id,
            titulo=titulo,
            descricao=descricao,
            status=False
        )

<<<<<<< HEAD

        db.session.add(tarefa)
        db.session.commit()


        return redirect("/dashboard")


    return render_template("nova_tarefa.html")
def concluirTarefa(id):

=======
        db.session.add(tarefa)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("nova_tarefa.html")


def editarTarefa(id):
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")

<<<<<<< HEAD

=======
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    tarefa = Tarefas.query.filter_by(
        id=id,
        user_id=usuario_id
    ).first()

<<<<<<< HEAD

    if tarefa:

        tarefa.status = True

        db.session.commit()


        db.session.delete(tarefa)

        db.session.commit()


=======
    if not tarefa:
        return redirect("/dashboard")

    if request.method == "POST":
        tarefa.titulo = request.form.get("titulo")
        tarefa.descricao = request.form.get("descricao")
        tarefa.status = request.form.get("status") == "on"

        db.session.commit()

        return redirect("/dashboard")

    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa
    )


def excluirTarefa(id):
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")

    tarefa = Tarefas.query.filter_by(
        id=id,
        user_id=usuario_id
    ).first()

    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()

    return redirect("/dashboard")


def concluirTarefa(id):
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect("/")

    tarefa = Tarefas.query.filter_by(
        id=id,
        user_id=usuario_id
    ).first()

    if tarefa:
        tarefa.status = True
        db.session.commit()

        db.session.delete(tarefa)
        db.session.commit()

>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    return redirect("/dashboard")