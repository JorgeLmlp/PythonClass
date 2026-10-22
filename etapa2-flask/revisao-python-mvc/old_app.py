from flask import Flask, Blueprint, request, jsonify
from database import db
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



with app.app_context():
    db.create_all()


db.init_app(app)




def atualizar_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Nenhum dado enviado'}), 400

    paciente.nome = dados.get('nome', paciente.nome)
    paciente.idade = dados.get('idade', paciente.idade)
    paciente.condicao_medica = dados.get('condicao_medica', paciente.condicao_medica)

    db.session.commit()

    return jsonify(paciente.to_dict()), 200


def deletar_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    db.session.delete(paciente)
    db.session.commit()

    return jsonify({'mensagem': 'Paciente removido com sucesso'}), 200


def index():
    return jsonify({'status': 'API rodando', 'endpoints': '/api/pacientes'}), 200



paciente_bp = Blueprint('paciente_bp', __name__, url_prefix='/api/pacientes')


paciente_bp.add_url_rule(
    '/', view_func=listar_pacientes, methods=['GET']
)
paciente_bp.add_url_rule(
    '/', view_func=criar_paciente, methods=['POST']
)

paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=obter_paciente, methods=['GET']
)
paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=atualizar_paciente, methods=['PUT']
)
paciente_bp.add_url_rule(
    '/<int:paciente_id>', view_func=deletar_paciente, methods=['DELETE']
)


app.register_blueprint(paciente_bp)


app.add_url_rule('/', view_func=index, methods=['GET'])



if __name__ == '__main__':
    
    app.run(debug=True)