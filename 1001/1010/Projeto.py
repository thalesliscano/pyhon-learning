from Prova import Prova
from Seminario import Seminario
from Trabalho import Trabalho

class Projeto:
    def __init__(self, notas_etapas:list[float], media_interna):
        self.notas_etapas = notas_etapas
        self.media_interna = media_interna
        self.resultado = 0

    def calcular_nota(self):
        soma = 0
        for nota in self.notas_etapas:
            soma += nota.resultado
        self.resultado = soma / self.media_interna
        return self.resultado