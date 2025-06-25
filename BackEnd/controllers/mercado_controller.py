from bottle import Bottle,  response, request
from models.Mercado import Mercado
from services.mercado_service import Mercado_service
import json

mercado_controller = Bottle()

@mercado_controller.get('/mercado')
def get_all():
    mercados = Mercado_service.get_all()
    response.content_type = 'application/json'
    return json.dumps(mercados,ensure_ascii=False)

@mercado_controller.get('/')
def getHelloWorld():
    return "hello world"

@mercado_controller.get('/mercado/<id>')
def get_byId(id):
    mercado = Mercado_service.get_byId(id)
    if mercado is None:
        response.status=404
        return {"erro":"Mercado Inexistente"}
    response.content_type = 'application/json'
    return json.dumps(mercado,ensure_ascii=False)

@mercado_controller.post('/mercado')
def create():
    dados = request.json
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    mercado = Mercado_service.create(dados['nome'])
    response.status=201
    if "erro" in mercado:
        response.status = 500
    return mercado

@mercado_controller.delete('/mercado/<id>')
def delete(id):
    resp = Mercado_service.delete(id)
    response.status=200
    if "erro" in resp:
        response.status = 500
    return resp

@mercado_controller.put('/mercado')
def update():
    dados = request.json
    if not dados or "id" not in dados or dados['id']=="":
        response.status = 400
        return {'erro': 'id não preenchido'}
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    mercado = Mercado_service.update(dados['id'],dados['nome'])
    response.status=200
    if "erro" in mercado:
        response.status = 500
    return mercado

