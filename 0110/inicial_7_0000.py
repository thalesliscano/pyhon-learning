import re

def normalizar(texto:str) -> list[str]:
    texto_clear = re.sub(r"[^\w\s]", " ",  texto)
    texto_clear = texto_clear.lower()
    texto_clear = " ".join(texto_clear.split())
    lista_palavras = texto_clear.split()
    return lista_palavras

valor_lista = normalizar("Oi tudo bem sou Thales Liscano Carvalho, tenho 18 anos agora!")
print(valor_lista)

