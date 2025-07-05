from bottle import Bottle, run
from services.criacaoBD import criar_banco
from controllers.mercado_controller import mercado_controller
from controllers.usuario_controller import usuario_controller
from controllers.produto_controller import produto_controller
from controllers.listaCompras_controller import listaCompras_controller
from controllers.itemCompra_controller import itemCompra_controller
from config.constantes import PORTA,HOST

criar_banco()
app = Bottle()
app.merge(mercado_controller)
app.merge(usuario_controller)
app.merge(produto_controller)
app.merge(listaCompras_controller)
app.merge(itemCompra_controller)

if __name__ == '__main__':
    run(app,host=HOST,port=PORTA, debug=True,reloader=True)
    