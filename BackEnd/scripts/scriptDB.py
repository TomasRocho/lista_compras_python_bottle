import sqlite3
import os

# Pega o caminho da pasta onde o script está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Monta o caminho para a pasta 'data' que está no mesmo nível de 'config'
db_path = os.path.join(BASE_DIR, '..', 'data', 'listaCompras.db')

conn = sqlite3.connect(db_path)
#tabela mercado
conn.execute("create table mercado (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE)")
conn.execute("insert into mercado (nome) values ('Dona')")
conn.execute("insert into mercado (nome) values ('Big Box')")
conn.execute("insert into mercado (nome) values ('Carrefour')")
conn.execute("insert into mercado (nome) values ('Oba')")

#tabela usuario
conn.execute("create table usuario (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE, email text not null unique COLLATE NOCASE, dataNascimento datetime not null, senha text null, administrador BOOLEAN NOT NULL CHECK (administrador IN (0, 1))default 0)")
conn.execute("insert into usuario (nome,email,dataNascimento,senha,administrador) values ('Tomas','tomas@uol.com.br','2005-10-05','segredo',1)")
conn.execute("insert into usuario (nome,email,dataNascimento,senha) values ('Luciano','luciano@uol.com.br','1974-05-22','segredo')")

#tabela produto
conn.execute("create table produto (id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE)")
conn.execute("insert into produto (nome) values ('Arroz pacote de 5 kg')")
conn.execute("insert into produto (nome) values ('Feijão pacote de 3 kg')")
conn.execute("insert into produto (nome) values ('Leite')")
conn.execute("insert into produto (nome) values ('Pão')")
conn.execute("insert into produto (nome) values ('Açúcar')")


#tabela listaCompras
conn.execute("""
             create table listaCompras (
                id integer primary key AUTOINCREMENT, nome text not null unique COLLATE NOCASE, idUsuario integer not null, idMercado integer not null, dataCompra datetime not null ,
                CONSTRAINT fk_usuario FOREIGN KEY (idUsuario) REFERENCES usuario(id),
                CONSTRAINT fk_mercado FOREIGN KEY (idMercado) REFERENCES mercado(id))
             """)
conn.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 1 de Tomas',1,1,'2025-01-01')")
conn.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 2 de Tomas',1,2,'2025-02-01')")
conn.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 1 de Luciano',2,1,'2025-03-01')")
conn.execute("insert into listaCompras (nome,idUsuario,idMercado,dataCompra) values ('Lista 2 de Luciano',2,2,'2025-04-01')")

#tabela itemCompra
conn.execute("""
            CREATE TABLE itemCompra (id INTEGER PRIMARY KEY AUTOINCREMENT,idListaCompras INTEGER NOT NULL,idProduto INTEGER NOT NULL,valorUnitario REAL NULL,quantidade REAL NULL,
                CONSTRAINT fk_listaCompras FOREIGN KEY (idListaCompras) REFERENCES listaCompras(id),
                CONSTRAINT fk_produto FOREIGN KEY (idProduto) REFERENCES produto(id)
            )
            """)
conn.execute("CREATE UNIQUE INDEX idxUniqueItemCompra ON itemCompra(idListaCompras,idProduto)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,1,0,0)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,2,100,2)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (1,3,20,5)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,3,2,1)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,4,40,1)")
conn.execute("insert into itemCompra (idListaCompras,idProduto,valorUnitario,quantidade) values (2,5,0,0)")


conn.commit()
