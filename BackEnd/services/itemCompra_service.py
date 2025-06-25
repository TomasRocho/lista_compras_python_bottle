import sqlite3
from models.ItemCompra import ItemCompra
from services.database import get_connection

class ItemCompra_service:
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select	ic.*,
                            p.id as idProduto, p.nome as nomeProduto,
                            lc.id as idListaCompras,lc.nome as nomeListaCompras,lc.dataCompra,
                            u.id as idUsuario, u.nome as nomeUsuario,u.email,u.senha,u.administrador,u.dataNascimento,
                            m.id as idMercado, m.nome as nomeMercado
                    from 	itemCompra ic 
                            join produto p 
                                on p.id =ic.idProduto
                            join listaCompras lc 
                                on lc.id =ic.idListaCompras
                            join mercado m
                                on m.id =lc.idMercado
                            join usuario u 
                                on u.id =lc.idUsuario
                    """
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        listas = [ItemCompra.from_row(row).to_dict() for row in rows]
        return listas
    
    def get_itemCompraByIdListaCompra(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select	ic.*,
                            p.id as idProduto, p.nome as nomeProduto,
                            lc.id as idListaCompras,lc.nome as nomeListaCompras,lc.dataCompra,
                            u.id as idUsuario, u.nome as nomeUsuario,u.email,u.senha,u.administrador,u.dataNascimento,
                            m.id as idMercado, m.nome as nomeMercado
                    from 	itemCompra ic 
                            join produto p 
                                on p.id =ic.idProduto
                            join listaCompras lc 
                                on lc.id =ic.idListaCompras
                            join mercado m
                                on m.id =lc.idMercado
                            join usuario u 
                                on u.id =lc.idUsuario
                    where   lc.id = ?                                
                    """
        cur.execute(stringSQL,(id,))
        rows = cur.fetchall()
        conn.close()
        listas = [ItemCompra.from_row(row).to_dict() for row in rows]
        return listas
    
    def get_byId(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    select	ic.*,
                            p.id as idProduto, p.nome as nomeProduto,
                            lc.id as idListaCompras,lc.nome as nomeListaCompras,lc.dataCompra,
                            u.id as idUsuario, u.nome as nomeUsuario,u.email,u.senha,u.administrador,u.dataNascimento,
                            m.id as idMercado, m.nome as nomeMercado
                    from 	itemCompra ic 
                            join produto p 
                                on p.id =ic.idProduto
                            join listaCompras lc 
                                on lc.id =ic.idListaCompras
                            join mercado m
                                on m.id =lc.idMercado
                            join usuario u 
                                on u.id =lc.idUsuario
                    where   ic.id = ?                                
                    """
        cur.execute(stringSQL,(id,))
        row = cur.fetchone()
        conn.close()
        itemCompra = None
        if row:
            return ItemCompra.from_row(row).to_dict()
        return itemCompra
    
    def create(idListaCompras,idProduto,valorUnitario,quantidade):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (?,?,?,?)
                    """
        try:
            cur.execute(stringSQL,(idListaCompras,idProduto,valorUnitario,quantidade,))
            id = cur.lastrowid
            conn.commit()
            conn.close()
            return {"id": id,
                "idProduto": idProduto,
                "valorUnitario": valorUnitario,
                "quantidade":quantidade
                }    
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "FOREIGN KEY" in detalhes:
                return {"erro": "idProduto inválido", "detalhes": detalhes}
            if "UNIQUE" in detalhes:
                return {"erro": "produto duplicado na listaCompras", "detalhes": detalhes}
            return {"erro": "erro ao incluir itemCompra", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "erro geral do banco de dados ao incluir itemCompra", "detalhes": str(e)}
        
    def delete(id):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    delete from itemCompra where id = ?
                    """
        try:
            cur.execute(stringSQL,(id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"sucesso":"item excluido"}
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"item inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            return {"erro": "erro ao excluir item", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "erro geral do banco de dados ao excluir item", "detalhes": str(e)}
        
    def update(id,idListaCompras,idProduto,valorUnitario,quantidade):
        conn = get_connection()
        cur = conn.cursor()
        stringSQL = """
                    update itemCompra set idListaCompras = ?, idProduto = ?, valorUnitario = ?, quantidade = ? where id = ?
                    """
        try:
            cur.execute(stringSQL,(idListaCompras,idProduto,valorUnitario,quantidade,id,))
            if cur.rowcount==1:
                conn.commit()
                conn.close()
                return {"id": id,
                        "idListaCompras": idListaCompras,
                        "idProduto": idProduto,
                        "valorUnitario": valorUnitario,
                        "quantidade": quantidade}  
            if cur.rowcount==0:
                conn.commit()
                conn.close()
                return {"erro":"item inexistente"}
        except sqlite3.IntegrityError as e:
            conn.close()
            detalhes = str(e)
            if "UNIQUE" in detalhes:
                return {"erro": "produto ja existente na lista", "detalhes": detalhes}
            if "FOREIGN KEY" in detalhes:
                return {"erro": "idListaCompras ou idProduto inexistentes", "detalhes": detalhes}
            return {"erro": "erro ao alterar item", "detalhes": detalhes}
        except sqlite3.Error as e:
            conn.close()
            return {"erro": "erro geral do banco de dados ao alterar item", "detalhes": str(e)}
    