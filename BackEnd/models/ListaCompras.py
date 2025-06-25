from models.ClasseBase import ClasseBase
from models.Usuario import Usuario
from models.Mercado import Mercado
from models.ItemCompra import ItemCompra


class ListaCompras(ClasseBase):
    def __init__(self,id,nome,dataCompra,usuario:Usuario,mercado:Mercado,listaItemCompra=None):
        super().__init__(id,nome)
        self.usuario = usuario
        self.mercado = mercado
        self.dataCompra = dataCompra
        self.listaItemCompra = listaItemCompra if listaItemCompra is not None else []

    def to_dict(self):
        return{
            "id":self.id,
            "nome":self.nome,
            "dataCompra": self.dataCompra,
            "usuario": self.usuario.to_dict(),
            "mercado": self.mercado.to_dict(),
            "listaItemCompra" : [itemCompra.to_dict() for itemCompra in self.listaItemCompra]
        }
    
    def to_dict_resumido(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "dataCompra": self.dataCompra
        }

    
    @staticmethod
    def from_row(row):
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

        return ListaCompras(
            id=row['id'],
            nome=row['nome'],
            dataCompra=row['dataCompra'],
            usuario=usr,
            mercado=merc,
            listaItemCompra=[]

        )

    

