from bottle import Bottle, template, request, redirect
import requests
from datetime import datetime
from datetime import date
from config.constantes import HOST_API, PORTA_API


listaCompras_controller = Bottle()

@listaCompras_controller.route('/listaCompras')
def listaListasCompras():
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    try:

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/getByIdUsuario/{usuarioLogado['id']}'
        response = requests.get(chamadaAPI)
        response.raise_for_status()
        listas = response.json() 
        #formata o campo data para o formato dd/mm/yyyy
        for lista in listas:
            lista["dataCompra"] = datetime.strptime(lista["dataCompra"], "%Y-%m-%d").strftime("%d/%m/%Y")
    except requests.RequestException as e:
        listas = []
        print(f"Erro ao acessar API: {e}")
    
    return template('listaListaCompras.tpl',listas=listas,usuario=usuarioLogado,mostrarVoltarIndex=True)    

@listaCompras_controller.route('/listaCompras/novo')
def novaLista():

    #carrega a lista de mercados para popular o <select> do template de edição
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado'
    response = requests.get(chamadaAPI)
    response.raise_for_status()
    mercados = response.json() 

    usuarioLogado = request.environ.get('beaker.session')['usuario']
    dataHoje = date.today().strftime("%d/%m/%Y")
    return template('editaListaCompras.tpl',listaCompras=None,usuario=usuarioLogado,mostrarVoltarIndex=True, mercados=mercados,dataHoje=dataHoje)

@listaCompras_controller.route('/listaCompras/editar/<id>')
def editaListaCompras(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/{id}'
    response = requests.get(chamadaAPI)
    listaRetornada = response.json() 
    listaRetornada["dataCompra"] = datetime.strptime(listaRetornada["dataCompra"], "%Y-%m-%d").strftime("%d/%m/%Y")

    #carrega a lista de mercados para popular o <select> do template de edição
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado'
    response = requests.get(chamadaAPI)
    response.raise_for_status()
    mercados = response.json() 


    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaListaCompras.tpl',listaCompras=listaRetornada,usuario=usuarioLogado,mostrarVoltarIndex=True, mercados=mercados,dataHoje=None) 

@listaCompras_controller.route('/listaCompras/salvar', method='POST')
def salvaCompras():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        dataCompra = request.forms.get('dataCompra')
        #formata o campo data para o formato "yyyy-mm-aa" para ser enviado ao backend
        dataCompra = datetime.strptime(dataCompra, "%d/%m/%Y").strftime("%Y-%m-%d")
        idMercado = request.forms.get('mercado')
        idUsuario = request.forms.get('idUsuario')
        payload = {
                'id': id,
                'nome': nome,
                'dataCompra': dataCompra,
                'idMercado': idMercado,
                'idUsuario': idUsuario
            }

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras'
        #inclusao
        if id=='':
            response = requests.post(chamadaAPI,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Lista")
        #alteracao    
        else:
            response = requests.put(chamadaAPI,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Lista")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Lista")
    redirect('/listaCompras')

@listaCompras_controller.route('/listaCompras/confirmaExclusao/<id>')
def confirmaExclusaoLista(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/{id}'
    response = requests.get(chamadaAPI)
    lista = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='listaCompras',descricaoObjeto=lista.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/listaCompras') 



@listaCompras_controller.route('/listaCompras/excluir/<id>')
def excluirLista(id):
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/listaCompras/{id}'
        response = requests.delete(chamadaAPI)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Lista")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Lista")
    redirect('/listaCompras')    



    