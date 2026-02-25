# lambda parametros: expressao
'''
# se misturar tudo, normalmente a ordem é assim
def funcao(parametro_normal, *args, **kwargs):
    pass
'''
usuarios = {}
def montar_usuario(**kwargs):
    novo_id = len(usuarios)
    usuarios[novo_id] = kwargs

montar_usuario(nome="Thales", sobre_nome="liscano",idade=23, nacionalidade="Brasileiro")
montar_usuario(nome="Richard", sobre_nome="Junior",idade=21, nacionalidade="EUA")

print(usuarios)