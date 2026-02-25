# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''

def exibir_perfil(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

exibir_perfil(nome="Thales", sobre_nome="liscano",idade=23, nacionalidade="Brasileiro")