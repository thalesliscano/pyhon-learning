class Pessoa:
    def __init__(self,nome, documento):
        self.nome = nome
        self.documento = documento

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def documento(self):
        return self._documento
    @documento.setter
    def documento(self, valor):
        self._documento = valor

    def apresentar(self):
        return f"{self.nome} ({self.documento})"

class Aluno(Pessoa):
    def __init__(self,nome, documento,matricula):
        super().__init__(nome,documento)
        self.matricula = matricula
    def apresentar(self):
        base = super().apresentar()
        return f"{base} | matrícula: {self.matricula}"
    
class Professor(Pessoa):

    def __init__(self,nome, documento, registro):
        super().__init__(nome,documento)
        self.registro = registro

    def apresentar(self):
        base = super().apresentar()
        return f"{base} | registro: {self.registro}"
    
aluno = Aluno("Thales", 1231234, "2334343")
professor = Professor("Vinicius", 24242, "123590")

print(aluno.apresentar())
print(professor.apresentar())