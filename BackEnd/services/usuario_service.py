import sqlite3
from models.Usuario import Usuario
from util.criptografia import Criptografia
from services.database import get_connection


class Usuario_service:
    
    
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from usuario
                    """
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        usuarios = [Usuario.from_row(row).to_dict() for row in rows]
        return usuarios
    
    def get_byId(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from usuario where id = ?
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        usuario = None
        if row:
            return Usuario.from_row(row).to_dict()
        return usuario
    
    def get_byEmail(email):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from usuario where email = ?
                    """
        cur.execute(stringSQL,(email,))
        row = cur.fetchone()
        conn.close()
        usuario = None
        if row:
            return Usuario.from_row(row).to_dict()
        return usuario
    
    def create(nome,email,senha,dataNascimento):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into usuario (nome,email,senha,dataNascimento) values (?,?,?,?)
                    """
        try:
            senha = Criptografia.criptografar_string(senha)
            cur.execute(stringSQL,(nome,email,senha,dataNascimento,))
            id = cur.lastrowid
            conn.commit()
            conn.close()
            return {"id": id,
                "nome": nome,
                "email": email,
                "dataNascimento": dataNascimento}    
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome ou email duplicados de usuário", "detalhes": detalhes}
            return {"erro": "Erro ao incluir usuário", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao incluir usuario", "detalhes": str(e)}
        
    def delete(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    delete from usuario where id = ?
                    """
        try:
            cur.execute(stringSQL,(id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"sucesso":"Usuario excluido"}
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Usuario inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "FOREIGN KEY" in detalhes:
                return {"erro": "Usuario utilizado em alguma lista de compras", "detalhes": detalhes}
            return {"erro": "Erro ao excluir usuario", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao excluir usuario", "detalhes": str(e)}
        
    def update(id,nome,email,dataNascimento,administrador):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update usuario set nome = ?, email = ?, dataNascimento = ? , administrador = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(nome,email,dataNascimento,administrador,id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"id": id,
                        "nome": nome,
                        "email": email,
                        "dataNascimento": dataNascimento,
                        "administrador": administrador}  
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Usuario inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome ou email duplicado de usuario", "detalhes": detalhes}
            return {"erro": "Erro ao alterar usuario", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao alterar usuario", "detalhes": str(e)}
        
        
    def logar(email,senha):
        usuarioBd = Usuario_service.get_byEmail(email)
        if usuarioBd == None:
            return{"erro": "Email não cadastrado"}
        #verifica se a senha está correta
        #a senha 'segredo' é utilizada como senha geral e funciona para qualquer usuario, usada somente para fim didático
        if senha!='segredo':
            if Criptografia.criptografar_string(senha) != usuarioBd.get("senha"):
                return{"erro": "Senha inválida"}
        return usuarioBd

    def alterarSenha(idUsuario,senhaAntiga,senhaNova):
        usuarioBd = Usuario_service.get_byId(idUsuario)
        if usuarioBd == None:
            return{"erro": "Id inválido"}
        #verifica se a senha antiga está correta
        #a senha 'segredo' é utilizada como senha geral e funciona para qualquer usuario, usada somente para fim didático
        if senhaAntiga!='segredo':
            if Criptografia.criptografar_string(senhaAntiga) != usuarioBd.get("senha"):
                return{"erro": "Senha antiga inválida"}
        if len(senhaNova)<5:
            return{"erro": "Senha deve possuir no mínimo 5 caracteres"}
        senhaNova = Criptografia.criptografar_string(senhaNova)
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update usuario set senha = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(senhaNova,idUsuario,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"id": idUsuario} 
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao alterar senha", "detalhes": str(e)}
    