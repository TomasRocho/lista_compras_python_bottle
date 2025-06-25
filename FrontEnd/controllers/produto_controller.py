from bottle import Bottle, template, request, redirect
import requests

produto_controller = Bottle()

@produto_controller.route('/produto')
def listaProduto():
    try:
        API_URL = 'http://localhost:8080/produto'
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança exceção se status != 200
        produtos = response.json()   # Assume que a API retorna JSON
    except requests.RequestException as e:
        produtos = []
        print(f"Erro ao acessar API: {e}")
    return template('listaProduto.tpl',produtos=produtos)    

@produto_controller.route('/produto/novo')
def novoProduto():
    return template('editaProduto.tpl',produto=None)

@produto_controller.route('/produto/editar/<id>')
def editaProduto(id):
    API_URL = 'http://localhost:8080/produto/'+id
    response = requests.get(API_URL)
    produtoRetornado = response.json() 
    print(produtoRetornado)
    return template('editaProduto.tpl',produto=produtoRetornado) 

@produto_controller.route('/produto/excluir/<id>')
def excluiProduto(id):
    API_URL = 'http://localhost:8080/produto/'+id
    response = requests.get(API_URL)
    produtoRetornado = response.json() 
    print(produtoRetornado)
    return template('confirmaExclusao.tpl',produto=produtoRetornado) 

@produto_controller.route('/produto/salvar', method='POST')
def salvaProduto():
    try:
        nome = request.forms.get('nome')
        id = request.forms.get('id')
        API_URL = 'http://localhost:8080/produto'
        if id=='':
            payload = {
                'nome': nome
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'))
        else:
            payload = {
                'id': id,
                'nome': nome
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'))

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e))
    redirect('/produto')

@produto_controller.route('/produto/exclusaoConfirmada/<id>')
def exclusaoConfirmadaProduto(id):
    try:
        API_URL = 'http://localhost:8080/produto/' + id
        print(API_URL)
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'))
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e))
    redirect('/produto')    
    