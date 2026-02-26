import os
import time

from Aluno import Aluno
from SistemaAcademico import SistemaAcademico
from Pessoa import Pessoa

sistema = SistemaAcademico()

state = True
print("Sistema abrindo")
print("-" * 20)

def limpar():
    os.system("cls" if os.name == 'nt' else "clear")
while(state):
    try:
        escolha = input("Você possui cadastro S ou N? (ou Q para sair) ").strip().lower()

        match escolha:
            case "s":
                matricula = input("Informe sua matricula por favor: ")

                aluno = sistema.buscar_aluno(matricula)
                if(aluno is None):
                    print("Matrícula não encontrada")
                else:
                    print("Aluno encontrado:")
                    print(aluno)

                time.sleep(3)
                limpar()
                
            case "n":
                nome = input("Informe seu nome: ")
                sobre_nome = input("Informe seu sobrenome: ")
                documento = input("Informe seu documento: ")

                aluno = Aluno(nome, sobre_nome, documento)

                print(aluno.mostrar_infos())
                sistema.cadastrar_alunos(aluno)

                time.sleep(3)
                
            case "q":
                print("Saindo...")
                state = False
            case _:
                print("opção inválida. Digite S, N ou Q.")
                time.sleep(3)
                limpar()
    except ValueError as e:
        print(f"Erro de validação: {e}")
    except TypeError as e:
        print(f"Erro de tipo: {e}")
    except Exception as e:
        print(f"ocorreu um erro inesperaado: {e}")