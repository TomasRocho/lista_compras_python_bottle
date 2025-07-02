from bottle import Bottle,  response, request
from services.itemCompra_service import ItemCompra_service
import json

itemCompra_controller = Bottle()

@itemCompra_controller.get('/itemCompra')
def get_all():
    itens = ItemCompra_service.get_all()
    response.content_type = 'application/json'
    return json.dumps(itens,ensure_ascii=False)

@itemCompra_controller.get('/itemCompra/listaCompras/<id>')
def get_byIdListaCompras(id):
    itens = ItemCompra_service.get_byIdListaCompras(id)
    response.content_type = 'application/json'
    return json.dumps(itens,ensure_ascii=False)

@itemCompra_controller.get('/itemCompra/<id>')
def get_byId(id):
    itemCompra = ItemCompra_service.get_byId(id)
    if itemCompra is None:
        response.status=404
        return {"erro":"ItemCompra Inexistente"}
    response.content_type = 'application/json'
    return json.dumps(itemCompra,ensure_ascii=False)

@itemCompra_controller.post('/itemCompra')
def create():
    dados = request.json
    if not dados or "idListaCompras" not in dados or dados['idListaCompras']=="":
        response.status = 400
        return {'erro': 'ListaCompras não preenchida'}
    if not dados or "idProduto" not in dados or dados['idProduto']=="":
        response.status = 400
        return {'erro': 'Produto não preenchido'}
    if not dados or "valorUnitario" not in dados or dados['valorUnitario']=="":
        response.status = 400
        return {'erro': 'Valor unitario não preenchido'}
    if not dados or "quantidade" not in dados or dados['quantidade']=="":
        response.status = 400
        return {'erro': 'Quantidade não preenchida'}
    itemCompra = ItemCompra_service.create(dados['idListaCompras'],dados['idProduto'],dados['valorUnitario'],dados['quantidade'])
    response.status=201
    if "erro" in itemCompra:
        response.status = 500
    return itemCompra

@itemCompra_controller.delete('/itemCompra/<id>')
def delete(id):
    resp = ItemCompra_service.delete(id)
    response.status=200
    if "erro" in resp:
        response.status = 500
    return resp

@itemCompra_controller.put('/itemCompra')
def update():
    dados = request.json
    if not dados or "id" not in dados or dados['id']=="":
        response.status = 400
        return {'erro': 'Id não preenchido'}
    if not dados or "idListaCompras" not in dados or dados['idListaCompras']=="":
        response.status = 400
        return {'erro': 'ListaCompras não preenchida'}
    if not dados or "idProduto" not in dados or dados['idProduto']=="":
        response.status = 400
        return {'erro': 'Produto não preenchido'}
    if not dados or "valorUnitario" not in dados or dados['valorUnitario']=="":
        response.status = 400
        return {'erro': 'Valor unitario não preenchido'}
    if not dados or "quantidade" not in dados or dados['quantidade']=="":
        response.status = 400
        return {'erro': 'Quantidade não preenchida'}
    itemCompra = ItemCompra_service.update(dados['id'],dados['idListaCompras'],dados['idProduto'],dados['valorUnitario'],dados['quantidade'])
    response.status=200
    if "erro" in itemCompra:
        response.status = 500
    return itemCompra

@itemCompra_controller.get('/itemCompra/valorMedio/<idProduto>')
def get_valorMedio(idProduto):
    valorTotal = ItemCompra_service.valorMedioProduto(idProduto)
    response.content_type = 'application/json'
    response.set_header('Access-Control-Allow-Origin', '*')
    return json.dumps(valorTotal,ensure_ascii=False)