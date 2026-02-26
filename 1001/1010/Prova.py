class Prova:
    def __init__(self, acertos, questoes):
        self.acertos = acertos
        self.questoes = questoes
        self.resultado = 0
    def calcular_nota(self):
        self.resultado = self.acertos / self.questoes * 10
        return self.resultado