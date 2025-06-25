from models.ClasseBase import ClasseBase


class Usuario(ClasseBase):
    def __init__(self,id,nome,email,dataNascimento,senha,administrador):
        super().__init__(id,nome)
        self.email=email
        self.dataNascimento=dataNascimento
        self.senha=senha
        self.administrador=administrador

    def to_dict(self):
        usuario_dict = super().to_dict()
        usuario_dict.update({
            "email": self.email,
            "dataNascimento": self.dataNascimento,
            "senha": self.senha,
            "administrador": self.administrador,
        })
        return usuario_dict
    
    @staticmethod
    def from_row(row):
        return Usuario(
            id=row['id'],
            nome=row['nome'],
            email=row['email'],
            dataNascimento=row['dataNascimento'],
            senha=row['senha'],
            administrador=row['administrador']
        )
   