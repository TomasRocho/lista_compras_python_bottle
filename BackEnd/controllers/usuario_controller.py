from bottle import Bottle, response, request
from models.Usuario import Usuario
from services.usuario_service import Usuario_service
import json

usuario_controller = Bottle()

@usuario_controller.get('/usuario')
def get_all():
    usuarios = Usuario_service.get_all()
    response.content_type = 'application/json'
    return json.dumps(usuarios,ensure_ascii=False)

@usuario_controller.get('/usuario/<id>')
def get_byId(id):
    usuario = Usuario_service.get_byId(id)
    if usuario is None:
        response.status=404
        return {"erro":"Usuario Inexistente"}
    response.content_type = 'application/json'
    return json.dumps(usuario,ensure_ascii=False)

@usuario_controller.post('/usuario')
def create():
    dados = request.json
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    if not dados or "email" not in dados or dados['email']=="":
        response.status = 400
        return {'erro': 'Email não preenchido'}
    if not dados or "senha" not in dados or dados['senha']=="":
        response.status = 400
        return {'erro': 'Senha não preenchida'}
    if not dados or "dataNascimento" not in dados or dados['dataNascimento']=="":
        response.status = 400
        return {'erro': 'Data de nascimento não preenchida'}
    usuario = Usuario_service.create(dados['nome'],dados['email'],dados['senha'],dados['dataNascimento'])
    response.status=201
    if "erro" in usuario:
        response.status = 500
    return usuario

@usuario_controller.delete('/usuario/<id>')
def delete(id):
    resp = Usuario_service.delete(id)
    response.status=200
    if "erro" in resp:
        response.status = 500
    return resp

@usuario_controller.put('/usuario')
def update():
    dados = request.json
    if not dados or "id" not in dados or dados['id']=="":
        response.status = 400
        return {'erro': 'id não preenchido'}
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    if not dados or "email" not in dados or dados['email']=="":
        response.status = 400
        return {'erro': 'Email não preenchido'}
    if not dados or "senha" not in dados or dados['senha']=="":
        response.status = 400
        return {'erro': 'Senha não preenchida'}
    if not dados or "dataNascimento" not in dados or dados['dataNascimento']=="":
        response.status = 400
        return {'erro': 'Data de nascimento não preenchida'}
    if not dados or "administrador" not in dados or dados['administrador']=="":
        response.status = 400
        return {'erro': 'Administrador não preenchido'}
    usuario = Usuario_service.update(dados['id'],dados['nome'],dados['email'],dados['senha'],dados['dataNascimento'],dados['administrador'])
    response.status=200
    if "erro" in usuario:
        response.status = 500
    return usuario