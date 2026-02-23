import re

# def agrupar_por_tamanho(palavras: list[str]  unicas: bool=True) -> dict[int  list[str]]
def agrupar_por_tamanho(palavras: list[str], unicas: bool=True) -> dict[int, list[str]]:
    dicionario_por_tamanho = {}
    print(palavras)
    for palavra in palavras:
        tam = len(palavra)
        # Verifica se existe ou não esse tamanho
        if tam not in dicionario_por_tamanho:
            dicionario_por_tamanho[tam] = [palavra]
        # Verifica se existe ja a palavra dentro do dicionario para evitar repetição
        if unicas:
            if palavra not in dicionario_por_tamanho[tam]:
                dicionario_por_tamanho[tam].append(palavra)
        # Caso ja exista o tam ele apenas joga pra dentro a palavra com o tamanho respectivo
        else:
            dicionario_por_tamanho[tam].append(palavra)
                
        print(dicionario_por_tamanho)
# normalizar
def normalizar(texto:str) -> list[str]:
    texto_limpo = re.sub(r"[^\w\s]", " ", texto)
    texto_limpo = " ".join(texto_limpo.split())
    list_texto_limpo = texto_limpo.split()
    return list_texto_limpo

texto = "thales oi oi oi oi tchau tchau tchau tchau otario bobão otario bobão otario bobão  coitado  coitado  coitado  coitado  coitado carlos carlos carlos 333323"


lista_palavras = normalizar(texto)
agrupar_por_tamanho(lista_palavras)







