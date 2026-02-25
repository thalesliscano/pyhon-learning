# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''

def contar_itens(*args) -> str:
    frase = ""
    for palavra in args:
        frase += palavra + " "
    return frase     

print(contar_itens("thales", "liscano", "carvalho", "filho", "otaviano"))