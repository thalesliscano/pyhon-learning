class Aluno:
    def __init__(self, notas:list[float], total_aulas:int,presencas:int):
        self.notas = notas
        self.total_aulas = total_aulas
        self.presencas = presencas

    def adicionar_nota(self, nota):
        if  nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida!")

    def registrar_presenca(self, presente:bool):
        if(presente):
            self.presencas += 1
    def media(self):
        soma = 0
        media = 0
        tam = len(self.notas)
        for nota in self.notas:
            soma += nota
        if(tam != 0):
            media = soma/ tam
            return media
        return 0.0
    
    def frequencia(self):
        frequencia_porcem = (self.presencas / self.total_aulas) * 100
        return frequencia_porcem
    
    def situacao_parcial(self):
        msg = ""
        if(self.media() >= 7 and self.frequencia() >= 75):
            msg = "Aprovado"
        elif(self.media() >= 5 and self.frequencia() >= 75):
            msg = "Recuperação"
        else:
            msg = "Reprovado"
        return msg