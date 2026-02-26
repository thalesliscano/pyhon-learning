class Trabalho:
    def __init__(self,nota, bonus):
        self.nota = nota
        self.bonus = bonus
        self.resultado = 0
    def calcular_nota(self):
        self.resultado = self.nota + self.bonus
        return self.resultado