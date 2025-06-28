from bottle import Bottle, template, request, redirect
import requests
from datetime import datetime


usuario_controller = Bottle()

@usuario_controller.route('/usuario')
def listaUsuario():
    try:
        API_URL = 'http://localhost:8080/usuario'
        response = requests.get(API_URL)
        response.raise_for_status()
        usuarios = response.json() 
        for usr in usuarios:
            usr["dataNascimento"] = datetime.strptime(usr["dataNascimento"], "%Y-%m-%d").strftime("%d/%m/%Y")
    except requests.RequestException as e:
        usuarios = []
        print(f"Erro ao acessar API: {e}")
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('listaUsuario.tpl',usuarios=usuarios,usuario=usuarioLogado,mostrarVoltarIndex=True)    

@usuario_controller.route('/usuario/novo')
def novoUsuario():
    return template('editaUsuario.tpl',usuario=None,exibeAdministrador=False,exibeSenha=True)

@usuario_controller.route('/usuario/editar/<id>')
def editaUsuario(id):
    API_URL = 'http://localhost:8080/usuario/'+id
    response = requests.get(API_URL)
    usuarioRetornado = response.json() 
    usuarioRetornado["dataNascimento"] = datetime.strptime(usuarioRetornado["dataNascimento"], "%Y-%m-%d").strftime("%d/%m/%Y")
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaUsuario.tpl',usr=usuarioRetornado,exibeAdministrador=True,exibeSenha=False,usuario=usuarioLogado,mostrarVoltarIndex=True) 

@usuario_controller.route('/usuario/salvar', method='POST')
def salvaUsuario():
    try:
        nome = request.forms.getunicode('nome')
        id = request.forms.get('id')
        dataNascimento = request.forms.get('dataNascimento')
        dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y").strftime("%Y-%m-%d")
        email = request.forms.get('email')
        administrador = 1 if request.forms.get('administrador') else 0
        senha = request.forms.get('senha')

        API_URL = 'http://localhost:8080/usuario'
        #inclusao
        if id=='':
            payload = {
                'nome': nome,
                'dataNascimento': dataNascimento,
                'email': email,
                'senha': senha
            }
            response = requests.post(API_URL,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Usuario")
        #alteracao    
        else:
            payload = {
                'id': id,
                'nome': nome,
                'dataNascimento': dataNascimento,
                'email': email,
                'administrador': administrador,
                'senha': senha
            }
            response = requests.put(API_URL,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Usuario")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Usuario")
    redirect('/usuario')

@usuario_controller.route('/usuario/confirmaExclusao/<id>')
def confirmaExclusaoUsuario(id):
    API_URL = 'http://localhost:8080/usuario/'+id
    response = requests.get(API_URL)
    usuarioRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='usuario',descricaoObjeto=usuarioRetornado.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True) 



@usuario_controller.route('/usuario/excluir/<id>')
def excluirUsuario(id):
    try:
        API_URL = 'http://localhost:8080/usuario/' + id
        print(API_URL)
        response = requests.delete(API_URL)
        if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Excluir Usuario")
    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Excluir Usuario")
    redirect('/usuario')    

@usuario_controller.route('/usuario/alterarSenha')
def alteraSenha():
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('alteraSenha.tpl',usuario=usuarioLogado,mostrarVoltarIndex=True) 

@usuario_controller.route('/usuario/salvarNovaSenha', method='POST')
def salvaNovaSenha():
    try:
        idUsuario = request.forms.get('id')
        senhaAntiga = request.forms.get('senhaAntiga')
        senhaNova = request.forms.get('senhaNova')

        API_URL = 'http://localhost:8080/usuario/alterarSenha'
        
        payload = {
            'idUsuario': idUsuario,
            'senhaAntiga': senhaAntiga,
            'senhaNova': senhaNova
        }
        response = requests.put(API_URL,json=payload)
        if response.status_code!=200:
            return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao alterar senha")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao alterar senha")
    redirect('/index')

@usuario_controller.route('/login')
def telaLogin():
    return template('login.tpl')

@usuario_controller.route('/usuario/logout' , method='POST')
def logout():
    session = request.environ.get('beaker.session')
    session['usuario'] = None
    redirect('/login')


@usuario_controller.route('/usuario/login', method='POST')
def login():
    try:
        email = request.forms.get('email')
        senha = request.forms.get('senha')

        API_URL = 'http://localhost:8080/login'
        
        payload = {
            'email': email,
            'senha': senha
        }
        response = requests.post(API_URL,json=payload)
        if response.status_code!=200:
            return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Login inválido")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao logar")
    
    session = request.environ.get('beaker.session')
    session['usuario'] = response.json()
    redirect('/index')

    