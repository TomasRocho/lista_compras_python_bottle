import sqlite3
from models.Usuario import Usuario
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
    
    def create(nome,email,senha,dataNascimento):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into usuario (nome,email,senha,dataNascimento) values (?,?,?,?)
                    """
        try:
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
        
    def update(id,nome,email,senha,dataNascimento,administrador):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update usuario set nome = ?, email = ?, senha = ?, dataNascimento = ? , administrador = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(nome,email,senha,dataNascimento,administrador,id,))
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
    