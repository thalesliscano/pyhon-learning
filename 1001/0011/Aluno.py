class Aluno:
    def __init__(self, nome, notas:list[float]):
        self.nome = nome
        self.notas = notas
    

    def adicionar_nota(self, nota:float):
        if(nota >= 0):
            self.notas.append(nota)
        else:
            print("Informe uma nota maior ou igual a 0 por por favor!")
    def media(self):
        soma = 0
        tam = len(self.notas)
        if(tam != 0):
            for nota in self.notas:
                soma += nota
            media = soma / tam
            return media
        return 0.0
    
    def aprovado(self, media:float):
        if(media >= 6):
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
    def maior_nota(self):
        maior = self.notas[0]
        for nota in self.notas:
            if(nota > maior):
                maior = nota
        print(maior)
