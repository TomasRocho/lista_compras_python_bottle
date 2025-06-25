from bottle import Bottle, run
from controllers.mercado_controller import mercado_controller
from controllers.usuario_controller import usuario_controller
from controllers.produto_controller import produto_controller
from controllers.listaCompras_controller import listaCompras_controller
from controllers.itemCompra_controller import itemCompra_controller


app = Bottle()
app.merge(mercado_controller)
app.merge(usuario_controller)
app.merge(produto_controller)
app.merge(listaCompras_controller)
app.merge(itemCompra_controller)

if __name__ == '__main__':
    run(app,host='localhost',port=8080, debug=True,reloader=True)
    