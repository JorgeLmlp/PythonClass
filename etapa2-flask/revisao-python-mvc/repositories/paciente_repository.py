from database import db
from models.paciente import Paciente
from flask import request, jsonify
class Paciente_reposityory:
    @staticmethod
    def listar_pacientes():
        pacientes = Paciente.query.all()
        return jsonify([p.to_dict() for p in pacientes]), 200

    @staticmethod
    def obter_paciente(paciente_id):
        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            return jsonify({'erro': 'Paciente não encontrado'}), 404
        return jsonify(paciente.to_dict()), 200

    @staticmethod
    def criar_paciente():
        dados = request.get_json()

        if not dados or 'nome' not in dados or 'idade' not in dados:
            return jsonify({'erro': 'Campos obrigatórios: nome, idade'}), 400

        novo_paciente = Paciente(
            nome=dados['nome'],
            idade=dados['idade'],
            condicao_medica=dados.get('condicao_medica')
        )

        db.session.add(novo_paciente)
        db.session.commit()

        return jsonify(novo_paciente.to_dict()), 201
    
    

class Paciente_service():
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