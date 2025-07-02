from bottle import Bottle, template, request, redirect
import requests
from config.constantes import HOST_API, PORTA_API

produto_controller = Bottle()

@produto_controller.route('/produto')
def listaProduto():
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto'
        response = requests.get(chamadaAPI)
        response.raise_for_status()
        produtos = response.json() 
    except requests.RequestException as e:
        produtos = []
        print(f"Erro ao acessar API: {e}")
    usuario = request.environ.get('beaker.session')['usuario']
    return template('listaProduto.tpl',produtos=produtos,usuario=usuario,mostrarVoltarIndex=True)    

@produto_controller.route('/produto/novo')
def novoProduto():
    usuario = request.environ.get('beaker.session')['usuario']
    return template('editaProduto.tpl',produto=None,usuario=usuario,mostrarVoltarIndex=True)

@produto_controller.route('/produto/editar/<id>')
def editaProduto(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto/{id}'
    response = requests.get(chamadaAPI)
    produtoRetornado = response.json() 
    print(produtoRetornado)
    usuario = request.environ.get('beaker.session')['usuario']
    return template('editaProduto.tpl',produto=produtoRetornado,usuario=usuario,mostrarVoltarIndex=True) 

@produto_controller.route('/produto/salvar', method='POST')
def salvaProduto():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto'
        payload = {
            'id': id,
            'nome': nome
        }
        #INCLUSÃO
        if id=='':
            response = requests.post(chamadaAPI,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Produto")
        #ALTERAÇÃO
        else:
            response = requests.put(chamadaAPI,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Produto")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Produto")
    redirect('/produto')

@produto_controller.route('/produto/confirmaExclusao/<id>')
def confirmaExclusaoProduto(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto/{id}'
    response = requests.get(chamadaAPI)
    produtoRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='produto',descricaoObjeto=produtoRetornado.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/produto') 



@produto_controller.route('/produto/excluir/<id>')
def excluiProduto(id):
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/produto/{id}'
        response = requests.delete(chamadaAPI)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Produto")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Produto")
    redirect('/produto')    
    