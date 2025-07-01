import sqlite3
import os


def criar_banco():

    # Pega o caminho da pasta onde o script está
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Monta o caminho para a pasta 'data' 
    db_path = os.path.join(BASE_DIR, '..', 'data', 'listaCompras.db')
    if os.path.exists(db_path):
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #tabela mercado
    cursor.execute("create table mercado (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE)")
    cursor.execute("insert into mercado (nome) values ('Dona')")
    cursor.execute("insert into mercado (nome) values ('Big Box')")
    cursor.execute("insert into mercado (nome) values ('Carrefour')")
    cursor.execute("insert into mercado (nome) values ('Oba')")

    #tabela usuario
    cursor.execute("create table usuario (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE, email text not null unique COLLATE NOCASE, dataNascimento datetime not null, senha text null, administrador BOOLEAN NOT NULL CHECK (administrador IN (0, 1))default 0)")
    cursor.execute("insert into usuario (nome,email,dataNascimento,senha,administrador) values ('Tomas','tomas@unb.br','2005-10-05','segredo',1)")
    cursor.execute("insert into usuario (nome,email,dataNascimento,senha,administrador) values ('Usuário Normal','usuarionormal@unb.br','2000-01-01','segredo',0)")
    cursor.execute("insert into usuario (nome,email,dataNascimento,senha,administrador) values ('Usuário Administrador','usuarioadministrador@unb.br','2000-12-31','segredo',1)")

    #tabela produto
    cursor.execute("create table produto (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE)")
    cursor.execute("insert into produto (nome) values ('Banana')")
    cursor.execute("insert into produto (nome) values ('Laranja')")
    cursor.execute("insert into produto (nome) values ('Leite')")
    cursor.execute("insert into produto (nome) values ('Pão')")
    cursor.execute("insert into produto (nome) values ('Açúcar')")
    cursor.execute("insert into produto (nome) values ('Arroz')")
    cursor.execute("insert into produto (nome) values ('Feijão')")


    #tabela listaCompras
    cursor.execute("""
                create table listaCompras (
                    id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE, idUsuario integer not null, idMercado integer not null, dataCompra datetime not null ,
                    CONSTRAINT fk_usuario FOREIGN KEY (idUsuario) REFERENCES usuario(id),
                    CONSTRAINT fk_mercado FOREIGN KEY (idMercado) REFERENCES mercado(id))
                """)
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 1 de Tomas',1,1,'2025-01-01')")
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 2 de Tomas',1,2,'2025-02-01')")
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 1 de Usuário Normal',2,1,'2025-03-01')")
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 2 de Usuário Normal',2,2,'2025-04-01')")
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 1 de Usuário Administrador',3,1,'2025-05-01')")
    cursor.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 2 de Usuário Administrador',3,2,'2025-06-01')")

    #tabela itemCompra
    cursor.execute("""
                CREATE TABLE itemCompra (id INTEGER PRIMARY KEY AUTOINCREMENT,idListaCompras INTEGER NOT NULL,idProduto INTEGER NOT NULL,valorUnitario REAL NULL,quantidade REAL NULL,
                    CONSTRAINT fk_listaCompras FOREIGN KEY (idListaCompras) REFERENCES listaCompras(id),
                    CONSTRAINT fk_produto FOREIGN KEY (idProduto) REFERENCES produto(id)
                )
                """)
    cursor.execute("CREATE UNIQUE INDEX idxUniqueItemCompra ON itemCompra(idListaCompras,idProduto)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,1,10,1)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,2,20,2)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,3,30,3)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,1,10,2)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,2,20,2)")
    cursor.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,3,30,2)")


    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso")