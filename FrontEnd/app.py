from bottle import Bottle, run
from controllers.produto_controller import produto_controller
from controllers.base_controller import base_controller
from controllers.mercado_controller import mercado_controller


app = Bottle()
app.merge(base_controller)
app.merge(produto_controller)
app.merge(mercado_controller)





if __name__ == '__main__':
    run(app,host='localhost',port=8081, debug=True,reloader=True)
    