from flask import Blueprint, request, jsonify
from core.materias.materias_service import MateriasService
from core.materias.materias import Materias
from core.autenticacao.autenticacao import autenticacao

service = MateriasService()

controller = Blueprint('materias', __name__, url_prefix='/materias')

@controller.route('/', methods=['GET'])
@autenticacao
def listar():
    objeto = service.listar_materiases()
    return jsonify(objeto)

@controller.route('/', methods=['POST'])
@autenticacao
def adicionar():
    dados = request.get_json()
    obj = Materias(id=0, nome=dados["nome"],
                      sigla_curricular=dados["sigla_curricular"],
                      descricao=dados["descricao"])
    objeto = service.adicionar_materias(obj)
    return jsonify(objeto), 201

@controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter(id):
    objeto = service.obter_materias_por_id(id)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Materias não encontrado"}), 404

@controller.route('/<int:id>', methods=['DELETE'])    
@autenticacao
def remover(id):
    sucesso = service.remover_materias(id)
    return jsonify(sucesso)

@controller.route('/', methods=['PUT'])
@autenticacao
def atualizar():
    dados = request.get_json()
    obj = Materias(id=dados["id"], nome=dados["nome"],
                      sigla_curricular=dados["sigla_curricular"],
                      descricao=dados["descricao"])
    objeto = service.atualizar_materias(obj)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Materias não encontrado"}), 404