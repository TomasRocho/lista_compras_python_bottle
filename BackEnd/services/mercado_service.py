import sqlite3
from models.Mercado import Mercado
from services.database import get_connection

class Mercado_service:
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from mercado
                    """
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        mercados = [Mercado.from_row(row).to_dict() for row in rows]
        return mercados
    
    def get_byId(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from mercado where id = ?
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        mercado = None
        if row:
            return Mercado.from_row(row).to_dict()
        return mercado
    
    def create(nome):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into mercado (nome) values (?)
                    """
        try:
            cur.execute(stringSQL,(nome,))
            id = cur.lastrowid
            conn.commit()
            conn.close()
            return {"id": id,
                "nome": nome}    
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome duplicado de mercado", "detalhes": detalhes}
            return {"erro": "Erro ao incluir mercado", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao incluir mercado", "detalhes": str(e)}
        
    def delete(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    delete from mercado where id = ?
                    """
        try:
            cur.execute(stringSQL,(id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"sucesso":"Mercado excluido"}
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Mercado inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "FOREIGN KEY" in detalhes:
                return {"erro": "Mercado utilizado em alguma lista de compras", "detalhes": detalhes}
            return {"erro": "Erro ao excluir mercado", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao excluir mercado", "detalhes": str(e)}
        
    def update(id,nome):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update mercado set nome = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(nome,id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"id": id,
                        "nome": nome}  
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Mercado inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome duplicado de mercado", "detalhes": detalhes}
            return {"erro": "Erro ao alterar mercado", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao alterar mercado", "detalhes": str(e)}