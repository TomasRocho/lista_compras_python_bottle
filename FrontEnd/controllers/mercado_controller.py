from bottle import Bottle, template, request, redirect
import requests

mercado_controller = Bottle()

@mercado_controller.route('/mercado')
def listaMercado():
    try:
        API_URL = 'http://localhost:8080/mercado'
        response = requests.get(API_URL)
        response.raise_for_status()
        mercados = response.json() 
    except requests.RequestException as e:
        mercados = []
        print(f"Erro ao acessar API: {e}")

    usuario = request.environ.get('beaker.session')['usuario']
    return template('listaMercado.tpl',mercados=mercados,usuario=usuario,mostrarVoltarIndex=True)    

@mercado_controller.route('/mercado/novo')
def novoMercado():
    return template('editaMercado.tpl',mercado=None)

@mercado_controller.route('/mercado/editar/<id>')
def editaMercado(id):
    API_URL = 'http://localhost:8080/mercado/'+id
    response = requests.get(API_URL)
    mercadoRetornado = response.json() 
    return template('editaMercado.tpl',mercado=mercadoRetornado) 

@mercado_controller.route('/mercado/salvar', method='POST')
def salvaMercado():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        API_URL = 'http://localhost:8080/mercado'
        if id=='':
            payload = {
                'nome': nome
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Mercado")
        else:
            payload = {
                'id': id,
                'nome': nome
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Mercado")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Mercado")
    redirect('/mercado')

@mercado_controller.route('/mercado/confirmaExclusao/<id>')
def confirmaExclusaoMercado(id):
    API_URL = 'http://localhost:8080/mercado/'+id
    response = requests.get(API_URL)
    mercadoRetornado = response.json() 
    return template('confirmaExclusao.tpl',nomeObjeto='mercado',descricaoObjeto=mercadoRetornado.get('nome'),id=id) 



@mercado_controller.route('/mercado/excluir/<id>')
def excluirMercado(id):
    try:
        API_URL = 'http://localhost:8080/mercado/' + id
        print(API_URL)
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Mercado")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Mercado")
    redirect('/mercado')    
    