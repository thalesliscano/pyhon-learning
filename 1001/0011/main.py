from Aluno import Aluno

class Main:
    def __init__(self):
        print("Classe Main Iniciada")
    def executar(self):
        print("Executar programa...")

    aluno = Aluno("Thales", [])
    print(aluno.media())
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(9)
    aluno.adicionar_nota(6)
    aluno.adicionar_nota(5.57)
    print(aluno.media())
    aluno.maior_nota()
if __name__ == "__main__":
    app = Main()
    app.executar()