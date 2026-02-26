from Aluno import Aluno

class SistemaAcademico:
    def __init__(self):
        self.alunos = []

    def cadastrar_alunos(self, aluno:Aluno):
        if(aluno not in self.alunos):
            self.alunos.append({"nome": aluno.nome, "matricula":aluno.matricula})
        else:
            print("Aluno ja cadastrado")

    def buscar_aluno(self,matricula):
        for aluno in self.alunos:
            if(aluno["matricula"] == matricula):
                for chave, valor in aluno.items():
                    print(f"{chave}: {valor}")
                return aluno
    def mostrar_alunos(self):
        for aluno in self.alunos:
            print(aluno)