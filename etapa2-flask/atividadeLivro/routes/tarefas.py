from flask import Blueprint
from controllers.tarefas_controller import (
    listarTarefas,
    criarTarefa,
    editarTarefa,
    excluirTarefa,
    concluirTarefa,
)


tarefas_bp = Blueprint(
    "tarefas_bp",
    __name__
)

tarefas_bp.route(
    "/tarefa/nova",
    methods=["GET", "POST"]
)(criarTarefa)


tarefas_bp.route(
    "/tarefa/concluir/<int:id>",
    methods=["POST"]
)(concluirTarefa)


tarefas_bp.route(
    "/dashboard"
)(listarTarefas)


tarefas_bp.route(
    "/tarefa/editar/<int:id>",
    methods=["GET", "POST"]
)(editarTarefa)


tarefas_bp.route(
    "/tarefa/excluir/<int:id>"
)(excluirTarefa)