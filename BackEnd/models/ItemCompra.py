from models.Produto import Produto
from models.Usuario import Usuario
from models.Mercado import Mercado
#from models.ListaCompras import ListaCompras
class ItemCompra:
    def __init__(self,id,listaCompras, produto: Produto, valorUnitario,quantidade):
        self.id = id
        self.listaCompras = listaCompras
        self.produto = produto
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade

    def to_dict(self):
        return{
            "id":self.id,
            "listaCompras":self.listaCompras.to_dict_resumido(),
            "produto":self.produto.to_dict(),
            "valorUnitario" : self.valorUnitario,
            "quantidade" : self.quantidade

        }
    
    @staticmethod
    def from_row(row):
        from models.ListaCompras import ListaCompras 
        prod = Produto(
            id=row['idProduto'],
            nome=row['nomeProduto']
        )
        usr = Usuario(
            id=row['idUsuario'],
            nome=row['nomeUsuario'],
            email=row['email'],
            dataNascimento=row['dataNascimento'],
            senha=row['senha'],
            administrador=row['administrador']
        )
        merc = Mercado(
            id=row['idMercado'],
            nome=row['nomeMercado']
        )
        lista = ListaCompras(
            id=row['idListaCompras'],
            nome=row['nomeListaCompras'],
            dataCompra=row['dataCompra'],
            usuario=usr,
            mercado=merc,
            listaItemCompra=[]
        )
        return ItemCompra(
            id=row['id'],
            listaCompras=lista,
            produto=prod,
            valorUnitario=row['valorUnitario'],
            quantidade=row['quantidade']
        )