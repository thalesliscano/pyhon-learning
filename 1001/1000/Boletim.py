class Boletim:
    def __init__(self):
        self.nota = None
        self.peso = None
        self.descricao = None
        self.notas = []

    def mostrar_infos(self):
        print(f"nota: {self.nota}\npeso:{self.peso}")

    def mostrar_notas(self):
        for nota in self.notas:
            print((nota, self.peso))

    def adicionar_lancamento(self, descricao, nota, peso):
        if(nota >= 0 and nota <= 10):
            self.nota = nota
            self.notas.append(self.nota)
        if(0 <= peso <= 10):
            self.peso = peso
        self.descricao = descricao
    
    def media_final(self):
        soma = 0
        media = 0
        for nota in self.notas:
            soma += (nota * self.peso)
        media = soma / (self.peso * 4)
        return media
    
    def situacao(self):
        media = self.media_final()
        if(media >= 6):
            print("Aprovado!")
        else:
            print("Reprovado!")