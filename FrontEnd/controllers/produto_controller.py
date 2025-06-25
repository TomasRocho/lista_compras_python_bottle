from bottle import Bottle, template
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
    return template('listaProdutos.tpl',produtos=produtos)    