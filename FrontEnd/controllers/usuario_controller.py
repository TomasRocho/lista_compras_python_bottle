from bottle import Bottle, template, request, redirect
import requests
from datetime import datetime
from config.constantes import HOST_API, PORTA_API


usuario_controller = Bottle()

@usuario_controller.route('/usuario')
def listaUsuario():
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario'
        response = requests.get(chamadaAPI)
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
    usuarioLogado = request.environ.get('beaker.session')['usuario']
    return template('editaUsuario.tpl',usr=None,exibeAdministrador=False,exibeSenha=True,usuario=usuarioLogado,mostrarVoltarIndex=True)

@usuario_controller.route('/usuario/editar/<id>')
def editaUsuario(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario/{id}'
    response = requests.get(chamadaAPI)
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
        payload = {
                'id': id,
                'nome': nome,
                'dataNascimento': dataNascimento,
                'email': email,
                'administrador': administrador,
                'senha': senha
            }

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario'
        #inclusao
        if id=='':
            response = requests.post(chamadaAPI,json=payload)
            if response.status_code!=201:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Usuario")
        #alteracao    
        else:
            response = requests.put(chamadaAPI,json=payload)
            if response.status_code!=200:
                return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Erro ao Salvar Usuario")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao Salvar Usuario")
    redirect('/usuario')

@usuario_controller.route('/usuario/confirmaExclusao/<id>')
def confirmaExclusaoUsuario(id):
    chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario/{id}'
    response = requests.get(chamadaAPI)
    usuarioRetornado = response.json() 
    usuario = request.environ.get('beaker.session')['usuario']
    return template('confirmaExclusao.tpl',nomeObjeto='usuario',descricaoObjeto=usuarioRetornado.get('nome'),id=id,usuario=usuario,mostrarVoltarIndex=True,rotaRetorno='/usuario') 



@usuario_controller.route('/usuario/excluir/<id>')
def excluirUsuario(id):
    try:
        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario/{id}'
        response = requests.delete(chamadaAPI)
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

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/usuario/alterarSenha'
        
        payload = {
            'idUsuario': idUsuario,
            'senhaAntiga': senhaAntiga,
            'senhaNova': senhaNova
        }
        response = requests.put(chamadaAPI,json=payload)
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

        chamadaAPI = f'http://{HOST_API}:{PORTA_API}/login'
        
        payload = {
            'email': email,
            'senha': senha
        }
        response = requests.post(chamadaAPI,json=payload)
        if response.status_code!=200:
            return template('erro.tpl',mensagem=response.json().get('erro'), tipoErro="Login inválido")

    except Exception as e:
        return template('erro', mensagem="Erro ao se comunicar com o servidor: " + str(e), tipoErro="Erro ao logar")
    
    session = request.environ.get('beaker.session')
    session['usuario'] = response.json()
    redirect('/index')

    