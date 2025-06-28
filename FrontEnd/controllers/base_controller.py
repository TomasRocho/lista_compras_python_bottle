from bottle import Bottle, static_file,template,request

base_controller = Bottle()

@base_controller.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@base_controller.route('/index')
def index():
    usuario = request.environ.get('beaker.session')['usuario']
    return template('index.tpl',usuario = usuario,mostrarVoltarIndex = False)



