from bottle import Bottle, template, request, redirect
import requests
from middleware.auth import admin_required

produto_controller = Bottle()

@produto_controller.route('/produto')
def listaProduto():
    try:
        API_URL = 'http://localhost:8080/produto'
        response = requests.get(API_URL)
        response.raise_for_status()
        produtos = response.json() 
    except requests.RequestException as e:
        produtos = []
        print(f"Erro ao acessar API: {e}")
    usuario = request.environ.get('beaker.session')['usuario']
    return template('listaProduto.tpl',produtos=produtos,usuario=usuario,mostrarVoltarIndex=True)    

@produto_controller.route('/produto/novo')
def novoProduto():
    return template('editaProduto.tpl',produto=None)

@produto_controller.route('/produto/editar/<id>')
def editaProduto(id):
    API_URL = 'http://localhost:8080/produto/'+id
    response = requests.get(API_URL)
    produtoRetornado = response.json() 
    print(produtoRetornado)
    usuario = request.environ.get('beaker.session')['usuario']
    return template('editaProduto.tpl',produto=produtoRetornado,usuario=usuario,mostrarVoltarIndex=True) 

@produto_controller.route('/produto/salvar', method='POST')
def salvaProduto():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        API_URL = 'http://localhost:8080/produto'
        if id=='':
            payload = {
                'nome': nome
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Produto")
        else:
            payload = {
                'id': id,
                'nome': nome
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Produto")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Produto")
    redirect('/produto')

@produto_controller.route('/produto/confirmaExclusao/<id>')
def confirmaExclusaoProduto(id):
    API_URL = 'http://localhost:8080/produto/'+id
    response = requests.get(API_URL)
    produtoRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='produto',descricaoObjeto=produtoRetornado.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/produto') 



@produto_controller.route('/produto/excluir/<id>')
def excluiProduto(id):
    try:
        API_URL = 'http://localhost:8080/produto/' + id
        print(API_URL)
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Produto")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Produto")
    redirect('/produto')    
    