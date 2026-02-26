class Pessoa():
    def __init__(self, nome:str, sobre_nome:str, idade:int):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá sou {self.nome} {self.sobre_nome} e tenho {self.idade} anos."
    def fazer_aniversario(self):
        self.idade += 1
        return self.idade
