from bottle import Bottle, template, request, redirect
import requests
from config.constantes import HOST_API, PORTA_API

mercado_controller = Bottle()

@mercado_controller.route('/mercado')
def listaMercado():
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado'
        response = requests.get(chamadaAPI)
        response.raise_for_status()
        mercados = response.json() 
    except requests.RequestException as e:
        mercados = []
        print(f"Erro ao acessar API: {e}")

    usuario = request.environ.get('beaker.session')['usuario']
    return template('listaMercado.tpl',mercados=mercados,usuario=usuario,mostrarVoltarIndex=True)    

@mercado_controller.route('/mercado/novo')
def novoMercado():
    usuario = request.environ.get('beaker.session')['usuario']
    return template('editaMercado.tpl',mercado=None,usuario=usuario,mostrarVoltarIndex=True)

@mercado_controller.route('/mercado/editar/<id>')
def editaMercado(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado/{id}'
    response = requests.get(chamadaAPI)
    mercadoRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('editaMercado.tpl',mercado=mercadoRetornado,usuario=usuario,mostrarVoltarIndex=True) 

@mercado_controller.route('/mercado/salvar', method='POST')
def salvaMercado():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        payload = {
                    'id': id,
                    'nome': nome
                }
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado'
        #INCLUSÃO
        if id=='':
            response = requests.post(chamadaAPI,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Mercado")
        #ALTERAÇÃO
        else:
            response = requests.put(chamadaAPI,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Mercado")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Mercado")
    redirect('/mercado')

@mercado_controller.route('/mercado/confirmaExclusao/<id>')
def confirmaExclusaoMercado(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado/{id}'
    response = requests.get(chamadaAPI)
    mercadoRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='mercado',descricaoObjeto=mercadoRetornado.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/mercado') 



@mercado_controller.route('/mercado/excluir/<id>')
def excluirMercado(id):
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/mercado/{id}'
        response = requests.delete(chamadaAPI)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Mercado")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Mercado")
    redirect('/mercado')    
    