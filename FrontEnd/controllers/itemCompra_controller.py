from bottle import Bottle, template, request, redirect
import requests
from datetime import datetime
import locale


itemCompra_controller = Bottle()

@itemCompra_controller.route('/itemCompra/<idListaCompras>')
def listaItensCompra(idListaCompras):
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    try:

        API_URL = 'http://localhost:8080/itemCompra/listaCompra/' + idListaCompras
        response = requests.get(API_URL)
        response.raise_for_status()
        itens = response.json() 

        API_URL_listaCompra = 'http://localhost:8080/listaCompras/' + idListaCompras
        response = requests.get(API_URL_listaCompra)
        response.raise_for_status()
        listaCompra = response.json() 

        API_URL_valorTotal = 'http://localhost:8080/listaCompras/valorTotal/' + idListaCompras
        response = requests.get(API_URL_valorTotal)
        response.raise_for_status()
        valorTotal = response.json()
        total = 0
        if valorTotal:
            total = valorTotal['valorCompra']
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(total, grouping=True)


    except requests.RequestException as e:
        itens = []
        print(f"Erro ao acessar API: {e}")
    
    return template('listaItemCompra.tpl',itens=itens,idListaCompras= idListaCompras,
                    usuario=usuarioLogado,mostrarVoltarIndex=True, 
                    listaCompra = listaCompra, valorTotal = valor_formatado)    

@itemCompra_controller.route('/itemCompra/novo/<idListaCompras>')
def novoItem(idListaCompras):
    API_URL_produtos = 'http://localhost:8080/produto'
    response = requests.get(API_URL_produtos)
    produtos = response.json() 
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaItemCompra.tpl',itemCompra=None,usuario=usuarioLogado,mostrarVoltarIndex=True, idListaCompras=idListaCompras,produtos=produtos)

@itemCompra_controller.route('/itemCompra/editar/<id>')
def editaItem(id):
    API_URL_produtos = 'http://localhost:8080/produto'
    response = requests.get(API_URL_produtos)
    produtos = response.json() 
    API_URL = 'http://localhost:8080/itemCompra/'+id
    response = requests.get(API_URL)
    item = response.json() 
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaItemCompra.tpl',itemCompra=item,usuario=usuarioLogado,mostrarVoltarIndex=True, idListaCompras=item['listaCompras']['id'],produtos=produtos)

@itemCompra_controller.route('/itemCompra/salvar', method='POST')
def salvaItem():
    try:
        id = request.forms.get('id')
        valorUnitario = request.forms.get('valorUnitario')
        quantidade = request.forms.get('quantidade')
        idListaCompras = request.forms.get('idListaCompras')
        idProduto = request.forms.get('produto')


        API_URL = 'http://localhost:8080/itemCompra'
        #inclusao
        if id=='':
            payload = {
                'idProduto': idProduto,
                'valorUnitario': valorUnitario,
                'quantidade': quantidade,
                'idListaCompras': idListaCompras
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Item")
        #alteracao    
        else:
            payload = {
                'id': id,
                'idProduto': idProduto,
                'valorUnitario': valorUnitario,
                'quantidade': quantidade,
                'idListaCompras': idListaCompras
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Item")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Item")
    redirect("/itemCompra/" + idListaCompras)

@itemCompra_controller.route('/itemCompra/confirmaExclusao/<id>')
def confirmaExclusaoItem(id):
    API_URL = 'http://localhost:8080/itemCompra/'+id
    response = requests.get(API_URL)
    item = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='itemCompra',descricaoObjeto=item.get('produto').get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/itemCompra/'+str(item['listaCompras']['id'])) 



@itemCompra_controller.route('/itemCompra/excluir/<id>')
def excluirItem(id):
    try:
        API_URL_GET = 'http://localhost:8080/itemCompra/'+id
        response = requests.get(API_URL_GET)
        item = response.json() 
        idLista = item['listaCompras']['id']
        API_URL = 'http://localhost:8080/itemCompra/' + id
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Item")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Item")
    redirect('/itemCompra/' + str(idLista))    



    