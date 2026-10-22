from flask import Blueprint
from repositories import paciente_repository

paciente_bp = Blueprint('paciente_bp', __name__, url_prefix='/api/pacientes')


paciente_bp.add_url_rule(
    '/', view_func=paciente_repository.listar_pacientes(), methods=['GET']
)
paciente_bp.add_url_rule(
    '/', view_func=paciente_repository.criar_paciente(), methods=['POST']
)

paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=paciente_repository.obter_paciente(), methods=['GET']
)
paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=paciente_repository.atualizar_paciente(), methods=['PUT']
)
paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=paciente_repository.deletar_paciente(), methods=['DELETE']
)

