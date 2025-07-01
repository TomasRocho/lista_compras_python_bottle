import sqlite3
from models.ListaCompras import ListaCompras
from services.database import get_connection

class ListaCompras_service:
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select     lc.*,
                               us.nome as nomeUsuario,us.email,us.senha,us.administrador,us.dataNascimento,
                               me.nome as nomeMercado
                    from       listacompras lc 
                               join usuario us 
                                   on us.id=lc.idUsuario 
                               join mercado me 
                                   on me.id=lc.idMercado
                    """
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        listas = [ListaCompras.from_row(row).to_dict() for row in rows]
        return listas
    
    def get_byIdUsuario(idUsuario):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select     lc.*,
                               us.nome as nomeUsuario,us.email,us.senha,us.administrador,us.dataNascimento,
                               me.nome as nomeMercado
                    from       listacompras lc 
                               join usuario us 
                                   on us.id=lc.idUsuario 
                               join mercado me 
                                   on me.id=lc.idMercado
                    where       us.id = ?
                    order by    lc.dataCompra desc
                    """
        cur.execute(stringSQL,(idUsuario,))
        rows = cur.fetchall()
        conn.close()
        listas = [ListaCompras.from_row(row).to_dict() for row in rows]
        return listas
    
    def get_byId(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select     lc.*,
                               us.nome as nomeUsuario,us.email,us.senha,us.administrador,us.dataNascimento,
                               me.nome as nomeMercado
                    from       listacompras lc 
                               join usuario us 
                                   on us.id=lc.idUsuario 
                               join mercado me 
                                   on me.id=lc.idMercado
                    where       lc.id = ?                                   
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        listaCompras = None
        if row:
            return ListaCompras.from_row(row).to_dict()
        return listaCompras
    
    def create(nome,dataCompra,idMercado,idUsuario):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into listaCompras (nome,dataCompra,idMercado,idUsuario) values (?,?,?,?)
                    """
        try:
            cur.execute(stringSQL,(nome,dataCompra,idMercado,idUsuario,))
            id = cur.lastrowid
            conn.commit()
            conn.close()
            return {"id": id,
                "nome": nome,
                "dataCompra": dataCompra
                }    
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome duplicado de listaCompras", "detalhes": detalhes}
            if "FOREIGN KEY" in detalhes:
                return {"erro": "IdMercado ou idUsuario inválidos", "detalhes": detalhes}
            return {"erro": "erro ao incluir listaCompras", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao incluir listaCompras", "detalhes": str(e)}
        
    def delete(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    delete from listaCompras where id = ?
                    """
        try:
            cur.execute(stringSQL,(id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"sucesso":"Lista excluida"}
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Lista inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "FOREIGN KEY" in detalhes:
                return {"erro": "Lista possui itens", "detalhes": detalhes}
            return {"erro": "erro ao excluir lista", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao excluir lista", "detalhes": str(e)}
        
    def update(id,nome,dataCompra,idMercado,idUsuario):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update listaCompras set nome = ?, dataCompra = ?, idMercado = ?, idUsuario = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(nome,dataCompra,idMercado,idUsuario,id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"id": id,
                        "nome": nome,
                        "dataCompra": dataCompra,
                        "idMercado": idMercado,
                        "idUsuario": idUsuario}  
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"Lista inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "Nome duplicado de lista", "detalhes": detalhes}
            if "FOREIGN KEY" in detalhes:
                return {"erro": "IdMercado ou idUsuario inexistentes", "detalhes": detalhes}
            return {"erro": "erro ao alterar lista", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "Erro geral do banco de dados ao alterar lista", "detalhes": str(e)}
    
    def valorTotalLista(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select	idListaCompras ,sum(valorUnitario*quantidade) as valorTotal
                    from	itemCompra 
                    where	idListaCompras = ?
                    group by idListaCompras                                
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        valorTotal = None
        if row:
            return {"valorCompra": row['valorTotal']}
        return valorTotal

    
    