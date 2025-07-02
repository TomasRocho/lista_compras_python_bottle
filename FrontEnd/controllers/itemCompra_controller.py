from bottle import Bottle, template, request, redirect
import requests
import locale
from config.constantes import HOST_API, PORTA_API


itemCompra_controller = Bottle()

@itemCompra_controller.route('/itemCompra/<idListaCompras>')
def listaItensCompra(idListaCompras):
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    try:

        #carrega todos os itens de uma determinada lista
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra/listaCompras/{idListaCompras}'
        response = requests.get(chamadaAPI)
        response.raise_for_status()
        itens = response.json() 

        #carrega todos os dados de uma lista para exibir no template
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/{idListaCompras}'
        response = requests.get(chamadaAPI)
        response.raise_for_status()
        listaCompras = response.json() 

        #retorna o valor total de uma lista de compras
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/valorTotal/{idListaCompras}'
        response = requests.get(chamadaAPI)
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
                    listaCompras = listaCompras, valorTotal = valor_formatado)    

@itemCompra_controller.route('/itemCompra/novo/<idListaCompras>')
def novoItem(idListaCompras):
    #carrega a lista de produtos para preencher o <SELECT> do template de edição
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto'
    response = requests.get(chamadaAPI)
    produtos = response.json() 
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaItemCompra.tpl',itemCompra=None,usuario=usuarioLogado,mostrarVoltarIndex=True, idListaCompras=idListaCompras,produtos=produtos)

@itemCompra_controller.route('/itemCompra/editar/<id>')
def editaItem(id):
    
    #carrega a lista de produtos para preencher o <SELECT> do template de edição
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto'
    response = requests.get(chamadaAPI)
    produtos = response.json() 

    #carrega um item completo para o template de edição
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra/{id}'
    response = requests.get(chamadaAPI)
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
        payload = {
                'id': id,
                'idProduto': idProduto,
                'valorUnitario': valorUnitario,
                'quantidade': quantidade,
                'idListaCompras': idListaCompras
            }


        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra'
        #inclusao
        if id=='':
            response = requests.post(chamadaAPI,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Item")
        #alteracao    
        else:
            response = requests.put(chamadaAPI,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Item")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Item")
    redirect(f"/itemCompra/{idListaCompras}")

@itemCompra_controller.route('/itemCompra/confirmaExclusao/<id>')
def confirmaExclusaoItem(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra/{id}'
    response = requests.get(chamadaAPI)
    item = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='itemCompra',descricaoObjeto=item.get('produto').get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/itemCompra/'+str(item['listaCompras']['id'])) 



@itemCompra_controller.route('/itemCompra/excluir/<id>')
def excluirItem(id):
    try:
        #retorna o id da lista de compras para poder fazer o redirect no final da função
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra/{id}'
        response = requests.get(chamadaAPI)
        item = response.json() 
        idLista = item['listaCompras']['id']

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/itemCompra/{id}'
        response = requests.delete(chamadaAPI)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Item")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Item")
    redirect(f'/itemCompra/{idLista}')    



    