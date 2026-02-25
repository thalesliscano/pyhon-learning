# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''

def contar_itens(*args) -> int:
    cont = len(args)
    print(cont)
    return cont 
        

contar_itens(2,23, 1, 78, 24, 57, 79)