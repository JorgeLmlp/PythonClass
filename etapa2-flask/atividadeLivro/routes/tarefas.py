from flask import Blueprint
from controllers.tarefas_controller import (
<<<<<<< HEAD
    concluirTarefa,
=======
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    listarTarefas,
    criarTarefa,
    editarTarefa,
    excluirTarefa,
<<<<<<< HEAD
    criarTarefa
=======
    concluirTarefa,
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
)


tarefas_bp = Blueprint(
    "tarefas_bp",
    __name__
)

tarefas_bp.route(
    "/tarefa/nova",
    methods=["GET", "POST"]
)(criarTarefa)

<<<<<<< HEAD
=======

>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
tarefas_bp.route(
    "/tarefa/concluir/<int:id>",
    methods=["POST"]
)(concluirTarefa)


tarefas_bp.route(
    "/dashboard"
)(listarTarefas)


tarefas_bp.route(
<<<<<<< HEAD
    "/tarefa/nova",
    methods=["GET", "POST"]
)(criarTarefa)


tarefas_bp.route(
=======
>>>>>>> 10736b3e2e96a3798075d0e80a3982922c396d7b
    "/tarefa/editar/<int:id>",
    methods=["GET", "POST"]
)(editarTarefa)


tarefas_bp.route(
    "/tarefa/excluir/<int:id>"
)(excluirTarefa)