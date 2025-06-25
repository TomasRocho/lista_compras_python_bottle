from bottle import Bottle,  response, request
from models.ListaCompras import ListaCompras
from services.listaCompras_service import ListaCompras_service
from services.itemCompra_service import ItemCompra_service
import json

listaCompras_controller = Bottle()

@listaCompras_controller.get('/listaCompras')
def get_all():
    listas = ListaCompras_service.get_all()
    response.content_type = 'application/json'
    return json.dumps(listas,ensure_ascii=False)

@listaCompras_controller.get('/listaCompras/<id>')
def get_byId(id):
    listaCompras = ListaCompras_service.get_byId(id)
    if listaCompras is None:
        response.status=404
        return {"erro":"ListaCompras Inexistente"}
    
    listaItensCompra = ItemCompra_service.get_itemCompraByIdListaCompra(id)
    listaCompras["listaItemCompra"] = listaItensCompra
    
    response.content_type = 'application/json'
    return json.dumps(listaCompras,ensure_ascii=False)

@listaCompras_controller.post('/listaCompras')
def create():
    dados = request.json
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    if not dados or "dataCompra" not in dados or dados['dataCompra']=="":
        response.status = 400
        return {'erro': 'Data da compra não preenchida'}
    if not dados or "idMercado" not in dados or dados['idMercado']=="":
        response.status = 400
        return {'erro': 'IdMercado não preenchido'}
    if not dados or "idUsuario" not in dados or dados['idUsuario']=="":
        response.status = 400
        return {'erro': 'IdUsuario não preenchido'}
    listaCompras = ListaCompras_service.create(dados['nome'],dados['dataCompra'],dados['idMercado'],dados['idUsuario'])
    response.status=201
    if "erro" in listaCompras:
        response.status = 500
    return listaCompras

@listaCompras_controller.delete('/listaCompras/<id>')
def delete(id):
    resp = ListaCompras_service.delete(id)
    response.status=200
    if "erro" in resp:
        response.status = 500
    return resp

@listaCompras_controller.put('/listaCompras')
def update():
    dados = request.json
    if not dados or "id" not in dados or dados['id']=="":
        response.status = 400
        return {'erro': 'Id não preenchido'}
    if not dados or "nome" not in dados or dados['nome']=="":
        response.status = 400
        return {'erro': 'Nome não preenchido'}
    if not dados or "dataCompra" not in dados or dados['dataCompra']=="":
        response.status = 400
        return {'erro': 'Data da compra não preenchida'}
    if not dados or "idMercado" not in dados or dados['idMercado']=="":
        response.status = 400
        return {'erro': 'IdMercado não preenchido'}
    if not dados or "idUsuario" not in dados or dados['idUsuario']=="":
        response.status = 400
        return {'erro': 'IdUsuario não preenchido'}
    listaCompras = ListaCompras_service.update(dados['id'],dados['nome'],dados['dataCompra'],dados['idMercado'],dados['idUsuario'])
    response.status=200
    if "erro" in listaCompras:
        response.status = 500
    return listaCompras