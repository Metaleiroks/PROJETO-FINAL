from flask import Blueprint, request, jsonify
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor
from core.autenticacao.autenticacao import autenticacao

service = ProfessorService()

controller = Blueprint('professor', __name__, url_prefix='/professores')

@controller.route('/', methods=['GET'])
@autenticacao
def listar():
    objeto = service.listar_professores()
    return jsonify(objeto)

@controller.route('/', methods=['POST'])
@autenticacao
def adicionar():
    dados = request.get_json()
    obj = Professor(id=0, nome=dados["nome"],
                      idade=dados["idade"],
                      formacao=dados["formacao"])
    objeto = service.adicionar_professor(obj)
    return jsonify(objeto), 201

@controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter(id):
    objeto = service.obter_professor_por_id(id)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404

@controller.route('/<int:id>', methods=['DELETE'])    
@autenticacao
def remover(id):
    sucesso = service.remover_professor(id)
    return jsonify(sucesso)

@controller.route('/', methods=['PUT'])
@autenticacao
def atualizar():
    dados = request.get_json()
    obj = Professor(id=dados["id"], nome=dados["nome"],
                      idade=dados["idade"],
                      formacao=dados["formacao"])
    objeto = service.atualizar_professor(obj)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404