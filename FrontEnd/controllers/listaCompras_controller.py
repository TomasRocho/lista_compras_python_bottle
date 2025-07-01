from bottle import Bottle, template, request, redirect
import requests
from datetime import datetime
from datetime import date


listaCompras_controller = Bottle()

@listaCompras_controller.route('/listaCompras')
def listaListasCompras():
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    try:

        API_URL = 'http://localhost:8080/listaCompras/getByIdUsuario/' + str(usuarioLogado['id'])
        response = requests.get(API_URL)
        response.raise_for_status()
        listas = response.json() 
        for lista in listas:
            lista["dataCompra"] = datetime.strptime(lista["dataCompra"], "%Y-%m-%d").strftime("%d/%m/%Y")
    except requests.RequestException as e:
        listas = []
        print(f"Erro ao acessar API: {e}")
    
    return template('listaCompras.tpl',listas=listas,usuario=usuarioLogado,mostrarVoltarIndex=True)    

@listaCompras_controller.route('/listaCompras/novo')
def novaLista():
    API_URL_mercados = 'http://localhost:8080/mercado'
    response = requests.get(API_URL_mercados)
    response.raise_for_status()
    mercados = response.json() 
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    dataHoje = date.today().strftime("%d/%m/%Y")
    return template('editaCompras.tpl',listaCompras=None,usuario=usuarioLogado,mostrarVoltarIndex=True, mercados=mercados,dataHoje=dataHoje)

@listaCompras_controller.route('/listaCompras/editar/<id>')
def editaListaCompras(id):
    API_URL = 'http://localhost:8080/listaCompras/'+id
    response = requests.get(API_URL)
    listaRetornada = response.json() 
    listaRetornada["dataCompra"] = datetime.strptime(listaRetornada["dataCompra"], "%Y-%m-%d").strftime("%d/%m/%Y")
    API_URL_mercados = 'http://localhost:8080/mercado'
    response = requests.get(API_URL_mercados)
    response.raise_for_status()
    mercados = response.json() 
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaCompras.tpl',listaCompras=listaRetornada,usuario=usuarioLogado,mostrarVoltarIndex=True, mercados=mercados,dataHoje=None) 

@listaCompras_controller.route('/listaCompras/salvar', method='POST')
def salvaCompras():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        dataCompra = request.forms.get('dataCompra')
        dataCompra = datetime.strptime(dataCompra, "%d/%m/%Y").strftime("%Y-%m-%d")
        idMercado = request.forms.get('mercado')
        idUsuario = request.forms.get('idUsuario')

        API_URL = 'http://localhost:8080/listaCompras'
        #inclusao
        if id=='':
            payload = {
                'nome': nome,
                'dataCompra': dataCompra,
                'idMercado': idMercado,
                'idUsuario': idUsuario
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Lista")
        #alteracao    
        else:
            payload = {
                'id': id,
                'nome': nome,
                'dataCompra': dataCompra,
                'idMercado': idMercado,
                'idUsuario': idUsuario
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Lista")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Lista")
    redirect('/listaCompras')

@listaCompras_controller.route('/listaCompras/confirmaExclusao/<id>')
def confirmaExclusaoLista(id):
    API_URL = 'http://localhost:8080/listaCompras/'+id
    response = requests.get(API_URL)
    lista = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='listaCompras',descricaoObjeto=lista.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/listaCompras') 



@listaCompras_controller.route('/listaCompras/excluir/<id>')
def excluirLista(id):
    try:
        API_URL = 'http://localhost:8080/listaCompras/' + id
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Lista")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Lista")
    redirect('/listaCompras')    



    