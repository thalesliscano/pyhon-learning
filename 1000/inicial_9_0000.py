# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''

def media (*args) -> float:
    soma = 0
    cont = 0
    for i in args:
        soma += i
        cont += 1
    media = soma / cont
    return media

print(media(10, 10, 10, 10))