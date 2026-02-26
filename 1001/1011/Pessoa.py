class Pessoa:
    def __init__(self,nome, sobre_nome, documento):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.documento = documento

    def mostrar_infos(self):
        return f"Nome: {self.nome} | Sobrenome: {self.sobre_nome} | documento: {self.documento}"