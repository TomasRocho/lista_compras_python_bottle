from models.Produto import Produto
from services.database import get_connection
import sqlite3

class Produto_service:
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from produto
                    """
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        produtos = [Produto.from_row(row).to_dict() for row in rows]
        return produtos
    
    def get_byId(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select * from produto where id = ?
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        produto = None
        if row:
            return Produto.from_row(row).to_dict()
        return produto
    
    def create(nome):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into produto (nome) values (?)
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
                return {"erro": "Nome duplicado de produto", "detalhes": detalhes}
            return {"erro": "Erro ao incluir produto", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao incluir produto", "detalhes": str(e)}
        
    def delete(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    delete from produto where id = ?
                    """
        try:
            cur.execute(stringSQL,(id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"sucesso":"Produto excluido"}
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Produto inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "FOREIGN KEY" in detalhes:
                return {"erro": "Produto utilizado em alguma lista de compras", "detalhes": detalhes}
            return {"erro": "Erro ao excluir produto", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao excluir produto", "detalhes": str(e)}
        
    def update(id,nome):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update produto set nome = ? where id = ?
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
                return {"erro":"Produto inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome duplicado de produto", "detalhes": detalhes}
            return {"erro": "Erro ao alterar produto", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao alterar produto", "detalhes": str(e)}
        
            
        

        

        
        