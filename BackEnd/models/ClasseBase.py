class ClasseBase:
    def __init__(self,id,nome):
        self.id=id
        self.nome=nome

    def to_dict(self)        :
        return{
            "id":self.id,
            "nome":self.nome
        }
    
    @staticmethod
    def from_row(row):
        return ClasseBase(
            id=row['id'],
            nome=row['nome']
        )