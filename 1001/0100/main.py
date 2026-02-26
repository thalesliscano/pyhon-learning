from Aluno import Aluno

aluno = Aluno([],43,0)
aluno.adicionar_nota(8)
aluno.adicionar_nota(8)
aluno.adicionar_nota(8)
aluno.adicionar_nota(6)
print(aluno.media())

i = 35
while i > 0:
    aluno.registrar_presenca(True)
    i -= 1
print(aluno.presencas)
print(aluno.frequencia())
print(aluno.situacao_parcial())