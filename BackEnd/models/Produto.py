from models.ClasseBase import ClasseBase


class Produto(ClasseBase):
    def __init__(self,id,nome):
        super().__init__(id,nome)