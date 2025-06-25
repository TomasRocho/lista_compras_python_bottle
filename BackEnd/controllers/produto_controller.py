from bottle import Bottle,  response, request
from models.Produto import Produto
from services.produto_service import Produto_service
import json

produto_controller = Bottle()

@produto_controller.get('/produto')
def get_all():
    produtos = Produto_service.get_all()
    response.content_type = 'application/json'
    return json.dumps(produtos,ensure_ascii=False)

@produto_controller.get('/produto/<id>')
def get_byId(id):
    produto = Produto_service.get_byId(id)
    if produto is None:
        response.status=404
        return {"erro":"Produto Inexistente"}
    response.content_type = 'application/json'
    return json.dumps(produto,ensure_ascii=False)

@produto_controller.post('/produto')
def create():
    dados = request.json
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    produto = Produto_service.create(dados['nome'])
    response.status=201
    if "erro" in produto:
        response.status = 500
    return produto

@produto_controller.delete('/produto/<id>')
def delete(id):
    resp = Produto_service.delete(id)
    response.status=200
    if "erro" in resp:
        response.status = 500
    return resp
    

@produto_controller.put('/produto')
def update():
    dados = request.json
    if not dados or "id" not in dados or dados['id']=="":
        response.status = 400
        return {'erro': 'Id não preenchido'}
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    produto = Produto_service.update(dados['id'],dados['nome'])
    response.status=200
    if "erro" in produto:
        response.status = 500
    return produto