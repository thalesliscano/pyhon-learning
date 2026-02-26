class Seminario:
    def __init__(self, nota_apresentacao, nota_conteudo ):
        self.nota_apresentacao = nota_apresentacao
        self.nota_conteudo = nota_conteudo
        self.resultado = 0

    def calcular_nota(self):
        self.resultado = (self.nota_apresentacao + self.nota_conteudo) / 2
        return self.resultado