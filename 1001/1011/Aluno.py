from Pessoa import Pessoa
import random

class Aluno(Pessoa):
    def __init__(self, nome, sobre_nome, documento ):
        super().__init__(nome,sobre_nome,documento)
        self.__matricula = f"2026{random.randint(0,9999):04d}"

    @property
    def matricula(self):
        return self.__matricula
    
    def mostrar_infos(self):
        dados = super().mostrar_infos()
        return f"Dados cadastrais: {dados}\nMatricula: {self.__matricula}"
