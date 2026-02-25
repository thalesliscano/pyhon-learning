# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''

def maior_valor(*args):
    maior = args[0]
    menor = args[0]

    for numero in args:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print(maior, menor)

maior_valor(2,23, 1, 78, 24, 57, 79)