from bottle import Bottle, run, route, redirect
from controllers.produto_controller import produto_controller
from controllers.base_controller import base_controller
from controllers.mercado_controller import mercado_controller
from controllers.usuario_controller import usuario_controller
from controllers.listaCompras_controller import listaCompras_controller
from controllers.itemCompra_controller import itemCompra_controller
from beaker.middleware import SessionMiddleware
from middleware.auth import login_required,admin_required
from config.constantes import HOST, PORTA

app = Bottle()
app.merge(base_controller)
app.merge(produto_controller)
app.merge(mercado_controller)
app.merge(usuario_controller)
app.merge(listaCompras_controller)
app.merge(itemCompra_controller)

# Define rotas que NÃO exigem login
rotas_livres = ['/login', '/usuario/login', '/static/', '/favicon.ico']

# Define rotas que NÃO exigem ser admistrador
rotas_nao_admin = ['/index','/login', '/usuario/login','/usuario/logout','/usuario/alterarSenha', '/static/', '/favicon.ico','/listaCompras','/itemCompra']

# Aplica login_required a todas as rotas, exceto as livres
for route in app.routes:
    rota_path = route.rule
    if not any(rota_path.startswith(prefixo) for prefixo in rotas_livres):
        route.callback = login_required(route.callback)

# Aplica admin_required a todas as rotas, exceto as nao_admin
for route in app.routes:
    rota_path = route.rule
    if not any(rota_path.startswith(prefixo) for prefixo in rotas_nao_admin):
        route.callback = admin_required(route.callback)        

# define a rota raiz, redirecionando para /index
@app.route('/')
@login_required
def index():
    redirect('/index')

# Define as propriedades das variavies de sessão
session_opts = {
    'session.type': 'file',          # Store sessions in files
    'session.data_dir': './data',    # Directory to store session files
    'session.cookie_expires': 3600,  # Session cookie expires in 1 hour (3600 seconds)
    'session.auto': True             # Automatically save session changes
}

#A biblioteca abaixo permite que o Bottle armazene variáveis de sessão para compartilhar por toda a aplicação
application = SessionMiddleware(app, session_opts)


if __name__ == '__main__':
    run(application,host=HOST,port=PORTA, debug=True,reloader=True)
    