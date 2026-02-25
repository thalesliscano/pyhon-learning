# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''
msg = ""
def buscar_chave(**kwargs):
    if("nome" in kwargs):
        print(kwargs["nome"])
    else:
        print("Nome não informado!")

buscar_chave(nome="thales", sobre_nome="liscano",idade=23, nacionalidade="Brasileiro")
buscar_chave(sobre_nome="liscano",idade=23, nacionalidade="Brasileiro")
