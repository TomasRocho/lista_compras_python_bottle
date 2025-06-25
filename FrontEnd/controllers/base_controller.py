from bottle import Bottle, static_file

base_controller = Bottle()

@base_controller.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')