from bottle import request, redirect,template
from functools import wraps

#módulo para criação de Decorators a serem utilizando nas rotas do sistema
#serão incluídos no módulo app.py, informando quais rotas exigem um usuário logado e quais exigem que o usuário seja administrado

#decorator que só permite acessar a rota informada se já existe um variável de sessao de Usuario (ou seja, já houve o login e um usuário foi logado com sucesso)
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')
        if not session or not session.get('usuario'):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

#decorator que só permite acessar a rota informada se o usuário logado possui a permissão de administrador
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')
        if not session or not session.get('usuario') or session.get('usuario')['administrador']!=1:
            return template('erro.tpl',mensagem="Somente usuário administrador acessa essa página", tipoErro="Usuário Não Autorizado")
        return func(*args, **kwargs)
    return wrapper
